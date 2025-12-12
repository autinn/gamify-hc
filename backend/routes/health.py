"""
Health check routes for monitoring and orchestration.

Provides multiple health check endpoints:
- /api/health - Detailed health status
- /api/health/live - Liveness probe (is app running?)
- /api/health/ready - Readiness probe (can accept traffic?)

Used by:
- Kubernetes liveness/readiness probes
- Load balancers for health checks
- Monitoring systems (Datadog, New Relic, etc.)
- CI/CD for deployment verification
"""

import time
from datetime import datetime

from flask import Blueprint, jsonify
from sqlalchemy import text

from backend.config.settings import get_settings
from backend.utils.logger import get_logger

health_bp = Blueprint('health', __name__, url_prefix='/api/health')
logger = get_logger(__name__)

# Track application start time for uptime calculation
_app_start_time = time.time()


@health_bp.route('', methods=['GET'])
def health_check():
    """
    Comprehensive health check with database connectivity.
    
    Returns detailed information about:
    - Application status
    - Database connectivity
    - Version information
    - Environment details
    - Uptime
    
    Used for monitoring dashboards and alerts.
    """
    settings = get_settings()
    health_status = {
        'status': 'ok',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'application': {
            'name': settings.APP_NAME,
            'version': settings.APP_VERSION,
            'environment': settings.FLASK_ENV,
        },
        'uptime_seconds': int(time.time() - _app_start_time),
    }
    
    # Check database connectivity
    db_status = _check_database()
    health_status['database'] = db_status
    
    # Overall status based on database health
    if db_status['status'] != 'ok':
        health_status['status'] = 'degraded'
        return jsonify(health_status), 503
    
    return jsonify(health_status), 200


@health_bp.route('/live', methods=['GET'])
def liveness_probe():
    """
    Kubernetes liveness probe.
    
    Checks if the application is running and responsive.
    Does NOT check database connectivity (by design).
    
    Returns:
        200 OK: Application is alive
        503 Service Unavailable: Application is dead
    
    Kubernetes will restart the pod if this fails.
    """
    return jsonify({
        'status': 'ok',
        'probe': 'liveness',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
    }), 200


@health_bp.route('/ready', methods=['GET'])
def readiness_probe():
    """
    Kubernetes readiness probe.
    
    Checks if the application can accept traffic.
    Includes database connectivity check.
    
    Returns:
        200 OK: Ready to accept traffic
        503 Service Unavailable: Not ready yet
    
    Kubernetes will not route traffic to pod if this fails.
    Load balancers use this to determine healthy backends.
    """
    # Check database connectivity
    db_status = _check_database()
    
    if db_status['status'] != 'ok':
        return jsonify({
            'status': 'not_ready',
            'probe': 'readiness',
            'reason': 'database_unavailable',
            'database': db_status,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
        }), 503
    
    return jsonify({
        'status': 'ready',
        'probe': 'readiness',
        'database': db_status,
        'timestamp': datetime.utcnow().isoformat() + 'Z',
    }), 200


def _check_database():
    """
    Check database connectivity and return status.
    
    Returns:
        dict: Database status with connection info
    """
    try:
        from flask import current_app
        
        # Get database session from app context
        db = current_app.db_session()
        
        try:
            # Execute simple query to verify connection
            start_time = time.time()
            result = db.execute(text("SELECT 1"))
            result.scalar()
            response_time_ms = int((time.time() - start_time) * 1000)
            
            # Get PostgreSQL version
            version_result = db.execute(text("SELECT version()"))
            version = version_result.scalar()
            pg_version = version.split(',')[0] if version else 'unknown'
            
            return {
                'status': 'ok',
                'type': 'postgresql',
                'version': pg_version,
                'response_time_ms': response_time_ms,
            }
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f'Database health check failed: {e}', exc_info=True)
        return {
            'status': 'error',
            'error': str(e),
            'type': 'postgresql',
        }

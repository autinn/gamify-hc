"""
Request Logger Middleware
Logs all incoming requests and outgoing responses
"""

import time
import uuid
from flask import request, g

from backend.utils.logger import get_logger

logger = get_logger(__name__)


def register_request_logger(app):
    """
    Register request/response logging middleware.
    
    Args:
        app: Flask application instance
    """
    
    @app.before_request
    def log_request_start():
        """Log incoming request and set request ID."""
        # Generate unique request ID for tracing
        g.request_id = str(uuid.uuid4())
        g.start_time = time.time()
        
        # Log request details
        logger.info(
            f'Request started',
            extra={
                'request_id': g.request_id,
                'method': request.method,
                'path': request.path,
                'remote_addr': request.remote_addr,
                'user_agent': request.headers.get('User-Agent', 'Unknown')
            }
        )
    
    @app.after_request
    def log_request_end(response):
        """Log outgoing response with duration."""
        if hasattr(g, 'start_time'):
            duration = time.time() - g.start_time
            
            # Log response details
            logger.info(
                f'Request completed',
                extra={
                    'request_id': getattr(g, 'request_id', 'unknown'),
                    'method': request.method,
                    'path': request.path,
                    'status_code': response.status_code,
                    'duration_ms': round(duration * 1000, 2)
                }
            )
            
            # Add request ID to response headers for client tracing
            response.headers['X-Request-ID'] = getattr(
                g, 'request_id', 'unknown'
            )
        
        return response
    
    @app.teardown_request
    def log_request_teardown(exception=None):
        """Log any exceptions during request teardown."""
        if exception is not None:
            logger.error(
                f'Request teardown exception: {str(exception)}',
                extra={
                    'request_id': getattr(g, 'request_id', 'unknown'),
                    'exception': str(exception)
                },
                exc_info=True
            )
    
    logger.info('Request logger registered')

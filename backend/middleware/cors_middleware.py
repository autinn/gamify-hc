"""
CORS Middleware
Handles Cross-Origin Resource Sharing configuration
"""

from flask_cors import CORS

from backend.config.settings import get_settings
from backend.utils.logger import get_logger

logger = get_logger(__name__)


def register_cors(app):
    """
    Register CORS middleware with configuration from settings.
    
    Args:
        app: Flask application instance
    """
    settings = get_settings()
    
    # Parse CORS origins from comma-separated string
    cors_origins = [
        origin.strip()
        for origin in settings.CORS_ORIGINS.split(',')
        if origin.strip()
    ]
    
    # Configure CORS
    CORS(
        app,
        resources={r"/api/*": {
            "origins": cors_origins,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": [
                "Content-Type",
                "Authorization",
                "X-Requested-With"
            ],
            "expose_headers": ["X-Request-ID"],
            "supports_credentials": True,
            "max_age": 3600  # Cache preflight for 1 hour
        }}
    )
    
    logger.info(
        f'CORS registered with origins: {cors_origins}'
    )

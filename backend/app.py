"""
Flask API for Gamify-HC
Modular REST API with clean architecture and 12-Factor principles
"""

from flask import Flask

from backend.config.settings import get_settings
from backend.middleware import (
    register_cors,
    register_error_handlers,
    register_request_logger,
)
from backend.routes.auth import auth_bp
from backend.routes.concepts import concepts_bp
from backend.routes.courses import courses_bp
from backend.routes.health import health_bp
from backend.routes.quiz import quiz_bp
from backend.routes.units import units_bp
from backend.routes.users import users_bp
from backend.utils.database_manager import DatabaseManager
from backend.utils.graceful_shutdown import (
    get_shutdown_handler,
    register_cleanup,
)
from backend.utils.logger import get_logger

logger = get_logger(__name__)


def create_app(database_url=None, auto_seed=True):
    """
    Create and configure Flask app with clean architecture.
    
    Args:
        database_url: Database connection string
            (uses settings if None)
        auto_seed: If True, seed database with initial data if empty.
            Default True. Set to False for testing.
            
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Only get settings if we need them (no database_url provided)
    if database_url:
        db_url = database_url
        flask_env = 'testing'
    else:
        settings = get_settings()
        db_url = settings.DATABASE_URL
        flask_env = settings.FLASK_ENV
    
    logger.info(f'Creating Flask app in {flask_env} mode')
    
    # Setup database manager
    db_manager = DatabaseManager(db_url, auto_seed=auto_seed)
    
    # Make db session available to blueprints via app context
    app.db_session = db_manager.get_session
    
    # Setup graceful shutdown
    shutdown_handler = get_shutdown_handler()
    shutdown_handler.setup()
    
    # Register cleanup handlers (LIFO order)
    register_cleanup(
        db_manager.cleanup,
        name='database_cleanup'
    )
    register_cleanup(
        lambda: logger.info('Application shutdown complete'),
        name='final_log'
    )
    
    logger.info('Graceful shutdown configured')
    
    # Register middleware (order matters!)
    register_request_logger(app)  # First: log all requests
    register_cors(app)  # Second: handle CORS
    register_error_handlers(app)  # Last: catch all errors
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(units_bp)
    app.register_blueprint(concepts_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(health_bp)
    
    logger.info('All blueprints registered')
    
    logger.info('Flask app created successfully')
    return app


if __name__ == '__main__':
    app = create_app()
    settings = get_settings()
    
    logger.info(
        f'Starting Flask development server on '
        f'{settings.SERVER_HOST}:{settings.SERVER_PORT}'
    )
    
    app.run(
        debug=settings.is_development(),
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT
    )

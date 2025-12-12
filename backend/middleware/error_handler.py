"""
Global Error Handler Middleware
Catches and formats all exceptions consistently
"""

from flask import jsonify
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from backend.utils.logger import get_logger
from backend.validators.auth_validators import ValidationError

logger = get_logger(__name__)


def register_error_handlers(app):
    """
    Register global error handlers for the Flask application.
    
    Args:
        app: Flask application instance
    """
    
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        """Handle validation errors from validators."""
        logger.warning(f'Validation error: {str(error)}')
        return jsonify({
            'error': str(error),
            'type': 'ValidationError'
        }), 400
    
    @app.errorhandler(ValueError)
    def handle_value_error(error):
        """Handle ValueError from business logic."""
        logger.warning(f'Value error: {str(error)}')
        return jsonify({
            'error': str(error),
            'type': 'ValueError'
        }), 400
    
    @app.errorhandler(SQLAlchemyError)
    def handle_database_error(error):
        """Handle database errors."""
        logger.error(f'Database error: {str(error)}')
        return jsonify({
            'error': 'Database error occurred',
            'type': 'DatabaseError'
        }), 500
    
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        """Handle HTTP exceptions (404, 405, etc.)."""
        logger.info(
            f'HTTP exception: {error.code} - {error.description}'
        )
        return jsonify({
            'error': error.description,
            'type': 'HTTPException'
        }), error.code
    
    @app.errorhandler(Exception)
    def handle_generic_error(error):
        """Handle all other unhandled exceptions."""
        logger.error(
            f'Unhandled exception: {str(error)}',
            exc_info=True
        )
        return jsonify({
            'error': 'Internal server error',
            'type': 'InternalError'
        }), 500
    
    @app.errorhandler(404)
    def handle_not_found(error):
        """Handle 404 Not Found errors."""
        logger.info(f'404 Not Found: {error}')
        return jsonify({
            'error': 'Resource not found',
            'type': 'NotFound'
        }), 404
    
    @app.errorhandler(405)
    def handle_method_not_allowed(error):
        """Handle 405 Method Not Allowed errors."""
        logger.info(f'405 Method Not Allowed: {error}')
        return jsonify({
            'error': 'Method not allowed',
            'type': 'MethodNotAllowed'
        }), 405
    
    logger.info('Error handlers registered')

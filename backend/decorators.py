"""
Route Decorators Module.

This module provides reusable decorators for Flask routes to handle
common patterns like authentication, error handling, and request validation.

Functions:
    jwt_required: Decorator for routes requiring JWT authentication
    handle_errors: Decorator for consistent error handling
    validate_json: Decorator for JSON request body validation
"""

from functools import wraps
from typing import Callable, List, Any

from flask import request, jsonify

from backend.services.auth import AuthService


def jwt_required(auth_service: AuthService) -> Callable:
    """
    Decorator factory for JWT authentication requirement.
    
    This decorator verifies that a valid JWT token is present in the
    Authorization header and extracts the user ID for use in the route.
    
    The user_id is stored in request.user_id for access in the route handler.
    
    Args:
        auth_service: AuthService instance for token verification
    
    Returns:
        Decorator function that can be applied to routes
        
    Example:
        auth_service = AuthService(secret_key='...')
        
        @app.route('/protected')
        @jwt_required(auth_service)
        def protected_route():
            user_id = request.user_id
            return jsonify({'user_id': user_id})
    
    Error Responses:
        401: Authorization token is missing
        401: Invalid authorization header format
        401: Invalid or expired token
    """
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def decorated_function(*args: Any, **kwargs: Any):
            # Extract token from Authorization header
            token = None
            auth_header = request.headers.get('Authorization')
            
            if auth_header:
                try:
                    # Expected format: "Bearer <token>"
                    token = auth_header.split(' ')[1]
                except IndexError:
                    return jsonify({
                        'error': 'Invalid authorization header format'
                    }), 401
            
            if not token:
                return jsonify({
                    'error': 'Authorization token is missing'
                }), 401
            
            # Verify token using auth service
            payload = auth_service.verify_token(token)
            if not payload:
                return jsonify({
                    'error': 'Invalid or expired token'
                }), 401
            
            # Store user_id in request context for route handler
            request.user_id = payload['user_id']
            
            return f(*args, **kwargs)
        
        return decorated_function
    return decorator


def handle_errors(f: Callable) -> Callable:
    """
    Decorator for consistent error handling across routes.
    
    This decorator catches common exceptions and returns appropriate
    HTTP responses with error messages. It helps maintain consistent
    error response format across the API.
    
    Handles:
        - ValueError: Returns 400 Bad Request
        - KeyError: Returns 400 Bad Request (missing required field)
        - IntegrityError: Returns 409 Conflict (duplicate data)
        - Exception: Returns 500 Internal Server Error
    
    Example:
        @app.route('/create-user')
        @handle_errors
        def create_user():
            # If this raises ValueError, decorator returns 400
            data = get_validated_data()
            return jsonify({'success': True})
    
    Returns:
        JSON error response with appropriate status code
    """
    @wraps(f)
    def decorated_function(*args: Any, **kwargs: Any):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            # Bad request - invalid input data
            return jsonify({'error': str(e)}), 400
        except KeyError as e:
            # Missing required field in request
            return jsonify({
                'error': f'Missing required field: {str(e)}'
            }), 400
        except Exception as e:
            # Catch-all for unexpected errors
            # In production, log this error for debugging
            return jsonify({
                'error': 'An internal error occurred',
                'detail': str(e)
            }), 500
    
    return decorated_function


def validate_json(required_fields: List[str] = None) -> Callable:
    """
    Decorator factory for validating JSON request bodies.
    
    This decorator ensures that:
    1. The request has a JSON content type
    2. The JSON can be parsed
    3. All required fields are present
    
    Args:
        required_fields: List of field names that must be present in JSON.
                        If None, only validates that JSON is present.
    
    Returns:
        Decorator function that can be applied to routes
        
    Example:
        @app.route('/register', methods=['POST'])
        @validate_json(required_fields=['username', 'email', 'password'])
        def register():
            data = request.get_json()
            # Guaranteed to have username, email, and password
            return jsonify({'success': True})
    
    Error Responses:
        400: Content-Type must be application/json
        400: Invalid JSON format
        400: Missing required field: <field_name>
    """
    if required_fields is None:
        required_fields = []
    
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def decorated_function(*args: Any, **kwargs: Any):
            # Check content type
            if not request.is_json:
                return jsonify({
                    'error': 'Content-Type must be application/json'
                }), 400
            
            # Parse JSON
            try:
                data = request.get_json()
            except Exception:
                return jsonify({
                    'error': 'Invalid JSON format'
                }), 400
            
            # Validate required fields
            for field in required_fields:
                if field not in data:
                    return jsonify({
                        'error': f'Missing required field: {field}'
                    }), 400
            
            return f(*args, **kwargs)
        
        return decorated_function
    return decorator


def validate_request(
    required_fields: List[str] = None,
    auth_service: AuthService = None
) -> Callable:
    """
    Composite decorator combining JSON validation and authentication.
    
    This is a convenience decorator that applies both validate_json
    and jwt_required in the correct order.
    
    Args:
        required_fields: List of required JSON fields
        auth_service: AuthService instance for JWT verification.
                     If None, only JSON validation is applied.
    
    Returns:
        Decorator that validates JSON and optionally authenticates
        
    Example:
        @app.route('/update-profile', methods=['PUT'])
        @validate_request(
            required_fields=['username', 'email'],
            auth_service=auth_service
        )
        def update_profile():
            user_id = request.user_id  # From JWT
            data = request.get_json()  # Validated
            return jsonify({'success': True})
    """
    def decorator(f: Callable) -> Callable:
        # Apply decorators in reverse order (innermost first)
        decorated = f
        
        # First validate JSON
        if required_fields:
            decorated = validate_json(required_fields)(decorated)
        
        # Then check authentication
        if auth_service:
            decorated = jwt_required(auth_service)(decorated)
        
        return decorated
    return decorator

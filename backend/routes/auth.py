"""
Authentication routes blueprint.

This module handles all authentication-related API endpoints for the gamify-hc
application. It provides endpoints for user registration, login, and token
management using JWT (JSON Web Tokens).

This module follows separation of concerns by delegating business logic to
service classes and keeping routes focused on HTTP request/response handling.

Endpoints:
    POST /api/auth/register: Register a new user
    POST /api/auth/login: Login and receive JWT token
    GET /api/auth/me: Get current user info (requires authentication)
"""

from flask import Blueprint, jsonify, request

from backend.config import Config
from backend.decorators import (
    jwt_required as jwt_required_decorator,
    validate_json,
    handle_errors
)
from backend.services.auth import AuthService
from backend.services.user import UserService
from backend.utils.database_manager import get_db

# Create blueprint for authentication-related routes
# All routes in this blueprint will be prefixed with '/api'
auth_bp = Blueprint('auth', __name__, url_prefix='/api')

# Initialize services
# AuthService handles JWT token management and validation logic
auth_service = AuthService(
    secret_key=Config.JWT_SECRET_KEY,
    algorithm=Config.JWT_ALGORITHM,
    expiration_hours=Config.JWT_EXPIRATION_HOURS
)

# UserService handles user CRUD operations and authentication
user_service = UserService(db_session=None)  # DB session set per request


# Create a backward-compatible jwt_required decorator for other routes
# This allows existing routes (like users.py) to continue using @jwt_required
# without needing to import auth_service
def jwt_required_compat(f):
    """
    Backward-compatible jwt_required decorator.
    
    This is a thin wrapper around the new jwt_required decorator that
    automatically provides the auth_service. It maintains compatibility
    with existing routes that import jwt_required from this module.
    
    Usage in other route files:
        from backend.routes.auth import jwt_required
        
        @users_bp.route('/profile')
        @jwt_required
        def get_profile():
            user_id = request.user_id
            return jsonify({'user_id': user_id})
    """
    return jwt_required_decorator(auth_service)(f)


# Export as 'jwt_required' for backward compatibility
jwt_required = jwt_required_compat


@auth_bp.route('/auth/register', methods=['POST'])
def register():
    """
    Register a new user.

    This endpoint creates a new user account with username, email, and
    password. The password is hashed before storage. Email must end with
    minerva.edu.

    Business logic is delegated to AuthService and UserService.

    Request Body:
        {
            'username': str,    # 3-50 characters
            'email': str,       # Must end with minerva.edu
            'password': str     # Minimum 8 characters
        }

    Returns:
        JSON response with the following structure:
        {
            'user_id': int,        # User ID
            'username': str,       # User's username
            'email': str,          # User's email address
            'created_at': str      # ISO format timestamp
        }

    HTTP Status Codes:
        201: Created - User successfully registered
        400: Bad Request - Validation error
        409: Conflict - Username or email already exists
        500: Internal Server Error - Registration failed
    """
    db = get_db()
    try:
        # Set database session for user service
        user_service.db_session = db
        
        # Parse request body
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        # Extract and sanitize input
        username = data.get('username', '').strip()
        email = data.get('email', '').strip().lower()
        password = data.get('password', '')

        # Validate registration data using auth service
        is_valid, error = auth_service.validate_registration_data(
            username=username,
            email=email,
            password=password
        )
        if not is_valid:
            # Return validation error
            return jsonify({'error': error}), 400

        # Check for existing username
        if user_service.user_exists_by_username(username):
            return jsonify({'error': 'Username already exists'}), 409

        # Check for existing email
        if user_service.user_exists_by_email(email):
            return jsonify({'error': 'Email already exists'}), 409

        # Create new user (service handles password hashing)
        new_user = user_service.create_user(
            username=username,
            email=email,
            password=password
        )

        # Convert user to dict for response
        user_dict = user_service.to_dict(new_user)

        return jsonify(user_dict), 201

    except ValueError as e:
        # Validation error from service
        db.rollback()
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Unexpected error
        db.rollback()
        return jsonify({
            'error': 'Registration failed',
            'detail': str(e)
        }), 500
    finally:
        db.close()


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    """
    Login and receive JWT token.

    This endpoint authenticates a user by username/email and password,
    and returns a JWT token for subsequent authenticated requests.

    Business logic is delegated to AuthService and UserService.

    Request Body:
        {
            'username': str,    # Username or email
            'password': str     # User's password
        }

    Returns:
        JSON response with the following structure:
        {
            'access_token': str,   # JWT token
            'user_id': int,        # User ID
            'username': str,       # User's username
            'email': str           # User's email address
        }

    HTTP Status Codes:
        200: Success - Login successful
        400: Bad Request - Missing credentials
        401: Unauthorized - Invalid credentials
    """
    db = get_db()
    try:
        # Set database session for user service
        user_service.db_session = db
        
        # Parse request body
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        username_or_email = data.get('username', '').strip()
        password = data.get('password', '')

        if not username_or_email or not password:
            return jsonify({
                'error': 'Username and password are required'
            }), 400

        # Authenticate user using service
        user = user_service.authenticate_user(
            username_or_email,
            password,
            auth_service
        )
        
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401

        # Generate JWT token using auth service
        token = auth_service.create_token(user.user_id)

        # Return token and user information
        return jsonify({
            'access_token': token,
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email
        }), 200

    finally:
        db.close()


@auth_bp.route('/auth/me', methods=['GET'])
@jwt_required_decorator(auth_service)
def get_current_user():
    """
    Get current authenticated user information.

    This endpoint requires a valid JWT token in the Authorization header.
    Returns the user information for the authenticated user.

    Business logic is delegated to UserService.

    Headers:
        Authorization: Bearer <jwt_token>

    Returns:
        JSON response with the following structure:
        {
            'user_id': int,        # User ID
            'username': str,       # User's username
            'email': str,          # User's email address
            'created_at': str,     # ISO format timestamp
            'has_completed_onboarding': bool  # Onboarding status
        }

    HTTP Status Codes:
        200: Success - User information returned
        401: Unauthorized - Invalid or missing token
        404: Not Found - User not found
    """
    db = get_db()
    try:
        # Set database session for user service
        user_service.db_session = db
        
        # Get user ID from JWT (set by jwt_required decorator)
        user_id = request.user_id

        # Retrieve user using service
        user = user_service.get_user_by_id(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Convert user to dict and add onboarding status
        user_dict = user_service.to_dict(user)
        user_dict['has_completed_onboarding'] = user.has_completed_onboarding

        return jsonify(user_dict), 200

    finally:
        db.close()

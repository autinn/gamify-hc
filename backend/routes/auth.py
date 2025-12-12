"""
Authentication routes blueprint - Thin controller layer.

This module handles HTTP concerns for authentication endpoints:
- Parse requests
- Validate input
- Call service layer
- Return responses

Business logic is in backend/services/auth_service.py
Data access is in backend/repositories/user_repository.py
"""

from functools import wraps

from flask import Blueprint, jsonify, request

from backend.schemas.auth_schemas import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from backend.utils.logger import get_logger
from backend.utils.service_factory import get_auth_service
from backend.validators.auth_validators import (
    ValidationError,
    validate_email,
    validate_password,
    validate_username,
)

# Create blueprint for authentication-related routes
auth_bp = Blueprint('auth', __name__, url_prefix='/api')

# Logger
logger = get_logger(__name__)


def jwt_required(f):
    """
    Decorator to require JWT authentication for a route.

    Usage:
        @auth_bp.route('/protected')
        @jwt_required
        def protected_route():
            # user_id is available in request.user_id
            pass
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                # Extract token from "Bearer <token>"
                token = auth_header.split(' ')[1]
            except IndexError:
                logger.warning('Invalid authorization header format')
                return jsonify({
                    'error': 'Invalid authorization header format'
                }), 401

        if not token:
            logger.warning('Authorization token missing')
            return jsonify({
                'error': 'Authorization token is missing'
            }), 401

        # Verify token using service layer
        try:
            auth_service = get_auth_service()
            payload = auth_service.verify_token(token)
            request.user_id = payload['user_id']
            return f(*args, **kwargs)
        except ValueError as e:
            logger.warning(f'Token verification failed: {str(e)}')
            return jsonify({'error': 'Invalid or expired token'}), 401

    return decorated_function


@auth_bp.route('/auth/register', methods=['POST'])
def register():
    """
    Register a new user - Thin controller.

    Request Body:
        {
            'username': str,    # 3-50 characters
            'email': str,       # Must end with minerva.edu
            'password': str     # Minimum 8 characters
        }

    Returns:
        {
            'user_id': int,
            'username': str,
            'email': str,
            'created_at': str
        }

    HTTP Status Codes:
        201: User successfully registered
        400: Validation error
        409: Username or email already exists
        500: Server error
    """
    try:
        # 1. Parse request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        # 2. Validate input
        username = data.get('username', '').strip()
        email = data.get('email', '').strip().lower()
        password = data.get('password', '')

        try:
            validate_username(username)
            validate_email(email)
            validate_password(password)
        except ValidationError as e:
            logger.info(f'Registration validation failed: {str(e)}')
            return jsonify({'error': str(e)}), 400

        # Create request DTO
        register_req = RegisterRequest(
            username=username,
            email=email,
            password=password
        )

        # 3. Call service layer (handles business logic)
        auth_service = get_auth_service()
        user = auth_service.register_user(
            register_req.username,
            register_req.email,
            register_req.password
        )

        # 4. Serialize response
        user_response = UserResponse.from_model(user)

        logger.info(f'User registered successfully: {username}')
        return jsonify(user_response.to_dict()), 201

    except ValueError as e:
        # Business logic errors (duplicate user, etc.)
        logger.info(f'Registration failed: {str(e)}')
        return jsonify({'error': str(e)}), 409
    except Exception as e:
        logger.error(f'Registration error: {str(e)}')
        return jsonify({'error': 'Registration failed'}), 500


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    """
    Login and receive JWT token - Thin controller.

    Request Body:
        {
            'username': str,    # Username or email
            'password': str     # User's password
        }

    Returns:
        {
            'access_token': str,
            'user_id': int,
            'username': str,
            'email': str
        }

    HTTP Status Codes:
        200: Login successful
        400: Missing credentials
        401: Invalid credentials
        500: Server error
    """
    try:
        # 1. Parse request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        username_or_email = data.get('username', '').strip()
        password = data.get('password', '')

        if not username_or_email or not password:
            return jsonify({
                'error': 'Username and password are required'
            }), 400

        # Create request DTO
        login_req = LoginRequest(
            username=username_or_email,
            password=password
        )

        # 2. Call service layer (handles authentication)
        auth_service = get_auth_service()
        token, user = auth_service.login_user(
            login_req.username,
            login_req.password
        )

        # 3. Serialize response
        user_response = UserResponse.from_model(user)
        token_response = TokenResponse(token=token, user=user_response)

        logger.info(f'User logged in successfully: {user.username}')
        return jsonify(token_response.to_dict()), 200

    except ValueError as e:
        # Invalid credentials
        logger.info(f'Login failed: {str(e)}')
        return jsonify({'error': str(e)}), 401
    except Exception as e:
        logger.error(f'Login error: {str(e)}')
        return jsonify({'error': 'Login failed'}), 500


@auth_bp.route('/auth/me', methods=['GET'])
@jwt_required
def get_current_user():
    """
    Get current authenticated user - Thin controller.

    Headers:
        Authorization: Bearer <jwt_token>

    Returns:
        {
            'user_id': int,
            'username': str,
            'email': str,
            'created_at': str
        }

    HTTP Status Codes:
        200: User information returned
        401: Invalid or missing token
        404: User not found
        500: Server error
    """
    try:
        # 1. Get user_id from JWT (set by @jwt_required)
        user_id = request.user_id

        # 2. Call service layer to get user
        auth_service = get_auth_service()
        user = auth_service.get_user_by_id(user_id)

        if not user:
            logger.warning(f'User not found: {user_id}')
            return jsonify({'error': 'User not found'}), 404

        # 3. Serialize response
        user_response = UserResponse.from_model(user)

        return jsonify(user_response.to_dict()), 200

    except Exception as e:
        logger.error(f'Get current user error: {str(e)}')
        return jsonify({'error': 'Failed to get user'}), 500

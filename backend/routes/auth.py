"""
Authentication routes blueprint.

This module handles all authentication-related API endpoints for the gamify-hc
application. It provides endpoints for user registration, login, and token
management using JWT (JSON Web Tokens).

Endpoints:
    POST /api/auth/register: Register a new user
    POST /api/auth/login: Login and receive JWT token
    GET /api/auth/me: Get current user info (requires authentication)
"""

import os
import re
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from backend.database.models import User
from backend.utils.database_manager import get_db

# Create blueprint for authentication-related routes
# All routes in this blueprint will be prefixed with '/api'
auth_bp = Blueprint('auth', __name__, url_prefix='/api')

# JWT configuration
JWT_SECRET_KEY = os.getenv(
    'JWT_SECRET_KEY', 'dev-secret-key-change-in-production'
)
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_HOURS = 24


def create_token(user_id):
    """
    Create a JWT token for a user.

    Args:
        user_id (int): The user ID to encode in the token

    Returns:
        str: Encoded JWT token
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def verify_token(token):
    """
    Verify a JWT token and extract user ID.

    Args:
        token (str): The JWT token to verify

    Returns:
        dict: Decoded token payload if valid, None otherwise
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def jwt_required(f):
    """
    Decorator to require JWT authentication for a route.

    Usage:
        @auth_bp.route('/protected')
        @jwt_required
        def protected_route():
            # user_id is available in g.user_id
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
                return jsonify({
                    'error': 'Invalid authorization header format'
                }), 401

        if not token:
            return jsonify({'error': 'Authorization token is missing'}), 401

        payload = verify_token(token)
        if not payload:
            return jsonify({'error': 'Invalid or expired token'}), 401

        # Store user_id in request context for use in route
        request.user_id = payload['user_id']
        return f(*args, **kwargs)

    return decorated_function


def validate_email(email):
    """
    Validate email format and check if it ends with minerva.edu.

    Args:
        email (str): Email address to validate

    Returns:
        tuple: (is_valid, error_message)
    """
    if not email:
        return False, 'Email is required'

    # Basic email format check (matches database constraint)
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return False, 'Invalid email format'

    # Check if email ends with minerva.edu
    if not email.endswith('minerva.edu'):
        return False, 'Email must end with minerva.edu'

    return True, None


def validate_username(username):
    """
    Validate username length (3-50 characters).

    Args:
        username (str): Username to validate

    Returns:
        tuple: (is_valid, error_message)
    """
    if not username:
        return False, 'Username is required'

    if len(username) < 3 or len(username) > 50:
        return False, 'Username must be between 3 and 50 characters'

    return True, None


def validate_password(password):
    """
    Validate password strength.

    Args:
        password (str): Password to validate

    Returns:
        tuple: (is_valid, error_message)
    """
    if not password:
        return False, 'Password is required'

    if len(password) < 8:
        return False, 'Password must be at least 8 characters long'

    return True, None


@auth_bp.route('/auth/register', methods=['POST'])
def register():
    """
    Register a new user.

    This endpoint creates a new user account with username, email, and
    password. The password is hashed before storage. Email must end with
    minerva.edu.

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
    """
    db = get_db()
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        username = data.get('username', '').strip()
        email = data.get('email', '').strip().lower()
        password = data.get('password', '')

        # Validate input
        is_valid, error = validate_username(username)
        if not is_valid:
            return jsonify({'error': error}), 400

        is_valid, error = validate_email(email)
        if not is_valid:
            return jsonify({'error': error}), 400

        is_valid, error = validate_password(password)
        if not is_valid:
            return jsonify({'error': error}), 400

        # Check for duplicate username
        existing_user = db.query(User).filter(
            User.username == username
        ).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 409

        # Check for duplicate email
        existing_email = db.query(User).filter(
            User.email == email
        ).first()
        if existing_email:
            return jsonify({'error': 'Email already exists'}), 409

        # Hash password
        password_hash = generate_password_hash(password)

        # Create new user
        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Return user data (without password_hash)
        return jsonify({
            'user_id': new_user.user_id,
            'username': new_user.username,
            'email': new_user.email,
            'created_at': (
                new_user.created_at.isoformat()
                if new_user.created_at else None
            )
        }), 201

    except IntegrityError as e:
        db.rollback()
        # Check if it's a duplicate username or email
        error_msg = str(e.orig) if hasattr(e, 'orig') else str(e)
        username_constraint = 'UNIQUE constraint failed: users.username'
        email_constraint = 'UNIQUE constraint failed: users.email'
        if ('username' in error_msg.lower() or
                username_constraint in error_msg):
            return jsonify({'error': 'Username already exists'}), 409
        elif ('email' in error_msg.lower() or
              email_constraint in error_msg):
            return jsonify({'error': 'Email already exists'}), 409
        else:
            return jsonify({'error': 'Registration failed'}), 500
    except Exception:
        db.rollback()
        return jsonify({'error': 'Registration failed'}), 500
    finally:
        db.close()


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    """
    Login and receive JWT token.

    This endpoint authenticates a user by username/email and password,
    and returns a JWT token for subsequent authenticated requests.

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
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        username_or_email = data.get('username', '').strip()
        password = data.get('password', '')

        if not username_or_email or not password:
            return jsonify({
                'error': 'Username and password are required'
            }), 400

        # Query user by username or email
        user = db.query(User).filter(
            (User.username == username_or_email) |
            (User.email == username_or_email.lower())
        ).first()

        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401

        # Verify password
        if not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid credentials'}), 401

        # Generate JWT token
        token = create_token(user.user_id)

        return jsonify({
            'access_token': token,
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email
        }), 200

    finally:
        db.close()


@auth_bp.route('/auth/me', methods=['GET'])
@jwt_required
def get_current_user():
    """
    Get current authenticated user information.

    This endpoint requires a valid JWT token in the Authorization header.
    Returns the user information for the authenticated user.

    Headers:
        Authorization: Bearer <jwt_token>

    Returns:
        JSON response with the following structure:
        {
            'user_id': int,        # User ID
            'username': str,       # User's username
            'email': str,          # User's email address
            'created_at': str      # ISO format timestamp
        }

    HTTP Status Codes:
        200: Success - User information returned
        401: Unauthorized - Invalid or missing token
    """
    db = get_db()
    try:
        user_id = request.user_id

        user = db.query(User).filter(
            User.user_id == user_id
        ).first()

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'created_at': (
                user.created_at.isoformat()
                if user.created_at else None
            )
        }), 200

    finally:
        db.close()

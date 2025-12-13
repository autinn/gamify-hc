"""
Authentication Service Module.

This module contains business logic for authentication and authorization,
including JWT token management, password hashing, and user validation.

Classes:
    AuthService: Handles authentication operations
"""

import re
from datetime import datetime, timedelta
from typing import Tuple, Optional, Dict, Any

import jwt
from werkzeug.security import check_password_hash, generate_password_hash

from backend.services.base_service import BaseService
from backend.database.models import User


class AuthService(BaseService):
    """
    Service class for authentication and authorization operations.
    
    This service handles all authentication-related business logic including:
    - JWT token creation and verification
    - Password hashing and verification
    - Email and username validation
    - User authentication
    
    The service is stateless and can be used without a database session
    for operations like token validation and password hashing.
    
    Attributes:
        secret_key (str): Secret key for JWT encoding/decoding
        algorithm (str): JWT algorithm (default: HS256)
        expiration_hours (int): Token expiration time in hours
    
    Example:
        auth_service = AuthService(
            secret_key='my-secret',
            algorithm='HS256',
            expiration_hours=24
        )
        token = auth_service.create_token(user_id=123)
        payload = auth_service.verify_token(token)
    """
    
    def __init__(
        self,
        secret_key: str,
        algorithm: str = 'HS256',
        expiration_hours: int = 24,
        db_session=None
    ):
        """
        Initialize the authentication service.
        
        Args:
            secret_key: Secret key for JWT token generation
            algorithm: JWT encoding algorithm (default: HS256)
            expiration_hours: Token expiration time in hours
            db_session: Optional database session for user queries
        """
        super().__init__(db_session)
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expiration_hours = expiration_hours
    
    def create_token(self, user_id: int) -> str:
        """
        Create a JWT token for a user.
        
        Generates a JSON Web Token with the user ID, expiration time,
        and issued-at time encoded in the payload.
        
        Args:
            user_id: The user ID to encode in the token
        
        Returns:
            Encoded JWT token as a string
            
        Example:
            token = auth_service.create_token(user_id=42)
            # Returns: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        """
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(hours=self.expiration_hours),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Verify a JWT token and extract its payload.
        
        Validates the token signature and expiration time. Returns the
        decoded payload if valid, or None if the token is invalid or expired.
        
        Args:
            token: The JWT token string to verify
        
        Returns:
            Dictionary containing the token payload if valid, None otherwise.
            Payload structure: {'user_id': int, 'exp': int, 'iat': int}
            
        Example:
            payload = auth_service.verify_token(token)
            if payload:
                user_id = payload['user_id']
            else:
                # Token is invalid or expired
                pass
        """
        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm]
            )
            return payload
        except jwt.ExpiredSignatureError:
            # Token has expired
            return None
        except jwt.InvalidTokenError:
            # Token is invalid (bad signature, malformed, etc.)
            return None
    
    def hash_password(self, password: str) -> str:
        """
        Hash a password using Werkzeug's security utilities.
        
        Uses PBKDF2 with SHA-256 by default, which is secure for
        password storage.
        
        Args:
            password: Plain text password to hash
        
        Returns:
            Hashed password string safe for database storage
            
        Example:
            hashed = auth_service.hash_password('my-secure-password')
            # Returns: 'pbkdf2:sha256:260000$...'
        """
        return generate_password_hash(password)
    
    def verify_password(self, hashed_password: str, password: str) -> bool:
        """
        Verify a password against its hash.
        
        Args:
            hashed_password: The stored password hash from database
            password: The plain text password to verify
        
        Returns:
            True if password matches the hash, False otherwise
            
        Example:
            if auth_service.verify_password(user.password, input_password):
                # Password is correct
                pass
        """
        return check_password_hash(hashed_password, password)
    
    def validate_email(self, email: str) -> Tuple[bool, Optional[str]]:
        """
        Validate email format and domain requirements.
        
        Checks that the email:
        1. Is provided and not empty
        2. Matches basic email format (user@domain.tld)
        3. Ends with 'minerva.edu' domain
        
        Args:
            email: Email address to validate
        
        Returns:
            Tuple of (is_valid, error_message)
            - is_valid: True if email passes all checks
            - error_message: Description of validation failure, or None if valid
            
        Example:
            valid, error = auth_service.validate_email('user@minerva.edu')
            if not valid:
                return jsonify({'error': error}), 400
        """
        if not email:
            return False, 'Email is required'
        
        # Basic email format check (matches database constraint)
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            return False, 'Invalid email format'
        
        # Check if email ends with minerva.edu (institution requirement)
        if not email.endswith('minerva.edu'):
            return False, 'Email must end with minerva.edu'
        
        return True, None
    
    def validate_username(self, username: str) -> Tuple[bool, Optional[str]]:
        """
        Validate username length requirements.
        
        Username must be between 3 and 50 characters to match database
        constraints and provide reasonable user experience.
        
        Args:
            username: Username to validate
        
        Returns:
            Tuple of (is_valid, error_message)
            
        Example:
            valid, error = auth_service.validate_username('john')
            if not valid:
                return jsonify({'error': error}), 400
        """
        if not username:
            return False, 'Username is required'
        
        if len(username) < 3 or len(username) > 50:
            return False, 'Username must be between 3 and 50 characters'
        
        return True, None
    
    def validate_password(self, password: str) -> Tuple[bool, Optional[str]]:
        """
        Validate password strength requirements.
        
        Password must be at least 8 characters long for basic security.
        Consider adding more requirements (uppercase, numbers, symbols)
        for production applications.
        
        Args:
            password: Password to validate
        
        Returns:
            Tuple of (is_valid, error_message)
            
        Example:
            valid, error = auth_service.validate_password('mypassword123')
            if not valid:
                return jsonify({'error': error}), 400
        """
        if not password:
            return False, 'Password is required'
        
        if len(password) < 8:
            return False, 'Password must be at least 8 characters long'
        
        return True, None
    
    def validate_registration_data(
        self,
        username: str,
        email: str,
        password: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Validate all registration data at once.
        
        Convenience method that validates username, email, and password
        in a single call. Returns on first validation failure.
        
        Args:
            username: Username to validate
            email: Email address to validate
            password: Password to validate
        
        Returns:
            Tuple of (is_valid, error_message)
            Returns first validation error encountered
            
        Example:
            valid, error = auth_service.validate_registration_data(
                username='john',
                email='john@minerva.edu',
                password='securepass123'
            )
            if not valid:
                return jsonify({'error': error}), 400
        """
        # Validate username
        valid, error = self.validate_username(username)
        if not valid:
            return valid, error
        
        # Validate email
        valid, error = self.validate_email(email)
        if not valid:
            return valid, error
        
        # Validate password
        valid, error = self.validate_password(password)
        if not valid:
            return valid, error

        return True, None

    def authenticate_user(
        self,
        username_or_email: str,
        password: str,
        db_session
    ) -> Optional[User]:
        """
        Authenticate a user with username/email and password.

        This method combines user lookup and password verification into
        a single authentication operation.

        Args:
            username_or_email: The username or email address to authenticate
            password: The plain text password to verify
            db_session: Database session for user lookup

        Returns:
            User object if authentication succeeds, None otherwise

        Example:
            user = auth_service.authenticate_user(
                username_or_email='john',
                password='mypassword',
                db_session=db
            )
            if user:
                token = auth_service.create_token(user.user_id)
                return jsonify({'token': token})
            else:
                return jsonify({'error': 'Invalid credentials'}), 401
        """
        # Look up user by username
        user = db_session.query(User).filter(
            User.username == username_or_email
        ).first()

        # If not found by username, try email
        if not user:
            user = db_session.query(User).filter(
                User.email == username_or_email.lower()
            ).first()

        if not user:
            return None

        # Verify password
        if not self.verify_password(user.password_hash, password):
            return None

        return user

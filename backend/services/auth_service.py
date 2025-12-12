"""
Authentication Service - Business logic for user authentication
Handles registration, login, and JWT token management
"""

from typing import Optional, Tuple
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from backend.database.models import User
from backend.repositories.user_repository import UserRepository
from backend.utils.logger import get_logger
from backend.utils.database_manager import get_db
from backend.config.settings import get_settings

logger = get_logger(__name__)


class AuthService:
    """
    Service for authentication operations.
    
    Handles user registration, login, JWT creation/verification,
    and password management.
    
    Example:
        >>> auth_service = AuthService()
        >>> user = auth_service.register_user(
        ...     'john', 'john@minerva.edu', 'pass123'
        ... )
    """

    def __init__(
        self,
        user_repository: Optional[UserRepository] = None,
        jwt_secret: Optional[str] = None,
        jwt_expiration_hours: Optional[int] = None
    ):
        """
        Initialize authentication service.
        
        Args:
            user_repository: User data access repository
                (creates new session if None)
            jwt_secret: Secret key for JWT signing
                (uses settings if None)
            jwt_expiration_hours: Token expiration time in hours
                (uses settings if None)
        """
        # Create repository if not provided
        if user_repository is None:
            session = get_db()
            self.user_repo = UserRepository(session)
            self._owns_session = True
        else:
            self.user_repo = user_repository
            self._owns_session = False
        
        # Use settings for JWT config
        settings = get_settings()
        self.jwt_secret = jwt_secret or settings.JWT_SECRET_KEY
        self.jwt_expiration_hours = (
            jwt_expiration_hours or settings.JWT_EXPIRATION_HOURS
        )

    def __del__(self):
        """Close session if we own it."""
        if (hasattr(self, '_owns_session') and self._owns_session and 
            hasattr(self, 'user_repo')):
            self.user_repo.close()

    def register_user(
        self,
        username: str,
        email: str,
        password: str
    ) -> User:
        """
        Register a new user account.
        
        Creates user with hashed password.
        
        Args:
            username: Unique username (3-50 chars)
            email: User email (must end with minerva.edu)
            password: Plain text password (will be hashed)
            
        Returns:
            User instance
            
        Raises:
            ValueError: If username or email already exists
            
        Example:
            >>> user = auth_service.register_user(
            ...     'john', 'john@minerva.edu', 'secure123'
            ... )
        """
        # Check for duplicate username
        if self.user_repo.username_exists(username):
            logger.warning(
                f"Registration failed: username '{username}' exists"
            )
            raise ValueError('Username already exists')
        
        # Check for duplicate email
        if self.user_repo.email_exists(email):
            logger.warning(f"Registration failed: email '{email}' exists")
            raise ValueError('Email already exists')
        
        # Hash password using pbkdf2:sha256 (compatible with all Python versions)
        password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        
        # Create user
        user = self.user_repo.create_user(username, email, password_hash)
        self.user_repo.commit()
        
        logger.info(f"User registered: {username} (ID: {user.user_id})")
        
        return user

    def login_user(
        self,
        username_or_email: str,
        password: str
    ) -> Tuple[str, User]:
        """
        Authenticate user and generate JWT token.
        
        Args:
            username_or_email: Username or email to authenticate
            password: Plain text password
            
        Returns:
            Tuple of (JWT token, User instance)
            
        Raises:
            ValueError: If credentials are invalid
            
        Example:
            >>> token, user = auth_service.login_user(
            ...     'john', 'secure123'
            ... )
        """
        # Try to find user by username or email
        user = self.user_repo.find_by_username(username_or_email)
        
        if not user:
            # Try email if username not found
            user = self.user_repo.find_by_email(username_or_email)
        
        if not user:
            logger.warning(
                f"Login failed: '{username_or_email}' not found"
            )
            raise ValueError('Invalid credentials')
        
        # Verify password
        if not check_password_hash(user.password_hash, password):
            logger.warning(
                f"Login failed: invalid password for '{username_or_email}'"
            )
            raise ValueError('Invalid credentials')
        
        logger.info(
            f"User logged in: {user.username} (ID: {user.user_id})"
        )
        
        # Generate token
        token = self.create_token(user.user_id)
        
        return token, user

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Get user by ID.
        
        Args:
            user_id: User's unique identifier
            
        Returns:
            User instance or None if not found
            
        Example:
            >>> user = auth_service.get_user_by_id(42)
        """
        return self.user_repo.get_by_id(user_id)

    def create_token(self, user_id: int) -> str:
        """
        Create a JWT token for a user.
        
        Args:
            user_id: User's unique identifier
            
        Returns:
            Encoded JWT token string
            
        Example:
            >>> token = auth_service.create_token(42)
        """
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(
                hours=self.jwt_expiration_hours
            ),
            'iat': datetime.utcnow()
        }
        
        token = jwt.encode(payload, self.jwt_secret, algorithm='HS256')
        logger.debug(f"JWT token created for user_id: {user_id}")
        
        return token

    def verify_token(self, token: str) -> dict:
        """
        Verify and decode a JWT token.
        
        Args:
            token: JWT token string
            
        Returns:
            Decoded token payload dict
            
        Raises:
            ValueError: If token is invalid or expired
            
        Example:
            >>> payload = auth_service.verify_token(token)
            >>> user_id = payload['user_id']
        """
        try:
            payload = jwt.decode(
                token,
                self.jwt_secret,
                algorithms=['HS256']
            )
            return payload
        except jwt.ExpiredSignatureError:
            logger.warning("Token verification failed: expired")
            raise ValueError('Token expired')
        except jwt.InvalidTokenError:
            logger.warning("Token verification failed: invalid")
            raise ValueError('Invalid token')

    def get_user_from_token(self, token: str) -> Optional[User]:
        """
        Get user from JWT token.
        
        Verifies token and retrieves user from database.
        
        Args:
            token: JWT token string
            
        Returns:
            User instance or None if token invalid
            
        Example:
            >>> user = auth_service.get_user_from_token(token)
            >>> if user:
            >>>     print(f"Authenticated as {user.username}")
        """
        payload = self.verify_token(token)
        
        if not payload:
            return None
        
        user_id = payload.get('user_id')
        if not user_id:
            return None
        
        return self.user_repo.get_user_by_id(user_id)

    def change_password(
        self,
        user_id: int,
        old_password: str,
        new_password: str
    ) -> bool:
        """
        Change user password.
        
        Args:
            user_id: User's unique identifier
            old_password: Current password for verification
            new_password: New password to set
            
        Returns:
            True if password changed successfully
            
        Raises:
            ValueError: If old password is incorrect or user not found
            
        Example:
            >>> success = auth_service.change_password(42, 'old', 'new')
        """
        user = self.user_repo.get_user_by_id(user_id)
        
        if not user:
            raise ValueError('User not found')
        
        # Verify old password
        if not check_password_hash(user.password_hash, old_password):
            logger.warning(
                f"Password change failed: invalid old password "
                f"for user_id {user_id}"
            )
            raise ValueError('Invalid old password')
        
        # Hash and set new password
        new_hash = generate_password_hash(
            new_password, method='pbkdf2:sha256'
        )
        user.password_hash = new_hash
        self.user_repo.commit()
        
        logger.info(f"Password changed for user_id: {user_id}")
        
        return True

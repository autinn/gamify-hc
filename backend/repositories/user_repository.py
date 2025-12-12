"""
User Repository - User data access
Handles all database operations related to users
"""

from typing import Optional
from sqlalchemy.orm import Session
from backend.database.models import User
from backend.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """
    Repository for User model operations.
    
    Provides methods for user-specific database queries including
    finding users by username/email and managing user accounts.
    
    Example:
        >>> from backend.utils.database_manager import get_db
        >>> session = get_db()
        >>> user_repo = UserRepository(session)
        >>> user = user_repo.find_by_username('john')
    """

    def __init__(self, session: Session):
        """
        Initialize user repository.
        
        Args:
            session: Database session
        """
        super().__init__(User, session)

    def find_by_username(self, username: str) -> Optional[User]:
        """
        Find a user by username.
        
        Args:
            username: Username to search for
            
        Returns:
            User instance or None if not found
            
        Example:
            >>> user = user_repo.find_by_username('john_doe')
        """
        return self.find_one(username=username)

    def find_by_email(self, email: str) -> Optional[User]:
        """
        Find a user by email address.
        
        Args:
            email: Email address to search for
            
        Returns:
            User instance or None if not found
            
        Example:
            >>> user = user_repo.find_by_email('john@minerva.edu')
        """
        return self.find_one(email=email)

    def create_user(
        self,
        username: str,
        email: str,
        password_hash: str
    ) -> User:
        """
        Create a new user account.
        
        Args:
            username: Unique username (3-50 characters)
            email: User's email address (must end with minerva.edu)
            password_hash: Bcrypt hashed password
            
        Returns:
            Created User instance
            
        Raises:
            IntegrityError: If username or email already exists
            
        Example:
            >>> from werkzeug.security import generate_password_hash
            >>> hash = generate_password_hash('password123')
            >>> user = user_repo.create_user('john', 'john@minerva.edu', hash)
            >>> user_repo.commit()
        """
        return self.create(
            username=username,
            email=email,
            password_hash=password_hash
        )

    def username_exists(self, username: str) -> bool:
        """
        Check if a username is already taken.
        
        Args:
            username: Username to check
            
        Returns:
            True if username exists, False otherwise
            
        Example:
            >>> if user_repo.username_exists('john'):
            >>>     print("Username already taken")
        """
        return self.exists(username=username)

    def email_exists(self, email: str) -> bool:
        """
        Check if an email is already registered.
        
        Args:
            email: Email address to check
            
        Returns:
            True if email exists, False otherwise
            
        Example:
            >>> if user_repo.email_exists('john@minerva.edu'):
            >>>     print("Email already registered")
        """
        return self.exists(email=email)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Get a user by their ID.
        
        Args:
            user_id: User's unique identifier
            
        Returns:
            User instance or None if not found
            
        Example:
            >>> user = user_repo.get_user_by_id(42)
        """
        return self.get_by_id(user_id)

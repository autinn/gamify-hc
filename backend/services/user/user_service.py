"""
User Service Module.

This module contains business logic for user management operations including
user creation, retrieval, updates, and user-related queries.

Classes:
    UserService: Handles user management operations
"""

from typing import Optional

from backend.database.models import User
from backend.services.base_service import BaseService


class UserService(BaseService):
    """
    Service class for user management operations.
    
    This service handles all user-related business logic including:
    - User creation and registration
    - User retrieval by ID, username, or email
    - User updates
    - User existence checks
    
    All methods that modify data require a database session to be provided
    either in the constructor or as a method parameter.
    
    Example:
        user_service = UserService(db_session=session)
        user = user_service.create_user(
            username='john',
            email='john@minerva.edu',
            hashed_password='...'
        )
    """
    
    def create_user(
        self,
        username: str,
        email: str,
        password: str = None,
        hashed_password: str = None
    ) -> User:
        """
        Create a new user in the database.
        
        This method can accept either a plain password (which will be hashed)
        or a pre-hashed password for flexibility.
        
        Args:
            username: Unique username for the user (3-50 characters)
            email: Unique email address (must end with minerva.edu)
            password: Plain text password to be hashed (mutually exclusive
                     with hashed_password)
            hashed_password: Pre-hashed password (mutually exclusive with
                            password)
        
        Returns:
            The created User object with database-generated fields populated
            
        Raises:
            IntegrityError: If username or email already exists
            ValueError: If database session is not initialized or if both/
                       neither password and hashed_password are provided
            
        Example:
            # With plain password (will be hashed)
            from backend.services.auth import AuthService
            auth_service = AuthService(...)
            
            user = user_service.create_user(
                username='john',
                email='john@minerva.edu',
                password='mypassword'
            )
            
            # Or with pre-hashed password
            hashed = auth_service.hash_password('mypassword')
            user = user_service.create_user(
                username='john',
                email='john@minerva.edu',
                hashed_password=hashed
            )
        """
        if not self.db_session:
            raise ValueError("Database session required for user creation")
        
        # Validate that exactly one of password or hashed_password is provided
        if (password is None) == (hashed_password is None):
            raise ValueError(
                "Must provide either 'password' or 'hashed_password'"
                " (but not both)"
            )
        
        # Hash password if plain password provided
        if password:
            from werkzeug.security import generate_password_hash
            hashed_password = generate_password_hash(password)
        
        # Create new user instance
        user = User(
            username=username,
            email=email,
            password_hash=hashed_password
        )
        
        # Save to database (will raise IntegrityError if duplicate)
        return self.save(user, commit=True)
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their ID.
        
        Args:
            user_id: The user's unique identifier
        
        Returns:
            User object if found, None otherwise
            
        Example:
            user = user_service.get_user_by_id(42)
            if user:
                print(f"Found user: {user.username}")
            else:
                print("User not found")
        """
        if not self.db_session:
            raise ValueError("Database session required for queries")
        
        return self.db_session.query(User).filter(
            User.user_id == user_id
        ).first()
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """
        Retrieve a user by their username.
        
        Usernames are unique in the database, so this will return at most
        one user.
        
        Args:
            username: The username to search for
        
        Returns:
            User object if found, None otherwise
            
        Example:
            user = user_service.get_user_by_username('john')
            if user:
                print(f"User ID: {user.user_id}")
        """
        if not self.db_session:
            raise ValueError("Database session required for queries")
        
        return self.db_session.query(User).filter(
            User.username == username
        ).first()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by their email address.
        
        Email addresses are unique in the database.
        
        Args:
            email: The email address to search for
        
        Returns:
            User object if found, None otherwise
            
        Example:
            user = user_service.get_user_by_email('john@minerva.edu')
        """
        if not self.db_session:
            raise ValueError("Database session required for queries")
        
        return self.db_session.query(User).filter(
            User.email == email
        ).first()
    
    def user_exists_by_username(self, username: str) -> bool:
        """
        Check if a user with the given username exists.
        
        More efficient than get_user_by_username when you only need to
        know if the user exists without loading the full object.
        
        Args:
            username: The username to check
        
        Returns:
            True if user exists, False otherwise
            
        Example:
            if user_service.user_exists_by_username('john'):
                return jsonify({'error': 'Username taken'}), 400
        """
        if not self.db_session:
            raise ValueError("Database session required for queries")
        
        return self.db_session.query(User).filter(
            User.username == username
        ).count() > 0
    
    def user_exists_by_email(self, email: str) -> bool:
        """
        Check if a user with the given email exists.
        
        Args:
            email: The email address to check
        
        Returns:
            True if user exists, False otherwise
            
        Example:
            if user_service.user_exists_by_email('john@minerva.edu'):
                return jsonify({'error': 'Email already registered'}), 400
        """
        if not self.db_session:
            raise ValueError("Database session required for queries")
        
        return self.db_session.query(User).filter(
            User.email == email
        ).count() > 0
    
    def authenticate_user(
        self,
        username: str,
        password: str,
        auth_service
    ) -> Optional[User]:
        """
        Authenticate a user with username and password.
        
        This method combines user lookup and password verification.
        It requires an AuthService instance for password verification.
        
        Args:
            username: The username to authenticate
            password: The plain text password to verify
            auth_service: AuthService instance for password verification
        
        Returns:
            User object if authentication succeeds, None otherwise
            
        Example:
            user = user_service.authenticate_user(
                username='john',
                password='mypassword',
                auth_service=auth_service
            )
            if user:
                token = auth_service.create_token(user.user_id)
                return jsonify({'token': token})
            else:
                return jsonify({'error': 'Invalid credentials'}), 401
        """
        if not self.db_session:
            raise ValueError("Database session required for authentication")
        
        # Get user by username or email
        user = self.get_user_by_username(username)
        if not user:
            # Try email lookup if username lookup failed
            user = self.get_user_by_email(username.lower())
        
        if not user:
            return None
        
        # Verify password using auth service
        if not auth_service.verify_password(user.password_hash, password):
            return None
        
        return user
    
    def to_dict(self, user: User, include_password: bool = False) -> dict:
        """
        Convert a User object to a dictionary for API responses.
        
        By default, the password field is excluded for security.
        Use include_password=True only for specific admin operations.
        
        Args:
            user: User object to convert
            include_password: Whether to include password hash (default: False)
        
        Returns:
            Dictionary representation of the user
            
        Example:
            user_dict = user_service.to_dict(user)
            return jsonify(user_dict), 200
        """
        data = {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.isoformat()
        }
        
        if include_password:
            data['password'] = user.password
        
        return data

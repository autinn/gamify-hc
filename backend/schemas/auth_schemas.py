"""
Authentication Schemas - DTOs for auth operations
Data transfer objects for registration, login, and user responses
"""

from dataclasses import dataclass
from typing import Optional

from backend.database.models import User


@dataclass
class RegisterRequest:
    """Request schema for user registration."""
    username: str
    email: str
    password: str


@dataclass
class LoginRequest:
    """Request schema for user login."""
    username: str
    password: str


@dataclass
class UserResponse:
    """Response schema for user data."""
    user_id: int
    username: str
    email: str
    created_at: Optional[str] = None

    @classmethod
    def from_model(cls, user: User) -> 'UserResponse':
        """
        Create UserResponse from User model.
        
        Args:
            user: User model instance
            
        Returns:
            UserResponse instance
        """
        return cls(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            created_at=(
                user.created_at.isoformat()
                if user.created_at else None
            )
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
        }


@dataclass
class TokenResponse:
    """Response schema for authentication with token."""
    access_token: str
    user_id: int
    username: str
    email: str
    created_at: Optional[str] = None

    @classmethod
    def from_user_and_token(
        cls,
        user: User,
        token: str
    ) -> 'TokenResponse':
        """
        Create TokenResponse from User model and token.
        
        Args:
            user: User model instance
            token: JWT token string
            
        Returns:
            TokenResponse instance
        """
        return cls(
            access_token=token,
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            created_at=(
                user.created_at.isoformat()
                if user.created_at else None
            )
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'access_token': self.access_token,
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
        }


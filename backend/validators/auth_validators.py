"""
Authentication Validators - Input validation for auth operations
Validates usernames, emails, and passwords with clear error messages
"""

import re


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_username(username: str) -> None:
    """
    Validate username format and length.
    
    Rules:
    - Required (not empty)
    - Between 3 and 50 characters
    
    Args:
        username: Username to validate
        
    Raises:
        ValidationError: If validation fails
        
    Example:
        >>> validate_username('john_doe')  # OK
        >>> validate_username('ab')  # Raises ValidationError
    """
    if not username:
        raise ValidationError('Username is required')
    
    if not isinstance(username, str):
        raise ValidationError('Username must be a string')
    
    username = username.strip()
    
    if len(username) < 3:
        raise ValidationError(
            'Username must be at least 3 characters long'
        )
    
    if len(username) > 50:
        raise ValidationError(
            'Username must be at most 50 characters long'
        )


def validate_email(email: str) -> None:
    """
    Validate email format and domain.
    
    Rules:
    - Required (not empty)
    - Valid email format (basic check)
    - Must end with 'minerva.edu'
    
    Args:
        email: Email address to validate
        
    Raises:
        ValidationError: If validation fails
        
    Example:
        >>> validate_email('john@minerva.edu')  # OK
        >>> validate_email('john@gmail.com')  # Raises ValidationError
    """
    if not email:
        raise ValidationError('Email is required')
    
    if not isinstance(email, str):
        raise ValidationError('Email must be a string')
    
    email = email.strip().lower()
    
    # Basic email format check
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        raise ValidationError('Invalid email format')
    
    # Check minerva.edu domain
    if not email.endswith('minerva.edu'):
        raise ValidationError('Email must end with minerva.edu')


def validate_password(password: str) -> None:
    """
    Validate password strength.
    
    Rules:
    - Required (not empty)
    - At least 8 characters long
    
    Args:
        password: Password to validate
        
    Raises:
        ValidationError: If validation fails
        
    Example:
        >>> validate_password('secure123')  # OK
        >>> validate_password('short')  # Raises ValidationError
    """
    if not password:
        raise ValidationError('Password is required')
    
    if not isinstance(password, str):
        raise ValidationError('Password must be a string')
    
    if len(password) < 8:
        raise ValidationError(
            'Password must be at least 8 characters long'
        )

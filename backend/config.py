"""
Configuration module for Gamify-HC backend.

This module centralizes all environment variable loading and configuration
management. It provides type-safe access to configuration values with
sensible defaults for development.

Environment variables should be defined in a .env file or set in the
environment. See .env.example for available configuration options.
"""

import os
from typing import Optional


def _str_to_bool(value: Optional[str], default: bool = False) -> bool:
    """
    Convert common string representations to boolean values.
    
    Args:
        value: String value to convert
        default: Default value if input is None
        
    Returns:
        Boolean value
    """
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y"}


def _get_int(key: str, default: int) -> int:
    """
    Get an integer environment variable with a default value.
    
    Args:
        key: Environment variable name
        default: Default value if not set or invalid
        
    Returns:
        Integer value
    """
    try:
        return int(os.getenv(key, default))
    except (ValueError, TypeError):
        return default


class Config:
    """
    Application configuration loaded from environment variables.
    
    All configuration values are loaded from the environment with sensible
    defaults for development. For production, ensure all sensitive values
    (especially JWT_SECRET_KEY and DATABASE_URL) are properly configured.
    """
    
    # Database Configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://gamify:gamify_secret@localhost:5432/gamify_hc"
    )
    
    SQLALCHEMY_ECHO: bool = _str_to_bool(
        os.getenv("SQLALCHEMY_ECHO"),
        default=False
    )
    
    SQLALCHEMY_POOL_SIZE: int = _get_int("SQLALCHEMY_POOL_SIZE", 10)
    SQLALCHEMY_MAX_OVERFLOW: int = _get_int("SQLALCHEMY_MAX_OVERFLOW", 20)
    SQLALCHEMY_POOL_PRE_PING: bool = _str_to_bool(
        os.getenv("SQLALCHEMY_POOL_PRE_PING"),
        default=True
    )
    SQLALCHEMY_POOL_RECYCLE: int = _get_int("SQLALCHEMY_POOL_RECYCLE", 300)
    
    AUTO_SEED_DATABASE: bool = _str_to_bool(
        os.getenv("AUTO_SEED_DATABASE"),
        default=True
    )
    
    # Flask Application Configuration
    FLASK_DEBUG: bool = _str_to_bool(
        os.getenv("FLASK_DEBUG"),
        default=True
    )
    
    FLASK_HOST: str = os.getenv("FLASK_HOST", "0.0.0.0")
    FLASK_PORT: int = _get_int("FLASK_PORT", 5001)
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    
    # JWT Configuration
    JWT_SECRET_KEY: str = os.getenv(
        "JWT_SECRET_KEY",
        "dev-secret-key-change-in-production"
    )
    
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_HOURS: int = _get_int("JWT_EXPIRATION_HOURS", 24)
    
    @classmethod
    def validate(cls) -> None:
        """
        Validate critical configuration values.
        
        Raises:
            ValueError: If required configuration is missing or invalid
        """
        if not cls.DATABASE_URL:
            raise ValueError(
                "DATABASE_URL is required. "
                "Please set it in your .env file or environment."
            )
        
        # Warn about insecure JWT secret in production (but don't fail)
        if (cls.FLASK_ENV == "production" and
                cls.JWT_SECRET_KEY == "dev-secret-key-change-in-production"):
            import warnings
            warnings.warn(
                "JWT_SECRET_KEY is set to the default development key in production! "
                "This is insecure. Please set a unique secret key.",
                UserWarning,
                stacklevel=2
            )
    
    @classmethod
    def get_database_config(cls) -> dict:
        """
        Get database configuration as a dictionary.
        
        Returns:
            Dictionary with database configuration
        """
        return {
            "database_url": cls.DATABASE_URL,
            "echo": cls.SQLALCHEMY_ECHO,
            "pool_size": cls.SQLALCHEMY_POOL_SIZE,
            "max_overflow": cls.SQLALCHEMY_MAX_OVERFLOW,
            "pool_pre_ping": cls.SQLALCHEMY_POOL_PRE_PING,
            "pool_recycle": cls.SQLALCHEMY_POOL_RECYCLE,
            "auto_seed": cls.AUTO_SEED_DATABASE,
        }
    
    @classmethod
    def get_flask_config(cls) -> dict:
        """
        Get Flask configuration as a dictionary.
        
        Returns:
            Dictionary with Flask configuration
        """
        return {
            "debug": cls.FLASK_DEBUG,
            "host": cls.FLASK_HOST,
            "port": cls.FLASK_PORT,
        }
    
    @classmethod
    def get_jwt_config(cls) -> dict:
        """
        Get JWT configuration as a dictionary.
        
        Returns:
            Dictionary with JWT configuration
        """
        return {
            "secret_key": cls.JWT_SECRET_KEY,
            "algorithm": cls.JWT_ALGORITHM,
            "expiration_hours": cls.JWT_EXPIRATION_HOURS,
        }

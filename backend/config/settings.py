"""
Application Settings - 12-Factor Configuration
All configuration loaded from environment variables
"""

import os
from typing import List, Optional


def _str_to_bool(value: Optional[str], default: bool = False) -> bool:
    """Convert string representation to boolean."""
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y"}


def _str_to_int(value: Optional[str], default: int) -> int:
    """Convert string to integer with default."""
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def _parse_list(value: Optional[str], delimiter: str = ",") -> List[str]:
    """Parse comma-separated string to list."""
    if not value:
        return []
    return [item.strip() for item in value.split(delimiter) if item.strip()]


class Settings:
    """
    Application settings loaded from environment variables.
    
    This class follows 12-Factor App methodology (Factor III: Config)
    by storing all configuration in environment variables, making it
    easy to change config without code changes.
    
    Attributes:
        DATABASE_URL: PostgreSQL connection string
        SQLALCHEMY_ECHO: Whether to log SQL queries
        FLASK_ENV: Environment (development, production, testing)
        HOST: Host to bind server to
        PORT: Port to run server on
        JWT_SECRET_KEY: Secret key for JWT tokens
        JWT_EXPIRATION_HOURS: Token expiration time
        CORS_ORIGINS: Allowed CORS origins
        LOG_LEVEL: Logging level
        LOG_FORMAT: Log format (json or text)
        APP_VERSION: Application version
        APP_NAME: Application name
        GUNICORN_WORKERS: Number of Gunicorn workers
        GUNICORN_THREADS: Threads per worker
        GUNICORN_TIMEOUT: Worker timeout
        DEBUG: Debug mode flag
        AUTO_RELOAD: Auto-reload on changes
    """

    def __init__(self):
        """Initialize settings from environment variables."""
        # Database Configuration
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        if not self.DATABASE_URL:
            raise ValueError(
                "DATABASE_URL environment variable is required. "
                "Example: postgresql://user:pass@localhost:5432/gamify_hc"
            )
        
        self.SQLALCHEMY_ECHO = _str_to_bool(
            os.getenv("SQLALCHEMY_ECHO"),
            default=False
        )

        # Server Configuration
        self.FLASK_ENV = os.getenv("FLASK_ENV", "production")
        self.HOST = os.getenv("HOST", "0.0.0.0")
        self.PORT = _str_to_int(os.getenv("PORT"), default=5001)

        # Security & Authentication
        self.JWT_SECRET_KEY = os.getenv(
            "JWT_SECRET_KEY",
            "dev-secret-key-change-in-production"
        )
        
        # Warn if using default JWT secret in production
        if (self.FLASK_ENV == "production" and
                self.JWT_SECRET_KEY == "dev-secret-key-change-in-production"):
            import warnings
            warnings.warn(
                "Using default JWT_SECRET_KEY in production! "
                "Set JWT_SECRET_KEY environment variable.",
                UserWarning
            )
        
        self.JWT_EXPIRATION_HOURS = _str_to_int(
            os.getenv("JWT_EXPIRATION_HOURS"),
            default=24
        )

        # CORS Configuration
        cors_origins = os.getenv("CORS_ORIGINS", "*")
        if cors_origins == "*":
            self.CORS_ORIGINS = "*"
        else:
            self.CORS_ORIGINS = _parse_list(cors_origins)

        # Logging Configuration
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
        self.LOG_FORMAT = os.getenv("LOG_FORMAT", "text").lower()
        
        # Validate log level
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if self.LOG_LEVEL not in valid_levels:
            self.LOG_LEVEL = "INFO"
        
        # Validate log format
        if self.LOG_FORMAT not in {"json", "text"}:
            self.LOG_FORMAT = "text"

        # Application Configuration
        self.APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
        self.APP_NAME = os.getenv("APP_NAME", "gamify-hc")

        # Gunicorn Configuration (Production)
        self.GUNICORN_WORKERS = _str_to_int(
            os.getenv("GUNICORN_WORKERS"),
            default=4
        )
        self.GUNICORN_THREADS = _str_to_int(
            os.getenv("GUNICORN_THREADS"),
            default=2
        )
        self.GUNICORN_TIMEOUT = _str_to_int(
            os.getenv("GUNICORN_TIMEOUT"),
            default=30
        )

        # Development Configuration
        self.DEBUG = _str_to_bool(os.getenv("DEBUG"), default=False)
        self.AUTO_RELOAD = _str_to_bool(
            os.getenv("AUTO_RELOAD"), default=False
        )

    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.FLASK_ENV == "development"

    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.FLASK_ENV == "production"

    @property
    def is_testing(self) -> bool:
        """Check if running in testing mode."""
        return self.FLASK_ENV == "testing"

    def __repr__(self) -> str:
        """String representation (hides sensitive data)."""
        return (
            f"Settings("
            f"env={self.FLASK_ENV}, "
            f"host={self.HOST}, "
            f"port={self.PORT}, "
            f"db=<hidden>, "
            f"jwt_secret=<hidden>)"
        )


# Singleton instance
_settings: Optional[Settings] = None


def get_settings() -> Settings:
    """
    Get the application settings singleton.
    
    This function provides access to the global settings instance,
    creating it on first access. This ensures settings are loaded
    once and reused throughout the application.
    
    Returns:
        Settings: The application settings instance
        
    Example:
        >>> from backend.config import get_settings
        >>> settings = get_settings()
        >>> print(settings.PORT)
        5001
    """
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


def reload_settings() -> Settings:
    """
    Reload settings from environment variables.
    
    Useful for testing when environment variables change.
    
    Returns:
        Settings: New settings instance
    """
    global _settings
    _settings = Settings()
    return _settings

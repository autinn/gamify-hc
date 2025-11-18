"""
Database manager for Flask application
Centralized database session management for Flask application
"""

from sqlalchemy.orm import Session
from backend.database.setup import create_database, DEFAULT_DATABASE_URL


class DatabaseManager:
    """Manages database connections and sessions"""

    def __init__(self, database_url=None):
        """Initialize database manager with optional custom database URL"""
        self.db_url = database_url or DEFAULT_DATABASE_URL
        # Use create_database() to ensure proper initialization and seeding
        self.engine, self.SessionLocal = create_database(
            database_url=self.db_url,
            auto_seed=True
        )

    def get_session(self) -> Session:
        """Create and return a new database session"""
        return self.SessionLocal()


def get_db():
    """
    Get database session from Flask application context.

    This function retrieves the database session that is injected by
    app.py. The session is used to perform database queries within
    route handlers.

    Returns:
        Session: SQLAlchemy database session object

    Note:
        The database session must be closed after use to prevent
        connection leaks. This is typically done in a finally block.
    """
    from flask import current_app
    return current_app.db_session()

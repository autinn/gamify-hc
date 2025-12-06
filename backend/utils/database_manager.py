"""
Database manager for Flask application
Centralized database session management for Flask application
"""

from sqlalchemy.orm import Session
from backend.database.setup import create_database, DEFAULT_DATABASE_URL


class DatabaseManager:
    """Manages database connections and sessions"""

    def __init__(self, database_url=None, engine=None, SessionLocal=None, auto_seed=True):
        """
        Initialize database manager with optional custom database URL or engine.

        Args:
            database_url: Database connection string (ignored if engine provided)
            engine: Optional SQLAlchemy engine to use (for testing)
            SessionLocal: Optional session factory to use (for testing)
            auto_seed: If True, seed database with initial data if empty. Default True.
        """
        if engine is not None and SessionLocal is not None:
            # Use provided engine and session factory (for testing)
            self.engine = engine
            self.SessionLocal = SessionLocal
            self.db_url = str(engine.url)
        else:
            # Create new engine and session factory
            self.db_url = database_url or DEFAULT_DATABASE_URL
            # Use create_database() to ensure proper initialization and seeding
            self.engine, self.SessionLocal = create_database(
                database_url=self.db_url,
                auto_seed=auto_seed
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

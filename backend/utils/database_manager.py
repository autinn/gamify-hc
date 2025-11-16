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

"""
Database utilities
Centralized database session management for Flask application
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.database.database import Base, DEFAULT_DATABASE_URL


class DatabaseManager:
    """Manages database connections and sessions"""
    
    def __init__(self, database_url=None):
        """Initialize database manager with optional custom database URL"""
        self.db_url = database_url or DEFAULT_DATABASE_URL
        self.engine = create_engine(self.db_url)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def get_session(self) -> Session:
        """Create and return a new database session"""
        return self.SessionLocal()

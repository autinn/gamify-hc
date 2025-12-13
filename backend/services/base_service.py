"""
Base Service Module.

This module provides the abstract base class for all service layer classes.
It defines common patterns, database session management, and shared utilities
that all services can inherit.

Classes:
    BaseService: Abstract base class for business logic services
"""

from abc import ABC
from typing import Optional
from sqlalchemy.orm import Session


class BaseService(ABC):
    """
    Abstract base class for all business logic services.
    
    This class provides common functionality for services including:
    - Database session management
    - Transaction handling helpers
    - Common error handling patterns
    - Logging utilities
    
    All service classes should inherit from this base to ensure consistent
    patterns across the application.
    
    Attributes:
        db_session (Session): SQLAlchemy database session for queries
        
    Example:
        class UserService(BaseService):
            def create_user(self, username, email):
                user = User(username=username, email=email)
                return self.save(user)
    """
    
    def __init__(self, db_session: Optional[Session] = None):
        """
        Initialize the service with a database session.
        
        Args:
            db_session: SQLAlchemy session for database operations.
                       If None, service methods should accept session as parameter.
        """
        self.db_session = db_session
    
    def save(self, entity, commit: bool = True):
        """
        Save an entity to the database.
        
        This is a convenience method that handles the common pattern of
        adding an entity and optionally committing the transaction.
        
        Args:
            entity: Database model instance to save
            commit: Whether to commit the transaction immediately
            
        Returns:
            The saved entity with updated fields (e.g., generated ID)
            
        Raises:
            IntegrityError: If database constraints are violated
            SQLAlchemyError: For other database errors
            
        Example:
            user = User(username='john', email='john@example.com')
            saved_user = self.save(user)
        """
        if not self.db_session:
            raise ValueError("Database session not initialized")
            
        self.db_session.add(entity)
        if commit:
            self.db_session.commit()
            self.db_session.refresh(entity)
        return entity
    
    def delete(self, entity, commit: bool = True):
        """
        Delete an entity from the database.
        
        Args:
            entity: Database model instance to delete
            commit: Whether to commit the transaction immediately
            
        Raises:
            SQLAlchemyError: If deletion fails
        """
        if not self.db_session:
            raise ValueError("Database session not initialized")
            
        self.db_session.delete(entity)
        if commit:
            self.db_session.commit()
    
    def commit(self):
        """
        Commit the current transaction.
        
        Use this when you've made multiple changes and want to commit them
        all at once, or when using save/delete with commit=False.
        
        Raises:
            SQLAlchemyError: If commit fails
        """
        if not self.db_session:
            raise ValueError("Database session not initialized")
        self.db_session.commit()
    
    def rollback(self):
        """
        Rollback the current transaction.
        
        Use this in exception handlers to undo changes when an error occurs.
        
        Example:
            try:
                # ... database operations
                self.commit()
            except Exception:
                self.rollback()
                raise
        """
        if not self.db_session:
            raise ValueError("Database session not initialized")
        self.db_session.rollback()
    
    def refresh(self, entity):
        """
        Refresh an entity from the database.
        
        This reloads the entity's state from the database, useful after
        commits to ensure you have the latest data.
        
        Args:
            entity: Database model instance to refresh
        """
        if not self.db_session:
            raise ValueError("Database session not initialized")
        self.db_session.refresh(entity)

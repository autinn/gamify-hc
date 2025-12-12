"""
Base Repository - Common CRUD operations
Provides base class for all repositories with common database operations
"""

from typing import Any, Generic, List, Optional, Type, TypeVar
from sqlalchemy.orm import Session
from backend.database.models import Base

# Generic type for model classes
ModelType = TypeVar('ModelType', bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Base repository providing common CRUD operations.
    
    This class provides a foundation for all repositories with
    standard create, read, update, delete operations. Specific
    repositories inherit from this and add model-specific methods.
    
    Attributes:
        model: SQLAlchemy model class
        session: Database session
        
    Example:
        >>> class UserRepository(BaseRepository[User]):
        >>>     def __init__(self, session):
        >>>         super().__init__(User, session)
        >>>
        >>>     def find_by_email(self, email):
        >>>         return self.find_one(email=email)
    """

    def __init__(self, model: Type[ModelType], session: Session):
        """
        Initialize repository.
        
        Args:
            model: SQLAlchemy model class
            session: Database session
        """
        self.model = model
        self.session = session

    def get_by_id(self, id_value: Any) -> Optional[ModelType]:
        """
        Get a single record by its primary key.
        
        Args:
            id_value: Primary key value
            
        Returns:
            Model instance or None if not found
        """
        return self.session.query(self.model).get(id_value)

    def get_all(self, limit: Optional[int] = None) -> List[ModelType]:
        """
        Get all records.
        
        Args:
            limit: Optional limit on number of records
            
        Returns:
            List of model instances
        """
        query = self.session.query(self.model)
        if limit:
            query = query.limit(limit)
        return query.all()

    def find_one(self, **filters) -> Optional[ModelType]:
        """
        Find a single record matching filters.
        
        Args:
            **filters: Field=value filters
            
        Returns:
            Model instance or None if not found
            
        Example:
            >>> user = repo.find_one(username='john')
        """
        return self.session.query(self.model).filter_by(**filters).first()

    def find_all(self, **filters) -> List[ModelType]:
        """
        Find all records matching filters.
        
        Args:
            **filters: Field=value filters
            
        Returns:
            List of model instances
            
        Example:
            >>> active_users = repo.find_all(is_active=True)
        """
        return self.session.query(self.model).filter_by(**filters).all()

    def create(self, **data) -> ModelType:
        """
        Create a new record.
        
        Args:
            **data: Field=value data for new record
            
        Returns:
            Created model instance
            
        Example:
            >>> user = repo.create(username='john', email='john@example.com')
        """
        instance = self.model(**data)
        self.session.add(instance)
        self.session.flush()  # Get ID without committing
        return instance

    def update(self, id_value: Any, **data) -> Optional[ModelType]:
        """
        Update a record by ID.
        
        Args:
            id_value: Primary key value
            **data: Field=value data to update
            
        Returns:
            Updated model instance or None if not found
            
        Example:
            >>> user = repo.update(1, email='newemail@example.com')
        """
        instance = self.get_by_id(id_value)
        if instance:
            for key, value in data.items():
                setattr(instance, key, value)
            self.session.flush()
        return instance

    def delete(self, id_value: Any) -> bool:
        """
        Delete a record by ID.
        
        Args:
            id_value: Primary key value
            
        Returns:
            True if deleted, False if not found
            
        Example:
            >>> success = repo.delete(1)
        """
        instance = self.get_by_id(id_value)
        if instance:
            self.session.delete(instance)
            self.session.flush()
            return True
        return False

    def count(self, **filters) -> int:
        """
        Count records matching filters.
        
        Args:
            **filters: Optional field=value filters
            
        Returns:
            Count of matching records
            
        Example:
            >>> total_users = repo.count()
            >>> active_count = repo.count(is_active=True)
        """
        query = self.session.query(self.model)
        if filters:
            query = query.filter_by(**filters)
        return query.count()

    def exists(self, **filters) -> bool:
        """
        Check if any record matching filters exists.
        
        Args:
            **filters: Field=value filters
            
        Returns:
            True if at least one record exists
            
        Example:
            >>> if repo.exists(username='john'):
            >>>     print("Username taken")
        """
        return self.count(**filters) > 0

    def commit(self):
        """Commit the current transaction."""
        self.session.commit()

    def rollback(self):
        """Rollback the current transaction."""
        self.session.rollback()

    def close(self):
        """Close the session."""
        self.session.close()

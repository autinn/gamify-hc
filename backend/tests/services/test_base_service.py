"""
Tests for BaseService class.

This module tests the common database operations provided by BaseService:
- save() - entity persistence
- delete() - entity removal
- commit() / rollback() - transaction management
- refresh() - entity refresh
- Error handling when db_session is None
"""

import pytest
from backend.services.base_service import BaseService
from backend.database.models import Course


class ConcreteService(BaseService):
    """Concrete implementation of BaseService for testing."""
    pass


class TestBaseServiceSave:
    """Tests for BaseService.save() method."""

    def test_save_entity_with_commit(self, clean_db):
        """Test saving an entity with immediate commit."""
        service = ConcreteService(db_session=clean_db)
        course = Course(
            title="Test Course",
            description="Test Description"
        )

        saved_course = service.save(course, commit=True)

        assert saved_course.course_id is not None
        assert saved_course.title == "Test Course"
        # Verify it's in the database
        found = clean_db.query(Course).filter(
            Course.course_id == saved_course.course_id
        ).first()
        assert found is not None

    def test_save_entity_without_commit(self, clean_db):
        """Test saving an entity without commit (staged only)."""
        service = ConcreteService(db_session=clean_db)
        course = Course(
            title="Uncommitted Course",
            description="Not yet committed"
        )

        saved_course = service.save(course, commit=False)

        # Entity is added but not committed
        assert course in clean_db.new or course in clean_db
        # Rollback to verify it wasn't persisted
        clean_db.rollback()

    def test_save_without_session_raises_error(self):
        """Test that save raises ValueError when db_session is None."""
        service = ConcreteService(db_session=None)
        course = Course(
            title="Test Course",
            description="Test Description"
        )

        with pytest.raises(ValueError, match="Database session not initialized"):
            service.save(course)


class TestBaseServiceDelete:
    """Tests for BaseService.delete() method."""

    def test_delete_entity_with_commit(self, clean_db):
        """Test deleting an entity with immediate commit."""
        # First create an entity
        course = Course(title="To Delete", description="Will be deleted")
        clean_db.add(course)
        clean_db.commit()
        clean_db.refresh(course)
        course_id = course.course_id

        service = ConcreteService(db_session=clean_db)
        service.delete(course, commit=True)

        # Verify it's gone
        found = clean_db.query(Course).filter(
            Course.course_id == course_id
        ).first()
        assert found is None

    def test_delete_entity_without_commit(self, clean_db):
        """Test deleting an entity without commit."""
        course = Course(title="Maybe Delete", description="Might be deleted")
        clean_db.add(course)
        clean_db.commit()
        clean_db.refresh(course)

        service = ConcreteService(db_session=clean_db)
        service.delete(course, commit=False)

        # Rollback should restore the entity
        clean_db.rollback()
        found = clean_db.query(Course).filter(
            Course.course_id == course.course_id
        ).first()
        assert found is not None

    def test_delete_without_session_raises_error(self):
        """Test that delete raises ValueError when db_session is None."""
        service = ConcreteService(db_session=None)
        course = Course(title="Test", description="Test")

        with pytest.raises(ValueError, match="Database session not initialized"):
            service.delete(course)


class TestBaseServiceTransactions:
    """Tests for BaseService transaction methods."""

    def test_commit(self, clean_db):
        """Test explicit commit."""
        service = ConcreteService(db_session=clean_db)
        course = Course(title="Commit Test", description="Testing commit")
        clean_db.add(course)

        service.commit()

        # Verify committed
        clean_db.expire_all()
        found = clean_db.query(Course).filter(
            Course.title == "Commit Test"
        ).first()
        assert found is not None

    def test_commit_without_session_raises_error(self):
        """Test that commit raises ValueError when db_session is None."""
        service = ConcreteService(db_session=None)

        with pytest.raises(ValueError, match="Database session not initialized"):
            service.commit()

    def test_rollback(self, clean_db):
        """Test explicit rollback."""
        service = ConcreteService(db_session=clean_db)
        course = Course(title="Rollback Test", description="Testing rollback")
        clean_db.add(course)

        service.rollback()

        # Verify not persisted
        found = clean_db.query(Course).filter(
            Course.title == "Rollback Test"
        ).first()
        assert found is None

    def test_rollback_without_session_raises_error(self):
        """Test that rollback raises ValueError when db_session is None."""
        service = ConcreteService(db_session=None)

        with pytest.raises(ValueError, match="Database session not initialized"):
            service.rollback()


class TestBaseServiceRefresh:
    """Tests for BaseService.refresh() method."""

    def test_refresh_entity(self, clean_db):
        """Test refreshing an entity from database."""
        course = Course(title="Original", description="Original desc")
        clean_db.add(course)
        clean_db.commit()
        clean_db.refresh(course)

        service = ConcreteService(db_session=clean_db)

        # Simulate external update (in real scenario, another session)
        # For this test, we just verify refresh doesn't error
        service.refresh(course)

        assert course.title == "Original"

    def test_refresh_without_session_raises_error(self):
        """Test that refresh raises ValueError when db_session is None."""
        service = ConcreteService(db_session=None)
        course = Course(title="Test", description="Test")

        with pytest.raises(ValueError, match="Database session not initialized"):
            service.refresh(course)


class TestBaseServiceInit:
    """Tests for BaseService initialization."""

    def test_init_with_session(self, clean_db):
        """Test initialization with a database session."""
        service = ConcreteService(db_session=clean_db)

        assert service.db_session is clean_db

    def test_init_without_session(self):
        """Test initialization without a database session."""
        service = ConcreteService()

        assert service.db_session is None

    def test_init_with_none_session(self):
        """Test initialization with explicit None session."""
        service = ConcreteService(db_session=None)

        assert service.db_session is None


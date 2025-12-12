"""
Course Repository - Course/Unit/Concept data access
Handles all database operations related to courses, units, and concepts
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from backend.database.models import Course, Unit, Concept
from backend.repositories.base_repository import BaseRepository


class CourseRepository(BaseRepository[Course]):
    """
    Repository for Course, Unit, and Concept model operations.
    
    Provides methods for querying the course hierarchy including
    courses, their units, and associated concepts.
    
    Example:
        >>> from backend.utils.database_manager import get_db
        >>> session = get_db()
        >>> course_repo = CourseRepository(session)
        >>> courses = course_repo.get_all_courses()
    """

    def __init__(self, session: Session):
        """
        Initialize course repository.
        
        Args:
            session: Database session
        """
        super().__init__(Course, session)

    def get_all_courses(self) -> List[Course]:
        """
        Get all courses.
        
        Returns:
            List of all Course instances
            
        Example:
            >>> courses = course_repo.get_all_courses()
            >>> for course in courses:
            >>>     print(course.title)
        """
        return self.get_all()

    def get_course_by_id(self, course_id: int) -> Optional[Course]:
        """
        Get a course by its ID.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            Course instance or None if not found
            
        Example:
            >>> course = course_repo.get_course_by_id(1)
        """
        return self.get_by_id(course_id)

    def get_units_by_course(self, course_id: int) -> List[Unit]:
        """
        Get all units for a specific course.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            List of Unit instances ordered by order_index
            
        Example:
            >>> units = course_repo.get_units_by_course(1)
        """
        return (
            self.session.query(Unit)
            .filter(Unit.course_id == course_id)
            .order_by(Unit.order_index)
            .all()
        )

    def get_unit_by_id(self, unit_id: int) -> Optional[Unit]:
        """
        Get a unit by its ID.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            Unit instance or None if not found
            
        Example:
            >>> unit = course_repo.get_unit_by_id(5)
        """
        return self.session.query(Unit).get(unit_id)

    def get_concepts_by_unit(self, unit_id: int) -> List[Concept]:
        """
        Get all concepts for a specific unit.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            List of Concept instances
            
        Example:
            >>> concepts = course_repo.get_concepts_by_unit(5)
        """
        return (
            self.session.query(Concept)
            .filter(Concept.unit_id == unit_id)
            .all()
        )

    def get_concept_by_id(self, concept_id: int) -> Optional[Concept]:
        """
        Get a concept by its ID.
        
        Args:
            concept_id: Concept unique identifier
            
        Returns:
            Concept instance or None if not found
            
        Example:
            >>> concept = course_repo.get_concept_by_id(10)
        """
        return self.session.query(Concept).get(concept_id)

    def get_course_with_units(self, course_id: int) -> Optional[Course]:
        """
        Get a course with all its units loaded.
        
        Uses eager loading for better performance.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            Course instance with units loaded, or None if not found
            
        Example:
            >>> course = course_repo.get_course_with_units(1)
            >>> for unit in course.units:
            >>>     print(unit.title)
        """
        from sqlalchemy.orm import joinedload
        
        return (
            self.session.query(Course)
            .options(joinedload(Course.units))
            .filter(Course.course_id == course_id)
            .first()
        )

    def get_unit_with_concepts(self, unit_id: int) -> Optional[Unit]:
        """
        Get a unit with all its concepts loaded.
        
        Uses eager loading for better performance.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            Unit instance with concepts loaded, or None if not found
            
        Example:
            >>> unit = course_repo.get_unit_with_concepts(5)
            >>> for concept in unit.concepts:
            >>>     print(concept.title)
        """
        from sqlalchemy.orm import joinedload
        
        return (
            self.session.query(Unit)
            .options(joinedload(Unit.concepts))
            .filter(Unit.unit_id == unit_id)
            .first()
        )

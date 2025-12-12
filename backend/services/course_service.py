"""
Course Service - Business logic for course management
Handles course, unit, and concept operations
"""

from typing import List, Optional

from backend.database.models import Course, Unit, Concept
from backend.repositories.course_repository import CourseRepository
from backend.utils.logger import get_logger

logger = get_logger(__name__)


class CourseService:
    """
    Service for course-related operations.
    
    Handles business logic for courses, units, and concepts
    including retrieving and organizing hierarchical data.
    
    Example:
        >>> from backend.utils.database_manager import get_db
        >>> from backend.repositories.course_repository import CourseRepository
        >>> session = get_db()
        >>> course_repo = CourseRepository(session)
        >>> course_service = CourseService(course_repo)
        >>> courses = course_service.get_all_courses()
    """

    def __init__(self, course_repository: CourseRepository):
        """
        Initialize course service.
        
        Args:
            course_repository: Course data access repository
        """
        self.course_repo = course_repository

    def get_all_courses(self) -> List[Course]:
        """
        Get all available courses.
        
        Returns:
            List of all Course instances
            
        Example:
            >>> courses = course_service.get_all_courses()
        """
        logger.debug("Fetching all courses")
        courses = self.course_repo.get_all_courses()
        logger.info(f"Retrieved {len(courses)} courses")
        return courses

    def get_course_by_id(self, course_id: int) -> Optional[Course]:
        """
        Get a specific course by ID.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            Course instance or None if not found
            
        Raises:
            ValueError: If course not found
            
        Example:
            >>> course = course_service.get_course_by_id(1)
        """
        logger.debug(f"Fetching course with ID: {course_id}")
        course = self.course_repo.get_course_by_id(course_id)
        
        if not course:
            logger.warning(f"Course not found: {course_id}")
            raise ValueError(f'Course with ID {course_id} not found')
        
        logger.debug(f"Retrieved course: {course.title}")
        return course

    def get_course_units(self, course_id: int) -> List[Unit]:
        """
        Get all units for a specific course.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            List of Unit instances ordered by order_index.
            Returns empty list if course doesn't exist.
            
        Example:
            >>> units = course_service.get_course_units(1)
        """
        logger.debug(f"Fetching units for course: {course_id}")
        units = self.course_repo.get_units_by_course(course_id)
        logger.info(f"Retrieved {len(units)} units for course {course_id}")
        return units

    def get_unit_by_id(self, unit_id: int) -> Optional[Unit]:
        """
        Get a specific unit by ID.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            Unit instance or None if not found
            
        Raises:
            ValueError: If unit not found
            
        Example:
            >>> unit = course_service.get_unit_by_id(5)
        """
        logger.debug(f"Fetching unit with ID: {unit_id}")
        unit = self.course_repo.get_unit_by_id(unit_id)
        
        if not unit:
            logger.warning(f"Unit not found: {unit_id}")
            raise ValueError(f'Unit with ID {unit_id} not found')
        
        logger.debug(f"Retrieved unit: {unit.title}")
        return unit

    def get_unit_concepts(self, unit_id: int) -> List[Concept]:
        """
        Get all concepts for a specific unit.
        
        Args:
            unit_id: Unit unique identifier
            
        Returns:
            List of Concept instances.
            Returns empty list if unit doesn't exist.
            
        Example:
            >>> concepts = course_service.get_unit_concepts(5)
        """
        logger.debug(f"Fetching concepts for unit: {unit_id}")
        concepts = self.course_repo.get_concepts_by_unit(unit_id)
        logger.info(f"Retrieved {len(concepts)} concepts for unit {unit_id}")
        return concepts

    def get_concept_by_id(self, concept_id: int) -> Optional[Concept]:
        """
        Get a specific concept by ID.
        
        Args:
            concept_id: Concept unique identifier
            
        Returns:
            Concept instance or None if not found
            
        Raises:
            ValueError: If concept not found
            
        Example:
            >>> concept = course_service.get_concept_by_id(10)
        """
        logger.debug(f"Fetching concept with ID: {concept_id}")
        concept = self.course_repo.get_concept_by_id(concept_id)
        
        if not concept:
            logger.warning(f"Concept not found: {concept_id}")
            raise ValueError(f'Concept with ID {concept_id} not found')
        
        logger.debug(f"Retrieved concept: {concept.title}")
        return concept

    def get_course_hierarchy(self, course_id: int) -> Course:
        """
        Get course with full hierarchy (units and concepts).
        
        Optimized with eager loading for better performance.
        
        Args:
            course_id: Course unique identifier
            
        Returns:
            Course instance with units and concepts loaded
            
        Raises:
            ValueError: If course not found
            
        Example:
            >>> course = course_service.get_course_hierarchy(1)
            >>> for unit in course.units:
            >>>     for concept in unit.concepts:
            >>>         print(concept.title)
        """
        logger.debug(
            f"Fetching course hierarchy for course: {course_id}"
        )
        course = self.course_repo.get_course_with_units(course_id)
        
        if not course:
            raise ValueError(f'Course with ID {course_id} not found')
        
        logger.info(
            f"Retrieved course hierarchy: {course.title} "
            f"with {len(course.units)} units"
        )
        return course

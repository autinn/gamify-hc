"""
Course Service Module.

This module provides business logic for course-related operations,
including course retrieval, course units, and course data serialization.

Classes:
    CourseService: Service for managing course operations
"""

from typing import Optional, List, Dict, Any

from backend.database.models import Course, Unit
from backend.services.base_service import BaseService
from backend.services.serializers import serialize_course, serialize_unit


class CourseService(BaseService):
    """
    Service for course management operations.
    
    This service handles:
    - Course retrieval (single and multiple)
    - Course units retrieval
    - Course data serialization
    
    Inherits from BaseService for common database operations.
    
    Example:
        course_service = CourseService(db_session=db)
        courses = course_service.get_all_courses()
    """
    
    def get_all_courses(self) -> List[Dict[str, Any]]:
        """
        Retrieve all courses from the database.
        
        Returns:
            List of course dictionaries with structure:
            [{
                'id': int,
                'code': str,
                'name': str,
                'description': str
            }, ...]
            
        Example:
            courses = course_service.get_all_courses()
            for course in courses:
                print(f"{course['name']}: {course['description']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        courses = self.db_session.query(Course).all()
        return [serialize_course(c) for c in courses]
    
    def get_course_by_id(self, course_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific course by ID.
        
        Args:
            course_id: The unique identifier of the course
        
        Returns:
            Course dictionary or None if not found:
            {
                'id': int,
                'code': str,
                'name': str,
                'description': str
            }
            
        Example:
            course = course_service.get_course_by_id(1)
            if course:
                print(f"Found: {course['name']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        course = self.db_session.query(Course).filter(
            Course.course_id == course_id
        ).first()
        
        if not course:
            return None

        return serialize_course(course)
    
    def get_course_units(self, course_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all units for a specific course.
        
        Units are returned in order by their order_index field,
        representing the intended sequence for learning.
        
        Args:
            course_id: The unique identifier of the course
        
        Returns:
            List of unit dictionaries with structure:
            [{
                'id': int,
                'course_id': int,
                'name': str,
                'description': str,
                'order_index': int
            }, ...]
            
        Example:
            units = course_service.get_course_units(1)
            for unit in units:
                print(f"Unit {unit['order_index']}: {unit['name']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        units = self.db_session.query(Unit).filter(
            Unit.course_id == course_id
        ).order_by(Unit.order_index).all()

        return [serialize_unit(u) for u in units]

"""
Course Schemas - DTOs for course/unit/concept operations
Data transfer objects for course hierarchy responses
"""

from dataclasses import dataclass

from backend.database.models import Course, Unit, Concept


@dataclass
class CourseResponse:
    """Response schema for course data."""
    id: int
    code: str
    name: str
    description: str

    @classmethod
    def from_model(cls, course: Course) -> 'CourseResponse':
        """
        Create CourseResponse from Course model.
        
        Args:
            course: Course model instance
            
        Returns:
            CourseResponse instance
        """
        return cls(
            id=course.course_id,
            code=course.title,
            name=course.title,
            description=course.description or ''
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'description': self.description,
        }


@dataclass
class UnitResponse:
    """Response schema for unit data."""
    id: int
    course_id: int
    name: str
    description: str
    order_index: int

    @classmethod
    def from_model(cls, unit: Unit) -> 'UnitResponse':
        """
        Create UnitResponse from Unit model.
        
        Args:
            unit: Unit model instance
            
        Returns:
            UnitResponse instance
        """
        return cls(
            id=unit.unit_id,
            course_id=unit.course_id,
            name=unit.title,
            description=unit.description or '',
            order_index=unit.order_index or 0
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'course_id': self.course_id,
            'name': self.name,
            'description': self.description,
            'order_index': self.order_index,
        }


@dataclass
class ConceptResponse:
    """Response schema for concept data."""
    id: int
    unit_id: int
    name: str  # Frontend expects 'name' field
    definition: str

    @classmethod
    def from_model(cls, concept: Concept) -> 'ConceptResponse':
        """
        Create ConceptResponse from Concept model.
        
        Args:
            concept: Concept model instance
            
        Returns:
            ConceptResponse instance
        """
        return cls(
            id=concept.concept_id,
            unit_id=concept.unit_id,
            name=concept.title,  # Map title to name for frontend
            definition=concept.definition or ''
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'unit_id': self.unit_id,
            'name': self.name,  # Frontend expects 'name' field
            'definition': self.definition,
        }

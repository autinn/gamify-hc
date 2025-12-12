"""
Unit Service Module.

This module provides business logic for unit-related operations,
including unit retrieval and unit concepts.

Classes:
    UnitService: Service for managing unit operations
"""

from typing import Optional, List, Dict, Any

from backend.database.models import Unit, Concept
from backend.services.base_service import BaseService


class UnitService(BaseService):
    """
    Service for unit management operations.
    
    This service handles:
    - Unit retrieval
    - Unit concepts retrieval
    - Unit data serialization
    
    Inherits from BaseService for common database operations.
    
    Example:
        unit_service = UnitService(db_session=db)
        unit = unit_service.get_unit_by_id(1)
    """
    
    def get_unit_by_id(self, unit_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific unit by ID.
        
        Args:
            unit_id: The unique identifier of the unit
        
        Returns:
            Unit dictionary or None if not found:
            {
                'id': int,
                'course_id': int,
                'name': str,
                'description': str,
                'order_index': int
            }
            
        Example:
            unit = unit_service.get_unit_by_id(1)
            if unit:
                print(f"Unit: {unit['name']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        unit = self.db_session.query(Unit).filter(
            Unit.unit_id == unit_id
        ).first()
        
        if not unit:
            return None
        
        return self.serialize_unit(unit)
    
    def get_unit_concepts(self, unit_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all concepts for a specific unit.
        
        Args:
            unit_id: The unique identifier of the unit
        
        Returns:
            List of concept dictionaries with structure:
            [{
                'id': int,
                'unit_id': int,
                'name': str,
                'tag': str,
                'definition': str
            }, ...]
            
        Example:
            concepts = unit_service.get_unit_concepts(1)
            for concept in concepts:
                print(f"{concept['name']}: {concept['definition']}")
        """
        if not self.db_session:
            raise ValueError("Database session required")
        
        concepts = self.db_session.query(Concept).filter(
            Concept.unit_id == unit_id
        ).all()
        
        return [self.serialize_concept(c) for c in concepts]
    
    @staticmethod
    def serialize_unit(unit: Unit) -> Dict[str, Any]:
        """
        Convert a Unit model instance to a dictionary.
        
        Args:
            unit: The Unit model instance to serialize
        
        Returns:
            Dictionary with unit data:
            {
                'id': int,
                'course_id': int,
                'name': str,
                'description': str,
                'order_index': int
            }
        """
        return {
            'id': unit.unit_id,
            'course_id': unit.course_id,
            'name': unit.title,
            'description': unit.description,
            'order_index': unit.order_index
        }
    
    @staticmethod
    def serialize_concept(concept: Concept) -> Dict[str, Any]:
        """
        Convert a Concept model instance to a dictionary.
        
        Args:
            concept: The Concept model instance to serialize
        
        Returns:
            Dictionary with concept data:
            {
                'id': int,
                'unit_id': int,
                'name': str,
                'tag': str,
                'definition': str
            }
            
        Note:
            Currently 'tag' uses the title field as a placeholder.
            This may be updated if a separate tag field is added.
        """
        return {
            'id': concept.concept_id,
            'unit_id': concept.unit_id,
            'name': concept.title,
            # TODO: Update when tag field is added to Concept model
            'tag': concept.title,
            'definition': concept.definition
        }

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
from backend.services.serializers import serialize_unit, serialize_concept


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

        return serialize_unit(unit)
    
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

        return [serialize_concept(c) for c in concepts]

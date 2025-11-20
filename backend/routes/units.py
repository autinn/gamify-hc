"""
Unit routes blueprint.

This module handles all unit-related API endpoints for the gamify-hc
application. It provides endpoints to retrieve unit information and
associated concepts.

Endpoints:
    GET /api/units/<unit_id>: Retrieve a specific unit by ID
    GET /api/units/<unit_id>/concepts: Retrieve all concepts for a unit
"""

from flask import Blueprint, jsonify
from backend.database.models import Unit, Concept
from backend.utils.database_manager import get_db

# Create blueprint for unit-related routes
# All routes in this blueprint will be prefixed with '/api'
units_bp = Blueprint('units', __name__, url_prefix='/api')


@units_bp.route('/units/<int:unit_id>', methods=['GET'])
def get_unit(unit_id):
    """
    Retrieve a specific unit by its ID.

    This endpoint fetches unit details including its ID, course
    association, name, description, and order index. If the unit is not
    found, returns a 404 error.

    Args:
        unit_id (int): The unique identifier of the unit to retrieve

    Returns:
        JSON response with the following structure:
        {
            'id': int,           # Unit ID
            'course_id': int,    # ID of the course this unit belongs to
            'name': str,         # Unit name/title
            'description': str, # Unit description
            'order_index': int  # Display order within the course
        }

    HTTP Status Codes:
        200: Success - Unit found and returned
        404: Not Found - Unit with the given ID does not exist

    Example:
        GET /api/units/1
        Returns: {"id": 1, "course_id": 1, "name": "...", ...}
    """
    db = get_db()
    try:
        unit = db.query(Unit).filter(
            Unit.unit_id == unit_id
        ).first()

        if not unit:
            return jsonify({'error': 'Unit not found'}), 404

        return jsonify({
            'id': unit.unit_id,
            'course_id': unit.course_id,
            'name': unit.title,
            'description': unit.description,
            'order_index': unit.order_index
        })
    finally:
        db.close()


@units_bp.route('/units/<int:unit_id>/concepts', methods=['GET'])
def get_unit_concepts(unit_id):
    """
    Retrieve all concepts associated with a specific unit.

    This endpoint fetches all concepts for a given unit, including their
    IDs, names, tags, and definitions.

    Args:
        unit_id (int): The unique identifier of the unit whose concepts
            should be retrieved

    Returns:
        JSON response containing a list of concepts, each with the
        following structure:
        [
            {
                'id': int,           # Concept ID
                'unit_id': int,      # Associated unit ID
                'name': str,         # Concept name/title
                'tag': str,          # Concept tag (currently uses
                                     # title as placeholder)
                'definition': str    # Concept definition/description
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of concepts (may be empty if no
            concepts exist for the unit)

    Example:
        GET /api/units/1/concepts
        Returns: [{"id": 1, "unit_id": 1, "name": "...", ...}, ...]
    """
    db = get_db()
    try:
        concepts = db.query(Concept).filter(
            Concept.unit_id == unit_id
        ).all()

        return jsonify([{
            'id': concept.concept_id,
            'unit_id': concept.unit_id,
            'name': concept.title,
            # TODO: Update when tag field is added to Concept model
            'tag': concept.title,
            'definition': concept.definition
        } for concept in concepts])
    finally:
        db.close()

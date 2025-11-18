"""
Unit routes blueprint
Handles all unit-related API endpoints
"""

from flask import Blueprint, jsonify
from backend.database.models import Unit, Concept
from backend.utils.database_manager import get_db

# Create blueprint
units_bp = Blueprint('units', __name__, url_prefix='/api')


@units_bp.route('/units/<int:unit_id>', methods=['GET'])
def get_unit(unit_id):
    """Get a specific unit"""
    db = get_db()
    try:
        unit = db.query(Unit).filter(Unit.unit_id == unit_id).first()
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
    """Get all concepts for a unit"""
    db = get_db()
    try:
        concepts = db.query(Concept).filter(
            Concept.unit_id == unit_id
        ).all()
        
        return jsonify([{
            'id': concept.concept_id,
            'unit_id': concept.unit_id,
            'name': concept.title,
            'tag': concept.title,  # Can be updated when tag field is added
            'definition': concept.definition
        } for concept in concepts])
    finally:
        db.close()

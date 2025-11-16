"""
Unit routes blueprint
Handles all unit-related API endpoints
"""

from flask import Blueprint, jsonify
from backend.database.models import Unit, Concept

# Create blueprint
units_bp = Blueprint('units', __name__, url_prefix='/api')


def get_db():
    """Get database session - will be injected by app.py"""
    from flask import current_app
    return current_app.db_session()


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


@units_bp.route('/units/<int:unit_id>/hcs', methods=['GET'])
def get_unit_hcs(unit_id):
    """Get all HCs for a unit"""
    db = get_db()
    try:
        hcs = db.query(Concept).filter(
            Concept.unit_id == unit_id
        ).all()
        
        return jsonify([{
            'id': hc.concept_id,
            'unit_id': hc.unit_id,
            'name': hc.title,
            'tag': hc.title,  # Can be updated when tag field is added
            'definition': hc.definition
        } for hc in hcs])
    finally:
        db.close()

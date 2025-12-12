"""
Unit routes blueprint - Thin controller layer.

This module handles HTTP concerns for unit-related endpoints:
- Parse requests
- Call service layer
- Return responses

Business logic is in backend/services/course_service.py
"""

from flask import Blueprint, jsonify

from backend.schemas.course_schemas import UnitResponse, ConceptResponse
from backend.utils.logger import get_logger
from backend.utils.service_factory import get_course_service

# Create blueprint for unit-related routes
units_bp = Blueprint('units', __name__, url_prefix='/api')

# Logger
logger = get_logger(__name__)


@units_bp.route('/units/<int:unit_id>', methods=['GET'])
def get_unit(unit_id):
    """
    Retrieve a specific unit by ID - Thin controller.

    Args:
        unit_id: Unit unique identifier

    Returns:
        {
            'id': int,
            'course_id': int,
            'name': str,
            'description': str,
            'order_index': int
        }

    HTTP Status Codes:
        200: Success
        404: Unit not found
        500: Server error
    """
    try:
        # 1. Call service layer
        course_service = get_course_service()
        unit = course_service.get_unit_by_id(unit_id)

        if not unit:
            return jsonify({'error': 'Unit not found'}), 404

        # 2. Serialize response
        unit_data = UnitResponse.from_model(unit).to_dict()

        return jsonify(unit_data), 200

    except ValueError as e:
        logger.info(f'Unit not found: {unit_id}')
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        logger.error(f'Get unit error: {str(e)}')
        return jsonify({'error': 'Failed to get unit'}), 500


@units_bp.route('/units/<int:unit_id>/concepts', methods=['GET'])
def get_unit_concepts(unit_id):
    """
    Retrieve all concepts for a unit - Thin controller.

    Args:
        unit_id: Unit unique identifier

    Returns:
        [
            {
                'id': int,
                'unit_id': int,
                'name': str,
                'tag': str,
                'definition': str
            },
            ...
        ]

    HTTP Status Codes:
        200: Success
        500: Server error
    """
    try:
        # 1. Call service layer
        course_service = get_course_service()
        concepts = course_service.get_unit_concepts(unit_id)

        # 2. Serialize response
        concepts_data = [
            ConceptResponse.from_model(c).to_dict()
            for c in concepts
        ]

        return jsonify(concepts_data), 200

    except Exception as e:
        logger.error(f'Get unit concepts error: {str(e)}')
        return jsonify({'error': 'Failed to get concepts'}), 500

"""
User routes blueprint - Thin controller layer.

This module handles HTTP concerns for user-related endpoints.
Business logic is in backend/services/progress_service.py
"""

from flask import Blueprint, jsonify

from backend.routes.auth import jwt_required
from backend.schemas.user_schemas import UserProgressResponse
from backend.utils.logger import get_logger
from backend.utils.service_factory import (
    get_progress_service,
    get_auth_service,
)

users_bp = Blueprint('users', __name__, url_prefix='/api')
logger = get_logger(__name__)


@users_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required
def get_user(user_id):
    """Get a specific user by ID."""
    try:
        from flask import request
        if request.user_id != user_id:
            return jsonify({
                'error': 'Forbidden: You can only access your own data'
            }), 403
        
        auth_service = get_auth_service()
        user = auth_service.get_user_by_id(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        from backend.schemas.auth_schemas import UserResponse
        user_data = UserResponse.from_model(user).to_dict()
        return jsonify(user_data), 200
        
    except Exception as e:
        logger.error(f'Get user error: {str(e)}')
        return jsonify({'error': 'Failed to get user'}), 500


@users_bp.route('/users/<int:user_id>/progress', methods=['GET'])
@jwt_required
def get_user_progress(user_id):
    """Get user's quiz card progress."""
    try:
        from flask import request
        if request.user_id != user_id:
            return jsonify({
                'error': 'Forbidden: You can only access your own data'
            }), 403
        
        progress_service = get_progress_service()
        progress_records = progress_service.get_user_progress_all(user_id)
        progress_data = [
            UserProgressResponse.from_user_card(card).to_dict()
            for card in progress_records
        ]
        return jsonify(progress_data), 200
        
    except Exception as e:
        logger.error(f'Get user progress error: {str(e)}')
        return jsonify({'error': 'Failed to get progress'}), 500


@users_bp.route('/progress/courses', methods=['GET'])
@jwt_required
def get_course_progress():
    """Get user's progress aggregated by courses."""
    try:
        from flask import request
        user_id = request.user_id
        
        progress_service = get_progress_service()
        chart_data = progress_service.get_courses_progress_chart_data(
            user_id
        )
        return jsonify(chart_data), 200
        
    except Exception as e:
        logger.error(f'Get course progress error: {str(e)}')
        return jsonify({'error': 'Failed to get course progress'}), 500


@users_bp.route(
    '/progress/courses/<int:course_id>/units', methods=['GET']
)
@jwt_required
def get_unit_progress(course_id):
    """Get user's progress aggregated by units in a course."""
    try:
        from flask import request
        user_id = request.user_id
        
        progress_service = get_progress_service()
        chart_data = progress_service.get_units_progress_chart_data(
            user_id, course_id
        )
        return jsonify(chart_data), 200
        
    except Exception as e:
        logger.error(f'Get unit progress error: {str(e)}')
        return jsonify({'error': 'Failed to get unit progress'}), 500


@users_bp.route(
    '/progress/courses/<int:course_id>/units/<int:unit_id>/concepts',
    methods=['GET']
)
@jwt_required
def get_concept_progress(course_id, unit_id):
    """Get user's progress aggregated by concepts in a unit."""
    try:
        from flask import request
        user_id = request.user_id
        
        progress_service = get_progress_service()
        chart_data = progress_service.get_concepts_progress_chart_data(
            user_id, course_id, unit_id
        )
        return jsonify(chart_data), 200
        
    except Exception as e:
        logger.error(f'Get concept progress error: {str(e)}')
        return jsonify({'error': 'Failed to get concept progress'}), 500

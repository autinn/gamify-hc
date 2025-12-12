"""
Course routes blueprint - Thin controller layer.

This module handles HTTP concerns for course-related endpoints:
- Parse requests
- Call service layer
- Return responses

Business logic is in backend/services/course_service.py
"""

from flask import Blueprint, jsonify

from backend.schemas.course_schemas import CourseResponse, UnitResponse
from backend.utils.logger import get_logger
from backend.utils.service_factory import get_course_service

# Create blueprint for course-related routes
courses_bp = Blueprint('courses', __name__, url_prefix='/api')

# Logger
logger = get_logger(__name__)


@courses_bp.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve all courses - Thin controller.

    Returns:
        [
            {
                'id': int,
                'code': str,
                'name': str,
                'description': str
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
        courses = course_service.get_all_courses()

        # 2. Serialize response
        courses_data = [
            CourseResponse.from_model(c).to_dict()
            for c in courses
        ]

        return jsonify(courses_data), 200

    except Exception as e:
        logger.error(f'Get courses error: {str(e)}')
        return jsonify({'error': 'Failed to get courses'}), 500


@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve a specific course by ID - Thin controller.

    Args:
        course_id: Course unique identifier

    Returns:
        {
            'id': int,
            'code': str,
            'name': str,
            'description': str
        }

    HTTP Status Codes:
        200: Success
        404: Course not found
        500: Server error
    """
    try:
        # 1. Call service layer
        course_service = get_course_service()
        course = course_service.get_course_by_id(course_id)

        if not course:
            return jsonify({'error': 'Course not found'}), 404

        # 2. Serialize response
        course_data = CourseResponse.from_model(course).to_dict()

        return jsonify(course_data), 200

    except ValueError as e:
        logger.info(f'Course not found: {course_id}')
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        logger.error(f'Get course error: {str(e)}')
        return jsonify({'error': 'Failed to get course'}), 500


@courses_bp.route('/courses/<int:course_id>/units', methods=['GET'])
def get_course_units(course_id):
    """
    Retrieve all units for a course - Thin controller.

    Args:
        course_id: Course unique identifier

    Returns:
        [
            {
                'id': int,
                'course_id': int,
                'name': str,
                'description': str,
                'order_index': int
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
        units = course_service.get_course_units(course_id)

        # 2. Serialize response
        units_data = [
            UnitResponse.from_model(u).to_dict()
            for u in units
        ]

        return jsonify(units_data), 200

    except Exception as e:
        logger.error(f'Get course units error: {str(e)}')
        return jsonify({'error': 'Failed to get units'}), 500

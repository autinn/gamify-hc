"""
Course routes blueprint.

This module handles all course-related API endpoints for the gamify-hc
application. It provides endpoints to retrieve course information and
associated units.

Endpoints:
    GET /api/courses: Retrieve all courses
    GET /api/courses/<course_id>: Retrieve a specific course by ID
    GET /api/courses/<course_id>/units: Retrieve all units for a course
"""

from flask import Blueprint, jsonify

from backend.utils.database_manager import get_db
from backend.services.course import CourseService
from backend.decorators import handle_errors

# Create blueprint for course-related routes
# All routes in this blueprint will be prefixed with '/api'
courses_bp = Blueprint('courses', __name__, url_prefix='/api')


@courses_bp.route('/courses', methods=['GET'])
@handle_errors
def get_courses():
    """
    Retrieve all courses.

    This endpoint fetches all available courses in the system.

    Returns:
        JSON response containing a list of courses, each with the
        following structure:
        [
            {
                'id': int,           # Course ID
                'code': str,          # Course code (currently uses title)
                'name': str,         # Course name/title
                'description': str   # Course description
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of courses (may be empty)

    Example:
        GET /api/courses
        Returns: [{"id": 1, "code": "EA50", "name": "...", ...}, ...]
    """
    db = get_db()
    try:
        course_service = CourseService(db_session=db)
        courses = course_service.get_all_courses()
        return jsonify(courses)
    finally:
        db.close()


@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
@handle_errors
def get_course(course_id):
    """
    Retrieve a specific course by its ID.

    This endpoint fetches course details including its ID, code, name,
    and description. If the course is not found, returns a 404 error.

    Args:
        course_id (int): The unique identifier of the course to retrieve

    Returns:
        JSON response with the following structure:
        {
            'id': int,           # Course ID
            'code': str,          # Course code (currently uses title)
            'name': str,         # Course name/title
            'description': str   # Course description
        }

    HTTP Status Codes:
        200: Success - Course found and returned
        404: Not Found - Course with the given ID does not exist

    Example:
        GET /api/courses/1
        Returns: {"id": 1, "code": "EA50", "name": "...", ...}
    """
    db = get_db()
    try:
        course_service = CourseService(db_session=db)
        course = course_service.get_course_by_id(course_id)

        if not course:
            return jsonify({'error': 'Course not found'}), 404

        return jsonify(course)
    finally:
        db.close()


@courses_bp.route('/courses/<int:course_id>/units', methods=['GET'])
@handle_errors
def get_course_units(course_id):
    """
    Retrieve all units associated with a specific course.

    This endpoint fetches all units for a given course, ordered by their
    order_index. Units are returned in the order they should be displayed
    or completed.

    Args:
        course_id (int): The unique identifier of the course whose units
            should be retrieved

    Returns:
        JSON response containing a list of units, each with the following
        structure:
        [
            {
                'id': int,           # Unit ID
                'course_id': int,    # Associated course ID
                'name': str,         # Unit name/title
                'description': str,  # Unit description
                'order_index': int   # Display order within the course
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of units (may be empty if no units
            exist for the course)

    Example:
        GET /api/courses/1/units
        Returns: [{"id": 1, "course_id": 1, "name": "...", ...}, ...]
    """
    db = get_db()
    try:
        course_service = CourseService(db_session=db)
        units = course_service.get_course_units(course_id)
        return jsonify(units)
    finally:
        db.close()

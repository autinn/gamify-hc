"""
Course routes blueprint
Handles all course-related API endpoints
"""

from flask import Blueprint, jsonify
from backend.database.models import Course, Unit

# Create blueprint
courses_bp = Blueprint('courses', __name__, url_prefix='/api')


def get_db():
    """Get database session - will be injected by app.py"""
    from flask import current_app
    return current_app.db_session()


@courses_bp.route('/courses', methods=['GET'])
def get_courses():
    """Get all courses"""
    db = get_db()
    try:
        courses = db.query(Course).all()
        return jsonify([{
            'id': c.course_id,
            'code': c.title,  # Will map to course code like "EA50"
            'name': c.title,
            'description': c.description
        } for c in courses])
    finally:
        db.close()


@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Get a specific course"""
    db = get_db()
    try:
        course = db.query(Course).filter(
            Course.course_id == course_id
        ).first()
        if not course:
            return jsonify({'error': 'Course not found'}), 404
        
        return jsonify({
            'id': course.course_id,
            'code': course.title,
            'name': course.title,
            'description': course.description
        })
    finally:
        db.close()


@courses_bp.route('/courses/<int:course_id>/units', methods=['GET'])
def get_course_units(course_id):
    """Get all units for a course"""
    db = get_db()
    try:
        units = db.query(Unit).filter(
            Unit.course_id == course_id
        ).order_by(Unit.order_index).all()
        
        return jsonify([{
            'id': u.unit_id,
            'course_id': u.course_id,
            'name': u.title,
            'description': u.description,
            'order_index': u.order_index
        } for u in units])
    finally:
        db.close()

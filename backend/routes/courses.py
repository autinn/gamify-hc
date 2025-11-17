"""
Course routes blueprint

Handles all course-related API endpoints for the Gamify-HC platform.
Courses contain units, which in turn contain Habits & Foundational Concepts (HCs).

Separation of concerns:
- Route handlers: HTTP request/response logic
- Serialization: Transform database models to JSON responses
- Error handling: Consistent error responses
"""

from flask import Blueprint, jsonify
from backend.database.models import Course, Unit


# ===============================
# BLUEPRINT SETUP
# ===============================

courses_bp = Blueprint('courses', __name__, url_prefix='/api')


# ===============================
# DATABASE ACCESS
# ===============================

def get_db_session():
    """Get database session from Flask app context.
    
    Returns:
        Session: SQLAlchemy database session
        
    Note: Session is managed by Flask app context and should be closed
    after use (handled by route handlers).
    """
    from flask import current_app
    return current_app.db_session()


# ===============================
# SERIALIZATION
# ===============================

def serialize_course(course: Course) -> dict:
    """Serialize Course model to JSON response format.
    
    Args:
        course: Course database model instance
        
    Returns:
        dict: Course data in API response format
    """
    return {
        'id': course.course_id,
        'code': course.title,  # Course code like "EA50", "FA50", "MC50"
        'name': course.title,
        'description': course.description or ''
    }


def serialize_unit(unit: Unit) -> dict:
    """Serialize Unit model to JSON response format.
    
    Args:
        unit: Unit database model instance
        
    Returns:
        dict: Unit data in API response format
    """
    return {
        'id': unit.unit_id,
        'course_id': unit.course_id,
        'name': unit.title,
        'description': unit.description or '',
        'order_index': unit.order_index
    }


# ===============================
# ERROR HANDLING
# ===============================

def error_response(message: str, status_code: int = 400) -> tuple:
    """Create a consistent error response.
    
    Args:
        message: Error message
        status_code: HTTP status code
        
    Returns:
        tuple: (JSON response, status code)
    """
    return jsonify({'error': message}), status_code


# ===============================
# ROUTE HANDLERS
# ===============================

@courses_bp.route('/courses', methods=['GET'])
def get_courses():
    """Get all courses.
    
    Returns:
        JSON array of all courses with their metadata.
        Each course contains units which hold Habits & Foundational Concepts.
        
    Example response:
        [
            {
                "id": 1,
                "code": "EA50",
                "name": "EA50 - Empirical Analyses",
                "description": "Empirical analysis and data-driven reasoning"
            }
        ]
    """
    db = get_db_session()
    try:
        courses = db.query(Course).all()
        return jsonify([serialize_course(course) for course in courses])
    except Exception as e:
        return error_response(f'Failed to fetch courses: {str(e)}', 500)
    finally:
        db.close()


@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id: int):
    """Get a specific course by ID.
    
    Args:
        course_id: Course ID from URL path
        
    Returns:
        JSON object with course details, or 404 if not found
        
    Example response:
        {
            "id": 1,
            "code": "EA50",
            "name": "EA50 - Empirical Analyses",
            "description": "Empirical analysis and data-driven reasoning"
        }
    """
    db = get_db_session()
    try:
        course = db.query(Course).filter(
            Course.course_id == course_id
        ).first()
        
        if not course:
            return error_response('Course not found', 404)
        
        return jsonify(serialize_course(course))
    except Exception as e:
        return error_response(f'Failed to fetch course: {str(e)}', 500)
    finally:
        db.close()


@courses_bp.route('/courses/<int:course_id>/units', methods=['GET'])
def get_course_units(course_id: int):
    """Get all units for a specific course.
    
    Units contain Habits & Foundational Concepts (HCs) that students learn.
    
    Args:
        course_id: Course ID from URL path
        
    Returns:
        JSON array of units, ordered by order_index, or 404 if course not found
        
    Example response:
        [
            {
                "id": 1,
                "course_id": 1,
                "name": "Data Visualization",
                "description": "Understanding and creating effective visualizations",
                "order_index": 1
            }
        ]
    """
    db = get_db_session()
    try:
        # Verify course exists
        course = db.query(Course).filter(
            Course.course_id == course_id
        ).first()
        
        if not course:
            return error_response('Course not found', 404)
        
        # Get units for this course, ordered by index
        units = db.query(Unit).filter(
            Unit.course_id == course_id
        ).order_by(Unit.order_index).all()
        
        return jsonify([serialize_unit(unit) for unit in units])
    except Exception as e:
        return error_response(f'Failed to fetch units: {str(e)}', 500)
    finally:
        db.close()

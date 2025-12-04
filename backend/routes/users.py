"""
User routes blueprint.

This module handles all user-related API endpoints for the gamify-hc
application. It provides endpoints to retrieve user information and
track user progress on quiz cards.

Endpoints:
    GET /api/users/<user_id>: Retrieve a specific user by ID
    GET /api/users/<user_id>/progress: Retrieve user's quiz card
        progress
    GET /api/progress/courses: Get user's progress aggregated by courses
    GET /api/progress/courses/<id>/units: Get user's progress aggregated by units in a course
    GET /api/progress/courses/<id>/units/<id>/concepts: Get user's progress aggregated by concepts in a unit
"""

from flask import Blueprint, jsonify, request
from sqlalchemy import func, join
from backend.database.models import User, UserCard, QuizCard, Concept, Unit, Course
from backend.utils.database_manager import get_db
from backend.routes.auth import jwt_required

# Create blueprint for user-related routes
# All routes in this blueprint will be prefixed with '/api'
users_bp = Blueprint('users', __name__, url_prefix='/api')


@users_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required
def get_user(user_id):
    """
    Retrieve a specific user by their ID.

    This endpoint fetches user details including their ID, username,
    email, and account creation timestamp. Requires authentication and
    users can only access their own data.

    Args:
        user_id (int): The unique identifier of the user to retrieve

    Returns:
        JSON response with the following structure:
        {
            'user_id': int,        # User ID
            'username': str,       # User's username
            'email': str,          # User's email address
            'created_at': str       # ISO format timestamp (or null)
        }

    HTTP Status Codes:
        200: Success - User found and returned
        401: Unauthorized - Invalid or missing token
        403: Forbidden - User can only access their own data
        404: Not Found - User with the given ID does not exist

    Example:
        GET /api/users/1
        Headers: Authorization: Bearer <jwt_token>
        Returns: {"user_id": 1, "username": "john_doe",
            "email": "john@example.com", "created_at": "2024-01-01T00:00:00"}
    """
    db = get_db()
    try:
        # Verify user can only access their own data
        if request.user_id != user_id:
            return jsonify({
                'error': 'Forbidden: You can only access your own data'
            }), 403

        # Query the database for the user with the given ID
        user = db.query(User).filter(
            User.user_id == user_id
        ).first()

        # Return 404 if user doesn't exist
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Build and return the user data as JSON
        # Convert datetime to ISO format string, or None if not set
        return jsonify({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'created_at': (
                user.created_at.isoformat()
                if user.created_at else None
            )
        })
    finally:
        # Always close the database session to prevent connection leaks
        db.close()


@users_bp.route('/users/<int:user_id>/progress', methods=['GET'])
@jwt_required
def get_user_progress(user_id):
    """
    Retrieve a user's quiz card progress.

    This endpoint fetches all quiz card progress records for a given
    user, including how many times they've seen each card, how many
    times they answered correctly, and when they last reviewed each
    card. Requires authentication and users can only access their own data.

    Args:
        user_id (int): The unique identifier of the user whose progress
            should be retrieved

    Returns:
        JSON response containing a list of progress records, each with
        the following structure:
        [
            {
                'quiz_card_id': int,    # ID of the quiz card
                'times_seen': int,      # Total times seen
                'times_correct': int,    # Number of correct answers
                'last_seen': str        # ISO format timestamp (or null)
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of progress records (may be empty
            if user has no progress tracked)
        401: Unauthorized - Invalid or missing token
        403: Forbidden - User can only access their own data

    Example:
        GET /api/users/1/progress
        Headers: Authorization: Bearer <jwt_token>
        Returns: [{"quiz_card_id": 1, "times_seen": 5, "times_correct": 3,
            "last_seen": "2024-01-15T10:30:00"}, ...]
    """
    db = get_db()
    try:
        # Verify user can only access their own data
        if request.user_id != user_id:
            return jsonify({
                'error': 'Forbidden: You can only access your own data'
            }), 403

        # Query all UserCard records for this user
        # These track the user's progress on each quiz card
        user_cards = db.query(UserCard).filter(
            UserCard.user_id == user_id
        ).all()

        # Build and return progress data for each quiz card
        return jsonify([{
            'quiz_card_id': uc.quiz_card_id,
            # Calculate total times seen from success and failure counts
            'times_seen': uc.success_count + uc.failure_count,
            'times_correct': uc.success_count,
            # Convert datetime to ISO format string, or None if not set
            'last_seen': (
                uc.last_reviewed.isoformat()
                if uc.last_reviewed else None
            )
        } for uc in user_cards])
    finally:
        # Always close the database session to prevent connection leaks
        db.close()


@users_bp.route('/progress/courses', methods=['GET'])
@jwt_required
def get_courses_progress():
    """
    Get user's progress aggregated by courses.
    
    Returns the success rate (success_count / total_attempts) for each course.
    
    Returns:
        JSON response with chart data:
        {
            'labels': ['Course 1', 'Course 2', ...],
            'values': [0.8, 0.6, ...],  # success_rate per course (0-1)
            'metadata': {...}
        }
    
    HTTP Status Codes:
        200: Success - Returns progress data
        401: Unauthorized - Invalid or missing token
    
    Example:
        GET /api/progress/courses
        Headers: Authorization: Bearer <jwt_token>
        Returns: {"labels": ["EA50", "FA50"], "values": [0.8, 0.6], ...}
    """
    db = get_db()
    try:
        user_id = request.user_id
        
        # Query: Group by course, sum success and repetitions (total attempts) for each course
        results = db.query(
            Course.title,
            func.sum(UserCard.success_count).label('total_success'),
            func.sum(UserCard.repetitions).label('total_repetitions')
        ).join(
            QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id
        ).join(
            Concept, QuizCard.concept_id == Concept.concept_id
        ).join(
            Unit, Concept.unit_id == Unit.unit_id
        ).join(
            Course, Unit.course_id == Course.course_id
        ).filter(
            UserCard.user_id == user_id
        ).group_by(
            Course.course_id, Course.title
        ).order_by(
            Course.course_id
        ).all()
        
        labels = [r[0] for r in results]
        values = []
        for r in results:
            success = r[1] or 0
            total = r[2] or 0
            rate = success / total if total > 0 else 0
            values.append(round(rate, 2))
        
        return jsonify({
            'labels': labels,
            'values': values,
            'metadata': {
                'type': 'courses',
                'count': len(labels),
                'timestamp': None
            }
        })
    finally:
        db.close()


@users_bp.route('/progress/courses/<int:course_id>/units', methods=['GET'])
@jwt_required
def get_units_progress(course_id):
    """
    Get user's progress aggregated by units in a course.
    
    Returns the total number of correct answers for each unit in the course.
    
    Args:
        course_id (int): The course ID
    
    Returns:
        JSON response with chart data:
        {
            'labels': ['Unit 1', 'Unit 2', ...],
            'values': [5, 3, ...],  # success_count per unit
            'metadata': {...}
        }
    
    HTTP Status Codes:
        200: Success - Returns progress data
        401: Unauthorized - Invalid or missing token
    
    Example:
        GET /api/progress/courses/1/units
        Headers: Authorization: Bearer <jwt_token>
        Returns: {"labels": ["Unit 1", "Unit 2"], "values": [5, 3], ...}
    """
    db = get_db()
    try:
        user_id = request.user_id
        
        # Query: Group by unit (within course), sum success and repetitions (total attempts) for each unit
        results = db.query(
            Unit.order_index,
            Unit.title,
            func.sum(UserCard.success_count).label('total_success'),
            func.sum(UserCard.repetitions).label('total_repetitions')
        ).join(
            QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id
        ).join(
            Concept, QuizCard.concept_id == Concept.concept_id
        ).join(
            Unit, Concept.unit_id == Unit.unit_id
        ).filter(
            UserCard.user_id == user_id,
            Unit.course_id == course_id
        ).group_by(
            Unit.unit_id, Unit.order_index, Unit.title
        ).order_by(
            Unit.order_index
        ).all()
        
        # Format labels as "Unit 1", "Unit 2", etc. based on order_index
        labels = [f"Unit {r[0] + 1}" if r[0] is not None else r[1] for r in results]
        values = []
        for r in results:
            success = r[2] or 0
            total = r[3] or 0
            rate = success / total if total > 0 else 0
            values.append(round(rate, 2))
        
        return jsonify({
            'labels': labels,
            'values': values,
            'metadata': {
                'type': 'units',
                'course_id': course_id,
                'count': len(labels),
                'timestamp': None
            }
        })
    finally:
        db.close()


@users_bp.route('/progress/courses/<int:course_id>/units/<int:unit_id>/concepts', methods=['GET'])
@jwt_required
def get_concepts_progress(course_id, unit_id):
    """
    Get user's progress aggregated by concepts in a unit.
    
    Returns the total number of correct answers for each concept in the unit.
    
    Args:
        course_id (int): The course ID
        unit_id (int): The unit ID
    
    Returns:
        JSON response with chart data:
        {
            'labels': ['Concept 1', 'Concept 2', ...],
            'values': [5, 3, ...],  # success_count per concept
            'metadata': {...}
        }
    
    HTTP Status Codes:
        200: Success - Returns progress data
        401: Unauthorized - Invalid or missing token
    
    Example:
        GET /api/progress/courses/1/units/1/concepts
        Headers: Authorization: Bearer <jwt_token>
        Returns: {"labels": ["Variables", "Loops"], "values": [5, 3], ...}
    """
    db = get_db()
    try:
        user_id = request.user_id
        
        # Query: Group by concept (within unit), sum success and repetitions (total attempts) for each concept
        results = db.query(
            Concept.title,
            func.sum(UserCard.success_count).label('total_success'),
            func.sum(UserCard.repetitions).label('total_repetitions')
        ).join(
            QuizCard, UserCard.quiz_card_id == QuizCard.quiz_card_id
        ).join(
            Concept, QuizCard.concept_id == Concept.concept_id
        ).filter(
            UserCard.user_id == user_id,
            Concept.unit_id == unit_id
        ).group_by(
            Concept.concept_id, Concept.title
        ).order_by(
            Concept.concept_id
        ).all()
        
        labels = [r[0] for r in results]
        values = []
        for r in results:
            success = r[1] or 0
            total = r[2] or 0
            rate = success / total if total > 0 else 0
            values.append(round(rate, 2))
        
        return jsonify({
            'labels': labels,
            'values': values,
            'metadata': {
                'type': 'concepts',
                'course_id': course_id,
                'unit_id': unit_id,
                'count': len(labels),
                'timestamp': None
            }
        })
    finally:
        db.close()

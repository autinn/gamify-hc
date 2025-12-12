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

from backend.utils.database_manager import get_db
from backend.routes.auth import jwt_required
from backend.services.user import UserService, UserProgressService
from backend.decorators import handle_errors, validate_json

# Create blueprint for user-related routes
# All routes in this blueprint will be prefixed with '/api'
users_bp = Blueprint('users', __name__, url_prefix='/api')


@users_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required
@handle_errors
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

        # Get user from service
        user_service = UserService(db_session=db)
        user = user_service.get_user_by_id(user_id)

        # Return 404 if user doesn't exist
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Build and return the user data as JSON
        return jsonify(user_service.to_dict(user))
    finally:
        # Always close the database session to prevent connection leaks
        db.close()


@users_bp.route('/users/<int:user_id>/progress', methods=['GET'])
@jwt_required
@handle_errors
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

        # Get progress from service
        progress_service = UserProgressService(db_session=db)
        progress = progress_service.get_user_quiz_progress(user_id)

        return jsonify(progress)
    finally:
        # Always close the database session to prevent connection leaks
        db.close()


@users_bp.route('/users/<int:user_id>/onboarding', methods=['GET'])
@jwt_required
@handle_errors
def get_onboarding_status(user_id):
    """
    Get user's onboarding completion status.
    
    This endpoint returns whether the user has completed the onboarding guide.
    Requires authentication and users can only access their own data.
    
    Args:
        user_id (int): The unique identifier of the user
    
    Returns:
        JSON response with the following structure:
        {
            'user_id': int,
            'has_completed_onboarding': bool
        }
    
    HTTP Status Codes:
        200: Success - Returns onboarding status
        401: Unauthorized - Invalid or missing token
        403: Forbidden - User can only access their own data
        404: Not Found - User with the given ID does not exist
    
    Example:
        GET /api/users/1/onboarding
        Headers: Authorization: Bearer <jwt_token>
        Returns: {"user_id": 1, "has_completed_onboarding": false}
    """
    db = get_db()
    try:
        # Verify user can only access their own data
        if request.user_id != user_id:
            return jsonify({
                'error': 'Forbidden: You can only access your own data'
            }), 403
        
        # Get onboarding status from service
        progress_service = UserProgressService(db_session=db)
        status = progress_service.get_onboarding_status(user_id)
        
        # Return 404 if user doesn't exist
        if not status:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify(status)
    finally:
        db.close()


@users_bp.route('/users/<int:user_id>/onboarding', methods=['PUT'])
@jwt_required
@handle_errors
@validate_json(['has_completed_onboarding'])
def update_onboarding_status(user_id):
    """
    Update user's onboarding completion status.
    
    This endpoint marks the user as having completed the onboarding guide.
    Requires authentication and users can only update their own data.
    
    Args:
        user_id (int): The unique identifier of the user
    
    Request Body:
        {
            'has_completed_onboarding': bool  # True to mark as completed
        }
    
    Returns:
        JSON response with the following structure:
        {
            'user_id': int,
            'has_completed_onboarding': bool
        }
    
    HTTP Status Codes:
        200: Success - Onboarding status updated
        400: Bad Request - Invalid request body
        401: Unauthorized - Invalid or missing token
        403: Forbidden - User can only update their own data
        404: Not Found - User with the given ID does not exist
    
    Example:
        PUT /api/users/1/onboarding
        Headers: Authorization: Bearer <jwt_token>
        Body: {"has_completed_onboarding": true}
        Returns: {"user_id": 1, "has_completed_onboarding": true}
    """
    db = get_db()
    try:
        # Verify user can only access their own data
        if request.user_id != user_id:
            return jsonify({
                'error': 'Forbidden: You can only access your own data'
            }), 403
        
        # Get request data
        data = request.get_json()
        has_completed = data.get('has_completed_onboarding')
        
        if not isinstance(has_completed, bool):
            return jsonify({
                'error': 'has_completed_onboarding must be a boolean'
            }), 400
        
        # Update onboarding status via service
        progress_service = UserProgressService(db_session=db)
        result = progress_service.update_onboarding_status(
            user_id, has_completed
        )
        
        # Return 404 if user doesn't exist
        if not result:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify(result)
    finally:
        db.close()


@users_bp.route('/progress/courses', methods=['GET'])
@jwt_required
@handle_errors
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
        
        # Get progress from service
        progress_service = UserProgressService(db_session=db)
        return jsonify(progress_service.get_courses_progress(user_id))
    finally:
        db.close()


@users_bp.route('/progress/courses/<int:course_id>/units', methods=['GET'])
@jwt_required
@handle_errors
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
        
        # Get progress from service
        progress_service = UserProgressService(db_session=db)
        return jsonify(
            progress_service.get_units_progress(user_id, course_id)
        )
    finally:
        db.close()


@users_bp.route('/progress/courses/<int:course_id>/units/<int:unit_id>/concepts', methods=['GET'])
@jwt_required
@handle_errors
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
        
        # Get progress from service
        progress_service = UserProgressService(db_session=db)
        return jsonify(
            progress_service.get_concepts_progress(
                user_id, unit_id, course_id
            )
        )
    finally:
        db.close()

"""
User routes blueprint.

This module handles all user-related API endpoints for the gamify-hc
application. It provides endpoints to retrieve user information and
track user progress on quiz cards.

Endpoints:
    GET /api/users/<user_id>: Retrieve a specific user by ID
    GET /api/users/<user_id>/progress: Retrieve user's quiz card
        progress
"""

from flask import Blueprint, jsonify, request
from backend.database.models import User, UserCard
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

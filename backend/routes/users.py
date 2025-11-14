"""
User routes blueprint
Handles all user-related API endpoints
"""

from flask import Blueprint, jsonify
from backend.database.database import User, UserCard

# Create blueprint
users_bp = Blueprint('users', __name__, url_prefix='/api')


def get_db():
    """Get database session - will be injected by app.py"""
    from flask import current_app
    return current_app.db_session()


@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user information"""
    db = get_db()
    try:
        user = db.query(User).filter(
            User.user_id == user_id
        ).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.isoformat() if user.created_at else None
        })
    finally:
        db.close()


@users_bp.route('/users/<int:user_id>/progress', methods=['GET'])
def get_user_progress(user_id):
    """Get user's quiz card progress"""
    db = get_db()
    try:
        user_cards = db.query(UserCard).filter(
            UserCard.user_id == user_id
        ).all()
        
        return jsonify([{
            'quiz_card_id': uc.quiz_card_id,
            'times_seen': uc.times_seen,
            'times_correct': uc.times_correct,
            'last_seen': uc.last_seen.isoformat() if uc.last_seen else None
        } for uc in user_cards])
    finally:
        db.close()

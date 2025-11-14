"""
HCs (Habits & Concepts) routes blueprint
Handles all HC-related API endpoints
"""

from flask import Blueprint, jsonify
from backend.database.database import Concept, QuizCard, QuizAnswer

# Create blueprint
hcs_bp = Blueprint('hcs', __name__, url_prefix='/api')


def get_db():
    """Get database session - will be injected by app.py"""
    from flask import current_app
    return current_app.db_session()


@hcs_bp.route('/hcs/<int:hc_id>', methods=['GET'])
def get_hc(hc_id):
    """Get a specific HC with its quizzes"""
    db = get_db()
    try:
        hc = db.query(Concept).filter(
            Concept.concept_id == hc_id
        ).first()
        if not hc:
            return jsonify({'error': 'HC not found'}), 404
        
        # Get quiz cards for this HC
        quiz_cards = db.query(QuizCard).filter(
            QuizCard.concept_id == hc_id
        ).all()
        
        return jsonify({
            'id': hc.concept_id,
            'unit_id': hc.unit_id,
            'name': hc.title,
            'tag': hc.title,  # Can be updated when tag field is added to DB
            'definition': hc.definition,
            'quizzes': [{
                'id': q.quiz_card_id,
                'question': q.question
            } for q in quiz_cards]
        })
    finally:
        db.close()


@hcs_bp.route('/hcs/<int:hc_id>/quizzes', methods=['GET'])
def get_hc_quizzes(hc_id):
    """Get all quizzes for an HC"""
    db = get_db()
    try:
        quiz_cards = db.query(QuizCard).filter(
            QuizCard.concept_id == hc_id
        ).all()
        
        result = []
        for q in quiz_cards:
            answers = db.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == q.quiz_card_id
            ).all()
            
            result.append({
                'id': q.quiz_card_id,
                'hc_id': q.concept_id,
                'question': q.question,
                'answers': [{
                    'id': a.answer_id,
                    'answer_text': a.answer_text,
                    'is_correct': a.is_correct,
                    'explanation': a.explanation
                } for a in answers]
            })
        
        return jsonify(result)
    finally:
        db.close()

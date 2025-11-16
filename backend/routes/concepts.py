"""
Concepts routes blueprint
Handles all concept-related API endpoints
"""

from flask import Blueprint, jsonify
from backend.database.models import Concept, QuizCard, QuizAnswer

# Create blueprint
concepts_bp = Blueprint('concepts', __name__, url_prefix='/api')


def get_db():
    """Get database session - will be injected by app.py"""
    from flask import current_app
    return current_app.db_session()


@concepts_bp.route('/concepts/<int:concept_id>', methods=['GET'])
def get_concept(concept_id):
    """Get a specific concept with its quizzes"""
    db = get_db()
    try:
        concept = db.query(Concept).filter(
            Concept.concept_id == concept_id
        ).first()
        if not concept:
            return jsonify({'error': 'Concept not found'}), 404
        
        # Get quiz cards for this concept
        quiz_cards = db.query(QuizCard).filter(
            QuizCard.concept_id == concept_id
        ).all()
        
        return jsonify({
            'id': concept.concept_id,
            'unit_id': concept.unit_id,
            'name': concept.title,
            # Can be updated when tag field is added to DB
            'tag': concept.title,
            'definition': concept.definition,
            'quizzes': [{
                'id': q.quiz_card_id,
                'question': q.question
            } for q in quiz_cards]
        })
    finally:
        db.close()


@concepts_bp.route('/concepts/<int:concept_id>/quiz-cards', methods=['GET'])
def get_concept_quiz_cards(concept_id):
    """Get all quiz cards for a concept"""
    db = get_db()
    try:
        quiz_cards = db.query(QuizCard).filter(
            QuizCard.concept_id == concept_id
        ).all()
        
        result = []
        for q in quiz_cards:
            answers = db.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == q.quiz_card_id
            ).all()
            
            result.append({
                'id': q.quiz_card_id,
                'concept_id': q.concept_id,
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


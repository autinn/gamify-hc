"""
Quiz routes blueprint
Handles all quiz-related API endpoints
"""

from flask import Blueprint, jsonify, request
from backend.database.models import (
    QuizCard, QuizAnswer, UserCard, Concept, Unit
)
from datetime import datetime

# Create blueprint
quiz_bp = Blueprint('quiz', __name__, url_prefix='/api')


def get_db():
    """Get database session - will be injected by app.py"""
    from flask import current_app
    return current_app.db_session()


@quiz_bp.route('/quiz-cards/<int:quiz_card_id>', methods=['GET'])
def get_quiz_card(quiz_card_id):
    """Get a quiz card with its answers"""
    db = get_db()
    try:
        quiz_card = db.query(QuizCard).filter(
            QuizCard.quiz_card_id == quiz_card_id
        ).first()
        if not quiz_card:
            return jsonify({'error': 'Quiz card not found'}), 404
        
        # Get answers
        answers = db.query(QuizAnswer).filter(
            QuizAnswer.quiz_card_id == quiz_card_id
        ).all()
        
        return jsonify({
            'id': quiz_card.quiz_card_id,
            'concept_id': quiz_card.concept_id,
            'question': quiz_card.question,
            'answers': [{
                'id': a.answer_id,
                'answer_text': a.answer_text,
                'is_correct': a.is_correct,
                'explanation': a.explanation
            } for a in answers]
        })
    finally:
        db.close()


@quiz_bp.route('/courses/<int:course_id>/quiz-cards', methods=['GET'])
def get_course_quiz_cards(course_id):
    """Get all quiz cards for a course"""
    db = get_db()
    try:
        # Get all units for this course
        units = db.query(Unit).filter(Unit.course_id == course_id).all()
        unit_ids = [u.unit_id for u in units]
        
        if not unit_ids:
            return jsonify([])
        
        # Get all concepts for these units
        concepts = db.query(Concept).filter(
            Concept.unit_id.in_(unit_ids)
        ).all()
        concept_ids = [c.concept_id for c in concepts]
        
        if not concept_ids:
            return jsonify([])
        
        # Get all quiz cards for these concepts
        quiz_cards = db.query(QuizCard).filter(
            QuizCard.concept_id.in_(concept_ids)
        ).all()
        
        result = []
        for qc in quiz_cards:
            answers = db.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == qc.quiz_card_id
            ).all()
            
            result.append({
                'id': qc.quiz_card_id,
                'concept_id': qc.concept_id,
                'question': qc.question,
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


@quiz_bp.route('/units/<int:unit_id>/quiz-cards', methods=['GET'])
def get_unit_quiz_cards(unit_id):
    """Get all quiz cards for a unit"""
    db = get_db()
    try:
        # Get all concepts for this unit
        concepts = db.query(Concept).filter(Concept.unit_id == unit_id).all()
        concept_ids = [c.concept_id for c in concepts]
        
        if not concept_ids:
            return jsonify([])
        
        # Get all quiz cards for these concepts
        quiz_cards = db.query(QuizCard).filter(
            QuizCard.concept_id.in_(concept_ids)
        ).all()
        
        result = []
        for qc in quiz_cards:
            answers = db.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == qc.quiz_card_id
            ).all()
            
            result.append({
                'id': qc.quiz_card_id,
                'concept_id': qc.concept_id,
                'question': qc.question,
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


@quiz_bp.route('/quiz-submit', methods=['POST'])
def submit_quiz_answer():
    """Submit a quiz answer"""
    db = get_db()
    try:
        data = request.get_json()
        
        user_id = data.get('user_id')
        quiz_card_id = data.get('quiz_card_id')
        answer_id = data.get('answer_id')
        
        if not all([user_id, quiz_card_id, answer_id]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check if answer is correct
        answer = db.query(QuizAnswer).filter(
            QuizAnswer.answer_id == answer_id
        ).first()
        
        if not answer:
            return jsonify({'error': 'Invalid answer_id'}), 400
        
        is_correct = answer.is_correct
        
        # Update or create UserCard
        user_card = db.query(UserCard).filter(
            UserCard.user_id == user_id,
            UserCard.quiz_card_id == quiz_card_id
        ).first()
        
        if user_card:
            # Update existing record
            user_card.repetitions = (user_card.repetitions or 0) + 1
            if is_correct:
                user_card.success_count = (user_card.success_count or 0) + 1
            else:
                user_card.failure_count = (user_card.failure_count or 0) + 1
            user_card.last_reviewed = datetime.utcnow()
        else:
            # Create new record
            user_card = UserCard(
                user_id=user_id,
                quiz_card_id=quiz_card_id,
                repetitions=1,
                success_count=1 if is_correct else 0,
                failure_count=0 if is_correct else 1,
                last_reviewed=datetime.utcnow()
            )
            db.add(user_card)
        
        db.commit()
        
        # Calculate total reviews for response
        total_reviews = user_card.success_count + user_card.failure_count
        
        return jsonify({
            'is_correct': is_correct,
            'explanation': answer.explanation,
            'times_seen': total_reviews,
            'times_correct': user_card.success_count
        })
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

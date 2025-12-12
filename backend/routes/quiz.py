"""
Quiz routes blueprint - Thin controller layer.

This module handles HTTP concerns for quiz-related endpoints.
Business logic is in backend/services/quiz_service.py
"""

from flask import Blueprint, jsonify, request

from backend.routes.auth import jwt_required
from backend.schemas.quiz_schemas import (
    QuizCardResponse,
    QuizSubmitRequest,
    QuizSubmitResponse,
)
from backend.utils.logger import get_logger
from backend.utils.service_factory import get_quiz_service
from backend.validators.quiz_validators import (
    ValidationError,
    validate_quiz_submission,
)

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api')
logger = get_logger(__name__)


@quiz_bp.route('/quiz-cards/<int:quiz_card_id>', methods=['GET'])
def get_quiz_card(quiz_card_id):
    """Get a specific quiz card by ID."""
    try:
        quiz_service = get_quiz_service()
        quiz_card = quiz_service.get_quiz_card_by_id(quiz_card_id)
        if not quiz_card:
            return jsonify({'error': 'Quiz card not found'}), 404
        card_data = QuizCardResponse.from_model(quiz_card).to_dict()
        return jsonify(card_data), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        logger.error(f'Get quiz card error: {str(e)}')
        return jsonify({'error': 'Failed to get quiz card'}), 500


@quiz_bp.route('/courses/<int:course_id>/quiz-cards', methods=['GET'])
def get_course_quiz_cards(course_id):
    """Get all quiz cards for a course."""
    try:
        quiz_service = get_quiz_service()
        quiz_cards = quiz_service.get_quiz_cards_by_course(course_id)
        cards_data = [
            QuizCardResponse.from_model(card).to_dict()
            for card in quiz_cards
        ]
        return jsonify(cards_data), 200
    except Exception as e:
        logger.error(f'Get course quiz cards error: {str(e)}')
        return jsonify({'error': 'Failed to get quiz cards'}), 500


@quiz_bp.route('/units/<int:unit_id>/quiz-cards', methods=['GET'])
def get_unit_quiz_cards(unit_id):
    """Get all quiz cards for a unit."""
    try:
        quiz_service = get_quiz_service()
        quiz_cards = quiz_service.get_quiz_cards_by_unit(unit_id)
        cards_data = [
            QuizCardResponse.from_model(card).to_dict()
            for card in quiz_cards
        ]
        return jsonify(cards_data), 200
    except Exception as e:
        logger.error(f'Get unit quiz cards error: {str(e)}')
        return jsonify({'error': 'Failed to get quiz cards'}), 500


@quiz_bp.route('/quiz-cards/random', methods=['GET'])
def get_random_quiz_cards():
    """Get all quiz cards from all courses."""
    try:
        quiz_service = get_quiz_service()
        quiz_cards = quiz_service.get_all_quiz_cards()
        cards_data = [
            QuizCardResponse.from_model(card).to_dict()
            for card in quiz_cards
        ]
        return jsonify(cards_data), 200
    except Exception as e:
        logger.error(f'Get random quiz cards error: {str(e)}')
        return jsonify({'error': 'Failed to get quiz cards'}), 500


@quiz_bp.route('/quiz-submit', methods=['POST'])
@jwt_required
def submit_quiz_answer():
    """Submit a quiz answer and update progress."""
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Request body is required'}), 400
        
        user_id = request.user_id
        
        try:
            validate_quiz_submission(data)
        except ValidationError as e:
            logger.info(f'Quiz validation failed: {str(e)}')
            return jsonify({'error': str(e)}), 400
        
        quiz_card_id = data['quiz_card_id']
        answer_id = data['answer_id']
        is_first_attempt = data.get('is_first_attempt', True)
        
        # Get quiz service to check if answer is correct
        quiz_service = get_quiz_service()
        
        # Check if the answer is correct
        is_correct = quiz_service.check_answer_correctness(
            answer_id
        )
        
        # Submit the answer with correctness and first attempt flag
        user_card = quiz_service.submit_quiz_answer(
            user_id=user_id,
            quiz_card_id=quiz_card_id,
            is_correct=is_correct,
            is_first_attempt=is_first_attempt
        )
        
        # Get the explanation for the correct answer
        explanation = quiz_service.get_answer_explanation(answer_id)
        
        response = QuizSubmitResponse.from_model_with_explanation(
            user_card, is_correct, explanation
        )
        logger.info(
            f'Quiz submitted: user={user_id}, '
            f'card={quiz_card_id}, correct={is_correct}, '
            f'first_attempt={is_first_attempt}'
        )
        return jsonify(response.to_dict()), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f'Quiz submission error: {str(e)}')
        return jsonify({'error': 'Failed to submit quiz'}), 500

"""
Concepts routes blueprint - Thin controller layer.

This module handles HTTP concerns for concept-related endpoints:
- Parse requests
- Call service layer
- Return responses

Business logic is in backend/services/course_service.py
and backend/services/quiz_service.py
"""

from flask import Blueprint, jsonify

from backend.schemas.course_schemas import ConceptResponse
from backend.schemas.quiz_schemas import QuizCardResponse
from backend.utils.logger import get_logger
from backend.utils.service_factory import get_course_service, get_quiz_service

# Create blueprint for concept-related routes
concepts_bp = Blueprint('concepts', __name__, url_prefix='/api')

# Logger
logger = get_logger(__name__)


@concepts_bp.route('/concepts/<int:concept_id>', methods=['GET'])
def get_concept(concept_id):
    """
    Retrieve a specific concept by ID - Thin controller.

    Args:
        concept_id: Concept unique identifier

    Returns:
        {
            'id': int,
            'unit_id': int,
            'name': str,
            'tag': str,
            'definition': str
        }

    HTTP Status Codes:
        200: Success
        404: Concept not found
        500: Server error
    """
    try:
        # 1. Call service layer
        course_service = get_course_service()
        concept = course_service.get_concept_by_id(concept_id)

        if not concept:
            return jsonify({'error': 'Concept not found'}), 404

        # 2. Serialize response
        concept_data = ConceptResponse.from_model(concept).to_dict()

        return jsonify(concept_data), 200

    except ValueError as e:
        logger.info(f'Concept not found: {concept_id}')
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        logger.error(f'Get concept error: {str(e)}')
        return jsonify({'error': 'Failed to get concept'}), 500


@concepts_bp.route('/concepts/<int:concept_id>/quiz-cards', methods=['GET'])
def get_concept_quiz_cards(concept_id):
    """
    Retrieve all quiz cards for a concept - Thin controller.

    Args:
        concept_id: Concept unique identifier

    Returns:
        [
            {
                'id': int,
                'concept_id': int,
                'question': str,
                'answers': [
                    {
                        'id': int,
                        'answer_text': str,
                        'is_correct': bool,
                        'explanation': str
                    },
                    ...
                ]
            },
            ...
        ]

    HTTP Status Codes:
        200: Success
        500: Server error
    """
    try:
        # 1. Call service layer
        quiz_service = get_quiz_service()
        quiz_cards = quiz_service.get_quiz_cards_by_concept(concept_id)

        # 2. Serialize response
        cards_data = [
            QuizCardResponse.from_model(card).to_dict()
            for card in quiz_cards
        ]

        return jsonify(cards_data), 200

    except Exception as e:
        logger.error(f'Get concept quiz cards error: {str(e)}')
        return jsonify({'error': 'Failed to get quiz cards'}), 500

"""
Concepts routes blueprint.

This module handles all concept-related API endpoints for the gamify-hc
application. It provides endpoints to retrieve concept information and
associated quiz cards.

Endpoints:
    GET /api/concepts/<concept_id>: Retrieve a specific concept by ID
    GET /api/concepts/<concept_id>/quiz-cards: Retrieve all quiz cards
        for a concept
"""

from flask import Blueprint, jsonify

from backend.utils.database_manager import get_db
from backend.services.course import ConceptService
from backend.decorators import handle_errors

# Create blueprint for concept-related routes
# All routes in this blueprint will be prefixed with '/api'
concepts_bp = Blueprint('concepts', __name__, url_prefix='/api')


@concepts_bp.route('/concepts/<int:concept_id>', methods=['GET'])
@handle_errors
def get_concept(concept_id):
    """
    Retrieve a specific concept by its ID.

    This endpoint fetches concept details including its ID, unit
    association, name, tag, and definition. If the concept is not
    found, returns a 404 error.

    Args:
        concept_id (int): The unique identifier of the concept to
            retrieve

    Returns:
        JSON response with the following structure:
        {
            'id': int,           # Concept ID
            'unit_id': int,      # ID of the unit this concept
                                 # belongs to
            'name': str,         # Concept title/name
            'tag': str,          # Concept tag (currently uses
                                 # title as placeholder)
            'definition': str    # Concept definition/description
        }

    HTTP Status Codes:
        200: Success - Concept found and returned
        404: Not Found - Concept with the given ID does not exist

    Example:
        GET /api/concepts/1
        Returns: {"id": 1, "unit_id": 1, "name": "Example", ...}
    """
    db = get_db()
    try:
        concept_service = ConceptService(db_session=db)
        concept = concept_service.get_concept_by_id(concept_id)

        if not concept:
            return jsonify({'error': 'Concept not found'}), 404

        return jsonify(concept)
    finally:
        db.close()


@concepts_bp.route('/concepts/<int:concept_id>/quiz-cards', methods=['GET'])
@handle_errors
def get_concept_quiz_cards(concept_id):
    """
    Retrieve all quiz cards associated with a specific concept.

    This endpoint fetches all quiz cards for a given concept,
    including their questions and all associated answers with
    correctness flags and explanations.

    Args:
        concept_id (int): The unique identifier of the concept whose
            quiz cards should be retrieved

    Returns:
        JSON response containing a list of quiz cards, each with the
        following structure:
        [
            {
                'id': int,                    # Quiz card ID
                'concept_id': int,             # Associated concept ID
                'question': str,               # Quiz question text
                'answers': [                   # List of possible answers
                    {
                        'id': int,             # Answer ID
                        'answer_text': str,    # Answer option text
                        'is_correct': bool,    # Whether this answer
                                               # is correct
                        'explanation': str     # Explanation for this
                                               # answer
                    },
                    ...
                ]
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of quiz cards (may be empty if
            no cards exist)

    Example:
        GET /api/concepts/1/quiz-cards
        Returns: [{"id": 1, "concept_id": 1, "question": "...",
            "answers": [...]}, ...]
    """
    db = get_db()
    try:
        concept_service = ConceptService(db_session=db)
        quiz_cards = concept_service.get_concept_quiz_cards(concept_id)
        return jsonify(quiz_cards)
    finally:
        db.close()

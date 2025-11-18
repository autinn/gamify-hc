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
from backend.database.models import Concept, QuizCard, QuizAnswer

# Create blueprint for concept-related routes
# All routes in this blueprint will be prefixed with '/api'
concepts_bp = Blueprint('concepts', __name__, url_prefix='/api')


def get_db():
    """
    Get database session from Flask application context.

    This function retrieves the database session that is injected by
    app.py. The session is used to perform database queries within
    route handlers.

    Returns:
        Session: SQLAlchemy database session object

    Note:
        The database session must be closed after use to prevent
        connection leaks. This is typically done in a finally block.
    """
    from flask import current_app
    return current_app.db_session()


@concepts_bp.route('/concepts/<int:concept_id>', methods=['GET'])
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
    # Get database session for querying
    db = get_db()
    try:
        # Query the database for the concept with the given ID
        concept = db.query(Concept).filter(
            Concept.concept_id == concept_id
        ).first()

        # Return 404 if concept doesn't exist
        if not concept:
            return jsonify({'error': 'Concept not found'}), 404

        # Build and return the concept data as JSON
        # Note: 'tag' currently uses title as a placeholder until
        # tag field is added to DB
        return jsonify({
            'id': concept.concept_id,
            'unit_id': concept.unit_id,
            'name': concept.title,
            # TODO: Update when tag field is added to Concept model
            'tag': concept.title,
            'definition': concept.definition
        })
    finally:
        # Always close the database session to prevent connection leaks
        db.close()


@concepts_bp.route('/concepts/<int:concept_id>/quiz-cards', methods=['GET'])
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
    # Get database session for querying
    db = get_db()
    try:
        # Query all quiz cards associated with the given concept
        quiz_cards = db.query(QuizCard).filter(
            QuizCard.concept_id == concept_id
        ).all()

        # Build the response list with quiz cards and their answers
        result = []
        for q in quiz_cards:
            # For each quiz card, fetch all associated answers
            answers = db.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == q.quiz_card_id
            ).all()

            # Construct the quiz card object with nested answer data
            result.append({
                'id': q.quiz_card_id,
                'concept_id': q.concept_id,
                'question': q.question,
                # Build list of answer objects with all relevant fields
                'answers': [{
                    'id': a.answer_id,
                    'answer_text': a.answer_text,
                    'is_correct': a.is_correct,
                    'explanation': a.explanation
                } for a in answers]
            })

        # Return the list of quiz cards as JSON
        # Note: Returns empty list if no quiz cards exist for the concept
        return jsonify(result)
    finally:
        # Always close the database session to prevent connection leaks
        db.close()

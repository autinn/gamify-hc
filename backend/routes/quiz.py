"""
Quiz routes blueprint.

This module handles all quiz-related API endpoints for the gamify-hc
application. It provides endpoints to retrieve quiz cards and submit
quiz answers for tracking user progress.

Endpoints:
    GET /api/quiz-cards/<quiz_card_id>: Retrieve a specific quiz card
    GET /api/courses/<course_id>/quiz-cards: Retrieve all quiz cards
        for a course
    GET /api/units/<unit_id>/quiz-cards: Retrieve all quiz cards for
        a unit
    POST /api/quiz-submit: Submit a quiz answer and update user progress
"""

from flask import Blueprint, jsonify, request

from backend.utils.database_manager import get_db
from backend.routes.auth import jwt_required
from backend.services.quiz import QuizService
from backend.decorators import handle_errors, validate_json

# Create blueprint for quiz-related routes
# All routes in this blueprint will be prefixed with '/api'
quiz_bp = Blueprint('quiz', __name__, url_prefix='/api')


@quiz_bp.route('/quiz-cards/<int:quiz_card_id>', methods=['GET'])
@handle_errors
def get_quiz_card(quiz_card_id):
    """
    Retrieve a specific quiz card by its ID.

    This endpoint fetches a quiz card with all its associated answers,
    including correctness flags and explanations.

    Args:
        quiz_card_id (int): The unique identifier of the quiz card to
            retrieve

    Returns:
        JSON response with the following structure:
        {
            'id': int,                    # Quiz card ID
            'concept_id': int,             # Associated concept ID
            'question': str,               # Quiz question text
            'answers': [                   # List of possible answers
                {
                    'id': int,             # Answer ID
                    'answer_text': str,    # Answer option text
                    'is_correct': bool,    # Whether this answer is
                                           # correct
                    'explanation': str     # Explanation for this answer
                },
                ...
            ]
        }

    HTTP Status Codes:
        200: Success - Quiz card found and returned
        404: Not Found - Quiz card with the given ID does not exist

    Example:
        GET /api/quiz-cards/1
        Returns: {"id": 1, "concept_id": 1, "question": "...",
            "answers": [...]}
    """
    db = get_db()
    try:
        quiz_service = QuizService(db_session=db)
        quiz_card = quiz_service.get_quiz_card_by_id(quiz_card_id)

        if not quiz_card:
            return jsonify({'error': 'Quiz card not found'}), 404

        return jsonify(quiz_card)
    finally:
        db.close()


@quiz_bp.route('/courses/<int:course_id>/quiz-cards', methods=['GET'])
@handle_errors
def get_course_quiz_cards(course_id):
    """
    Retrieve all quiz cards associated with a specific course.

    This endpoint fetches all quiz cards for all units within a given
    course. It traverses the course -> units -> concepts -> quiz cards
    hierarchy to collect all relevant quiz cards.

    Args:
        course_id (int): The unique identifier of the course whose quiz
            cards should be retrieved

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
                        'is_correct': bool,    # Whether this answer is
                                               # correct
                        'explanation': str     # Explanation for this
                                               # answer
                    },
                    ...
                ]
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of quiz cards (may be empty if no
            cards exist for the course)

    Example:
        GET /api/courses/1/quiz-cards
        Returns: [{"id": 1, "concept_id": 1, "question": "...",
            "answers": [...]}, ...]
    """
    db = get_db()
    try:
        quiz_service = QuizService(db_session=db)
        quiz_cards = quiz_service.get_course_quiz_cards(course_id)
        return jsonify(quiz_cards)
    finally:
        db.close()


@quiz_bp.route('/units/<int:unit_id>/quiz-cards', methods=['GET'])
@handle_errors
def get_unit_quiz_cards(unit_id):
    """
    Retrieve all quiz cards associated with a specific unit.

    This endpoint fetches all quiz cards for all concepts within a given
    unit. It traverses the unit -> concepts -> quiz cards hierarchy.

    Args:
        unit_id (int): The unique identifier of the unit whose quiz cards
            should be retrieved

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
                        'is_correct': bool,    # Whether this answer is
                                               # correct
                        'explanation': str     # Explanation for this
                                               # answer
                    },
                    ...
                ]
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of quiz cards (may be empty if no
            cards exist for the unit)

    Example:
        GET /api/units/1/quiz-cards
        Returns: [{"id": 1, "concept_id": 1, "question": "...",
            "answers": [...]}, ...]
    """
    db = get_db()
    try:
        quiz_service = QuizService(db_session=db)
        quiz_cards = quiz_service.get_unit_quiz_cards(unit_id)
        return jsonify(quiz_cards)
    finally:
        db.close()


@quiz_bp.route('/quiz-cards/random', methods=['GET'])
@handle_errors
def get_random_quiz_cards():
    """
    Retrieve all quiz cards from all courses (for global random quiz).

    This endpoint fetches all quiz cards across all courses, units, and
    concepts. Used for practice mode where users want random questions
    from the entire system. The frontend will shuffle these and limit
    to a specific number.

    Returns:
        JSON response containing a list of all quiz cards with the
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
                        'is_correct': bool,    # Whether this answer is
                                               # correct
                        'explanation': str     # Explanation for this
                                               # answer
                    },
                    ...
                ]
            },
            ...
        ]

    HTTP Status Codes:
        200: Success - Returns list of all quiz cards

    Example:
        GET /api/quiz-cards/random
        Returns: [{"id": 1, "concept_id": 1, "question": "...",
            "answers": [...]}, ...]
    """
    db = get_db()
    try:
        quiz_service = QuizService(db_session=db)
        quiz_cards = quiz_service.get_all_quiz_cards()
        return jsonify(quiz_cards)
    finally:
        db.close()


@quiz_bp.route('/quiz-submit', methods=['POST'])
@jwt_required
@handle_errors
def submit_quiz_answer():
    """
    Submit a quiz answer and update user progress.

    This endpoint processes a quiz answer submission, validates the answer,
    and updates the user's progress tracking (UserCard). It handles both
    new submissions and updates to existing progress records. Requires
    authentication and uses the authenticated user's ID from the JWT token.

    Request Body (JSON):
        {
            'quiz_card_id': int,   # ID of the quiz card being answered
            'answer_id': int,      # ID of the selected answer
            'is_first_attempt': bool  # True if first try (optional)
        }

    Headers:
        Authorization: Bearer <jwt_token>

    Returns:
        JSON response with the following structure:
        {
            'is_correct': bool,    # Whether the submitted answer is
                                   # correct
            'explanation': str,    # Explanation for the answer (may be
                                   # null)
            'times_seen': int,     # Total number of submission attempts
                                   # for this quiz card
            'times_correct': int   # Number of times user answered correctly
                                   # on the first attempt
        }

    HTTP Status Codes:
        200: Success - Answer processed and progress updated
        400: Bad Request - Missing required fields or invalid answer_id
        401: Unauthorized - Invalid or missing token
        500: Internal Server Error - Database error occurred

    Example:
        POST /api/quiz-submit
        Headers: Authorization: Bearer <jwt_token>
        Body: {"quiz_card_id": 1, "answer_id": 2, "is_first_attempt": true}
        Returns: {"is_correct": true, "explanation": "...",
            "times_seen": 3, "times_correct": 2}
    """
    db = get_db()
    try:
        data = request.get_json()
        
        # Extract fields from request
        quiz_card_id = data.get('quiz_card_id') if data else None
        answer_id = data.get('answer_id') if data else None
        # Default to True so existing clients still count first-try
        is_first_attempt = True if data is None else data.get(
            'is_first_attempt', True
        )

        if not all([quiz_card_id, answer_id]):
            return jsonify({
                'error': 'Missing required fields: quiz_card_id and answer_id'
            }), 400

        # Use authenticated user_id from JWT token
        user_id = request.user_id

        # Submit answer via service
        quiz_service = QuizService(db_session=db)
        try:
            result = quiz_service.submit_answer(
                user_id=user_id,
                quiz_card_id=quiz_card_id,
                answer_id=answer_id,
                is_first_attempt=bool(is_first_attempt)
            )
            return jsonify(result)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    finally:
        db.close()

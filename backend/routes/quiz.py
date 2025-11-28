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
from sqlalchemy.exc import IntegrityError
from backend.database.models import (
    QuizCard, QuizAnswer, UserCard, Concept, Unit
)
from backend.utils.database_manager import get_db
from backend.routes.auth import jwt_required
from datetime import datetime

# Create blueprint for quiz-related routes
# All routes in this blueprint will be prefixed with '/api'
quiz_bp = Blueprint('quiz', __name__, url_prefix='/api')


def _serialize_quiz_card_with_answers(quiz_card, answers):
    """
    Serialize a QuizCard model instance with its answers to a dictionary.

    Args:
        quiz_card (QuizCard): The quiz card model instance
        answers (list): List of QuizAnswer instances for this quiz card

    Returns:
        dict: Serialized quiz card data with id, concept_id, question,
            and answers
    """
    return {
        'id': quiz_card.quiz_card_id,
        'concept_id': quiz_card.concept_id,
        'question': quiz_card.question,
        'answers': [{
            'id': a.answer_id,
            'answer_text': a.answer_text,
            'is_correct': a.is_correct,
            'explanation': a.explanation
        } for a in answers]
    }


def _get_quiz_cards_for_concepts(db, concept_ids):
    """
    Retrieve and serialize all quiz cards for a list of concept IDs.

    Args:
        db: Database session
        concept_ids (list): List of concept IDs to fetch quiz cards for

    Returns:
        list: List of serialized quiz cards with their answers
    """
    if not concept_ids:
        return []

    quiz_cards = db.query(QuizCard).filter(
        QuizCard.concept_id.in_(concept_ids)
    ).all()

    result = []
    for qc in quiz_cards:
        answers = db.query(QuizAnswer).filter(
            QuizAnswer.quiz_card_id == qc.quiz_card_id
        ).all()
        result.append(_serialize_quiz_card_with_answers(qc, answers))

    return result


@quiz_bp.route('/quiz-cards/<int:quiz_card_id>', methods=['GET'])
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
        quiz_card = db.query(QuizCard).filter(
            QuizCard.quiz_card_id == quiz_card_id
        ).first()

        if not quiz_card:
            return jsonify({'error': 'Quiz card not found'}), 404

        # Get all answers for this quiz card
        answers = db.query(QuizAnswer).filter(
            QuizAnswer.quiz_card_id == quiz_card_id
        ).all()

        return jsonify(
            _serialize_quiz_card_with_answers(quiz_card, answers)
        )
    finally:
        db.close()


@quiz_bp.route('/courses/<int:course_id>/quiz-cards', methods=['GET'])
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
        # Get all units for this course
        units = db.query(Unit).filter(
            Unit.course_id == course_id
        ).all()
        unit_ids = [u.unit_id for u in units]

        if not unit_ids:
            return jsonify([])

        # Get all concepts for these units
        concepts = db.query(Concept).filter(
            Concept.unit_id.in_(unit_ids)
        ).all()
        concept_ids = [c.concept_id for c in concepts]

        # Get and serialize all quiz cards for these concepts
        result = _get_quiz_cards_for_concepts(db, concept_ids)
        return jsonify(result)
    finally:
        db.close()


@quiz_bp.route('/units/<int:unit_id>/quiz-cards', methods=['GET'])
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
        # Get all concepts for this unit
        concepts = db.query(Concept).filter(
            Concept.unit_id == unit_id
        ).all()
        concept_ids = [c.concept_id for c in concepts]

        # Get and serialize all quiz cards for these concepts
        result = _get_quiz_cards_for_concepts(db, concept_ids)
        return jsonify(result)
    finally:
        db.close()


@quiz_bp.route('/quiz-cards/random', methods=['GET'])
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
        # Get ALL quiz cards from the database (no filtering)
        quiz_cards = db.query(QuizCard).all()

        result = []
        for qc in quiz_cards:
            answers = db.query(QuizAnswer).filter(
                QuizAnswer.quiz_card_id == qc.quiz_card_id
            ).all()
            result.append(_serialize_quiz_card_with_answers(qc, answers))

        return jsonify(result)
    finally:
        db.close()


@quiz_bp.route('/quiz-submit', methods=['POST'])
@jwt_required
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
            'answer_id': int       # ID of the selected answer
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
            'times_seen': int,     # Total number of times user has seen
                                   # this quiz card
            'times_correct': int   # Number of times user answered
                                   # correctly
        }

    HTTP Status Codes:
        200: Success - Answer processed and progress updated
        400: Bad Request - Missing required fields or invalid answer_id
        401: Unauthorized - Invalid or missing token
        500: Internal Server Error - Database error occurred

    Example:
        POST /api/quiz-submit
        Headers: Authorization: Bearer <jwt_token>
        Body: {"quiz_card_id": 1, "answer_id": 2}
        Returns: {"is_correct": true, "explanation": "...",
            "times_seen": 3, "times_correct": 2}
    """
    db = get_db()
    try:
        data = request.get_json()

        # Use authenticated user_id from JWT token instead of request body
        user_id = request.user_id
        quiz_card_id = data.get('quiz_card_id') if data else None
        answer_id = data.get('answer_id') if data else None

        if not all([quiz_card_id, answer_id]):
            return jsonify({
                'error': 'Missing required fields: quiz_card_id and answer_id'
            }), 400

        # Validate that the answer exists
        answer = db.query(QuizAnswer).filter(
            QuizAnswer.answer_id == answer_id
        ).first()

        if not answer:
            return jsonify({'error': 'Invalid answer_id'}), 400

        is_correct = answer.is_correct

        # Find or create UserCard to track progress
        user_card = db.query(UserCard).filter(
            UserCard.user_id == user_id,
            UserCard.quiz_card_id == quiz_card_id
        ).first()

        if user_card:
            # Update existing progress record
            user_card.repetitions = (user_card.repetitions or 0) + 1
            if is_correct:
                user_card.success_count = (
                    user_card.success_count or 0
                ) + 1
            else:
                user_card.failure_count = (
                    user_card.failure_count or 0
                ) + 1
            user_card.last_reviewed = datetime.utcnow()
        else:
            # Create new progress record
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
        db.refresh(user_card)

        # Calculate total reviews for response
        total_reviews = (
            user_card.success_count + user_card.failure_count
        )

        return jsonify({
            'is_correct': is_correct,
            'explanation': answer.explanation,
            'times_seen': total_reviews,
            'times_correct': user_card.success_count
        })
    except IntegrityError:
        db.rollback()
        # UserCard already exists, try to update it instead
        user_card = db.query(UserCard).filter(
            UserCard.user_id == user_id,
            UserCard.quiz_card_id == quiz_card_id
        ).first()
        if user_card:
            # Update existing progress record
            user_card.repetitions = (user_card.repetitions or 0) + 1
            if is_correct:
                user_card.success_count = (
                    user_card.success_count or 0
                ) + 1
            else:
                user_card.failure_count = (
                    user_card.failure_count or 0
                ) + 1
            user_card.last_reviewed = datetime.utcnow()
            db.commit()
            db.refresh(user_card)
            total_reviews = user_card.success_count + user_card.failure_count
            return jsonify({
                'is_correct': is_correct,
                'explanation': answer.explanation,
                'times_seen': total_reviews,
                'times_correct': user_card.success_count
            })
        else:
            return jsonify({'error': 'Failed to update progress'}), 500
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

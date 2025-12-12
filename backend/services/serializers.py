"""
Shared Serializers Module.

This module provides centralized serialization functions for converting
database model instances to dictionaries suitable for API responses.

Having serializers in a single location ensures:
- Consistent data format across all endpoints
- Single point of maintenance when model changes occur
- DRY principle adherence

Functions:
    serialize_course: Convert Course model to dict
    serialize_unit: Convert Unit model to dict
    serialize_concept: Convert Concept model to dict
    serialize_quiz_card_with_answers: Convert QuizCard with answers to dict
    serialize_user: Convert User model to dict
"""

from typing import Dict, Any, List

from backend.database.models import (
    Course, Unit, Concept, QuizCard, QuizAnswer, User
)


def serialize_course(course: Course) -> Dict[str, Any]:
    """
    Convert a Course model instance to a dictionary.

    Args:
        course: The Course model instance to serialize

    Returns:
        Dictionary with course data:
        {
            'id': int,
            'code': str,
            'name': str,
            'description': str
        }

    Note:
        Currently 'code' and 'name' both use the title field.
        This may be updated if a separate code field is added.
    """
    return {
        'id': course.course_id,
        'code': course.title,
        'name': course.title,
        'description': course.description
    }


def serialize_unit(unit: Unit) -> Dict[str, Any]:
    """
    Convert a Unit model instance to a dictionary.

    Args:
        unit: The Unit model instance to serialize

    Returns:
        Dictionary with unit data:
        {
            'id': int,
            'course_id': int,
            'name': str,
            'description': str,
            'order_index': int
        }
    """
    return {
        'id': unit.unit_id,
        'course_id': unit.course_id,
        'name': unit.title,
        'description': unit.description,
        'order_index': unit.order_index
    }


def serialize_concept(concept: Concept) -> Dict[str, Any]:
    """
    Convert a Concept model instance to a dictionary.

    Args:
        concept: The Concept model instance to serialize

    Returns:
        Dictionary with concept data:
        {
            'id': int,
            'unit_id': int,
            'name': str,
            'tag': str,
            'definition': str
        }

    Note:
        Currently 'tag' uses the title field as a placeholder.
        This may be updated if a separate tag field is added.
    """
    return {
        'id': concept.concept_id,
        'unit_id': concept.unit_id,
        'name': concept.title,
        'tag': concept.title,
        'definition': concept.definition
    }


def serialize_quiz_card_with_answers(
    quiz_card: QuizCard,
    answers: List[QuizAnswer]
) -> Dict[str, Any]:
    """
    Convert a QuizCard with its answers to a dictionary.

    Args:
        quiz_card: The QuizCard model instance
        answers: List of QuizAnswer model instances for this card

    Returns:
        Dictionary with quiz card and answers:
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
                }, ...
            ]
        }
    """
    return {
        'id': quiz_card.quiz_card_id,
        'concept_id': quiz_card.concept_id,
        'question': quiz_card.question,
        'answers': [
            {
                'id': ans.answer_id,
                'answer_text': ans.answer_text,
                'is_correct': ans.is_correct,
                'explanation': ans.explanation
            }
            for ans in answers
        ]
    }


def serialize_user(
    user: User,
    include_password: bool = False
) -> Dict[str, Any]:
    """
    Convert a User object to a dictionary for API responses.

    By default, the password field is excluded for security.
    Use include_password=True only for specific admin operations.

    Args:
        user: User object to convert
        include_password: Whether to include password hash (default: False)

    Returns:
        Dictionary representation of the user:
        {
            'user_id': int,
            'username': str,
            'email': str,
            'created_at': str (ISO format)
        }
    """
    data = {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    }

    if include_password:
        data['password'] = user.password_hash

    return data

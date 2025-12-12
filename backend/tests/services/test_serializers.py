"""
Tests for shared serializer functions.

This module tests all serialization functions in backend/services/serializers.py:
- serialize_course()
- serialize_unit()
- serialize_concept()
- serialize_quiz_card_with_answers()
- serialize_user()
"""

import pytest
from datetime import datetime
from backend.services.serializers import (
    serialize_course,
    serialize_unit,
    serialize_concept,
    serialize_quiz_card_with_answers,
    serialize_user
)
from backend.database.models import (
    Course, Unit, Concept, QuizCard, QuizAnswer, User
)


class TestSerializeCourse:
    """Tests for serialize_course function."""

    def test_serialize_course(self, sample_course):
        """Test serializing a course to dictionary."""
        result = serialize_course(sample_course)

        assert result['id'] == sample_course.course_id
        assert result['code'] == sample_course.title
        assert result['name'] == sample_course.title
        assert result['description'] == sample_course.description

    def test_serialize_course_has_expected_keys(self, sample_course):
        """Test that serialized course has all expected keys."""
        result = serialize_course(sample_course)

        expected_keys = {'id', 'code', 'name', 'description'}
        assert set(result.keys()) == expected_keys


class TestSerializeUnit:
    """Tests for serialize_unit function."""

    def test_serialize_unit(self, sample_unit):
        """Test serializing a unit to dictionary."""
        result = serialize_unit(sample_unit)

        assert result['id'] == sample_unit.unit_id
        assert result['course_id'] == sample_unit.course_id
        assert result['name'] == sample_unit.title
        assert result['description'] == sample_unit.description
        assert result['order_index'] == sample_unit.order_index

    def test_serialize_unit_has_expected_keys(self, sample_unit):
        """Test that serialized unit has all expected keys."""
        result = serialize_unit(sample_unit)

        expected_keys = {'id', 'course_id', 'name', 'description', 'order_index'}
        assert set(result.keys()) == expected_keys


class TestSerializeConcept:
    """Tests for serialize_concept function."""

    def test_serialize_concept(self, sample_concept):
        """Test serializing a concept to dictionary."""
        result = serialize_concept(sample_concept)

        assert result['id'] == sample_concept.concept_id
        assert result['unit_id'] == sample_concept.unit_id
        assert result['name'] == sample_concept.title
        assert result['tag'] == sample_concept.title  # Currently uses title
        assert result['definition'] == sample_concept.definition

    def test_serialize_concept_has_expected_keys(self, sample_concept):
        """Test that serialized concept has all expected keys."""
        result = serialize_concept(sample_concept)

        expected_keys = {'id', 'unit_id', 'name', 'tag', 'definition'}
        assert set(result.keys()) == expected_keys


class TestSerializeQuizCardWithAnswers:
    """Tests for serialize_quiz_card_with_answers function."""

    def test_serialize_quiz_card_with_answers(
        self, sample_quiz_card, sample_quiz_answers
    ):
        """Test serializing a quiz card with its answers."""
        result = serialize_quiz_card_with_answers(
            sample_quiz_card,
            sample_quiz_answers
        )

        assert result['id'] == sample_quiz_card.quiz_card_id
        assert result['concept_id'] == sample_quiz_card.concept_id
        assert result['question'] == sample_quiz_card.question
        assert len(result['answers']) == len(sample_quiz_answers)

    def test_serialize_quiz_card_answer_structure(
        self, sample_quiz_card, sample_quiz_answers
    ):
        """Test that answers have correct structure."""
        result = serialize_quiz_card_with_answers(
            sample_quiz_card,
            sample_quiz_answers
        )

        for answer in result['answers']:
            expected_keys = {
                'id', 'answer_text', 'is_correct', 'explanation'
            }
            assert set(answer.keys()) == expected_keys

    def test_serialize_quiz_card_with_empty_answers(self, sample_quiz_card):
        """Test serializing a quiz card with no answers."""
        result = serialize_quiz_card_with_answers(sample_quiz_card, [])

        assert result['id'] == sample_quiz_card.quiz_card_id
        assert result['answers'] == []

    def test_serialize_quiz_card_answer_values(
        self, sample_quiz_card, sample_quiz_answers
    ):
        """Test that answer values are correctly serialized."""
        result = serialize_quiz_card_with_answers(
            sample_quiz_card,
            sample_quiz_answers
        )

        # Find the correct answer
        correct_answers = [
            a for a in result['answers'] if a['is_correct']
        ]
        assert len(correct_answers) == 1
        assert correct_answers[0]['answer_text'] == "Pie chart"

    def test_serialize_quiz_card_has_expected_keys(
        self, sample_quiz_card, sample_quiz_answers
    ):
        """Test that serialized quiz card has all expected keys."""
        result = serialize_quiz_card_with_answers(
            sample_quiz_card,
            sample_quiz_answers
        )

        expected_keys = {'id', 'concept_id', 'question', 'answers'}
        assert set(result.keys()) == expected_keys


class TestSerializeUser:
    """Tests for serialize_user function."""

    def test_serialize_user_without_password(self, sample_user):
        """Test serializing a user without password hash."""
        result = serialize_user(sample_user)

        assert result['user_id'] == sample_user.user_id
        assert result['username'] == sample_user.username
        assert result['email'] == sample_user.email
        assert 'created_at' in result
        assert 'password' not in result

    def test_serialize_user_with_password(self, sample_user):
        """Test serializing a user with password hash included."""
        result = serialize_user(sample_user, include_password=True)

        assert result['user_id'] == sample_user.user_id
        assert result['username'] == sample_user.username
        assert result['email'] == sample_user.email
        assert 'password' in result
        assert result['password'] == sample_user.password_hash

    def test_serialize_user_created_at_format(self, sample_user):
        """Test that created_at is in ISO format."""
        result = serialize_user(sample_user)

        # Verify it's a valid ISO format string
        created_at = result['created_at']
        assert isinstance(created_at, str)
        # Should be parseable as datetime
        datetime.fromisoformat(created_at)

    def test_serialize_user_has_expected_keys_without_password(
        self, sample_user
    ):
        """Test that serialized user has expected keys (no password)."""
        result = serialize_user(sample_user)

        expected_keys = {'user_id', 'username', 'email', 'created_at'}
        assert set(result.keys()) == expected_keys

    def test_serialize_user_has_expected_keys_with_password(self, sample_user):
        """Test that serialized user has expected keys (with password)."""
        result = serialize_user(sample_user, include_password=True)

        expected_keys = {'user_id', 'username', 'email', 'created_at', 'password'}
        assert set(result.keys()) == expected_keys


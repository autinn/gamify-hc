"""
Tests for QuizService.

This module tests quiz management functionality:
- Get quiz card by ID
- Get course quiz cards
- Get unit quiz cards
- Get all quiz cards
- Submit answer (with UserCard tracking)
"""

import pytest
from datetime import datetime
from backend.services.quiz import QuizService
from backend.database.models import QuizCard, QuizAnswer, UserCard


class TestQuizServiceGetById:
    """Tests for getting quiz card by ID."""

    def test_get_quiz_card_by_id_found(
        self, quiz_service, sample_quiz_card, sample_quiz_answers
    ):
        """Test getting an existing quiz card by ID."""
        card = quiz_service.get_quiz_card_by_id(sample_quiz_card.quiz_card_id)

        assert card is not None
        assert card['id'] == sample_quiz_card.quiz_card_id
        assert card['concept_id'] == sample_quiz_card.concept_id
        assert card['question'] == sample_quiz_card.question

    def test_get_quiz_card_by_id_includes_answers(
        self, quiz_service, sample_quiz_card, sample_quiz_answers
    ):
        """Test that quiz card includes answers."""
        card = quiz_service.get_quiz_card_by_id(sample_quiz_card.quiz_card_id)

        assert 'answers' in card
        assert len(card['answers']) == 2

    def test_get_quiz_card_by_id_not_found(self, quiz_service, clean_db):
        """Test getting a nonexistent quiz card by ID."""
        card = quiz_service.get_quiz_card_by_id(99999)

        assert card is None

    def test_get_quiz_card_by_id_structure(
        self, quiz_service, sample_quiz_card, sample_quiz_answers
    ):
        """Test that returned quiz card has expected structure."""
        card = quiz_service.get_quiz_card_by_id(sample_quiz_card.quiz_card_id)

        card_keys = {'id', 'concept_id', 'question', 'answers'}
        assert set(card.keys()) == card_keys

        answer_keys = {'id', 'answer_text', 'is_correct', 'explanation'}
        assert set(card['answers'][0].keys()) == answer_keys

    def test_get_quiz_card_by_id_without_session_raises_error(self):
        """Test that getting card without db_session raises error."""
        service = QuizService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_quiz_card_by_id(1)


class TestQuizServiceGetCourseCards:
    """Tests for getting quiz cards by course."""

    def test_get_course_quiz_cards_empty(
        self, quiz_service, sample_course
    ):
        """Test getting cards for course with no cards."""
        cards = quiz_service.get_course_quiz_cards(sample_course.course_id)

        # Empty if no quiz cards exist
        assert isinstance(cards, list)

    def test_get_course_quiz_cards_with_data(
        self, quiz_service, populated_test_data
    ):
        """Test getting cards for course with quiz cards."""
        course = populated_test_data['courses'][0]  # EA50

        cards = quiz_service.get_course_quiz_cards(course.course_id)

        # EA50 has quiz cards from multiple units
        assert len(cards) >= 1

    def test_get_course_quiz_cards_includes_answers(
        self, quiz_service, populated_test_data
    ):
        """Test that course cards include answers."""
        course = populated_test_data['courses'][0]

        cards = quiz_service.get_course_quiz_cards(course.course_id)

        for card in cards:
            assert 'answers' in card
            assert len(card['answers']) >= 1

    def test_get_course_quiz_cards_nonexistent_course(
        self, quiz_service, clean_db
    ):
        """Test getting cards for nonexistent course returns empty list."""
        cards = quiz_service.get_course_quiz_cards(99999)

        assert cards == []

    def test_get_course_quiz_cards_without_session_raises_error(self):
        """Test that getting cards without db_session raises error."""
        service = QuizService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_course_quiz_cards(1)


class TestQuizServiceGetUnitCards:
    """Tests for getting quiz cards by unit."""

    def test_get_unit_quiz_cards_empty(self, quiz_service, sample_unit):
        """Test getting cards for unit with no cards."""
        cards = quiz_service.get_unit_quiz_cards(sample_unit.unit_id)

        assert isinstance(cards, list)

    def test_get_unit_quiz_cards_with_data(
        self, quiz_service, sample_unit, sample_concept, 
        sample_quiz_card, sample_quiz_answers
    ):
        """Test getting cards for unit with quiz cards."""
        cards = quiz_service.get_unit_quiz_cards(sample_unit.unit_id)

        assert len(cards) == 1
        assert cards[0]['id'] == sample_quiz_card.quiz_card_id

    def test_get_unit_quiz_cards_nonexistent_unit(self, quiz_service, clean_db):
        """Test getting cards for nonexistent unit returns empty list."""
        cards = quiz_service.get_unit_quiz_cards(99999)

        assert cards == []

    def test_get_unit_quiz_cards_without_session_raises_error(self):
        """Test that getting cards without db_session raises error."""
        service = QuizService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_unit_quiz_cards(1)


class TestQuizServiceGetAllCards:
    """Tests for getting all quiz cards."""

    def test_get_all_quiz_cards_empty(self, quiz_service, clean_db):
        """Test getting all cards when none exist."""
        cards = quiz_service.get_all_quiz_cards()

        assert cards == []

    def test_get_all_quiz_cards_with_data(
        self, quiz_service, populated_test_data
    ):
        """Test getting all cards in system."""
        cards = quiz_service.get_all_quiz_cards()

        # populated_test_data has 3 quiz cards
        assert len(cards) == 3

    def test_get_all_quiz_cards_includes_answers(
        self, quiz_service, sample_quiz_card, sample_quiz_answers
    ):
        """Test that all cards include answers."""
        cards = quiz_service.get_all_quiz_cards()

        for card in cards:
            assert 'answers' in card

    def test_get_all_quiz_cards_without_session_raises_error(self):
        """Test that getting cards without db_session raises error."""
        service = QuizService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_all_quiz_cards()


class TestQuizServiceSubmitAnswer:
    """Tests for answer submission."""

    def test_submit_answer_correct(
        self, quiz_service, sample_user, sample_quiz_card, sample_quiz_answers
    ):
        """Test submitting a correct answer."""
        correct_answer = next(a for a in sample_quiz_answers if a.is_correct)

        result = quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id,
            is_first_attempt=True
        )

        assert result['is_correct'] is True
        assert result['times_seen'] == 1
        assert result['times_correct'] == 1
        assert 'explanation' in result

    def test_submit_answer_incorrect(
        self, quiz_service, sample_user, sample_quiz_card, sample_quiz_answers
    ):
        """Test submitting an incorrect answer."""
        incorrect_answer = next(
            a for a in sample_quiz_answers if not a.is_correct
        )

        result = quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=incorrect_answer.answer_id,
            is_first_attempt=True
        )

        assert result['is_correct'] is False
        assert result['times_seen'] == 1
        assert result['times_correct'] == 0

    def test_submit_answer_creates_user_card(
        self, quiz_service, sample_user, sample_quiz_card, 
        sample_quiz_answers, clean_db
    ):
        """Test that submitting answer creates UserCard record."""
        correct_answer = next(a for a in sample_quiz_answers if a.is_correct)

        # Verify no UserCard exists
        existing = clean_db.query(UserCard).filter(
            UserCard.user_id == sample_user.user_id,
            UserCard.quiz_card_id == sample_quiz_card.quiz_card_id
        ).first()
        assert existing is None

        quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id
        )

        # Verify UserCard was created
        user_card = clean_db.query(UserCard).filter(
            UserCard.user_id == sample_user.user_id,
            UserCard.quiz_card_id == sample_quiz_card.quiz_card_id
        ).first()
        assert user_card is not None

    def test_submit_answer_updates_existing_user_card(
        self, quiz_service, sample_user, sample_quiz_card, 
        sample_quiz_answers, clean_db
    ):
        """Test that submitting answer updates existing UserCard."""
        correct_answer = next(a for a in sample_quiz_answers if a.is_correct)

        # Submit first answer
        quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id,
            is_first_attempt=True
        )

        # Submit second answer
        result = quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id,
            is_first_attempt=True
        )

        assert result['times_seen'] == 2
        assert result['times_correct'] == 2

    def test_submit_answer_not_first_attempt_no_success_increment(
        self, quiz_service, sample_user, sample_quiz_card, sample_quiz_answers
    ):
        """Test that non-first attempts don't increment success count."""
        correct_answer = next(a for a in sample_quiz_answers if a.is_correct)

        # First attempt
        quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id,
            is_first_attempt=True
        )

        # Second attempt (not first)
        result = quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id,
            is_first_attempt=False  # Not first attempt
        )

        # times_seen increments but times_correct should stay at 1
        assert result['times_seen'] == 2
        assert result['times_correct'] == 1

    def test_submit_answer_invalid_answer_id(
        self, quiz_service, sample_user, sample_quiz_card
    ):
        """Test submitting with invalid answer_id raises error."""
        with pytest.raises(ValueError, match="answer"):
            quiz_service.submit_answer(
                user_id=sample_user.user_id,
                quiz_card_id=sample_quiz_card.quiz_card_id,
                answer_id=99999  # Invalid
            )

    def test_submit_answer_updates_last_reviewed(
        self, quiz_service, sample_user, sample_quiz_card, 
        sample_quiz_answers, clean_db
    ):
        """Test that submitting answer updates last_reviewed timestamp."""
        correct_answer = next(a for a in sample_quiz_answers if a.is_correct)
        before = datetime.utcnow()

        quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id
        )

        user_card = clean_db.query(UserCard).filter(
            UserCard.user_id == sample_user.user_id,
            UserCard.quiz_card_id == sample_quiz_card.quiz_card_id
        ).first()

        assert user_card.last_reviewed is not None
        assert user_card.last_reviewed >= before

    def test_submit_answer_without_session_raises_error(self):
        """Test that submitting without db_session raises error."""
        service = QuizService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.submit_answer(1, 1, 1)


class TestQuizServiceIntegration:
    """Integration tests for QuizService."""

    def test_get_card_then_submit_answer(
        self, quiz_service, sample_user, sample_quiz_card, sample_quiz_answers
    ):
        """Test getting a card and then submitting an answer."""
        # Get the card
        card = quiz_service.get_quiz_card_by_id(sample_quiz_card.quiz_card_id)
        assert card is not None

        # Find correct answer from card
        correct_answer_id = next(
            a['id'] for a in card['answers'] if a['is_correct']
        )

        # Submit answer
        result = quiz_service.submit_answer(
            user_id=sample_user.user_id,
            quiz_card_id=card['id'],
            answer_id=correct_answer_id
        )

        assert result['is_correct'] is True

    def test_multiple_users_independent_progress(
        self, quiz_service, sample_quiz_card, sample_quiz_answers, clean_db
    ):
        """Test that different users have independent progress."""
        from werkzeug.security import generate_password_hash
        from backend.database.models import User

        # Create two users
        user1 = User(
            username="user1",
            email="user1@minerva.edu",
            password_hash=generate_password_hash("pass")
        )
        user2 = User(
            username="user2",
            email="user2@minerva.edu",
            password_hash=generate_password_hash("pass")
        )
        clean_db.add_all([user1, user2])
        clean_db.commit()
        clean_db.refresh(user1)
        clean_db.refresh(user2)

        correct_answer = next(a for a in sample_quiz_answers if a.is_correct)

        # User1 submits twice
        quiz_service.submit_answer(
            user_id=user1.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id
        )
        result1 = quiz_service.submit_answer(
            user_id=user1.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id
        )

        # User2 submits once
        result2 = quiz_service.submit_answer(
            user_id=user2.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_id=correct_answer.answer_id
        )

        # Progress should be independent
        assert result1['times_seen'] == 2
        assert result2['times_seen'] == 1


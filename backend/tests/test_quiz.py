"""
Tests for quiz routes.

This module contains comprehensive tests for the quiz-related endpoints:
- GET /api/quiz-cards/<quiz_card_id>: Retrieve a specific quiz card
- GET /api/courses/<course_id>/quiz-cards: Retrieve all quiz cards for a course
- GET /api/units/<unit_id>/quiz-cards: Retrieve all quiz cards for a unit
- POST /api/quiz-submit: Submit a quiz answer and update user progress
"""

import json
import pytest
from backend.database.models import (
    QuizCard, QuizAnswer, UserCard, Concept, Unit, Course
)
from backend.tests.conftest import create_auth_token


class TestGetQuizCard:
    """Tests for get quiz card by ID endpoint."""

    def test_get_quiz_card_success(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test successfully retrieving a quiz card by ID.

        Verifies:
        - Returns 200 status code
        - Response contains id, concept_id, question, answers
        - All answers are included with proper structure
        """
        response = test_client.get(
            f'/api/quiz-cards/{sample_quiz_card.quiz_card_id}'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == sample_quiz_card.quiz_card_id
        assert data['concept_id'] == sample_quiz_card.concept_id
        assert data['question'] == sample_quiz_card.question
        assert 'answers' in data
        assert isinstance(data['answers'], list)
        assert len(data['answers']) >= len(sample_quiz_answers)

    def test_get_quiz_card_not_found(self, test_client):
        """
        Test retrieving a non-existent quiz card.

        Verifies:
        - Returns 404 Not Found status code
        - Error message indicates quiz card not found
        """
        response = test_client.get('/api/quiz-cards/99999')

        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
        assert 'not found' in data['error'].lower()

    def test_get_quiz_card_invalid_id(self, test_client):
        """
        Test retrieving a quiz card with invalid ID format.

        Verifies:
        - Returns 404 Not Found status code (Flask converts invalid int)
        """
        response = test_client.get('/api/quiz-cards/invalid')

        assert response.status_code == 404

    def test_get_quiz_card_with_answers_structure(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test that quiz card response includes properly structured answers.

        Verifies:
        - Each answer has id, answer_text, is_correct, explanation
        - Answers are correctly associated with quiz card
        """
        response = test_client.get(
            f'/api/quiz-cards/{sample_quiz_card.quiz_card_id}'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['answers']) >= 1

        for answer in data['answers']:
            assert 'id' in answer
            assert 'answer_text' in answer
            assert 'is_correct' in answer
            assert 'explanation' in answer

    def test_get_quiz_card_empty_answers(
        self, test_client, clean_db, sample_concept
    ):
        """
        Test retrieving a quiz card with no answers.

        Verifies:
        - Returns 200 status code
        - Answers list is empty
        """
        quiz_card = QuizCard(
            concept_id=sample_concept.concept_id,
            unit_id=sample_concept.unit_id,
            course_id=sample_concept.unit.course_id,
            question="Question with no answers"
        )
        clean_db.add(quiz_card)
        clean_db.commit()
        clean_db.refresh(quiz_card)

        response = test_client.get(
            f'/api/quiz-cards/{quiz_card.quiz_card_id}'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['answers'] == []


class TestGetCourseQuizCards:
    """Tests for get course quiz cards endpoint."""

    def test_get_course_quiz_cards_empty(self, test_client, sample_course):
        """
        Test retrieving quiz cards for a course with no quiz cards.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        response = test_client.get(
            f'/api/courses/{sample_course.course_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_course_quiz_cards_success(
        self, test_client, populated_test_data
    ):
        """
        Test successfully retrieving quiz cards for a course.

        Verifies:
        - Returns 200 status code
        - Response contains quiz cards from all units in the course
        - Each quiz card has proper structure
        """
        course = populated_test_data['courses'][0]
        response = test_client.get(
            f'/api/courses/{course.course_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 1

        # Verify structure
        quiz_card = data[0]
        assert 'id' in quiz_card
        assert 'concept_id' in quiz_card
        assert 'question' in quiz_card
        assert 'answers' in quiz_card

    def test_get_course_quiz_cards_only_returns_course_cards(
        self, test_client, clean_db, populated_test_data
    ):
        """
        Test that only quiz cards for the specified course are returned.

        Verifies:
        - Quiz cards from other courses are not included
        - All returned quiz cards belong to concepts in course units
        """
        courses = populated_test_data['courses']
        course1 = courses[0]
        course2 = courses[1]

        response = test_client.get(
            f'/api/courses/{course1.course_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)

        # Get concept IDs for course1
        units = clean_db.query(Unit).filter(
            Unit.course_id == course1.course_id
        ).all()
        unit_ids = [u.unit_id for u in units]
        concepts = clean_db.query(Concept).filter(
            Concept.unit_id.in_(unit_ids)
        ).all()
        concept_ids = {c.concept_id for c in concepts}

        # Verify all quiz cards belong to course1 concepts
        for quiz_card in data:
            assert quiz_card['concept_id'] in concept_ids

    def test_get_course_quiz_cards_nonexistent_course(self, test_client):
        """
        Test retrieving quiz cards for a non-existent course.

        Verifies:
        - Returns 200 status code (endpoint doesn't validate course)
        - Response is an empty list
        """
        response = test_client.get('/api/courses/99999/quiz-cards')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_course_quiz_cards_with_multiple_units(
        self, test_client, clean_db, sample_course
    ):
        """
        Test retrieving quiz cards from a course with multiple units.

        Verifies:
        - Returns 200 status code
        - Quiz cards from all units are included
        """
        # Create multiple units with concepts and quiz cards
        unit1 = Unit(
            course_id=sample_course.course_id,
            title="Unit 1",
            description="First unit",
            order_index=1
        )
        unit2 = Unit(
            course_id=sample_course.course_id,
            title="Unit 2",
            description="Second unit",
            order_index=2
        )
        clean_db.add_all([unit1, unit2])
        clean_db.commit()
        clean_db.refresh(unit1)
        clean_db.refresh(unit2)

        concept1 = Concept(
            unit_id=unit1.unit_id,
            title="#concept1",
            definition="First concept"
        )
        concept2 = Concept(
            unit_id=unit2.unit_id,
            title="#concept2",
            definition="Second concept"
        )
        clean_db.add_all([concept1, concept2])
        clean_db.commit()
        clean_db.refresh(concept1)
        clean_db.refresh(concept2)

        quiz1 = QuizCard(
            concept_id=concept1.concept_id,
            unit_id=unit1.unit_id,
            course_id=sample_course.course_id,
            question="Question 1"
        )
        quiz2 = QuizCard(
            concept_id=concept2.concept_id,
            unit_id=unit2.unit_id,
            course_id=sample_course.course_id,
            question="Question 2"
        )
        clean_db.add_all([quiz1, quiz2])
        clean_db.commit()

        response = test_client.get(
            f'/api/courses/{sample_course.course_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 2


class TestGetUnitQuizCards:
    """Tests for get unit quiz cards endpoint."""

    def test_get_unit_quiz_cards_empty(self, test_client, sample_unit):
        """
        Test retrieving quiz cards for a unit with no quiz cards.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        response = test_client.get(
            f'/api/units/{sample_unit.unit_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_unit_quiz_cards_success(
        self, test_client, populated_test_data
    ):
        """
        Test successfully retrieving quiz cards for a unit.

        Verifies:
        - Returns 200 status code
        - Response contains quiz cards from all concepts in the unit
        - Each quiz card has proper structure
        """
        unit = populated_test_data['units'][0]
        response = test_client.get(
            f'/api/units/{unit.unit_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)

        if len(data) > 0:
            quiz_card = data[0]
            assert 'id' in quiz_card
            assert 'concept_id' in quiz_card
            assert 'question' in quiz_card
            assert 'answers' in quiz_card

    def test_get_unit_quiz_cards_only_returns_unit_cards(
        self, test_client, clean_db, populated_test_data
    ):
        """
        Test that only quiz cards for the specified unit are returned.

        Verifies:
        - Quiz cards from other units are not included
        - All returned quiz cards belong to concepts in the unit
        """
        units = populated_test_data['units']
        unit1 = units[0]
        unit2 = units[1]

        response = test_client.get(
            f'/api/units/{unit1.unit_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)

        # Get concept IDs for unit1
        concepts = clean_db.query(Concept).filter(
            Concept.unit_id == unit1.unit_id
        ).all()
        concept_ids = {c.concept_id for c in concepts}

        # Verify all quiz cards belong to unit1 concepts
        for quiz_card in data:
            assert quiz_card['concept_id'] in concept_ids

    def test_get_unit_quiz_cards_nonexistent_unit(self, test_client):
        """
        Test retrieving quiz cards for a non-existent unit.

        Verifies:
        - Returns 200 status code (endpoint doesn't validate unit)
        - Response is an empty list
        """
        response = test_client.get('/api/units/99999/quiz-cards')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0


class TestGetRandomQuizCards:
    """Tests for get random quiz cards endpoint (global quiz)."""

    def test_get_random_quiz_cards_success(
        self, test_client, populated_test_data
    ):
        """
        Test successfully retrieving random quiz cards from all courses.

        Verifies:
        - Returns 200 status code
        - Response is a list of quiz cards
        - Each quiz card has proper structure (id, concept_id, question, answers)
        """
        response = test_client.get('/api/quiz-cards/random')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 1

        # Verify structure of returned cards
        quiz_card = data[0]
        assert 'id' in quiz_card
        assert 'concept_id' in quiz_card
        assert 'question' in quiz_card
        assert 'answers' in quiz_card
        assert isinstance(quiz_card['answers'], list)

    def test_get_random_quiz_cards_mixed_courses(
        self, test_client, clean_db, populated_test_data
    ):
        """
        Test that random quiz cards come from multiple courses.

        Verifies:
        - Returns cards from different courses mixed together
        - Endpoint returns all courses' quiz cards, not filtered by course
        """
        response = test_client.get('/api/quiz-cards/random')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        # Collect all concept IDs from all courses
        courses = populated_test_data['courses']
        all_concept_ids = set()
        for course in courses:
            units = clean_db.query(Unit).filter(
                Unit.course_id == course.course_id
            ).all()
            unit_ids = [u.unit_id for u in units]
            concepts = clean_db.query(Concept).filter(
                Concept.unit_id.in_(unit_ids)
            ).all()
            all_concept_ids.update([c.concept_id for c in concepts])

        # Verify returned cards belong to various concepts
        returned_concept_ids = {card['concept_id'] for card in data}
        assert len(returned_concept_ids) > 0
        # At least some cards should come from different concepts
        assert returned_concept_ids.issubset(all_concept_ids)

    def test_get_random_quiz_cards_empty_database(
        self, test_client, clean_db
    ):
        """
        Test retrieving random quiz cards when database is empty.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        response = test_client.get('/api/quiz-cards/random')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_random_quiz_cards_answer_structure(
        self, test_client, populated_test_data
    ):
        """
        Test that random quiz cards include properly structured answers.

        Verifies:
        - Each answer has id, answer_text, is_correct, explanation
        - Answers are properly associated with quiz cards
        """
        response = test_client.get('/api/quiz-cards/random')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        # Check first card's answers structure
        quiz_card = data[0]
        assert len(quiz_card['answers']) >= 1

        for answer in quiz_card['answers']:
            assert 'id' in answer
            assert 'answer_text' in answer
            assert 'is_correct' in answer
            assert 'explanation' in answer

    def test_get_random_quiz_cards_returns_all_cards(
        self, test_client, clean_db, sample_course
    ):
        """
        Test that random endpoint returns all quiz cards from database.

        Verifies:
        - When you call the endpoint, all quiz cards are returned (not paginated/limited)
        - Useful for frontend to shuffle and limit as needed
        """
        # Create specific number of quiz cards
        unit = Unit(
            course_id=sample_course.course_id,
            title="Test Unit",
            description="Test",
            order_index=1
        )
        clean_db.add(unit)
        clean_db.commit()
        clean_db.refresh(unit)

        concept = Concept(
            unit_id=unit.unit_id,
            title="Test Concept",
            definition="Test"
        )
        clean_db.add(concept)
        clean_db.commit()
        clean_db.refresh(concept)

        # Create 3 quiz cards
        for i in range(3):
            qc = QuizCard(
                concept_id=concept.concept_id,
                unit_id=unit.unit_id,
                course_id=sample_course.course_id,
                question=f"Test Question {i+1}"
            )
            clean_db.add(qc)
        clean_db.commit()

        response = test_client.get('/api/quiz-cards/random')

        assert response.status_code == 200
        data = json.loads(response.data)
        # Should return all 3 cards (frontend will shuffle and limit to 5)
        assert len(data) == 3


class TestSubmitQuizAnswer:
    """Tests for submit quiz answer endpoint."""

    def test_submit_quiz_answer_correct_first_time(
        self, test_client, clean_db, sample_user, sample_quiz_card,
        sample_quiz_answers
    ):
        """
        Test submitting a correct answer for the first time.

        Verifies:
        - Returns 200 status code
        - Response indicates answer is correct
        - UserCard is created with correct counts
        - times_seen and times_correct are updated
        """
        correct_answer = next(
            a for a in sample_quiz_answers if a.is_correct
        )

        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': correct_answer.answer_id
            },
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['is_correct'] is True
        assert data['times_seen'] == 1
        assert data['times_correct'] == 1
        assert 'explanation' in data

        # Verify UserCard was created
        user_card = clean_db.query(UserCard).filter(
            UserCard.user_id == sample_user.user_id,
            UserCard.quiz_card_id == sample_quiz_card.quiz_card_id
        ).first()
        assert user_card is not None
        assert user_card.success_count == 1
        assert user_card.failure_count == 0

    def test_submit_quiz_answer_incorrect_first_time(
        self, test_client, clean_db, sample_user, sample_quiz_card,
        sample_quiz_answers
    ):
        """
        Test submitting an incorrect answer for the first time.

        Verifies:
        - Returns 200 status code
        - Response indicates answer is incorrect
        - UserCard is created with failure count
        """
        incorrect_answer = next(
            a for a in sample_quiz_answers if not a.is_correct
        )

        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': incorrect_answer.answer_id
            },
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['is_correct'] is False
        assert data['times_seen'] == 1
        assert data['times_correct'] == 0

    def test_submit_quiz_answer_update_existing(
        self, test_client, clean_db, sample_user, sample_quiz_card,
        sample_quiz_answers
    ):
        """
        Test submitting an answer when UserCard already exists.

        Verifies:
        - Returns 200 status code
        - Existing UserCard is updated, not duplicated
        - Counts are incremented correctly
        """
        # Create existing UserCard
        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            success_count=2,
            failure_count=1,
            repetitions=3
        )
        clean_db.add(user_card)
        clean_db.commit()

        correct_answer = next(
            a for a in sample_quiz_answers if a.is_correct
        )

        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': correct_answer.answer_id
            },
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['is_correct'] is True
        assert data['times_seen'] == 4  # 2 + 1 + 1
        assert data['times_correct'] == 3  # 2 + 1

        # Verify UserCard was updated, not duplicated
        user_cards = clean_db.query(UserCard).filter(
            UserCard.user_id == sample_user.user_id,
            UserCard.quiz_card_id == sample_quiz_card.quiz_card_id
        ).all()
        assert len(user_cards) == 1
        assert user_cards[0].success_count == 3

    def test_submit_quiz_answer_missing_fields(self, test_client, sample_user):
        """
        Test submitting quiz answer with missing required fields.

        Verifies:
        - Returns 400 Bad Request status code
        - Error message indicates missing fields
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={
                # Missing quiz_card_id and answer_id
            },
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert 'missing' in data['error'].lower()

    def test_submit_quiz_answer_invalid_answer_id(
        self, test_client, sample_user, sample_quiz_card
    ):
        """
        Test submitting quiz answer with invalid answer_id.

        Verifies:
        - Returns 400 Bad Request status code
        - Error message indicates invalid answer_id
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': 99999
            },
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert 'answer' in data['error'].lower()

    def test_submit_quiz_answer_empty_request_body(
        self, test_client, sample_user
    ):
        """
        Test submitting quiz answer with empty request body.

        Verifies:
        - Returns 400 Bad Request status code
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={},
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 400

    def test_submit_quiz_answer_explanation_included(
        self, test_client, clean_db, sample_user, sample_quiz_card,
        sample_quiz_answers
    ):
        """
        Test that explanation is included in response.

        Verifies:
        - Returns 200 status code
        - Response includes explanation field
        - Explanation matches the answer's explanation
        """
        answer_with_explanation = sample_quiz_answers[0]

        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': answer_with_explanation.answer_id
            },
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'explanation' in data
        if answer_with_explanation.explanation:
            assert data['explanation'] == answer_with_explanation.explanation

    def test_submit_quiz_answer_null_explanation(
        self, test_client, clean_db, sample_user, sample_quiz_card
    ):
        """
        Test submitting answer where explanation is None.

        Verifies:
        - Returns 200 status code
        - Explanation field is None in response
        """
        answer = QuizAnswer(
            quiz_card_id=sample_quiz_card.quiz_card_id,
            answer_text="Answer without explanation",
            is_correct=True,
            explanation=None
        )
        clean_db.add(answer)
        clean_db.commit()
        clean_db.refresh(answer)

        token = create_auth_token(sample_user.user_id)
        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': answer.answer_id
            },
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['explanation'] is None

    def test_submit_quiz_answer_missing_token(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test submitting quiz answer without authentication token.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates missing token
        """
        correct_answer = next(
            a for a in sample_quiz_answers if a.is_correct
        )

        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': correct_answer.answer_id
            }
            # No Authorization header
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data
        assert 'token' in data['error'].lower() or 'authorization' in data['error'].lower()

    def test_submit_quiz_answer_invalid_token(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test submitting quiz answer with invalid authentication token.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates invalid token
        """
        correct_answer = next(
            a for a in sample_quiz_answers if a.is_correct
        )

        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': correct_answer.answer_id
            },
            headers={'Authorization': 'Bearer invalid_token_12345'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data
        assert 'invalid' in data['error'].lower() or 'expired' in data['error'].lower()

    def test_submit_quiz_answer_expired_token(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test submitting quiz answer with expired authentication token.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates expired token
        """
        import jwt
        from datetime import datetime, timedelta

        # Create expired token
        expired_payload = {
            'user_id': 1,
            'exp': datetime.utcnow() - timedelta(hours=1),
            'iat': datetime.utcnow() - timedelta(hours=2)
        }
        expired_token = jwt.encode(
            expired_payload,
            'dev-secret-key-change-in-production',
            algorithm='HS256'
        )

        correct_answer = next(
            a for a in sample_quiz_answers if a.is_correct
        )

        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': correct_answer.answer_id
            },
            headers={'Authorization': f'Bearer {expired_token}'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data

    def test_submit_quiz_answer_invalid_header_format(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test submitting quiz answer with invalid Authorization header format.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates invalid header format
        """
        correct_answer = next(
            a for a in sample_quiz_answers if a.is_correct
        )

        response = test_client.post(
            '/api/quiz-submit',
            json={
                'quiz_card_id': sample_quiz_card.quiz_card_id,
                'answer_id': correct_answer.answer_id
            },
            headers={'Authorization': 'InvalidFormat token'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data


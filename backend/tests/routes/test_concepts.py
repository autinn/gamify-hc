"""
Tests for concept routes.

This module contains comprehensive tests for the concept-related endpoints:
- GET /api/concepts/<concept_id>: Retrieve a specific concept by ID
- GET /api/concepts/<concept_id>/quiz-cards: Retrieve all quiz cards for a concept
"""

import json
import pytest
from backend.database.models import Concept, QuizCard, QuizAnswer


class TestGetConcept:
    """Tests for get concept by ID endpoint."""

    def test_get_concept_success(self, test_client, sample_concept):
        """
        Test successfully retrieving a concept by ID.

        Verifies:
        - Returns 200 status code
        - Response contains id, unit_id, name, tag, definition
        - All fields match the database record
        """
        response = test_client.get(
            f'/api/concepts/{sample_concept.concept_id}'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == sample_concept.concept_id
        assert data['unit_id'] == sample_concept.unit_id
        assert data['name'] == sample_concept.title
        assert data['tag'] == sample_concept.title  # Currently uses title
        assert data['definition'] == sample_concept.definition

    def test_get_concept_not_found(self, test_client):
        """
        Test retrieving a non-existent concept.

        Verifies:
        - Returns 404 Not Found status code
        - Error message indicates concept not found
        """
        response = test_client.get('/api/concepts/99999')

        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
        assert 'not found' in data['error'].lower()

    def test_get_concept_invalid_id(self, test_client):
        """
        Test retrieving a concept with invalid ID format.

        Verifies:
        - Returns 404 Not Found status code (Flask converts invalid int)
        """
        response = test_client.get('/api/concepts/invalid')

        assert response.status_code == 404

    def test_get_concept_with_null_definition(
        self, test_client, clean_db, sample_unit
    ):
        """
        Test retrieving a concept with null definition.

        Verifies:
        - Returns 200 status code
        - Definition field is None
        """
        concept = Concept(
            unit_id=sample_unit.unit_id,
            title="#testconcept",
            definition=None
        )
        clean_db.add(concept)
        clean_db.commit()
        clean_db.refresh(concept)

        response = test_client.get(
            f'/api/concepts/{concept.concept_id}'
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['definition'] is None

    def test_get_concept_tag_field(self, test_client, sample_concept):
        """
        Test that tag field is populated (currently uses title).

        Verifies:
        - Tag field is present and matches name/title
        """
        response = test_client.get(
            f'/api/concepts/{sample_concept.concept_id}'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'tag' in data
        assert data['tag'] == sample_concept.title


class TestGetConceptQuizCards:
    """Tests for get concept quiz cards endpoint."""

    def test_get_concept_quiz_cards_empty(
        self, test_client, sample_concept
    ):
        """
        Test retrieving quiz cards for a concept with no quiz cards.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        response = test_client.get(
            f'/api/concepts/{sample_concept.concept_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_concept_quiz_cards_success(
        self, test_client, populated_test_data
    ):
        """
        Test successfully retrieving quiz cards for a concept.

        Verifies:
        - Returns 200 status code
        - Response contains list of quiz cards
        - Each quiz card has id, concept_id, question, answers
        - Each answer has id, answer_text, is_correct, explanation
        """
        concept = populated_test_data['concepts'][0]
        response = test_client.get(
            f'/api/concepts/{concept.concept_id}/quiz-cards'
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
        assert isinstance(quiz_card['answers'], list)

        # Verify answer structure if answers exist
        if len(quiz_card['answers']) > 0:
            answer = quiz_card['answers'][0]
            assert 'id' in answer
            assert 'answer_text' in answer
            assert 'is_correct' in answer
            assert 'explanation' in answer

    def test_get_concept_quiz_cards_structure(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test that quiz card structure matches expected format.

        Verifies:
        - All quiz cards have consistent structure
        - Answers are properly nested
        """
        response = test_client.get(
            f'/api/concepts/{sample_quiz_card.concept_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        for quiz_card in data:
            assert isinstance(quiz_card['id'], int)
            assert isinstance(quiz_card['concept_id'], int)
            assert isinstance(quiz_card['question'], str)
            assert isinstance(quiz_card['answers'], list)

            for answer in quiz_card['answers']:
                assert isinstance(answer['id'], int)
                assert isinstance(answer['answer_text'], str)
                assert isinstance(answer['is_correct'], bool)
                assert isinstance(answer['explanation'], (str, type(None)))

    def test_get_concept_quiz_cards_only_returns_concept_cards(
        self, test_client, populated_test_data
    ):
        """
        Test that only quiz cards for the specified concept are returned.

        Verifies:
        - Quiz cards from other concepts are not included
        - All returned quiz cards have matching concept_id
        """
        concepts = populated_test_data['concepts']
        concept1 = concepts[0]
        concept2 = concepts[1]

        response = test_client.get(
            f'/api/concepts/{concept1.concept_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)

        # Verify all quiz cards belong to concept1
        for quiz_card in data:
            assert quiz_card['concept_id'] == concept1.concept_id
            assert quiz_card['concept_id'] != concept2.concept_id

    def test_get_concept_quiz_cards_nonexistent_concept(
        self, test_client
    ):
        """
        Test retrieving quiz cards for a non-existent concept.

        Verifies:
        - Returns 200 status code (endpoint doesn't validate concept)
        - Response is an empty list
        """
        response = test_client.get('/api/concepts/99999/quiz-cards')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_concept_quiz_cards_with_multiple_answers(
        self, test_client, sample_quiz_card, sample_quiz_answers
    ):
        """
        Test retrieving quiz cards with multiple answers.

        Verifies:
        - Returns 200 status code
        - All answers are included in the response
        - Answers are properly associated with quiz card
        """
        response = test_client.get(
            f'/api/concepts/{sample_quiz_card.concept_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        # Find the quiz card we're testing
        quiz_card = None
        for qc in data:
            if qc['id'] == sample_quiz_card.quiz_card_id:
                quiz_card = qc
                break

        assert quiz_card is not None
        assert len(quiz_card['answers']) >= len(sample_quiz_answers)

    def test_get_concept_quiz_cards_with_null_explanation(
        self, test_client, clean_db, sample_concept
    ):
        """
        Test retrieving quiz cards where some answers have null explanations.

        Verifies:
        - Returns 200 status code
        - Answers with null explanations are included
        - Explanation field is None for those answers
        """
        quiz_card = QuizCard(
            concept_id=sample_concept.concept_id,
            unit_id=sample_concept.unit_id,
            course_id=sample_concept.unit.course_id,
            question="Test question"
        )
        clean_db.add(quiz_card)
        clean_db.commit()
        clean_db.refresh(quiz_card)

        answer = QuizAnswer(
            quiz_card_id=quiz_card.quiz_card_id,
            answer_text="Test answer",
            is_correct=True,
            explanation=None
        )
        clean_db.add(answer)
        clean_db.commit()

        response = test_client.get(
            f'/api/concepts/{sample_concept.concept_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        # Find the quiz card we just created
        found = False
        for qc in data:
            if qc['id'] == quiz_card.quiz_card_id:
                assert len(qc['answers']) >= 1
                for ans in qc['answers']:
                    if ans['answer_text'] == "Test answer":
                        assert ans['explanation'] is None
                        found = True
        assert found

    def test_get_concept_quiz_cards_empty_answers(
        self, test_client, clean_db, sample_concept
    ):
        """
        Test retrieving quiz cards with no answers.

        Verifies:
        - Returns 200 status code
        - Quiz card is included with empty answers list
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
            f'/api/concepts/{sample_concept.concept_id}/quiz-cards'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        # Find the quiz card we just created
        found = False
        for qc in data:
            if qc['id'] == quiz_card.quiz_card_id:
                assert qc['answers'] == []
                found = True
        assert found


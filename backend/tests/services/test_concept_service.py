"""
Tests for ConceptService.

This module tests concept management functionality:
- Get concept by ID
- Get concept quiz cards
"""

import pytest
from backend.services.course import ConceptService
from backend.database.models import Concept, QuizCard, QuizAnswer


class TestConceptServiceGetById:
    """Tests for getting concept by ID."""

    def test_get_concept_by_id_found(self, concept_service, sample_concept):
        """Test getting an existing concept by ID."""
        concept = concept_service.get_concept_by_id(sample_concept.concept_id)

        assert concept is not None
        assert concept['id'] == sample_concept.concept_id
        assert concept['unit_id'] == sample_concept.unit_id
        assert concept['name'] == sample_concept.title
        assert concept['definition'] == sample_concept.definition

    def test_get_concept_by_id_not_found(self, concept_service, clean_db):
        """Test getting a nonexistent concept by ID."""
        concept = concept_service.get_concept_by_id(99999)

        assert concept is None

    def test_get_concept_by_id_structure(self, concept_service, sample_concept):
        """Test that returned concept has expected structure."""
        concept = concept_service.get_concept_by_id(sample_concept.concept_id)

        expected_keys = {'id', 'unit_id', 'name', 'tag', 'definition'}
        assert set(concept.keys()) == expected_keys

    def test_get_concept_by_id_tag_uses_title(
        self, concept_service, sample_concept
    ):
        """Test that tag field currently uses title as placeholder."""
        concept = concept_service.get_concept_by_id(sample_concept.concept_id)

        # Currently tag = title (placeholder behavior)
        assert concept['tag'] == concept['name']

    def test_get_concept_by_id_without_session_raises_error(self):
        """Test that getting concept without db_session raises error."""
        service = ConceptService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_concept_by_id(1)


class TestConceptServiceGetQuizCards:
    """Tests for getting concept quiz cards."""

    def test_get_concept_quiz_cards_empty(self, concept_service, sample_concept):
        """Test getting quiz cards for concept with no cards."""
        # sample_concept has no quiz cards by default
        cards = concept_service.get_concept_quiz_cards(sample_concept.concept_id)

        # May be empty if sample_quiz_card fixture wasn't used
        assert isinstance(cards, list)

    def test_get_concept_quiz_cards_single(
        self, concept_service, sample_concept, sample_quiz_card, sample_quiz_answers
    ):
        """Test getting a single quiz card with answers."""
        cards = concept_service.get_concept_quiz_cards(sample_concept.concept_id)

        assert len(cards) == 1
        assert cards[0]['id'] == sample_quiz_card.quiz_card_id
        assert cards[0]['concept_id'] == sample_concept.concept_id
        assert len(cards[0]['answers']) == 2  # sample_quiz_answers has 2 answers

    def test_get_concept_quiz_cards_structure(
        self, concept_service, sample_concept, sample_quiz_card, sample_quiz_answers
    ):
        """Test that returned quiz cards have expected structure."""
        cards = concept_service.get_concept_quiz_cards(sample_concept.concept_id)

        card_keys = {'id', 'concept_id', 'question', 'answers'}
        assert set(cards[0].keys()) == card_keys

        answer_keys = {'id', 'answer_text', 'is_correct', 'explanation'}
        assert set(cards[0]['answers'][0].keys()) == answer_keys

    def test_get_concept_quiz_cards_answers_included(
        self, concept_service, sample_concept, sample_quiz_card, sample_quiz_answers
    ):
        """Test that quiz card answers are included and correct."""
        cards = concept_service.get_concept_quiz_cards(sample_concept.concept_id)

        answers = cards[0]['answers']
        correct_answers = [a for a in answers if a['is_correct']]
        incorrect_answers = [a for a in answers if not a['is_correct']]

        assert len(correct_answers) == 1
        assert len(incorrect_answers) == 1
        assert correct_answers[0]['answer_text'] == "Pie chart"

    def test_get_concept_quiz_cards_nonexistent_concept(
        self, concept_service, clean_db
    ):
        """Test getting quiz cards for nonexistent concept returns empty list."""
        cards = concept_service.get_concept_quiz_cards(99999)

        assert cards == []

    def test_get_concept_quiz_cards_without_session_raises_error(self):
        """Test that getting quiz cards without db_session raises error."""
        service = ConceptService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_concept_quiz_cards(1)


class TestConceptServiceIntegration:
    """Integration tests for ConceptService."""

    def test_get_concept_then_quiz_cards(
        self, concept_service, sample_concept, sample_quiz_card, sample_quiz_answers
    ):
        """Test getting a concept and then its quiz cards."""
        concept = concept_service.get_concept_by_id(sample_concept.concept_id)
        cards = concept_service.get_concept_quiz_cards(concept['id'])

        assert concept is not None
        assert len(cards) == 1
        assert cards[0]['concept_id'] == concept['id']

    def test_quiz_cards_belong_to_correct_concept(
        self, concept_service, populated_test_data
    ):
        """Test that quiz cards are correctly associated with their concepts."""
        concepts = populated_test_data['concepts']

        for concept in concepts:
            cards = concept_service.get_concept_quiz_cards(concept.concept_id)
            for card in cards:
                assert card['concept_id'] == concept.concept_id

    def test_multiple_concepts_independent_quiz_cards(
        self, concept_service, populated_test_data
    ):
        """Test that different concepts have their own quiz cards."""
        concept1 = populated_test_data['concepts'][0]
        concept3 = populated_test_data['concepts'][2]  # Different unit

        cards1 = concept_service.get_concept_quiz_cards(concept1.concept_id)
        cards3 = concept_service.get_concept_quiz_cards(concept3.concept_id)

        # Quiz card IDs should be different
        card1_ids = {c['id'] for c in cards1}
        card3_ids = {c['id'] for c in cards3}

        assert card1_ids.isdisjoint(card3_ids)


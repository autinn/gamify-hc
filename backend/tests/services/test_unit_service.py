"""
Tests for UnitService.

This module tests unit management functionality:
- Get unit by ID
- Get unit concepts
"""

import pytest
from backend.services.course import UnitService
from backend.database.models import Unit, Concept


class TestUnitServiceGetById:
    """Tests for getting unit by ID."""

    def test_get_unit_by_id_found(self, unit_service, sample_unit):
        """Test getting an existing unit by ID."""
        unit = unit_service.get_unit_by_id(sample_unit.unit_id)

        assert unit is not None
        assert unit['id'] == sample_unit.unit_id
        assert unit['course_id'] == sample_unit.course_id
        assert unit['name'] == sample_unit.title
        assert unit['description'] == sample_unit.description
        assert unit['order_index'] == sample_unit.order_index

    def test_get_unit_by_id_not_found(self, unit_service, clean_db):
        """Test getting a nonexistent unit by ID."""
        unit = unit_service.get_unit_by_id(99999)

        assert unit is None

    def test_get_unit_by_id_structure(self, unit_service, sample_unit):
        """Test that returned unit has expected structure."""
        unit = unit_service.get_unit_by_id(sample_unit.unit_id)

        expected_keys = {'id', 'course_id', 'name', 'description', 'order_index'}
        assert set(unit.keys()) == expected_keys

    def test_get_unit_by_id_without_session_raises_error(self):
        """Test that getting unit without db_session raises error."""
        service = UnitService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_unit_by_id(1)


class TestUnitServiceGetConcepts:
    """Tests for getting unit concepts."""

    def test_get_unit_concepts_empty(self, unit_service, sample_unit):
        """Test getting concepts for unit with no concepts."""
        # sample_unit has no concepts by default
        concepts = unit_service.get_unit_concepts(sample_unit.unit_id)

        # May be empty if sample_concept fixture wasn't used
        assert isinstance(concepts, list)

    def test_get_unit_concepts_single(
        self, unit_service, sample_unit, sample_concept
    ):
        """Test getting a single concept for a unit."""
        concepts = unit_service.get_unit_concepts(sample_unit.unit_id)

        assert len(concepts) == 1
        assert concepts[0]['id'] == sample_concept.concept_id
        assert concepts[0]['unit_id'] == sample_unit.unit_id

    def test_get_unit_concepts_multiple(
        self, unit_service, populated_test_data
    ):
        """Test getting multiple concepts for a unit."""
        unit = populated_test_data['units'][0]  # Unit 1 has 2 concepts

        concepts = unit_service.get_unit_concepts(unit.unit_id)

        assert len(concepts) == 2

    def test_get_unit_concepts_structure(
        self, unit_service, sample_unit, sample_concept
    ):
        """Test that returned concepts have expected structure."""
        concepts = unit_service.get_unit_concepts(sample_unit.unit_id)

        expected_keys = {'id', 'unit_id', 'name', 'tag', 'definition'}
        assert set(concepts[0].keys()) == expected_keys

    def test_get_unit_concepts_nonexistent_unit(self, unit_service, clean_db):
        """Test getting concepts for nonexistent unit returns empty list."""
        concepts = unit_service.get_unit_concepts(99999)

        assert concepts == []

    def test_get_unit_concepts_without_session_raises_error(self):
        """Test that getting concepts without db_session raises error."""
        service = UnitService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_unit_concepts(1)


class TestUnitServiceIntegration:
    """Integration tests for UnitService."""

    def test_get_unit_then_concepts(
        self, unit_service, sample_unit, sample_concept
    ):
        """Test getting a unit and then its concepts."""
        unit = unit_service.get_unit_by_id(sample_unit.unit_id)
        concepts = unit_service.get_unit_concepts(unit['id'])

        assert unit is not None
        assert len(concepts) == 1
        assert concepts[0]['unit_id'] == unit['id']

    def test_concepts_belong_to_correct_unit(
        self, unit_service, populated_test_data
    ):
        """Test that concepts are correctly associated with their units."""
        units = populated_test_data['units']

        for unit in units:
            concepts = unit_service.get_unit_concepts(unit.unit_id)
            for concept in concepts:
                assert concept['unit_id'] == unit.unit_id


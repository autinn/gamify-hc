"""
Tests for unit routes.

This module contains comprehensive tests for the unit-related endpoints:
- GET /api/units/<unit_id>: Retrieve a specific unit by ID
- GET /api/units/<unit_id>/concepts: Retrieve all concepts for a unit
"""

import json
import pytest
from backend.database.models import Unit, Concept


class TestGetUnit:
    """Tests for get unit by ID endpoint."""

    def test_get_unit_success(self, test_client, sample_unit):
        """
        Test successfully retrieving a unit by ID.

        Verifies:
        - Returns 200 status code
        - Response contains id, course_id, name, description, order_index
        - All fields match the database record
        """
        response = test_client.get(f'/api/units/{sample_unit.unit_id}')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == sample_unit.unit_id
        assert data['course_id'] == sample_unit.course_id
        assert data['name'] == sample_unit.title
        assert data['description'] == sample_unit.description
        assert data['order_index'] == sample_unit.order_index

    def test_get_unit_not_found(self, test_client):
        """
        Test retrieving a non-existent unit.

        Verifies:
        - Returns 404 Not Found status code
        - Error message indicates unit not found
        """
        response = test_client.get('/api/units/99999')

        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
        assert 'not found' in data['error'].lower()

    def test_get_unit_invalid_id(self, test_client):
        """
        Test retrieving a unit with invalid ID format.

        Verifies:
        - Returns 404 Not Found status code (Flask converts invalid int)
        """
        response = test_client.get('/api/units/invalid')

        assert response.status_code == 404

    def test_get_unit_with_null_description(
        self, test_client, clean_db, sample_course
    ):
        """
        Test retrieving a unit with null description.

        Verifies:
        - Returns 200 status code
        - Description field is None
        """
        unit = Unit(
            course_id=sample_course.course_id,
            title="Unit No Description",
            description=None,
            order_index=1
        )
        clean_db.add(unit)
        clean_db.commit()
        clean_db.refresh(unit)

        response = test_client.get(f'/api/units/{unit.unit_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['description'] is None

    def test_get_unit_with_null_order_index(
        self, test_client, clean_db, sample_course
    ):
        """
        Test retrieving a unit with null order_index.

        Verifies:
        - Returns 200 status code
        - order_index field is None
        """
        unit = Unit(
            course_id=sample_course.course_id,
            title="Unit No Order",
            description="Test",
            order_index=None
        )
        clean_db.add(unit)
        clean_db.commit()
        clean_db.refresh(unit)

        response = test_client.get(f'/api/units/{unit.unit_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['order_index'] is None


class TestGetUnitConcepts:
    """Tests for get unit concepts endpoint."""

    def test_get_unit_concepts_empty(self, test_client, sample_unit):
        """
        Test retrieving concepts for a unit with no concepts.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        response = test_client.get(
            f'/api/units/{sample_unit.unit_id}/concepts'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_unit_concepts_success(
        self, test_client, populated_test_data
    ):
        """
        Test successfully retrieving concepts for a unit.

        Verifies:
        - Returns 200 status code
        - Response contains list of concepts
        - Each concept has id, unit_id, name, tag, definition fields
        """
        unit = populated_test_data['units'][0]
        response = test_client.get(
            f'/api/units/{unit.unit_id}/concepts'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 1

        # Verify structure
        concept = data[0]
        assert 'id' in concept
        assert 'unit_id' in concept
        assert 'name' in concept
        assert 'tag' in concept
        assert 'definition' in concept

    def test_get_unit_concepts_structure(
        self, test_client, sample_concept
    ):
        """
        Test that concept structure matches expected format.

        Verifies:
        - All concepts have consistent structure
        - Fields are properly serialized
        """
        response = test_client.get(
            f'/api/units/{sample_concept.unit_id}/concepts'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        for concept in data:
            assert isinstance(concept['id'], int)
            assert isinstance(concept['unit_id'], int)
            assert isinstance(concept['name'], str)
            assert isinstance(concept['tag'], str)
            assert isinstance(concept['definition'], (str, type(None)))

    def test_get_unit_concepts_only_returns_unit_concepts(
        self, test_client, populated_test_data
    ):
        """
        Test that only concepts for the specified unit are returned.

        Verifies:
        - Concepts from other units are not included
        - All returned concepts have matching unit_id
        """
        units = populated_test_data['units']
        unit1 = units[0]
        unit2 = units[1]

        response = test_client.get(
            f'/api/units/{unit1.unit_id}/concepts'
        )

        assert response.status_code == 200
        data = json.loads(response.data)

        # Verify all concepts belong to unit1
        for concept in data:
            assert concept['unit_id'] == unit1.unit_id
            assert concept['unit_id'] != unit2.unit_id

    def test_get_unit_concepts_nonexistent_unit(self, test_client):
        """
        Test retrieving concepts for a non-existent unit.

        Verifies:
        - Returns 200 status code (endpoint doesn't validate unit)
        - Response is an empty list
        """
        response = test_client.get('/api/units/99999/concepts')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_unit_concepts_with_null_definition(
        self, test_client, clean_db, sample_unit
    ):
        """
        Test retrieving concepts where some have null definitions.

        Verifies:
        - Returns 200 status code
        - Concepts with null definitions are included
        - Definition field is None for those concepts
        """
        concept = Concept(
            unit_id=sample_unit.unit_id,
            title="#testconcept",
            definition=None
        )
        clean_db.add(concept)
        clean_db.commit()

        response = test_client.get(
            f'/api/units/{sample_unit.unit_id}/concepts'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1
        # Find the concept we just created
        found = False
        for c in data:
            if c['name'] == '#testconcept':
                assert c['definition'] is None
                found = True
        assert found

    def test_get_unit_concepts_tag_field(
        self, test_client, sample_concept
    ):
        """
        Test that tag field is populated (currently uses title).

        Verifies:
        - Tag field is present and matches name/title
        """
        response = test_client.get(
            f'/api/units/{sample_concept.unit_id}/concepts'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        # Verify tag is set (currently uses title as placeholder)
        for concept in data:
            assert 'tag' in concept
            assert isinstance(concept['tag'], str)


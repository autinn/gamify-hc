"""
Tests for course routes.

This module contains comprehensive tests for the course-related endpoints:
- GET /api/courses: Retrieve all courses
- GET /api/courses/<course_id>: Retrieve a specific course by ID
- GET /api/courses/<course_id>/units: Retrieve all units for a course
"""

import json
import pytest
from backend.database.models import Course, Unit


class TestGetCourses:
    """Tests for get all courses endpoint."""

    def test_get_courses_empty(self, test_client):
        """
        Test retrieving all courses when database is empty.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        response = test_client.get('/api/courses')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_courses_success(self, test_client, populated_test_data):
        """
        Test successfully retrieving all courses.

        Verifies:
        - Returns 200 status code
        - Response contains list of courses
        - Each course has id, code, name, description fields
        """
        response = test_client.get('/api/courses')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 2

        # Verify structure of first course
        course = data[0]
        assert 'id' in course
        assert 'code' in course
        assert 'name' in course
        assert 'description' in course

    def test_get_courses_structure(self, test_client, sample_course):
        """
        Test that course structure matches expected format.

        Verifies:
        - All courses have consistent structure
        - Fields are properly serialized
        """
        response = test_client.get('/api/courses')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1

        for course in data:
            assert isinstance(course['id'], int)
            assert isinstance(course['code'], str)
            assert isinstance(course['name'], str)
            assert isinstance(course['description'], (str, type(None)))


class TestGetCourse:
    """Tests for get course by ID endpoint."""

    def test_get_course_success(self, test_client, sample_course):
        """
        Test successfully retrieving a course by ID.

        Verifies:
        - Returns 200 status code
        - Response contains id, code, name, description
        - All fields match the database record
        """
        response = test_client.get(f'/api/courses/{sample_course.course_id}')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == sample_course.course_id
        assert data['code'] == sample_course.title
        assert data['name'] == sample_course.title
        assert data['description'] == sample_course.description

    def test_get_course_not_found(self, test_client):
        """
        Test retrieving a non-existent course.

        Verifies:
        - Returns 404 Not Found status code
        - Error message indicates course not found
        """
        response = test_client.get('/api/courses/99999')

        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
        assert 'not found' in data['error'].lower()

    def test_get_course_invalid_id(self, test_client):
        """
        Test retrieving a course with invalid ID format.

        Verifies:
        - Returns 404 Not Found status code (Flask converts invalid int)
        """
        response = test_client.get('/api/courses/invalid')

        assert response.status_code == 404

    def test_get_course_with_null_description(
        self, test_client, clean_db
    ):
        """
        Test retrieving a course with null description.

        Verifies:
        - Returns 200 status code
        - Description field is None
        """
        course = Course(
            title="Test Course",
            description=None
        )
        clean_db.add(course)
        clean_db.commit()
        clean_db.refresh(course)

        response = test_client.get(f'/api/courses/{course.course_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['description'] is None


class TestGetCourseUnits:
    """Tests for get course units endpoint."""

    def test_get_course_units_empty(self, test_client, sample_course):
        """
        Test retrieving units for a course with no units.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        response = test_client.get(
            f'/api/courses/{sample_course.course_id}/units'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_course_units_success(
        self, test_client, populated_test_data
    ):
        """
        Test successfully retrieving units for a course.

        Verifies:
        - Returns 200 status code
        - Response contains list of units
        - Units are ordered by order_index
        - Each unit has id, course_id, name, description, order_index
        """
        course = populated_test_data['courses'][0]
        response = test_client.get(
            f'/api/courses/{course.course_id}/units'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) >= 2

        # Verify structure
        unit = data[0]
        assert 'id' in unit
        assert 'course_id' in unit
        assert 'name' in unit
        assert 'description' in unit
        assert 'order_index' in unit

        # Verify ordering
        order_indices = [u['order_index'] for u in data]
        assert order_indices == sorted(order_indices)

    def test_get_course_units_ordering(
        self, test_client, clean_db, sample_course
    ):
        """
        Test that units are returned in order_index order.

        Verifies:
        - Units are sorted by order_index ascending
        """
        # Create units with non-sequential order_index
        unit1 = Unit(
            course_id=sample_course.course_id,
            title="Unit 1",
            description="First unit",
            order_index=3
        )
        unit2 = Unit(
            course_id=sample_course.course_id,
            title="Unit 2",
            description="Second unit",
            order_index=1
        )
        unit3 = Unit(
            course_id=sample_course.course_id,
            title="Unit 3",
            description="Third unit",
            order_index=2
        )
        clean_db.add_all([unit1, unit2, unit3])
        clean_db.commit()

        response = test_client.get(
            f'/api/courses/{sample_course.course_id}/units'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 3
        # Verify order: 1, 2, 3
        assert data[0]['order_index'] == 1
        assert data[1]['order_index'] == 2
        assert data[2]['order_index'] == 3

    def test_get_course_units_only_returns_course_units(
        self, test_client, populated_test_data
    ):
        """
        Test that only units for the specified course are returned.

        Verifies:
        - Units from other courses are not included
        - All returned units have matching course_id
        """
        courses = populated_test_data['courses']
        course1 = courses[0]
        course2 = courses[1]

        response = test_client.get(
            f'/api/courses/{course1.course_id}/units'
        )

        assert response.status_code == 200
        data = json.loads(response.data)

        # Verify all units belong to course1
        for unit in data:
            assert unit['course_id'] == course1.course_id
            assert unit['course_id'] != course2.course_id

    def test_get_course_units_nonexistent_course(self, test_client):
        """
        Test retrieving units for a non-existent course.

        Verifies:
        - Returns 200 status code (endpoint doesn't validate course)
        - Response is an empty list
        """
        response = test_client.get('/api/courses/99999/units')

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_course_units_with_null_description(
        self, test_client, clean_db, sample_course
    ):
        """
        Test retrieving units where some have null descriptions.

        Verifies:
        - Returns 200 status code
        - Units with null descriptions are included
        - Description field is None for those units
        """
        unit = Unit(
            course_id=sample_course.course_id,
            title="Unit No Description",
            description=None,
            order_index=1
        )
        clean_db.add(unit)
        clean_db.commit()

        response = test_client.get(
            f'/api/courses/{sample_course.course_id}/units'
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]['description'] is None


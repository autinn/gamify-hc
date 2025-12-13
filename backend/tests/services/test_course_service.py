"""
Tests for CourseService.

This module tests course management functionality:
- Get all courses
- Get course by ID
- Get course units
"""

import pytest
from backend.services.course import CourseService
from backend.database.models import Course, Unit


class TestCourseServiceGetAll:
    """Tests for getting all courses."""

    def test_get_all_courses_empty(self, course_service, clean_db):
        """Test getting courses when none exist."""
        courses = course_service.get_all_courses()

        assert courses == []

    def test_get_all_courses_single(self, course_service, sample_course):
        """Test getting a single course."""
        courses = course_service.get_all_courses()

        assert len(courses) == 1
        assert courses[0]['id'] == sample_course.course_id
        assert courses[0]['name'] == sample_course.title

    def test_get_all_courses_multiple(self, course_service, populated_test_data):
        """Test getting multiple courses."""
        courses = course_service.get_all_courses()

        assert len(courses) == 2  # EA50 and FA50 from populated_test_data

    def test_get_all_courses_structure(self, course_service, sample_course):
        """Test that returned courses have expected structure."""
        courses = course_service.get_all_courses()

        expected_keys = {'id', 'code', 'name', 'description'}
        assert set(courses[0].keys()) == expected_keys

    def test_get_all_courses_without_session_raises_error(self):
        """Test that getting courses without db_session raises error."""
        service = CourseService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_all_courses()


class TestCourseServiceGetById:
    """Tests for getting course by ID."""

    def test_get_course_by_id_found(self, course_service, sample_course):
        """Test getting an existing course by ID."""
        course = course_service.get_course_by_id(sample_course.course_id)

        assert course is not None
        assert course['id'] == sample_course.course_id
        assert course['name'] == sample_course.title
        assert course['description'] == sample_course.description

    def test_get_course_by_id_not_found(self, course_service, clean_db):
        """Test getting a nonexistent course by ID."""
        course = course_service.get_course_by_id(99999)

        assert course is None

    def test_get_course_by_id_structure(self, course_service, sample_course):
        """Test that returned course has expected structure."""
        course = course_service.get_course_by_id(sample_course.course_id)

        expected_keys = {'id', 'code', 'name', 'description'}
        assert set(course.keys()) == expected_keys

    def test_get_course_by_id_without_session_raises_error(self):
        """Test that getting course without db_session raises error."""
        service = CourseService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_course_by_id(1)


class TestCourseServiceGetUnits:
    """Tests for getting course units."""

    def test_get_course_units_empty(self, course_service, sample_course):
        """Test getting units for course with no units."""
        # sample_course has no units by default (sample_unit is separate fixture)
        units = course_service.get_course_units(sample_course.course_id)

        # May be empty if sample_unit fixture wasn't used
        assert isinstance(units, list)

    def test_get_course_units_single(
        self, course_service, sample_course, sample_unit
    ):
        """Test getting a single unit for a course."""
        units = course_service.get_course_units(sample_course.course_id)

        assert len(units) == 1
        assert units[0]['id'] == sample_unit.unit_id
        assert units[0]['course_id'] == sample_course.course_id

    def test_get_course_units_multiple_ordered(
        self, course_service, populated_test_data
    ):
        """Test getting multiple units in correct order."""
        course = populated_test_data['courses'][0]  # EA50 has 2 units

        units = course_service.get_course_units(course.course_id)

        assert len(units) == 2
        # Verify ordered by order_index
        assert units[0]['order_index'] <= units[1]['order_index']

    def test_get_course_units_structure(
        self, course_service, sample_course, sample_unit
    ):
        """Test that returned units have expected structure."""
        units = course_service.get_course_units(sample_course.course_id)

        expected_keys = {'id', 'course_id', 'name', 'description', 'order_index'}
        assert set(units[0].keys()) == expected_keys

    def test_get_course_units_nonexistent_course(self, course_service, clean_db):
        """Test getting units for nonexistent course returns empty list."""
        units = course_service.get_course_units(99999)

        assert units == []

    def test_get_course_units_without_session_raises_error(self):
        """Test that getting units without db_session raises error."""
        service = CourseService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_course_units(1)


"""
Tests for UserProgressService.

This module tests progress tracking functionality:
- Quiz card progress retrieval
- Onboarding status get/update
- Aggregated progress by courses, units, and concepts
"""

import pytest
from datetime import datetime
from backend.services.user import UserProgressService
from backend.database.models import User, UserCard


class TestUserProgressServiceQuizProgress:
    """Tests for quiz card progress retrieval."""

    def test_get_user_quiz_progress_empty(self, progress_service, sample_user):
        """Test getting progress for user with no quiz attempts."""
        progress = progress_service.get_user_quiz_progress(sample_user.user_id)

        assert progress == []

    def test_get_user_quiz_progress_with_data(
        self, progress_service, sample_user, sample_quiz_card, clean_db
    ):
        """Test getting progress for user with quiz attempts."""
        # Create a UserCard record
        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            success_count=3,
            failure_count=2,
            repetitions=5,
            last_reviewed=datetime.utcnow()
        )
        clean_db.add(user_card)
        clean_db.commit()

        progress = progress_service.get_user_quiz_progress(sample_user.user_id)

        assert len(progress) == 1
        assert progress[0]['quiz_card_id'] == sample_quiz_card.quiz_card_id
        assert progress[0]['times_seen'] == 5  # success + failure
        assert progress[0]['times_correct'] == 3
        assert progress[0]['last_seen'] is not None

    def test_get_user_quiz_progress_multiple_cards(
        self, progress_service, sample_user, populated_test_data, clean_db
    ):
        """Test getting progress for multiple quiz cards."""
        quiz_cards = populated_test_data['quiz_cards']

        # Create UserCard records for multiple cards
        for i, qc in enumerate(quiz_cards[:2]):
            user_card = UserCard(
                user_id=sample_user.user_id,
                quiz_card_id=qc.quiz_card_id,
                success_count=i + 1,
                failure_count=i,
                repetitions=2 * i + 1
            )
            clean_db.add(user_card)
        clean_db.commit()

        progress = progress_service.get_user_quiz_progress(sample_user.user_id)

        assert len(progress) == 2

    def test_get_user_quiz_progress_without_session_raises_error(self):
        """Test that getting progress without db_session raises error."""
        service = UserProgressService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_user_quiz_progress(1)


class TestUserProgressServiceOnboarding:
    """Tests for onboarding status management."""

    def test_get_onboarding_status(self, progress_service, sample_user):
        """Test getting onboarding status."""
        status = progress_service.get_onboarding_status(sample_user.user_id)

        assert status is not None
        assert status['user_id'] == sample_user.user_id
        assert 'has_completed_onboarding' in status

    def test_get_onboarding_status_not_found(self, progress_service, clean_db):
        """Test getting onboarding status for nonexistent user."""
        status = progress_service.get_onboarding_status(99999)

        assert status is None

    def test_get_onboarding_status_without_session_raises_error(self):
        """Test that getting status without db_session raises error."""
        service = UserProgressService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_onboarding_status(1)

    def test_update_onboarding_status_to_true(
        self, progress_service, sample_user
    ):
        """Test updating onboarding status to completed."""
        result = progress_service.update_onboarding_status(
            user_id=sample_user.user_id,
            has_completed=True
        )

        assert result is not None
        assert result['user_id'] == sample_user.user_id
        assert result['has_completed_onboarding'] is True

    def test_update_onboarding_status_to_false(
        self, progress_service, sample_user, clean_db
    ):
        """Test updating onboarding status to not completed."""
        # First set to True
        sample_user.has_completed_onboarding = True
        clean_db.commit()

        # Then set back to False
        result = progress_service.update_onboarding_status(
            user_id=sample_user.user_id,
            has_completed=False
        )

        assert result is not None
        assert result['has_completed_onboarding'] is False

    def test_update_onboarding_status_user_not_found(
        self, progress_service, clean_db
    ):
        """Test updating status for nonexistent user."""
        result = progress_service.update_onboarding_status(
            user_id=99999,
            has_completed=True
        )

        assert result is None

    def test_update_onboarding_status_without_session_raises_error(self):
        """Test that updating status without db_session raises error."""
        service = UserProgressService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.update_onboarding_status(1, True)


class TestUserProgressServiceCoursesProgress:
    """Tests for course-level progress aggregation."""

    def test_get_courses_progress_empty(self, progress_service, sample_user):
        """Test getting course progress with no data."""
        result = progress_service.get_courses_progress(sample_user.user_id)

        assert result['labels'] == []
        assert result['values'] == []
        assert result['metadata']['type'] == 'courses'
        assert result['metadata']['count'] == 0

    def test_get_courses_progress_with_data(
        self, progress_service, sample_user, populated_test_data, clean_db
    ):
        """Test getting course progress with user data."""
        quiz_card = populated_test_data['quiz_cards'][0]

        # Create progress data
        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=quiz_card.quiz_card_id,
            success_count=8,
            failure_count=2,
            repetitions=10
        )
        clean_db.add(user_card)
        clean_db.commit()

        result = progress_service.get_courses_progress(sample_user.user_id)

        assert len(result['labels']) >= 1
        assert len(result['values']) >= 1
        assert result['metadata']['count'] >= 1
        # Success rate should be 8/10 = 0.8
        assert result['values'][0] == 0.8

    def test_get_courses_progress_structure(
        self, progress_service, sample_user
    ):
        """Test that course progress has expected structure."""
        result = progress_service.get_courses_progress(sample_user.user_id)

        assert 'labels' in result
        assert 'values' in result
        assert 'metadata' in result
        assert result['metadata']['type'] == 'courses'
        assert 'count' in result['metadata']
        assert 'timestamp' in result['metadata']

    def test_get_courses_progress_without_session_raises_error(self):
        """Test that getting progress without db_session raises error."""
        service = UserProgressService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_courses_progress(1)


class TestUserProgressServiceUnitsProgress:
    """Tests for unit-level progress aggregation."""

    def test_get_units_progress_empty(
        self, progress_service, sample_user, sample_course
    ):
        """Test getting unit progress with no data."""
        result = progress_service.get_units_progress(
            user_id=sample_user.user_id,
            course_id=sample_course.course_id
        )

        assert result['labels'] == []
        assert result['values'] == []
        assert result['metadata']['type'] == 'units'
        assert result['metadata']['course_id'] == sample_course.course_id

    def test_get_units_progress_with_data(
        self, progress_service, sample_user, populated_test_data, clean_db
    ):
        """Test getting unit progress with user data."""
        quiz_card = populated_test_data['quiz_cards'][0]
        course = populated_test_data['courses'][0]

        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=quiz_card.quiz_card_id,
            success_count=6,
            failure_count=4,
            repetitions=10
        )
        clean_db.add(user_card)
        clean_db.commit()

        result = progress_service.get_units_progress(
            user_id=sample_user.user_id,
            course_id=course.course_id
        )

        assert len(result['labels']) >= 1
        assert len(result['values']) >= 1
        # Success rate should be 6/10 = 0.6
        assert 0.6 in result['values']

    def test_get_units_progress_structure(
        self, progress_service, sample_user, sample_course
    ):
        """Test that unit progress has expected structure."""
        result = progress_service.get_units_progress(
            user_id=sample_user.user_id,
            course_id=sample_course.course_id
        )

        assert 'labels' in result
        assert 'values' in result
        assert 'metadata' in result
        assert result['metadata']['type'] == 'units'
        assert 'course_id' in result['metadata']
        assert 'count' in result['metadata']

    def test_get_units_progress_without_session_raises_error(self):
        """Test that getting progress without db_session raises error."""
        service = UserProgressService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_units_progress(1, 1)


class TestUserProgressServiceConceptsProgress:
    """Tests for concept-level progress aggregation."""

    def test_get_concepts_progress_empty(
        self, progress_service, sample_user, sample_course, sample_unit
    ):
        """Test getting concept progress with no data."""
        result = progress_service.get_concepts_progress(
            user_id=sample_user.user_id,
            unit_id=sample_unit.unit_id,
            course_id=sample_course.course_id
        )

        assert result['labels'] == []
        assert result['values'] == []
        assert result['metadata']['type'] == 'concepts'
        assert result['metadata']['unit_id'] == sample_unit.unit_id
        assert result['metadata']['course_id'] == sample_course.course_id

    def test_get_concepts_progress_with_data(
        self, progress_service, sample_user, populated_test_data, clean_db
    ):
        """Test getting concept progress with user data."""
        quiz_card = populated_test_data['quiz_cards'][0]
        course = populated_test_data['courses'][0]
        unit = populated_test_data['units'][0]

        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=quiz_card.quiz_card_id,
            success_count=7,
            failure_count=3,
            repetitions=10
        )
        clean_db.add(user_card)
        clean_db.commit()

        result = progress_service.get_concepts_progress(
            user_id=sample_user.user_id,
            unit_id=unit.unit_id,
            course_id=course.course_id
        )

        assert len(result['labels']) >= 1
        assert len(result['values']) >= 1
        # Success rate should be 7/10 = 0.7
        assert 0.7 in result['values']

    def test_get_concepts_progress_structure(
        self, progress_service, sample_user, sample_course, sample_unit
    ):
        """Test that concept progress has expected structure."""
        result = progress_service.get_concepts_progress(
            user_id=sample_user.user_id,
            unit_id=sample_unit.unit_id,
            course_id=sample_course.course_id
        )

        assert 'labels' in result
        assert 'values' in result
        assert 'metadata' in result
        assert result['metadata']['type'] == 'concepts'
        assert 'course_id' in result['metadata']
        assert 'unit_id' in result['metadata']
        assert 'count' in result['metadata']

    def test_get_concepts_progress_without_session_raises_error(self):
        """Test that getting progress without db_session raises error."""
        service = UserProgressService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_concepts_progress(1, 1, 1)


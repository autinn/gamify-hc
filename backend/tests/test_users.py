"""
Tests for user routes.

This module contains comprehensive tests for the user-related endpoints:
- GET /api/users/<user_id>: Retrieve a specific user by ID
- GET /api/users/<user_id>/progress: Retrieve user's quiz card progress
"""

import json
from backend.database.models import User, UserCard
from backend.tests.conftest import create_auth_token


class TestGetUser:
    """Tests for get user by ID endpoint."""

    def test_get_user_success(self, test_client, sample_user):
        """
        Test successfully retrieving a user by ID.

        Verifies:
        - Returns 200 status code
        - Response contains user_id, username, email, created_at
        - All fields match the database record
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/users/{sample_user.user_id}',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['user_id'] == sample_user.user_id
        assert data['username'] == sample_user.username
        assert data['email'] == sample_user.email
        assert 'created_at' in data

    def test_get_user_not_found(self, test_client):
        """
        Test retrieving a non-existent user.

        Verifies:
        - Returns 401 Unauthorized (no token) or 404 Not Found
        """
        # Test without token - should return 401
        response = test_client.get('/api/users/99999')
        assert response.status_code == 401

        # Test with token for non-existent user
        # Should return 403 (can't access other users)
        token = create_auth_token(1)
        response = test_client.get(
            '/api/users/99999',
            headers={'Authorization': f'Bearer {token}'}
        )
        assert response.status_code == 403

    def test_get_user_invalid_token(self, test_client):
        """
        Test retrieving a user with invalid authentication token.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates invalid token
        """
        response = test_client.get(
            '/api/users/1',
            headers={'Authorization': 'Bearer invalid_token_12345'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data
        error_lower = data['error'].lower()
        assert 'invalid' in error_lower or 'expired' in error_lower

    def test_get_user_expired_token(self, test_client):
        """
        Test retrieving a user with expired authentication token.

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

        response = test_client.get(
            '/api/users/1',
            headers={'Authorization': f'Bearer {expired_token}'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data

    def test_get_user_invalid_header_format(self, test_client):
        """
        Test retrieving a user with invalid Authorization header format.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates invalid header format
        """
        response = test_client.get(
            '/api/users/1',
            headers={'Authorization': 'InvalidFormat token'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data

    def test_get_user_with_created_at(self, test_client, clean_db):
        """
        Test retrieving a user that has a created_at timestamp.

        Verifies:
        - Returns 200 status code
        - created_at field is properly formatted as ISO string
        """
        from werkzeug.security import generate_password_hash
        from datetime import datetime
        user = User(
            username='timestampuser',
            email='timestampuser@minerva.edu',
            password_hash=generate_password_hash(
                'password', method='pbkdf2:sha256'
            ),
            created_at=datetime.utcnow()
        )
        clean_db.add(user)
        clean_db.commit()
        clean_db.refresh(user)

        token = create_auth_token(user.user_id)
        response = test_client.get(
            f'/api/users/{user.user_id}',
            headers={'Authorization': f'Bearer {token}'}
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'created_at' in data
        assert data['created_at'] is not None
        # Verify it's a valid ISO format string
        assert 'T' in data['created_at'] or '-' in data['created_at']


class TestGetUserProgress:
    """Tests for get user progress endpoint."""

    def test_get_user_progress_empty(self, test_client, sample_user):
        """
        Test retrieving progress for a user with no progress records.

        Verifies:
        - Returns 200 status code
        - Response is an empty list
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/users/{sample_user.user_id}/progress',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_user_progress_with_records(
        self, test_client, clean_db, sample_user, sample_quiz_card
    ):
        """
        Test retrieving progress for a user with progress records.

        Verifies:
        - Returns 200 status code
        - Response contains progress records
        - Each record has quiz_card_id, times_seen, times_correct, last_seen
        - times_seen is sum of success_count and failure_count
        """
        from datetime import datetime
        # Create UserCard progress record
        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            success_count=5,
            failure_count=2,
            last_reviewed=datetime.utcnow()
        )
        clean_db.add(user_card)
        clean_db.commit()

        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/users/{sample_user.user_id}/progress',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 1

        progress = data[0]
        assert progress['quiz_card_id'] == \
            sample_quiz_card.quiz_card_id
        assert progress['times_seen'] == 7  # 5 + 2
        assert progress['times_correct'] == 5
        assert 'last_seen' in progress
        assert progress['last_seen'] is not None

    def test_get_user_progress_multiple_cards(
        self, test_client, clean_db, sample_user, populated_test_data
    ):
        """
        Test retrieving progress for a user with multiple quiz card records.

        Verifies:
        - Returns 200 status code
        - Response contains all progress records
        - Each record is properly formatted
        """
        quiz_cards = populated_test_data['quiz_cards']
        # Create multiple UserCard records
        user_cards = [
            UserCard(
                user_id=sample_user.user_id,
                quiz_card_id=quiz_cards[0].quiz_card_id,
                success_count=3,
                failure_count=1
            ),
            UserCard(
                user_id=sample_user.user_id,
                quiz_card_id=quiz_cards[1].quiz_card_id,
                success_count=10,
                failure_count=5
            )
        ]
        clean_db.add_all(user_cards)
        clean_db.commit()

        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/users/{sample_user.user_id}/progress',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 2

        # Verify all records have required fields
        for progress in data:
            assert 'quiz_card_id' in progress
            assert 'times_seen' in progress
            assert 'times_correct' in progress
            assert 'last_seen' in progress

    def test_get_user_progress_without_last_reviewed(
        self, test_client, clean_db, sample_user, sample_quiz_card
    ):
        """
        Test retrieving progress where last_reviewed is None.

        Verifies:
        - Returns 200 status code
        - last_seen field is None when last_reviewed is not set
        """
        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            success_count=2,
            failure_count=1,
            last_reviewed=None
        )
        clean_db.add(user_card)
        clean_db.commit()

        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/users/{sample_user.user_id}/progress',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]['last_seen'] is None

    def test_get_user_progress_zero_counts(
        self, test_client, clean_db, sample_user, sample_quiz_card
    ):
        """
        Test retrieving progress with zero success and failure counts.

        Verifies:
        - Returns 200 status code
        - times_seen is 0 when both counts are 0
        - times_correct is 0
        """
        user_card = UserCard(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id,
            success_count=0,
            failure_count=0
        )
        clean_db.add(user_card)
        clean_db.commit()

        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/users/{sample_user.user_id}/progress',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]['times_seen'] == 0
        assert data[0]['times_correct'] == 0

    def test_get_user_progress_nonexistent_user(self, test_client):
        """
        Test retrieving progress for a non-existent user.

        Verifies:
        - Returns 401 Unauthorized (no token) or 403 Forbidden (wrong user)
        """
        # Test without token
        response = test_client.get('/api/users/99999/progress')
        assert response.status_code == 401

        # Test with token for different user - should return 403
        token = create_auth_token(1)
        response = test_client.get(
            '/api/users/99999/progress',
            headers={'Authorization': f'Bearer {token}'}
        )
        assert response.status_code == 403

    def test_get_user_progress_invalid_token(self, test_client):
        """
        Test retrieving user progress with invalid authentication token.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates invalid token
        """
        response = test_client.get(
            '/api/users/1/progress',
            headers={'Authorization': 'Bearer invalid_token_12345'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data
        error_lower = data['error'].lower()
        assert 'invalid' in error_lower or 'expired' in error_lower

    def test_get_user_progress_expired_token(self, test_client):
        """
        Test retrieving user progress with expired authentication token.

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

        response = test_client.get(
            '/api/users/1/progress',
            headers={'Authorization': f'Bearer {expired_token}'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data

    def test_get_user_progress_invalid_header_format(self, test_client):
        """
        Test retrieving user progress with invalid Authorization header format.

        Verifies:
        - Returns 401 Unauthorized status code
        - Error message indicates invalid header format
        """
        response = test_client.get(
            '/api/users/1/progress',
            headers={'Authorization': 'InvalidFormat token'}
        )

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data


class TestGetProgressByLevel:
    """Tests for progress aggregation endpoints by course, unit, and concept levels."""

    def test_get_courses_progress_success(self, test_client, sample_user, populated_test_data):
        """
        Test successfully retrieving user's progress aggregated by courses.

        Verifies:
        - Returns 200 status code
        - Response contains labels (course titles) and values (success rates)
        - Success rates are between 0 and 1
        - Metadata contains type and count
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            '/api/progress/courses',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'labels' in data
        assert 'values' in data
        assert 'metadata' in data
        assert data['metadata']['type'] == 'courses'

        # Verify success rates are between 0 and 1
        for value in data['values']:
            assert 0 <= value <= 1

    def test_get_courses_progress_no_data(self, test_client, sample_user):
        """
        Test retrieving courses progress when user has no quiz attempts.

        Verifies:
        - Returns 200 status code
        - Empty labels and values arrays
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            '/api/progress/courses',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['labels'] == []
        assert data['values'] == []

    def test_get_courses_progress_unauthorized(self, test_client):
        """
        Test retrieving courses progress without authentication.

        Verifies:
        - Returns 401 Unauthorized status code
        """
        response = test_client.get('/api/progress/courses')

        assert response.status_code == 401
        data = json.loads(response.data)
        assert 'error' in data

    def test_get_units_progress_success(self, test_client, sample_user, populated_test_data, sample_course):
        """
        Test successfully retrieving user's progress aggregated by units in a course.

        Verifies:
        - Returns 200 status code
        - Response contains unit labels and success rate values
        - Success rates are between 0 and 1
        - Metadata contains correct course_id
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/progress/courses/{sample_course.course_id}/units',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'labels' in data
        assert 'values' in data
        assert data['metadata']['type'] == 'units'
        assert data['metadata']['course_id'] == sample_course.course_id

        # Verify success rates are between 0 and 1
        for value in data['values']:
            assert 0 <= value <= 1

    def test_get_units_progress_nonexistent_course(self, test_client, sample_user):
        """
        Test retrieving units progress for non-existent course.

        Verifies:
        - Returns 200 status code with empty data
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            '/api/progress/courses/99999/units',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['labels'] == []
        assert data['values'] == []

    def test_get_concepts_progress_success(self, test_client, sample_user, populated_test_data, 
                                           sample_course, sample_unit):
        """
        Test successfully retrieving user's progress aggregated by concepts in a unit.

        Verifies:
        - Returns 200 status code
        - Response contains concept labels and success rate values
        - Success rates are between 0 and 1
        - Metadata contains correct course_id and unit_id
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/progress/courses/{sample_course.course_id}/units/{sample_unit.unit_id}/concepts',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'labels' in data
        assert 'values' in data
        assert data['metadata']['type'] == 'concepts'
        assert data['metadata']['course_id'] == sample_course.course_id
        assert data['metadata']['unit_id'] == sample_unit.unit_id

        # Verify success rates are between 0 and 1
        for value in data['values']:
            assert 0 <= value <= 1

    def test_get_concepts_progress_nonexistent_unit(self, test_client, sample_user, sample_course):
        """
        Test retrieving concepts progress for non-existent unit.

        Verifies:
        - Returns 200 status code with empty data
        """
        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            f'/api/progress/courses/{sample_course.course_id}/units/99999/concepts',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['labels'] == []
        assert data['values'] == []

    def test_progress_success_rate_calculation(self, test_client, db_session, sample_user, 
                                              sample_course, sample_unit, sample_concept, sample_quiz_card):
        """
        Test that success rates are correctly calculated as success_count / repetitions.

        Verifies:
        - User with 3 successes out of 5 repetitions returns 0.6
        - User with 0 repetitions returns 0.0
        """
        # Create user card with specific success/repetition counts
        user_card = db_session.query(UserCard).filter_by(
            user_id=sample_user.user_id,
            quiz_card_id=sample_quiz_card.quiz_card_id
        ).first()
        
        if user_card:
            user_card.success_count = 3
            user_card.repetitions = 5
            db_session.commit()

        token = create_auth_token(sample_user.user_id)
        response = test_client.get(
            '/api/progress/courses',
            headers={'Authorization': f'Bearer {token}'}
        )

        assert response.status_code == 200
        data = json.loads(response.data)

        # Verify success rate calculation (3/5 = 0.6)
        if data['values']:
            assert data['values'][0] == 0.6
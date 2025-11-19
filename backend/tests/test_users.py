"""
Tests for user routes.

This module contains comprehensive tests for the user-related endpoints:
- GET /api/users/<user_id>: Retrieve a specific user by ID
- GET /api/users/<user_id>/progress: Retrieve user's quiz card progress
"""

import json
import pytest
from backend.database.models import User, UserCard, QuizCard
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

        # Test with token for non-existent user - should return 403 (can't access other users)
        token = create_auth_token(1)
        response = test_client.get(
            '/api/users/99999',
            headers={'Authorization': f'Bearer {token}'}
        )
        assert response.status_code == 403

    def test_get_user_invalid_id(self, test_client):
        """
        Test retrieving a user with invalid ID format.

        Verifies:
        - Returns 401 Unauthorized (no token)
        """
        response = test_client.get('/api/users/invalid')
        assert response.status_code == 401

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
            password_hash=generate_password_hash('password'),
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

    def test_get_user_without_created_at(self, test_client, clean_db):
        """
        Test retrieving a user without created_at timestamp.

        Verifies:
        - Returns 200 status code
        - created_at field is None
        """
        from werkzeug.security import generate_password_hash
        user = User(
            username='notimestamp',
            email='notimestamp@minerva.edu',
            password_hash=generate_password_hash('password'),
            created_at=None
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
        assert data['created_at'] is None


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


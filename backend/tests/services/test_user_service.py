"""
Tests for UserService.

This module tests user management functionality:
- User creation (with plain password and hashed password)
- User retrieval by ID, username, and email
- User existence checks
"""

import pytest
from werkzeug.security import check_password_hash
from backend.services.user import UserService
from backend.database.models import User


class TestUserServiceCreate:
    """Tests for user creation."""

    def test_create_user_with_plain_password(self, user_service):
        """Test creating a user with plain password (auto-hashed)."""
        user = user_service.create_user(
            username="newuser",
            email="newuser@minerva.edu",
            password="plainPassword123"
        )

        assert user is not None
        assert user.user_id is not None
        assert user.username == "newuser"
        assert user.email == "newuser@minerva.edu"
        # Password should be hashed
        assert user.password_hash != "plainPassword123"
        assert check_password_hash(user.password_hash, "plainPassword123")

    def test_create_user_with_hashed_password(self, user_service):
        """Test creating a user with pre-hashed password."""
        from werkzeug.security import generate_password_hash
        hashed = generate_password_hash("hashedPassword123")

        user = user_service.create_user(
            username="hasheduser",
            email="hashed@minerva.edu",
            hashed_password=hashed
        )

        assert user is not None
        assert user.password_hash == hashed

    def test_create_user_without_password_raises_error(self, user_service):
        """Test that creating user without any password raises error."""
        with pytest.raises(ValueError, match="password"):
            user_service.create_user(
                username="nopassword",
                email="nopass@minerva.edu"
            )

    def test_create_user_with_both_passwords_raises_error(self, user_service):
        """Test that providing both password types raises error."""
        from werkzeug.security import generate_password_hash
        hashed = generate_password_hash("password")

        with pytest.raises(ValueError, match="password"):
            user_service.create_user(
                username="bothpass",
                email="both@minerva.edu",
                password="plainPassword",
                hashed_password=hashed
            )

    def test_create_user_without_session_raises_error(self):
        """Test that creating user without db_session raises error."""
        service = UserService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.create_user(
                username="test",
                email="test@minerva.edu",
                password="password123"
            )


class TestUserServiceGetById:
    """Tests for getting user by ID."""

    def test_get_user_by_id_found(self, user_service, sample_user):
        """Test retrieving an existing user by ID."""
        user = user_service.get_user_by_id(sample_user.user_id)

        assert user is not None
        assert user.user_id == sample_user.user_id
        assert user.username == sample_user.username

    def test_get_user_by_id_not_found(self, user_service, clean_db):
        """Test retrieving a non-existent user by ID."""
        user = user_service.get_user_by_id(99999)

        assert user is None

    def test_get_user_by_id_without_session_raises_error(self):
        """Test that getting user without db_session raises error."""
        service = UserService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_user_by_id(1)


class TestUserServiceGetByUsername:
    """Tests for getting user by username."""

    def test_get_user_by_username_found(self, user_service, sample_user):
        """Test retrieving an existing user by username."""
        user = user_service.get_user_by_username(sample_user.username)

        assert user is not None
        assert user.user_id == sample_user.user_id
        assert user.username == sample_user.username

    def test_get_user_by_username_not_found(self, user_service, clean_db):
        """Test retrieving a non-existent user by username."""
        user = user_service.get_user_by_username("nonexistent_user")

        assert user is None

    def test_get_user_by_username_case_sensitive(self, user_service, sample_user):
        """Test that username lookup is case sensitive."""
        # sample_user.username is "test_user"
        user = user_service.get_user_by_username("TEST_USER")

        # Should not find because case doesn't match
        assert user is None

    def test_get_user_by_username_without_session_raises_error(self):
        """Test that getting user without db_session raises error."""
        service = UserService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_user_by_username("test")


class TestUserServiceGetByEmail:
    """Tests for getting user by email."""

    def test_get_user_by_email_found(self, user_service, sample_user):
        """Test retrieving an existing user by email."""
        user = user_service.get_user_by_email(sample_user.email)

        assert user is not None
        assert user.user_id == sample_user.user_id
        assert user.email == sample_user.email

    def test_get_user_by_email_not_found(self, user_service, clean_db):
        """Test retrieving a non-existent user by email."""
        user = user_service.get_user_by_email("nonexistent@minerva.edu")

        assert user is None

    def test_get_user_by_email_without_session_raises_error(self):
        """Test that getting user without db_session raises error."""
        service = UserService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.get_user_by_email("test@minerva.edu")


class TestUserServiceExistsByUsername:
    """Tests for checking username existence."""

    def test_user_exists_by_username_true(self, user_service, sample_user):
        """Test checking existence of existing username."""
        exists = user_service.user_exists_by_username(sample_user.username)

        assert exists is True

    def test_user_exists_by_username_false(self, user_service, clean_db):
        """Test checking existence of non-existent username."""
        exists = user_service.user_exists_by_username("nonexistent_user")

        assert exists is False

    def test_user_exists_by_username_without_session_raises_error(self):
        """Test that checking existence without db_session raises error."""
        service = UserService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.user_exists_by_username("test")


class TestUserServiceExistsByEmail:
    """Tests for checking email existence."""

    def test_user_exists_by_email_true(self, user_service, sample_user):
        """Test checking existence of existing email."""
        exists = user_service.user_exists_by_email(sample_user.email)

        assert exists is True

    def test_user_exists_by_email_false(self, user_service, clean_db):
        """Test checking existence of non-existent email."""
        exists = user_service.user_exists_by_email("nonexistent@minerva.edu")

        assert exists is False

    def test_user_exists_by_email_without_session_raises_error(self):
        """Test that checking existence without db_session raises error."""
        service = UserService(db_session=None)

        with pytest.raises(ValueError, match="session"):
            service.user_exists_by_email("test@minerva.edu")


class TestUserServiceMultipleUsers:
    """Tests involving multiple users."""

    def test_create_multiple_users(self, user_service):
        """Test creating multiple distinct users."""
        user1 = user_service.create_user(
            username="user1",
            email="user1@minerva.edu",
            password="password1"
        )
        user2 = user_service.create_user(
            username="user2",
            email="user2@minerva.edu",
            password="password2"
        )

        assert user1.user_id != user2.user_id
        assert user1.username != user2.username

    def test_get_correct_user_among_multiple(self, user_service):
        """Test getting the correct user when multiple exist."""
        user1 = user_service.create_user(
            username="findme",
            email="findme@minerva.edu",
            password="password"
        )
        user_service.create_user(
            username="notme",
            email="notme@minerva.edu",
            password="password"
        )

        found = user_service.get_user_by_username("findme")

        assert found.user_id == user1.user_id


"""
Tests for AuthService.

This module tests authentication and authorization functionality:
- JWT token creation and verification
- Password hashing and verification
- Email, username, and password validation
- User authentication
"""

import pytest
import jwt
import time
from datetime import datetime, timedelta
from backend.services.auth import AuthService


class TestAuthServiceTokens:
    """Tests for JWT token operations."""

    def test_create_token(self, auth_service):
        """Test creating a JWT token."""
        token = auth_service.create_token(user_id=123)

        assert token is not None
        assert isinstance(token, str)
        # Verify token structure (three parts separated by dots)
        assert len(token.split('.')) == 3

    def test_create_token_contains_user_id(self, auth_service):
        """Test that created token contains the user_id."""
        user_id = 42
        token = auth_service.create_token(user_id=user_id)

        # Decode to verify content
        payload = jwt.decode(
            token,
            'test-secret-key',
            algorithms=['HS256']
        )
        assert payload['user_id'] == user_id

    def test_create_token_contains_expiration(self, auth_service):
        """Test that created token has expiration claim."""
        token = auth_service.create_token(user_id=1)

        payload = jwt.decode(
            token,
            'test-secret-key',
            algorithms=['HS256']
        )
        assert 'exp' in payload
        assert 'iat' in payload

    def test_verify_token_valid(self, auth_service):
        """Test verifying a valid token."""
        token = auth_service.create_token(user_id=123)

        payload = auth_service.verify_token(token)

        assert payload is not None
        assert payload['user_id'] == 123

    def test_verify_token_invalid(self, auth_service):
        """Test verifying an invalid token returns None."""
        invalid_token = "invalid.token.here"

        payload = auth_service.verify_token(invalid_token)

        assert payload is None

    def test_verify_token_wrong_secret(self, auth_service):
        """Test verifying a token with wrong secret returns None."""
        # Create token with different secret
        other_service = AuthService(
            secret_key='different-secret',
            algorithm='HS256',
            expiration_hours=24
        )
        token = other_service.create_token(user_id=123)

        payload = auth_service.verify_token(token)

        assert payload is None

    def test_verify_token_expired(self):
        """Test verifying an expired token returns None."""
        # Create service with very short expiration
        service = AuthService(
            secret_key='test-secret',
            algorithm='HS256',
            expiration_hours=0  # Immediate expiration
        )

        # Create token that's already expired
        payload = {
            'user_id': 123,
            'exp': datetime.utcnow() - timedelta(hours=1),
            'iat': datetime.utcnow() - timedelta(hours=2)
        }
        expired_token = jwt.encode(payload, 'test-secret', algorithm='HS256')

        result = service.verify_token(expired_token)

        assert result is None


class TestAuthServicePasswords:
    """Tests for password hashing and verification."""

    def test_hash_password(self, auth_service):
        """Test password hashing."""
        password = "mySecurePassword123"

        hashed = auth_service.hash_password(password)

        assert hashed is not None
        assert hashed != password
        assert len(hashed) > len(password)

    def test_hash_password_different_each_time(self, auth_service):
        """Test that same password produces different hashes (salted)."""
        password = "samePassword"

        hash1 = auth_service.hash_password(password)
        hash2 = auth_service.hash_password(password)

        assert hash1 != hash2

    def test_verify_password_correct(self, auth_service):
        """Test verifying correct password."""
        password = "correctPassword"
        hashed = auth_service.hash_password(password)

        result = auth_service.verify_password(hashed, password)

        assert result is True

    def test_verify_password_incorrect(self, auth_service):
        """Test verifying incorrect password."""
        password = "correctPassword"
        wrong_password = "wrongPassword"
        hashed = auth_service.hash_password(password)

        result = auth_service.verify_password(hashed, wrong_password)

        assert result is False


class TestAuthServiceEmailValidation:
    """Tests for email validation."""

    def test_validate_email_valid_minerva(self, auth_service):
        """Test validating a valid minerva.edu email."""
        valid, error = auth_service.validate_email("user@minerva.edu")

        assert valid is True
        assert error is None

    def test_validate_email_valid_subdomain(self, auth_service):
        """Test validating email with subdomain."""
        valid, error = auth_service.validate_email("user@uni.minerva.edu")

        assert valid is True
        assert error is None

    def test_validate_email_empty(self, auth_service):
        """Test validating empty email."""
        valid, error = auth_service.validate_email("")

        assert valid is False
        assert "required" in error.lower()

    def test_validate_email_none(self, auth_service):
        """Test validating None email."""
        valid, error = auth_service.validate_email(None)

        assert valid is False
        assert "required" in error.lower()

    def test_validate_email_invalid_format(self, auth_service):
        """Test validating email with invalid format."""
        valid, error = auth_service.validate_email("notanemail")

        assert valid is False
        assert "format" in error.lower()

    def test_validate_email_wrong_domain(self, auth_service):
        """Test validating email with non-minerva domain."""
        valid, error = auth_service.validate_email("user@gmail.com")

        assert valid is False
        assert "minerva.edu" in error.lower()

    def test_validate_email_missing_at(self, auth_service):
        """Test validating email missing @ symbol."""
        valid, error = auth_service.validate_email("userminerva.edu")

        assert valid is False


class TestAuthServiceUsernameValidation:
    """Tests for username validation."""

    def test_validate_username_valid(self, auth_service):
        """Test validating a valid username."""
        valid, error = auth_service.validate_username("validuser")

        assert valid is True
        assert error is None

    def test_validate_username_minimum_length(self, auth_service):
        """Test validating username at minimum length (3)."""
        valid, error = auth_service.validate_username("abc")

        assert valid is True
        assert error is None

    def test_validate_username_too_short(self, auth_service):
        """Test validating username that's too short."""
        valid, error = auth_service.validate_username("ab")

        assert valid is False
        assert "3" in error or "character" in error.lower()

    def test_validate_username_too_long(self, auth_service):
        """Test validating username that's too long (>50)."""
        long_username = "a" * 51
        valid, error = auth_service.validate_username(long_username)

        assert valid is False
        assert "50" in error or "character" in error.lower()

    def test_validate_username_empty(self, auth_service):
        """Test validating empty username."""
        valid, error = auth_service.validate_username("")

        assert valid is False
        assert "required" in error.lower()

    def test_validate_username_none(self, auth_service):
        """Test validating None username."""
        valid, error = auth_service.validate_username(None)

        assert valid is False
        assert "required" in error.lower()


class TestAuthServicePasswordValidation:
    """Tests for password validation."""

    def test_validate_password_valid(self, auth_service):
        """Test validating a valid password."""
        valid, error = auth_service.validate_password("securePassword123")

        assert valid is True
        assert error is None

    def test_validate_password_minimum_length(self, auth_service):
        """Test validating password at minimum length (8)."""
        valid, error = auth_service.validate_password("12345678")

        assert valid is True
        assert error is None

    def test_validate_password_too_short(self, auth_service):
        """Test validating password that's too short."""
        valid, error = auth_service.validate_password("1234567")

        assert valid is False
        assert "8" in error or "character" in error.lower()

    def test_validate_password_empty(self, auth_service):
        """Test validating empty password."""
        valid, error = auth_service.validate_password("")

        assert valid is False
        assert "required" in error.lower()

    def test_validate_password_none(self, auth_service):
        """Test validating None password."""
        valid, error = auth_service.validate_password(None)

        assert valid is False
        assert "required" in error.lower()


class TestAuthServiceRegistrationValidation:
    """Tests for combined registration data validation."""

    def test_validate_registration_all_valid(self, auth_service):
        """Test validating all valid registration data."""
        valid, error = auth_service.validate_registration_data(
            username="validuser",
            email="valid@minerva.edu",
            password="validPassword123"
        )

        assert valid is True
        assert error is None

    def test_validate_registration_invalid_username(self, auth_service):
        """Test that invalid username fails validation."""
        valid, error = auth_service.validate_registration_data(
            username="ab",  # Too short
            email="valid@minerva.edu",
            password="validPassword123"
        )

        assert valid is False
        assert error is not None

    def test_validate_registration_invalid_email(self, auth_service):
        """Test that invalid email fails validation."""
        valid, error = auth_service.validate_registration_data(
            username="validuser",
            email="invalid@gmail.com",  # Wrong domain
            password="validPassword123"
        )

        assert valid is False
        assert "minerva" in error.lower()

    def test_validate_registration_invalid_password(self, auth_service):
        """Test that invalid password fails validation."""
        valid, error = auth_service.validate_registration_data(
            username="validuser",
            email="valid@minerva.edu",
            password="short"  # Too short
        )

        assert valid is False
        assert error is not None


class TestAuthServiceAuthentication:
    """Tests for user authentication."""

    def test_authenticate_user_by_username(
        self, auth_service_with_db, sample_user
    ):
        """Test authenticating user by username."""
        user = auth_service_with_db.authenticate_user(
            username_or_email=sample_user.username,
            password="test_password",
            db_session=auth_service_with_db.db_session
        )

        assert user is not None
        assert user.user_id == sample_user.user_id

    def test_authenticate_user_by_email(
        self, auth_service_with_db, sample_user
    ):
        """Test authenticating user by email."""
        user = auth_service_with_db.authenticate_user(
            username_or_email=sample_user.email,
            password="test_password",
            db_session=auth_service_with_db.db_session
        )

        assert user is not None
        assert user.user_id == sample_user.user_id

    def test_authenticate_user_wrong_password(
        self, auth_service_with_db, sample_user
    ):
        """Test authentication with wrong password."""
        user = auth_service_with_db.authenticate_user(
            username_or_email=sample_user.username,
            password="wrong_password",
            db_session=auth_service_with_db.db_session
        )

        assert user is None

    def test_authenticate_user_nonexistent(self, auth_service_with_db, clean_db):
        """Test authentication with nonexistent user."""
        user = auth_service_with_db.authenticate_user(
            username_or_email="nonexistent_user",
            password="any_password",
            db_session=clean_db
        )

        assert user is None

    def test_authenticate_user_case_insensitive_email(
        self, auth_service_with_db, sample_user
    ):
        """Test that email authentication is case insensitive."""
        user = auth_service_with_db.authenticate_user(
            username_or_email=sample_user.email.upper(),
            password="test_password",
            db_session=auth_service_with_db.db_session
        )

        assert user is not None
        assert user.user_id == sample_user.user_id


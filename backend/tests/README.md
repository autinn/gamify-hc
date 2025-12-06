# Backend Tests

This directory contains pytest tests for the backend API.

## Prerequisites

- Docker must be installed and running (testcontainers uses Docker)
- Python dependencies installed: `pip install -r requirements.txt`

No manual database setup required - tests automatically spin up a PostgreSQL container using testcontainers.

## Running Tests

Run all tests:
```bash
pytest backend/tests/
```

Run with verbose output:
```bash
pytest backend/tests/ -v
```

Run a specific test file:
```bash
pytest backend/tests/test_health.py
pytest backend/tests/test_auth.py
pytest backend/tests/test_courses.py
```

Run a specific test:
```bash
pytest backend/tests/test_health.py::TestHealthEndpoint::test_health_check
```

## Test Structure

- `conftest.py` - Pytest configuration and fixtures
- `test_health.py` - Health check endpoint tests
- `test_auth.py` - Authentication endpoint tests
- `test_users.py` - User endpoint tests
- `test_courses.py` - Course endpoint tests
- `test_units.py` - Unit endpoint tests
- `test_concepts.py` - Concept endpoint tests
- `test_quiz.py` - Quiz endpoint tests
- `test_index_usage.py` - Database index existence and usage tests

## Test Fixtures

The test suite uses pytest fixtures defined in `conftest.py`:

- `postgres_container` - Testcontainers PostgreSQL container (session-scoped)
- `test_database_url` - Connection URL from the container
- `test_engine` - Shared test database engine
- `test_session_factory` - Session factory for creating test sessions
- `db_session` - Database session for tests
- `clean_db` - Cleaned database before each test
- `test_client` - Flask test client with test database
- `populated_test_data` - Database populated with comprehensive test data
- `auth_token` - JWT authentication token for testing protected endpoints
- Individual fixtures for sample data:
  - `sample_course` - Single course
  - `sample_unit` - Single unit
  - `sample_concept` - Single concept
  - `sample_quiz_card` - Single quiz card
  - `sample_quiz_answers` - Quiz answers for a card
  - `sample_user` - Single user

## Test Data

Test data is populated using the `populated_test_data` fixture in `conftest.py`. This fixture creates:
- 2 courses (EA50, FA50)
- 3 units
- 4 concepts
- 3 quiz cards
- 4 quiz answers
- 1 test user

## How Testcontainers Works

When you run `pytest`:
1. Testcontainers starts a fresh PostgreSQL 16 container
2. Tests run against this isolated database
3. Container is automatically destroyed after tests complete

This ensures:
- Tests are isolated from development data
- Same PostgreSQL version as production
- No manual setup required

## Dependencies

Tests require:
- pytest
- pytest-flask
- requests
- psycopg2-binary
- testcontainers[postgresql]
- Docker (running)

Install Python dependencies:
```bash
pip install -r requirements.txt
```

# Backend Tests

This directory contains pytest tests for the backend API.

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
pytest backend/tests/test_api.py
```

Run a specific test:
```bash
pytest backend/tests/test_api.py::TestHealthEndpoint::test_health_check
```

## Test Structure

- `conftest.py` - Pytest configuration and fixtures
- `test_api.py` - API endpoint tests
- `fixtures.py` - Test data population functions

## Test Fixtures

The test suite uses pytest fixtures defined in `conftest.py`:

- `test_database_url` - In-memory SQLite database URL
- `db_session` - Database session for tests
- `clean_db` - Cleaned database before each test
- `test_client` - Flask test client
- `populated_test_data` - Database populated with test data
- Individual fixtures for sample data (course, unit, concept, etc.)

## Test Data

Test data is populated using functions from `fixtures.py`. The `populate_test_data()` function creates:
- 2 courses (EA50, FA50)
- 3 units
- 4 concepts
- 3 quiz cards
- 7 quiz answers
- 1 test user

## Dependencies

Tests require:
- pytest
- pytest-flask
- requests

Install with:
```bash
pip install -r requirements.txt
```


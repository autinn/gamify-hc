# Backend Tests

This directory contains pytest tests for the backend API, organized into two categories:
- **Route Tests** (`routes/`): Integration tests for API endpoints
- **Service Tests** (`services/`): Unit tests for business logic services

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

Run only route tests:
```bash
pytest backend/tests/routes/
```

Run only service tests:
```bash
pytest backend/tests/services/
```

Run a specific test file:
```bash
pytest backend/tests/routes/test_auth.py
pytest backend/tests/services/test_auth_service.py
```

Run a specific test:
```bash
pytest backend/tests/routes/test_health.py::TestHealthEndpoint::test_health_check
pytest backend/tests/services/test_base_service.py::TestBaseServiceSave::test_save_entity_with_commit
```

## Test Structure

```
backend/tests/
├── __init__.py
├── conftest.py              # Shared fixtures for all tests
├── README.md
├── test_index_usage.py      # Database index tests
├── routes/                  # API endpoint integration tests
│   ├── __init__.py
│   ├── test_auth.py         # Authentication endpoints
│   ├── test_users.py        # User endpoints
│   ├── test_courses.py      # Course endpoints
│   ├── test_units.py        # Unit endpoints
│   ├── test_concepts.py     # Concept endpoints
│   ├── test_quiz.py         # Quiz endpoints
│   └── test_health.py       # Health check endpoint
└── services/                # Service unit tests
    ├── __init__.py
    ├── test_base_service.py      # BaseService transaction methods
    ├── test_serializers.py       # Serialization functions
    ├── test_auth_service.py      # JWT, password hashing, validation
    ├── test_user_service.py      # User CRUD operations
    ├── test_progress_service.py  # Progress tracking
    ├── test_course_service.py    # Course retrieval
    ├── test_unit_service.py      # Unit retrieval
    ├── test_concept_service.py   # Concept retrieval
    └── test_quiz_service.py      # Quiz cards, answer submission
```

## Test Fixtures

The test suite uses pytest fixtures defined in `conftest.py`:

### Database Fixtures
- `postgres_container` - Testcontainers PostgreSQL container (session-scoped)
- `test_database_url` - Connection URL from the container
- `test_engine` - Shared test database engine
- `test_session_factory` - Session factory for creating test sessions
- `db_session` - Database session for tests
- `clean_db` - Cleaned database before each test
- `test_client` - Flask test client with test database

### Sample Data Fixtures
- `sample_course` - Single course
- `sample_unit` - Single unit
- `sample_concept` - Single concept
- `sample_quiz_card` - Single quiz card
- `sample_quiz_answers` - Quiz answers for a card
- `sample_user` - Single user
- `populated_test_data` - Comprehensive test data (2 courses, 3 units, etc.)
- `auth_token` - JWT authentication token for protected endpoints

### Service Fixtures (for unit testing services)
- `auth_service` - AuthService instance (no DB session)
- `auth_service_with_db` - AuthService instance with DB session
- `user_service` - UserService instance
- `progress_service` - UserProgressService instance
- `course_service` - CourseService instance
- `unit_service` - UnitService instance
- `concept_service` - ConceptService instance
- `quiz_service` - QuizService instance

## Test Categories

### Route Tests (Integration)
Test the API endpoints end-to-end through the Flask test client:
- HTTP request/response handling
- Status codes
- JSON payloads
- Authentication/authorization
- Error responses

### Service Tests (Unit)
Test the business logic layer in isolation:
- Individual method behavior
- Database operations
- Validation logic
- Error handling
- Edge cases

## Test Data

Test data is populated using the `populated_test_data` fixture:
- 2 courses (EA50, FA50)
- 3 units (2 for EA50, 1 for FA50)
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

## Writing New Tests

### Adding Route Tests
1. Create file in `routes/` directory: `test_<feature>.py`
2. Use `test_client` fixture for HTTP requests
3. Use `clean_db` or `populated_test_data` for database state
4. Use `auth_token` for authenticated endpoints

### Adding Service Tests
1. Create file in `services/` directory: `test_<service>_service.py`
2. Use appropriate service fixture (e.g., `user_service`)
3. Test each method's success and error cases
4. Test with `db_session=None` for error handling

Example service test:
```python
class TestMyServiceMethod:
    def test_method_success(self, my_service, sample_data):
        result = my_service.my_method(sample_data.id)
        assert result is not None
        assert result['field'] == expected_value

    def test_method_not_found(self, my_service, clean_db):
        result = my_service.my_method(99999)
        assert result is None

    def test_method_without_session_raises_error(self):
        service = MyService(db_session=None)
        with pytest.raises(ValueError, match="session"):
            service.my_method(1)
```

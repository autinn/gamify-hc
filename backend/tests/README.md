# Testing Guide for Gamify-HC Backend

This document describes the testing strategy for the refactored clean architecture.

## Testing Philosophy

We follow a **layered testing approach** that matches our architecture:

```
Unit Tests        → Services (business logic with mocked repositories)
                  → Validators (input validation)

Integration Tests → Repositories (data access with test database)

E2E Tests         → Full stack (routes → services → repositories → database)
```

## Quick Start

### Run All Tests
```bash
pytest
```

### Run Specific Layer
```bash
pytest backend/tests/unit/         # Fast unit tests
pytest backend/tests/integration/  # Integration tests
pytest backend/tests/e2e/          # End-to-end tests (current location)
```

### Run with Coverage
```bash
pytest --cov=backend --cov-report=html
open htmlcov/index.html
```

## Prerequisites

- Docker must be installed and running (testcontainers uses Docker)
- Python dependencies installed: `pip install -r requirements.txt`

No manual database setup required - tests automatically spin up a PostgreSQL container.

## Current Test Structure

```
backend/tests/
├── conftest.py                # Pytest fixtures (database, client, etc.)
├── README.md                  # This file
│
# Current E2E tests (refactoring in progress)
├── test_auth.py              # Authentication endpoints
├── test_concepts.py          # Concept endpoints
├── test_courses.py           # Course endpoints
├── test_health.py            # Health check endpoints
├── test_quiz.py              # Quiz endpoints
├── test_units.py             # Unit endpoints
├── test_users.py             # User endpoints
└── test_index_usage.py       # Database indexes
│
# Future structure (to be added)
├── unit/                      # Unit tests (fast, mocked)
│   ├── test_auth_service.py
│   ├── test_quiz_service.py
│   ├── test_course_service.py
│   └── test_validators.py
│
└── integration/               # Integration tests (database)
    └── test_repositories.py
```

## Test Layers

### Unit Tests (Services & Validators)

**Goal**: Test business logic in isolation with mocked dependencies

**Example**:
```python
from unittest.mock import Mock
from backend.services.quiz_service import QuizService

def test_calculate_sm2():
    mock_quiz_repo = Mock()
    service = QuizService(quiz_repo=mock_quiz_repo)
    
    ef, interval = service._calculate_sm2(
        correctness=5,
        easiness_factor=2.5,
        interval=1
    )
    
    assert ef == 2.6
    assert interval == 6
```

### Integration Tests (Repositories)

**Goal**: Test data access with real test database

**Example**:
```python
def test_user_repository_create(db_session):
    repo = UserRepository(db_session)
    user = repo.create(User(
        username='test',
        email='test@minerva.edu',
        password_hash='hashed'
    ))
    assert user.user_id is not None
```

### E2E Tests (Full Stack)

**Goal**: Test complete user workflows (current tests are here)

**Example**:
```python
def test_quiz_submission_flow(test_client, auth_token):
    response = test_client.post(
        '/api/quiz-submit',
        json={'user_id': 1, 'quiz_card_id': 1, 'answer_id': 1},
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200
```

## Test Fixtures

The test suite uses pytest fixtures defined in `conftest.py`:

- **`postgres_container`** - Testcontainers PostgreSQL container (session-scoped)
- **`test_database_url`** - Connection URL from the container
- **`test_engine`** - Shared test database engine
- **`test_session_factory`** - Session factory for creating test sessions
- **`db_session`** - Database session for tests (function-scoped, cleaned)
- **`clean_db`** - Cleaned database before each test
- **`test_client`** - Flask test client with test database
- **`populated_test_data`** - Database populated with comprehensive test data
- **`auth_token`** - JWT authentication token for testing protected endpoints
- **Sample data fixtures**:
  - `sample_course`, `sample_unit`, `sample_concept`
  - `sample_quiz_card`, `sample_quiz_answers`
  - `sample_user`

## Test Data

Test data is populated using the `populated_test_data` fixture in `conftest.py`. This fixture creates:
- 2 courses (EA50, FA50)
- 3 units
- 4 concepts
- 3 quiz cards
- 4 quiz answers
- 1 test user (`testuser@minerva.edu`)

## How Testcontainers Works

When you run `pytest`:
1. Testcontainers starts a fresh PostgreSQL 16 container
2. Tests run against this isolated database
3. Container is automatically destroyed after tests complete

This ensures:
- ✅ Tests are isolated from development data
- ✅ Same PostgreSQL version as production
- ✅ No manual setup required
- ✅ Reproducible test environment

## Writing Good Tests

### Arrange-Act-Assert Pattern

```python
def test_something():
    # Arrange: Set up test data
    user = User(username='test')
    
    # Act: Execute the code under test
    result = service.process(user)
    
    # Assert: Verify the outcome
    assert result.success is True
```

### Test One Thing Per Test

```python
# ❌ Bad: Tests multiple things
def test_user_creation_and_login():
    user = create_user()
    token = login_user()
    ...

# ✅ Good: One test per behavior
def test_user_creation():
    user = create_user()
    assert user.id is not None

def test_user_login():
    token = login_user()
    assert token is not None
```

### Descriptive Test Names

```python
# ❌ Bad
def test_quiz():
    ...

# ✅ Good
def test_submit_quiz_with_correct_answer_increases_easiness_factor():
    ...
```

## Test Coverage Goals

| Layer | Target | Current Status |
|-------|--------|----------------|
| Routes | 90%+ | ✅ Good coverage |
| Services | 95%+ | ⏳ Needs unit tests |
| Repositories | 85%+ | ⏳ Needs integration tests |
| Validators | 100% | ⏳ Needs unit tests |
| Overall | 90%+ | ✅ Currently good |

## Continuous Integration

Tests run automatically on:
- Pull requests (via GitHub Actions)
- Merges to main branch
- Scheduled nightly runs

CI configuration: `.github/workflows/ci.yaml`

## Next Steps for Test Refactoring

The refactored clean architecture requires layered testing:

1. **Create `unit/` directory** for service/validator tests with mocked dependencies
2. **Create `integration/` directory** for repository tests with real database  
3. **Move current tests** to `e2e/` directory (they're already E2E tests)
4. **Add unit tests** for each service:
   - `test_auth_service.py` - Registration, login, JWT logic
   - `test_quiz_service.py` - SM-2 algorithm, scoring
   - `test_course_service.py` - Course retrieval logic
   - `test_progress_service.py` - Analytics calculations
5. **Add integration tests** for repositories:
   - `test_user_repository.py` - CRUD operations
   - `test_quiz_repository.py` - Query logic
   - `test_course_repository.py` - Hierarchical queries
   - `test_progress_repository.py` - Progress tracking
6. **Add validator tests**:
   - `test_auth_validators.py` - Email/password validation
   - `test_quiz_validators.py` - Quiz input validation
7. **Improve coverage** to meet 90%+ target

## Best Practices

1. **Test behavior, not implementation** - Focus on what code does, not how
2. **Keep tests independent** - No test should depend on another
3. **Use descriptive names** - Test names should explain what they verify
4. **Test edge cases** - Minimum/maximum values, empty inputs, nulls
5. **Mock external dependencies** in unit tests (repositories, APIs)
6. **Use real database** in integration tests
7. **Clean up after tests** - Fixtures should properly clean up resources
8. **Keep tests fast** - Unit tests should run in milliseconds
9. **Use factories** for test data creation
10. **Test error paths** - Not just happy paths

## Debugging Tests

```bash
# Verbose output
pytest -v

# Show print statements
pytest -s

# Drop into debugger on failure
pytest --pdb

# Run last failed tests only
pytest --lf

# Run specific test with verbose output
pytest backend/tests/test_auth.py::TestAuthEndpoints::test_register -v -s

# Run with coverage report
pytest --cov=backend --cov-report=term-missing
```

## Dependencies

Tests require:
- **pytest** - Test framework
- **pytest-flask** - Flask testing utilities
- **requests** - HTTP library
- **psycopg2-binary** - PostgreSQL adapter
- **testcontainers[postgresql]** - Docker container management
- **Docker** (running) - Required for testcontainers

Install Python dependencies:
```bash
pip install -r requirements.txt
```

## References

- **Architecture**: See `ARCHITECTURE.md` for clean architecture details
- **Pytest Documentation**: https://docs.pytest.org/
- **Flask Testing**: https://flask.palletsprojects.com/testing/
- **Testcontainers**: https://testcontainers-python.readthedocs.io/
- **Mocking**: https://docs.python.org/3/library/unittest.mock.html

```

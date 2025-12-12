# Architecture Documentation

This document describes the architecture of the Gamify-HC backend, which follows **Clean Architecture** principles and **12-Factor App** methodology.

## Table of Contents
- [Overview](#overview)
- [Architecture Layers](#architecture-layers)
- [Request Flow](#request-flow)
- [Design Principles](#design-principles)
- [12-Factor App Compliance](#12-factor-app-compliance)
- [Directory Structure](#directory-structure)
- [Component Details](#component-details)

---

## Overview

The Gamify-HC backend is a Flask-based REST API that implements a **layered architecture** with clear separation of concerns. Each layer has a specific responsibility and communicates only with adjacent layers.

### Key Characteristics:
- **Stateless processes** - No server-side sessions
- **Environment-based configuration** - All config via environment variables
- **Structured logging** - JSON logs to stdout/stderr
- **Horizontal scalability** - Can run multiple instances
- **Production-ready** - Gunicorn WSGI, graceful shutdown, health checks

---

## Architecture Layers

The application is organized into the following layers, from top to bottom:

```
┌─────────────────────────────────────────────────────────────┐
│                      HTTP Layer (Flask)                      │
│                    Routes/Controllers                        │
│  • Parse HTTP requests                                       │
│  • Call services                                             │
│  • Return HTTP responses                                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      Middleware Layer                        │
│  • Request logging (with request IDs)                       │
│  • CORS handling                                             │
│  • Global error handling                                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Validation Layer                          │
│  • Input validation                                          │
│  • Business rule validation                                  │
│  • Error messages                                            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                     Service Layer                            │
│  • Business logic                                            │
│  • Orchestration                                             │
│  • Transaction management                                    │
│  • SM-2 spaced repetition algorithm                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Repository Layer                          │
│  • Data access                                               │
│  • Query construction                                        │
│  • Model mapping                                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      Database Layer                          │
│  • PostgreSQL 16                                             │
│  • SQLAlchemy ORM                                            │
│  • Connection pooling                                        │
└─────────────────────────────────────────────────────────────┘
```

### Layer Communication Rules:
1. **Routes** → Call **Services** (never repositories directly)
2. **Services** → Call **Repositories** (never database directly)
3. **Repositories** → Query **Database** via SQLAlchemy
4. **Data flows up** through **Schemas/DTOs**
5. **Cross-cutting concerns** handled by **Middleware**

---

## Request Flow

### Example: Submit Quiz Answer

```
1. HTTP Request
   POST /api/quiz-submit
   {
     "user_id": 1,
     "quiz_card_id": 5,
     "answer_id": 12
   }

2. Middleware
   ├─ Request Logger: Generate request ID, log request
   ├─ CORS: Check origin
   └─ Error Handler: Setup exception handling

3. Route (quiz.py)
   ├─ Parse request body
   ├─ Validate JWT token
   └─ Call QuizService.submit_quiz()

4. Validator (quiz_validators.py)
   ├─ Validate user_id, quiz_card_id, answer_id
   └─ Check required fields

5. Service (quiz_service.py)
   ├─ Get quiz card via QuizRepository
   ├─ Validate answer via QuizRepository
   ├─ Calculate SM-2 score (easiness factor, interval)
   ├─ Create progress record via ProgressRepository
   └─ Return result

6. Repository (quiz_repository.py, progress_repository.py)
   ├─ Query database for quiz card
   ├─ Query database for answer
   ├─ Insert progress record
   └─ Return models

7. Schema (quiz_schemas.py)
   ├─ Convert models to DTOs
   └─ Serialize to JSON

8. HTTP Response
   {
     "success": true,
     "correct": true,
     "next_review": "2025-12-15T10:30:00Z",
     "easiness_factor": 2.6
   }

9. Middleware
   └─ Request Logger: Log response, calculate duration
```

---

## Design Principles

### 1. Separation of Concerns
Each layer has a single, well-defined responsibility:
- **Routes**: HTTP concerns only
- **Services**: Business logic only
- **Repositories**: Data access only
- **Validators**: Input validation only
- **Schemas**: Data transformation only

### 2. Dependency Injection
Dependencies are injected, not hardcoded:
```python
# Service accepts repositories as parameters
class QuizService:
    def __init__(self, quiz_repo=None, progress_repo=None):
        self.quiz_repo = quiz_repo or QuizRepository()
        self.progress_repo = progress_repo or ProgressRepository()
```

### 3. Single Responsibility Principle
Each class/module does one thing:
- `QuizService` - Quiz business logic
- `QuizRepository` - Quiz data access
- `QuizValidator` - Quiz input validation
- `QuizSchema` - Quiz data transformation

### 4. Interface Segregation
Small, focused interfaces instead of large ones:
- `BaseRepository` - Common CRUD operations
- Specific repositories extend with custom queries

### 5. DRY (Don't Repeat Yourself)
Common code is extracted:
- `BaseRepository` - Shared repository logic
- `get_db()` - Database session management
- `get_logger()` - Logger creation
- `@jwt_required` - Authentication decorator

---

## 12-Factor App Compliance

| Factor | Implementation |
|--------|---------------|
| **I. Codebase** | Single git repository with branches |
| **II. Dependencies** | `requirements.txt` with pinned versions |
| **III. Config** | Environment variables via `backend/config/settings.py` |
| **IV. Backing Services** | PostgreSQL via DATABASE_URL |
| **V. Build, Release, Run** | Docker multi-stage builds, separate stages |
| **VI. Processes** | Stateless, share-nothing, Gunicorn workers |
| **VII. Port Binding** | Self-contained, exports via PORT env var |
| **VIII. Concurrency** | Horizontal scaling via Gunicorn workers |
| **IX. Disposability** | Fast startup, graceful shutdown handlers |
| **X. Dev/Prod Parity** | Docker ensures consistency |
| **XI. Logs** | JSON/text to stdout/stderr, no file writes |
| **XII. Admin Processes** | CLI tool (`python -m backend.cli`) |

---

## Directory Structure

```
backend/
├── cli.py                      # Admin CLI tool (12-Factor XII)
├── __main__.py                 # CLI entry point
├── app.py                      # Flask application factory
├── gunicorn_config.py          # Production WSGI config
│
├── config/                     # Configuration (12-Factor III)
│   ├── __init__.py
│   └── settings.py             # Environment-based settings
│
├── database/                   # Database layer
│   ├── models.py               # SQLAlchemy ORM models
│   ├── setup.py                # Database initialization
│   └── seed_data/              # Initial data
│       ├── seed.py
│       ├── cx50.py             # Complex Systems course
│       ├── ea50.py             # Empirical Analysis course
│       ├── fa50.py             # Formal Analysis course
│       └── mc50.py             # Meaningful Communication course
│
├── middleware/                 # Cross-cutting concerns
│   ├── __init__.py
│   ├── cors_middleware.py      # CORS configuration
│   ├── error_handler.py        # Global exception handling
│   └── request_logger.py       # Request/response logging
│
├── repositories/               # Data access layer
│   ├── __init__.py
│   ├── base_repository.py      # Common CRUD operations
│   ├── course_repository.py    # Course data access
│   ├── progress_repository.py  # Progress data access
│   ├── quiz_repository.py      # Quiz data access
│   └── user_repository.py      # User data access
│
├── routes/                     # HTTP layer (thin controllers)
│   ├── __init__.py
│   ├── auth.py                 # Authentication endpoints
│   ├── concepts.py             # Concept endpoints
│   ├── courses.py              # Course endpoints
│   ├── health.py               # Health check endpoints
│   ├── quiz.py                 # Quiz endpoints
│   ├── units.py                # Unit endpoints
│   └── users.py                # User endpoints
│
├── schemas/                    # Data transfer objects (DTOs)
│   ├── __init__.py
│   ├── auth_schemas.py         # Auth request/response schemas
│   ├── course_schemas.py       # Course DTOs
│   ├── quiz_schemas.py         # Quiz DTOs
│   └── user_schemas.py         # User DTOs
│
├── services/                   # Business logic layer
│   ├── __init__.py
│   ├── auth_service.py         # Authentication logic
│   ├── course_service.py       # Course business logic
│   ├── progress_service.py     # Progress analytics
│   └── quiz_service.py         # Quiz logic (SM-2 algorithm)
│
├── utils/                      # Utilities
│   ├── __init__.py
│   ├── database_manager.py     # DB session management
│   ├── graceful_shutdown.py    # Shutdown signal handlers
│   └── logger.py               # Structured logging
│
├── validators/                 # Input validation
│   ├── __init__.py
│   ├── auth_validators.py      # Auth input validation
│   └── quiz_validators.py      # Quiz input validation
│
└── tests/                      # Test suite
    ├── conftest.py             # Pytest fixtures
    ├── test_auth.py
    ├── test_concepts.py
    ├── test_courses.py
    ├── test_health.py
    ├── test_quiz.py
    ├── test_units.py
    └── test_users.py
```

---

## Component Details

### Configuration Layer (`backend/config/`)

**Purpose**: Centralized, environment-based configuration

**Key Files**:
- `settings.py` - Settings class with validation

**Design**:
```python
class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    
    # Server
    SERVER_HOST: str = os.getenv("HOST", "0.0.0.0")
    SERVER_PORT: int = int(os.getenv("PORT", "5001"))
    
    # Security
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = os.getenv("LOG_FORMAT", "text")
```

**Benefits**:
- Single source of truth for configuration
- Type validation
- Environment-specific settings
- No hardcoded values

---

### Middleware Layer (`backend/middleware/`)

**Purpose**: Cross-cutting concerns that apply to all requests

**Components**:

1. **Request Logger** (`request_logger.py`)
   - Generates unique request IDs
   - Logs request/response details
   - Calculates request duration
   - Adds `X-Request-ID` header

2. **CORS Middleware** (`cors_middleware.py`)
   - Configures allowed origins
   - Handles preflight requests
   - Environment-based settings

3. **Error Handler** (`error_handler.py`)
   - Catches all exceptions
   - Returns consistent JSON errors
   - Logs with stack traces
   - HTTP status code mapping

**Registration Order** (in `app.py`):
```python
register_request_logger(app)  # First: log all requests
register_cors(app)             # Second: handle CORS
register_error_handlers(app)   # Last: catch all errors
```

---

### Repository Layer (`backend/repositories/`)

**Purpose**: Data access abstraction

**Pattern**: Repository Pattern

**Structure**:
```python
class BaseRepository:
    """Common CRUD operations"""
    def get_by_id(self, id)
    def get_all(self)
    def create(self, entity)
    def update(self, entity)
    def delete(self, id)

class QuizRepository(BaseRepository):
    """Quiz-specific queries"""
    def get_by_concept(self, concept_id)
    def get_random_by_unit(self, unit_id)
    def get_answers(self, quiz_card_id)
```

**Benefits**:
- Encapsulates database queries
- Easy to test (can mock repositories)
- Consistent interface
- Can swap database implementations

---

### Service Layer (`backend/services/`)

**Purpose**: Business logic and orchestration

**Key Services**:

1. **AuthService** (`auth_service.py`)
   - User registration
   - Password hashing (werkzeug)
   - JWT token generation
   - Token verification

2. **QuizService** (`quiz_service.py`)
   - SM-2 spaced repetition algorithm
   - Score calculation
   - Next review date calculation
   - Progress tracking

3. **CourseService** (`course_service.py`)
   - Course/Unit/Concept retrieval
   - Hierarchical data assembly

4. **ProgressService** (`progress_service.py`)
   - Progress aggregation by course/unit/concept
   - Statistics calculation
   - Performance analytics

**SM-2 Algorithm** (QuizService):
```python
def _calculate_sm2(self, correctness, easiness_factor, interval):
    """
    SM-2 Spaced Repetition Algorithm
    
    correctness: 0-5 (0=total blackout, 5=perfect recall)
    easiness_factor: >1.3 (default 2.5)
    interval: days until next review
    """
    # Update easiness factor
    new_ef = easiness_factor + (0.1 - (5 - correctness) * 
                               (0.08 + (5 - correctness) * 0.02))
    new_ef = max(1.3, new_ef)
    
    # Calculate interval
    if correctness < 3:
        new_interval = 1  # Repeat tomorrow
    elif interval == 0:
        new_interval = 1
    elif interval == 1:
        new_interval = 6
    else:
        new_interval = round(interval * new_ef)
    
    return new_ef, new_interval
```

---

### Schemas Layer (`backend/schemas/`)

**Purpose**: Data transformation and serialization

**Pattern**: Data Transfer Objects (DTOs)

**Example**:
```python
@dataclass
class QuizSubmitRequest:
    """Request schema for quiz submission"""
    user_id: int
    quiz_card_id: int
    answer_id: int
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data['user_id'],
            quiz_card_id=data['quiz_card_id'],
            answer_id=data['answer_id']
        )

@dataclass
class QuizSubmitResponse:
    """Response schema for quiz submission"""
    success: bool
    correct: bool
    next_review: str
    easiness_factor: float
    
    def to_dict(self):
        return {
            'success': self.success,
            'correct': self.correct,
            'next_review': self.next_review,
            'easiness_factor': self.easiness_factor
        }
```

**Benefits**:
- Type safety
- Validation
- Consistent API contracts
- Easy to test

---

### Routes Layer (`backend/routes/`)

**Purpose**: HTTP request/response handling (thin controllers)

**Pattern**: Thin Controller Pattern

**Structure**:
```python
@quiz_bp.route('/quiz-submit', methods=['POST'])
@jwt_required
def submit_quiz():
    """Thin controller - delegates to service"""
    try:
        # 1. Parse request
        data = request.get_json()
        quiz_request = QuizSubmitRequest.from_dict(data)
        
        # 2. Validate
        validate_quiz_submission(quiz_request)
        
        # 3. Call service
        result = quiz_service.submit_quiz(quiz_request)
        
        # 4. Serialize response
        response = QuizSubmitResponse.from_dict(result)
        
        # 5. Return HTTP response
        return jsonify(response.to_dict()), 200
        
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
```

**Benefits**:
- Routes are easy to read
- Business logic is in services (testable)
- Consistent error handling
- Clear HTTP concerns

---

### Validators Layer (`backend/validators/`)

**Purpose**: Input validation and business rule enforcement

**Structure**:
```python
class ValidationError(Exception):
    """Custom validation exception"""
    pass

def validate_email(email: str):
    """Validate email format"""
    if not email or '@' not in email:
        raise ValidationError("Invalid email format")
    if not email.endswith('@minerva.edu'):
        raise ValidationError("Must use @minerva.edu email")

def validate_password(password: str):
    """Validate password strength"""
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters")
```

**Benefits**:
- Centralized validation logic
- Reusable across endpoints
- Clear error messages
- Easy to test

---

### Utils Layer (`backend/utils/`)

**Key Utilities**:

1. **Logger** (`logger.py`)
   - JSON format for production
   - Text format for development
   - Request ID correlation
   - Log to stdout/stderr

2. **Database Manager** (`database_manager.py`)
   - Session factory
   - Connection pooling
   - Cleanup on shutdown

3. **Graceful Shutdown** (`graceful_shutdown.py`)
   - SIGTERM/SIGINT handlers
   - Cleanup coordination
   - In-flight request completion

---

## Testing Strategy

### Layer-Specific Testing:

1. **Repository Tests**
   - Use test database
   - Test queries return correct data
   - Test filtering, ordering, pagination

2. **Service Tests**
   - Mock repositories
   - Test business logic
   - Test SM-2 algorithm
   - Test error handling

3. **Route Tests**
   - Mock services
   - Test HTTP request/response
   - Test authentication
   - Test error responses

4. **Integration Tests**
   - Full stack (routes → services → repositories → database)
   - Test real workflows
   - Test transaction handling

5. **E2E Tests**
   - Full API calls
   - Test user scenarios
   - Test data consistency

---

## Migration from Old Architecture

### Old Architecture Issues:
- ❌ Business logic in routes (fat controllers)
- ❌ Direct database queries in routes
- ❌ Hardcoded configuration
- ❌ Inconsistent error handling
- ❌ No logging structure
- ❌ Print statements instead of logging

### New Architecture Benefits:
- ✅ Thin controllers (HTTP concerns only)
- ✅ Service layer (business logic)
- ✅ Repository layer (data access)
- ✅ Environment-based configuration
- ✅ Global error handling middleware
- ✅ Structured JSON logging
- ✅ Production WSGI server (Gunicorn)
- ✅ Graceful shutdown
- ✅ Health check endpoints
- ✅ Admin CLI tool

### Migration Steps:
1. ✅ Extract configuration to environment variables
2. ✅ Create repository layer
3. ✅ Create service layer
4. ✅ Create schemas/DTOs
5. ✅ Create validators
6. ✅ Refactor routes to thin controllers
7. ✅ Add middleware layer
8. ✅ Add Gunicorn configuration
9. ✅ Add graceful shutdown
10. ✅ Add CLI tool
11. ✅ Add health checks
12. ✅ Update documentation
13. ⏳ Update tests

---

## Best Practices

### 1. Always Use Services in Routes
```python
# ❌ Bad: Direct database access in route
@app.route('/users/<id>')
def get_user(id):
    user = db.query(User).filter_by(id=id).first()
    return jsonify(user.to_dict())

# ✅ Good: Use service
@app.route('/users/<id>')
def get_user(id):
    user = auth_service.get_user_by_id(id)
    return jsonify(UserResponse.from_model(user).to_dict())
```

### 2. Always Use Repositories in Services
```python
# ❌ Bad: Direct database in service
class QuizService:
    def get_quiz(self, id):
        return db.query(QuizCard).filter_by(id=id).first()

# ✅ Good: Use repository
class QuizService:
    def __init__(self, quiz_repo=None):
        self.quiz_repo = quiz_repo or QuizRepository()
    
    def get_quiz(self, id):
        return self.quiz_repo.get_by_id(id)
```

### 3. Always Use Schemas for Serialization
```python
# ❌ Bad: Manual dict construction
return jsonify({
    'id': user.id,
    'username': user.username,
    'email': user.email
})

# ✅ Good: Use schema
return jsonify(UserResponse.from_model(user).to_dict())
```

### 4. Always Validate Input
```python
# ❌ Bad: No validation
data = request.get_json()
result = service.submit_quiz(data)

# ✅ Good: Validate first
data = request.get_json()
validate_quiz_submission(data)
result = service.submit_quiz(data)
```

### 5. Always Use Logger, Never Print
```python
# ❌ Bad
print(f"User {user_id} logged in")

# ✅ Good
logger.info(f"User {user_id} logged in")
```

---

## Performance Considerations

### Database Connection Pooling
```python
engine = create_engine(
    database_url,
    pool_size=10,           # 10 persistent connections
    max_overflow=20,        # 20 additional connections
    pool_pre_ping=True,     # Verify connections before use
    pool_recycle=300,       # Recycle after 5 minutes
)
```

### Gunicorn Worker Configuration
```python
# CPU-bound: workers = (2 x cores) + 1, threads = 1
# I/O-bound: workers = cores, threads = 2-4

workers = 4
threads = 2
worker_class = 'sync'  # or 'gevent' for I/O
```

### Caching Strategy
- **In-memory**: Course/Unit/Concept data (rarely changes)
- **Redis**: User sessions, rate limiting (future)
- **Database**: Quiz progress, user data

---

## Security Considerations

1. **JWT Tokens**
   - 24-hour expiration (configurable)
   - Signed with secret key
   - Includes user_id claim

2. **Password Hashing**
   - Werkzeug's `generate_password_hash`
   - Salted and hashed
   - Never store plain passwords

3. **CORS**
   - Configured via environment
   - Whitelist specific origins in production
   - Never use `*` in production

4. **SQL Injection**
   - Protected by SQLAlchemy ORM
   - Parameterized queries
   - No raw SQL

5. **Environment Variables**
   - Never commit `.env` file
   - Use platform secrets management
   - Rotate JWT_SECRET_KEY regularly

---

## Future Enhancements

1. **Caching Layer**
   - Redis for session management
   - Cache course data
   - Rate limiting

2. **Background Jobs**
   - Celery for async tasks
   - Email notifications
   - Analytics aggregation

3. **API Versioning**
   - `/api/v1/`, `/api/v2/`
   - Backward compatibility
   - Deprecation strategy

4. **GraphQL**
   - Alternative to REST
   - Client-driven queries
   - Reduced over-fetching

5. **Database Migrations**
   - Alembic for schema changes
   - Version-controlled migrations
   - Rollback capability

---

## Conclusion

The Gamify-HC backend architecture prioritizes:
- **Maintainability** - Clear layer separation
- **Testability** - Each layer can be tested independently
- **Scalability** - Stateless, horizontally scalable
- **Reliability** - Graceful shutdown, health checks
- **Observability** - Structured logging, request tracing
- **12-Factor Compliance** - Cloud-native, portable

This architecture provides a solid foundation for future growth and ensures the codebase remains maintainable as the team and feature set expand.

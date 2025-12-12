# Backend

This directory holds the backend API layer for the Gamify-HC project. The
Flask application uses a **clean architecture** with clear separation of
concerns and follows **12-Factor App** methodology.

## Architecture Overview

The backend implements a layered architecture:

```
Routes (HTTP) → Middleware → Validators → Services (Business Logic) 
  → Repositories (Data Access) → Database (PostgreSQL)
```

**Key Features:**
- ✅ **Thin Controllers** - Routes handle HTTP concerns only
- ✅ **Service Layer** - Business logic and orchestration
- ✅ **Repository Pattern** - Data access abstraction
- ✅ **Environment-based Config** - No hardcoded values
- ✅ **Structured Logging** - JSON logs to stdout/stderr
- ✅ **Production WSGI** - Gunicorn with worker processes
- ✅ **Graceful Shutdown** - SIGTERM/SIGINT handlers
- ✅ **Health Checks** - Liveness and readiness probes
- ✅ **Admin CLI** - One-off admin processes

📖 **For detailed architecture documentation, see [`ARCHITECTURE.md`](../ARCHITECTURE.md)**

## Project Structure

```
backend/
├── app.py                 # Flask application factory with blueprint registration
├── database/
│   ├── models.py         # SQLAlchemy database models
│   ├── setup.py          # Database setup and initialization
│   └── seed_data/        # Database seeding scripts
├── routes/               # API route blueprints
│   ├── auth.py          # Authentication endpoints (register, login, JWT)
│   ├── courses.py       # Course endpoints
│   ├── units.py         # Unit endpoints
│   ├── concepts.py      # Concept endpoints
│   ├── quiz.py          # Quiz submission endpoints
│   └── users.py         # User profile and progress endpoints
├── tests/                # Test suite
│   ├── conftest.py      # Pytest fixtures and configuration
│   └── test_*.py        # Test files for each feature
└── utils/
    └── database_manager.py  # Database session management
```

## Local Setup

### Quick Start: Run Everything with Docker (Recommended)

The simplest way to run the application is with Docker Compose, which starts all services together:

```bash
docker compose up --build
```

This starts:
- PostgreSQL on port 5432
- Backend API on port 5001
- Frontend on port 3000

**Verify it's working:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:5001/api/health
- You should see: `{"status": "ok", "message": "Gamify-HC API is running"}`

All environment variables (including `DATABASE_URL`) are automatically configured by `docker-compose.yml`.

---

### Alternative: Run Components Individually (Outside Docker)

If you want to run the backend Flask app directly on your machine (outside Docker), follow these steps:

#### Step 1: Start PostgreSQL

PostgreSQL is required. Start it with Docker:

```bash
docker compose up postgres -d
```

This starts PostgreSQL with the `gamify_hc` database for development.
(Tests use testcontainers and don't require this step.)

#### Step 2: Create Virtual Environment

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Step 3: Start the API

From the **project root directory**, run:

```bash
DATABASE_URL="postgresql://gamify:gamify_secret@localhost:5432/gamify_hc" python run.py
```

**What happens when you run this:**

1. **Database Initialization** (automatic):
   - `run.py` → calls `create_app()` from `backend/app.py`
   - `create_app()` → creates `DatabaseManager` instance
   - `DatabaseManager` → calls `create_database()` from `backend/database/setup.py`
   - `create_database()` → connects to PostgreSQL and creates tables
   - Tables are created automatically from SQLAlchemy models
   - If database is empty, it automatically seeds with initial data from `database/seed_data/`

2. **API Server Starts**:
   - Flask API runs at **http://localhost:5001**
   - All endpoints are available under `/api/*`

**Verify it's working:**
- Open http://localhost:5001/api/health in your browser
- You should see: `{"status": "ok", "message": "Gamify-HC API is running"}`

## Backend Architecture

### Design Philosophy

The backend is structured using a **modular blueprint architecture** to keep
code organized, maintainable, and scalable. Each feature area is isolated in
its own module, making it easy to understand, test, and extend.

### Where Things Belong

#### **Application Entry Point**
- **`run.py`** (project root) - Entry point that starts the Flask server
- **`backend/app.py`** - Flask application factory that:
  - Creates and configures the Flask app
  - Initializes the database connection
  - Registers all route blueprints
  - Sets up CORS for frontend integration

#### **Database Layer**
- **`backend/database/models.py`** - SQLAlchemy ORM models (Course, Unit, Concept, etc.)
- **`backend/database/setup.py`** - Database initialization utilities:
  - `create_database()` - Creates tables and auto-seeds if empty
  - Handles database connection string resolution
- **`backend/database/seed_data/`** - Seed scripts for initial data
- **`backend/utils/database_manager.py`** - Database session management:
  - `DatabaseManager` class - Manages database connections for Flask app
  - `get_db()` function - Retrieves database session from Flask context

#### **API Routes (Blueprints)**
- **`backend/routes/`** - Each file contains a Flask blueprint for a feature:
  - `auth.py` - Authentication (register, login, JWT)
  - `courses.py` - Course endpoints
  - `units.py` - Unit endpoints
  - `concepts.py` - Concept endpoints
  - `quiz.py` - Quiz submission endpoints
  - `users.py` - User profile and progress endpoints

**Blueprint Pattern:**
- Each blueprint is self-contained with its own routes
- All routes are automatically prefixed with `/api`
- Blueprints are registered in `app.py` to keep route registration centralized

#### **Testing**
- **`backend/tests/`** - Test files mirror the route structure
- Uses pytest fixtures for database setup/teardown

### Application Flow

```
run.py
  └─> create_app() [app.py]
       ├─> DatabaseManager() [utils/database_manager.py]
       │    └─> create_database() [database/setup.py]
       │         ├─> Creates tables from models
       │         └─> Auto-seeds if database is empty
       │
       └─> Register Blueprints [routes/*.py]
            └─> All routes available at /api/*
```

### Key Architectural Decisions

1. **Blueprint Architecture**: Routes are organized by feature, not by HTTP method
   - Makes it easy to find all endpoints for a feature
   - Allows multiple developers to work on different features simultaneously
   - Each blueprint can be tested independently

2. **Database Session Management**: Centralized via `DatabaseManager`
   - Database initialization happens once at app startup
   - Sessions are created per-request via `get_db()` helper
   - Ensures proper connection handling and cleanup

3. **Automatic Database Setup**: Database and tables are created automatically
   - No manual migration steps needed for development
   - Seeding happens automatically if database is empty
   - Environment variables allow customization without code changes

4. **Separation of Concerns**:
   - Models define data structure (`database/models.py`)
   - Routes handle HTTP requests/responses (`routes/*.py`)
   - Utilities handle cross-cutting concerns (`utils/`)
   - Setup handles initialization (`database/setup.py`)

## API Endpoints

### Authentication (`/api/auth`)
- `POST /api/auth/register` - Register a new user (requires .minerva.edu email)
- `POST /api/auth/login` - Login and receive JWT token
- `GET /api/auth/me` - Get current user info (requires JWT authentication)

### Courses (`/api/courses`)
- `GET /api/courses` - Get all courses
- `GET /api/courses/:id` - Get specific course
- `GET /api/courses/:id/units` - Get units for a course

### Units (`/api/units`)
- `GET /api/units/:id` - Get specific unit
- `GET /api/units/:id/concepts` - Get concepts for a unit

### Concepts (`/api/concepts`)
- `GET /api/concepts/:id` - Get concept with quiz cards
- `GET /api/concepts/:id/quiz-cards` - Get all quiz cards for a concept

### Quiz (`/api/quiz`)
- `GET /api/quiz-cards/:id` - Get quiz card with answers
- `POST /api/quiz-submit` - Submit quiz answer

### Users (`/api/users`)
- `GET /api/users/:id` - Get user info
- `GET /api/users/:id/progress` - Get user progress

### Health Checks (`/api/health`)
- `GET /api/health` - Comprehensive health status with database check
- `GET /api/health/live` - Liveness probe (Kubernetes/monitoring)
- `GET /api/health/ready` - Readiness probe (load balancers/orchestration)

**Health Check Details:**

`/api/health` - Returns detailed status including:
- Application info (name, version, environment)
- Database connectivity and response time
- Uptime in seconds
- PostgreSQL version

`/api/health/live` - Simple liveness check:
- Returns 200 OK if app is running
- Does NOT check database (by design)
- Used by Kubernetes to restart crashed pods

`/api/health/ready` - Readiness check with database:
- Returns 200 OK if ready to accept traffic
- Returns 503 if database is unavailable
- Used by load balancers to route traffic
- Used during rolling deployments

## Authentication

The API uses JWT (JSON Web Tokens) for authentication:

1. Register or login to receive an `access_token`
2. Include the token in subsequent requests:
   ```
   Authorization: Bearer <access_token>
   ```
3. Tokens expire after 24 hours

## Environment Variables

The application looks for the following environment variables:

- `DATABASE_URL` – PostgreSQL connection string.
  - **With Docker**: Automatically set by `docker-compose.yml` (no action needed)
  - **Without Docker**: Must be set manually before running `python run.py`
- `SQLALCHEMY_ECHO` – controls SQLAlchemy's query logging. Set to `1`,
  `true`, `yes`, etc. to enable verbose SQL logging. Defaults to `0` (disabled).
- `JWT_SECRET_KEY` – Secret key for JWT token signing. Defaults to a dev key
  (change in production). Should be a secure random string.
- `POSTGRES_PASSWORD` – (Docker only) PostgreSQL password. Defaults to `gamify_secret`.
- `TEST_DATABASE_URL` – (Testing only) Override the test database URL.

Example usage (running Flask outside Docker):

```bash
DATABASE_URL="postgresql://gamify:gamify_secret@localhost:5432/gamify_hc" \
SQLALCHEMY_ECHO=1 \
JWT_SECRET_KEY="your-secret-key-here" \
python run.py
```

**Note**: When using `docker compose up`, all environment variables are automatically configured - you don't need to set them manually.

## Testing

Tests use testcontainers to automatically spin up a PostgreSQL container.
No manual database setup required - just run pytest:

```bash
pytest
```

Tests are located in `backend/tests/` and use pytest fixtures for database
setup and teardown. The test database is automatically created and destroyed
for each test session.

## Admin CLI Tool (12-Factor: Admin Processes)

The backend includes a Click-based CLI for administrative tasks. These commands
are designed to run as **one-off processes**, separate from the web application,
following 12-Factor App methodology.

### Available Commands

#### Seed Database
```bash
python -m backend.cli seed
```
Populates the database with course data from `backend/database/seed_data/`.

Options:
- `--force` - Re-seed even if data already exists (clears existing course data)

#### Create User
```bash
python -m backend.cli create-user
```
Creates a new user account. Prompts for username, email, and password.
Useful for creating test accounts or admin users.

#### Database Info
```bash
python -m backend.cli db-info
```
Displays database statistics and health information:
- Table counts (courses, units, concepts, quiz cards, users)
- PostgreSQL version
- Connection status

#### Reset Database (DANGER!)
```bash
python -m backend.cli reset-db
```
Drops and recreates all tables, **deleting all data** including users and progress.
Requires confirmation. Use with caution!

### Usage Examples

```bash
# Seed a fresh database
python -m backend.cli seed

# Create a test user
python -m backend.cli create-user
# (then follow prompts)

# Check database statistics
python -m backend.cli db-info

# Force re-seed (clears and re-populates)
python -m backend.cli seed --force

# Reset everything (careful!)
python -m backend.cli reset-db
```

**Note**: All CLI commands require the `DATABASE_URL` environment variable to be set.

## Database

- **ORM**: SQLAlchemy
- **Database**: PostgreSQL 16 (required for both development and production)
- **Migrations**: Currently handled via `database/setup.py`. Consider Alembic
  for production migrations.
- **Seeding**: Automatic on first startup. Seed data scripts are in
  `database/seed_data/`

### Why PostgreSQL Only?

We standardized on PostgreSQL to ensure consistency between development, testing,
and production environments. This avoids "works on my machine" bugs caused by
SQL dialect differences between SQLite and PostgreSQL.
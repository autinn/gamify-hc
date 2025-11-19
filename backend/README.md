# Backend

This directory holds the backend API layer for the Gamify-HC project. The
Flask application uses a modular blueprint architecture with SQLAlchemy models
for database operations. The database automatically initializes and seeds when
the Flask app starts.

## Project Structure

```
backend/
├── app.py                 # Flask application factory with blueprint registration
├── database/
│   ├── models.py         # SQLAlchemy database models
│   ├── setup.py          # Database setup and initialization
│   ├── gamify_hc.db      # SQLite database (auto-created on startup)
│   └── seed_data/        # Database seeding scripts
├── routes/               # API route blueprints
│   ├── auth.py          # Authentication endpoints (register, login, JWT)
│   ├── courses.py       # Course endpoints
│   ├── units.py         # Unit endpoints
│   ├── concepts.py      # Concept endpoints
│   ├── quiz.py          # Quiz submission endpoints
│   └── users.py         # User profile and progress endpoints
└── utils/
    └── database_manager.py  # Database session management
```

## Local Setup

### Step 1: Create Virtual Environment

Create and activate a Python virtual environment (if you have not already):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Initialize Database & Start API

From the **project root directory**, run:

```bash
python run.py
```

**What happens when you run this:**

1. **Database Initialization** (automatic):
   - `run.py` → calls `create_app()` from `backend/app.py`
   - `create_app()` → creates `DatabaseManager` instance
   - `DatabaseManager` → calls `create_database()` from `backend/database/setup.py`
   - `create_database()` → creates SQLite database file at `backend/database/gamify_hc.db`
   - Tables are created automatically from SQLAlchemy models
   - If database is empty, it automatically seeds with initial data from `database/seed_data/`

2. **API Server Starts**:
   - Flask API runs at **http://localhost:5001**
   - All endpoints are available under `/api/*`

**Verify it's working:**
- Open http://localhost:5001/api/health in your browser
- You should see: `{"status": "ok", "message": "Gamify-HC API is running"}`

### Step 3: (Optional) Configure Environment Variables

Defaults are provided, so you can skip this for a quick start. See the
[Environment Variables](#environment-variables) section below for customization
options.

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

### Health Check
- `GET /api/health` - Check if API is running

## Authentication

The API uses JWT (JSON Web Tokens) for authentication:

1. Register or login to receive an `access_token`
2. Include the token in subsequent requests:
   ```
   Authorization: Bearer <access_token>
   ```
3. Tokens expire after 24 hours (configurable via `JWT_EXPIRATION_HOURS`)

## Environment Variables

The application looks for the following environment variables:

- `DATABASE_URL` – SQLAlchemy connection string. Defaults to a bundled SQLite
  file (`sqlite:///backend/database/gamify_hc.db`). Override this when you want to
  point the app at a different database (for example a temporary test database
  during CI or a local Postgres instance).
- `SQLALCHEMY_ECHO` – controls SQLAlchemy's query logging. Set to `1`,
  `true`, `yes`, etc. to enable verbose SQL logging. Defaults to `0` (disabled).
- `JWT_SECRET_KEY` – Secret key for JWT token signing. Defaults to a dev key
  (change in production). Should be a secure random string.

Example usage:

```bash
DATABASE_URL="sqlite:///backend/database/dev.db" \
SQLALCHEMY_ECHO=1 \
JWT_SECRET_KEY="your-secret-key-here" \
python run.py
```

## Testing

Run the test suite from the project root:

```bash
pytest
```

Tests are located in `backend/tests/` and use pytest fixtures for database
setup and teardown.

## Database

- **ORM**: SQLAlchemy
- **Database**: SQLite (default, can be configured for PostgreSQL, MySQL, etc.)
- **Migrations**: Currently handled via `database/setup.py`. Consider Alembic
  for production migrations.
- **Seeding**: Automatic on first startup. Seed data scripts are in
  `database/seed_data/`
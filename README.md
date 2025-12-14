# gamify-hc

A gamified learning platform for Habits of Mind and Foundational Concepts, enabling learners to test themselves on situational quiz questions and track their progress. 


## Documentation Guide

This main README provides a high-level overview of the Gamify-HC project, including:
- **Quick Start Instructions**: Steps to run the application using Docker.
- **Project Structure**: A breakdown of the folder and file organization.
- **API Endpoints**: A summary of the available backend API routes.
- **Environment Variables**: Key configuration options for the project.
- **Alternate Development Setup**: Instructions for running the project locally without Docker.

For more detailed information about specific parts of the project, refer to the following:

- **Frontend Documentation**: The `frontend/README.md` contains details about the React-based frontend, including its architecture, available scripts, development setup, and testing. It provides insights into the layered architecture, data flow, and state management patterns used in the frontend.

- **Backend Documentation**: The `backend/README.md` provides an in-depth look at the Flask-based backend, including its project structure, API endpoints, authentication, database setup, and testing. It also includes instructions for running the backend locally or with Docker, as well as testing guidelines.

Testing instructions for both the frontend and backend are detailed in their respective READMEs.

## Deployment Guide

### Quick Start (Docker)

The easiest way to run the application is with Docker.

0. **Prerequisites**
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

1. **Set up environment variables for development:**
   This is meant to be used in the context of development. 
   For deployment, please set up .env manually.
   ```bash
   ./scripts/check-env.sh
   ```
   - Check if you have a .env file.
   - Create .env from .env.example if missing.
   - Warn you that you are using insecure development variables.

2. **Build, create and start containers:**
   ```bash
   docker compose up
   ```

What you get:
- PostgreSQL 16 on `5432`
- Backend API on `http://localhost:5001`
- Frontend on `http://localhost:3000`
- Docs at `http://localhost:5001/api/docs` (spec served from `docs/swagger.json`)
- Health at `http://localhost:5001/api/health` → `{"status": "ok", "message": "Gamify-HC API is running"}`

`docker-compose.yml` wires all environment variables (including `DATABASE_URL`) for you.



### Continued Opperations with Docker and enviroment variables

#### Making Changes and Switching Branches
Docker caches image layers, so when switching branches or making changes, Docker may use cached images that contain older code. To ensure you're running the latest code:

```bash
# Stop containers and remove volumes (use -v if you expect DB schema changes between branches)
docker compose down -v

# Rebuild images without cache to ensure fresh builds
docker compose build --no-cache

# Start services with rebuilt images
docker compose up
```

#### Docker Commands

```bash
# Start services (foreground)
docker compose up

# Start services (background)
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down

# Rebuild after code changes
docker compose up --build

# Delete the database (for reinitialization later)
docker compose down -v
```

### Environment Variables

The application can be customized using environment variables. A template file `.env.example` is provided with all available options.

#### Setup for Development

**Set up environment variables for development:**
```bash
./scripts/check-env.sh
```
This script will:
- ✅ Check if you have a `.env` file
- 🚀 Create `.env` from `.env.example` if missing
- ⚠️ Warn you that you are using insecure development variables

**Note**: This is meant to be used in the context of development. For deployment, please set up `.env` manually.

**For Docker**: Docker Compose automatically reads the `.env` file from the project root. You can also pass individual variables:
```bash
# Option 1: Use .env file (recommended)
./scripts/check-env.sh  # Sets up .env for development
docker compose up

# Option 2: Set individual variables inline
JWT_SECRET_KEY=your-secure-secret docker compose up
```

#### Available Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://gamify:gamify_secret@localhost:5432/gamify_hc` |
| `POSTGRES_PASSWORD` | PostgreSQL password (for Docker) | `gamify_secret` |
| `POSTGRES_PORT` | PostgreSQL port exposed to host | `5432` |
| `FLASK_DEBUG` | Enable Flask debug mode | `True` |
| `FLASK_HOST` | Server host address | `0.0.0.0` |
| `FLASK_PORT` | Server port number | `5001` |
| `FLASK_ENV` | Flask environment | `development` |
| `JWT_SECRET_KEY` | Secret key for JWT tokens (**MUST change in production**) | `dev-secret-key-change-in-production` |
| `JWT_ALGORITHM` | JWT encoding algorithm | `HS256` |
| `JWT_EXPIRATION_HOURS` | JWT token expiration time | `24` |
| `SQLALCHEMY_ECHO` | Enable SQL query logging | `False` |
| `AUTO_SEED_DATABASE` | Auto-seed database if empty | `True` |

For a complete list with detailed descriptions, see `.env.example`.

**⚠️ Security Warning**: Never commit your `.env` file to version control. The `.env` file is already in `.gitignore`.

---

## Alternate Development Setup 

For development, you may want to run the services directly on your machine instead of in Docker containers.

**Note**: This requires more setup than using Docker. The Docker approach (above) is recommended for simplicity.

### 0. Prerequisites

1. **Start PostgreSQL** (required for backend):
   ```bash
   docker compose up postgres -d
   ```
   This starts only the PostgreSQL container. The backend and frontend will run directly on your machine.

2. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```

### 1. Install Python Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Start Backend API

**Using the .env file (recommended)**:
```bash
# Copy and edit .env file
cp .env.example .env
# The backend automatically loads .env via python-dotenv
python run.py
```

✅ API runs at: **http://localhost:5001**

The database will be automatically created and seeded on first run.

Test it: Open http://localhost:5001/api/health in your browser

### 3. Start Frontend (in new terminal)
```bash
cd frontend
npm install  # first time only
npm start
```
✅ Frontend runs at: **http://localhost:3000**

---

## API Endpoints

All endpoints start with `/api/`:

**Authentication:**
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and receive JWT token
- `GET /api/auth/me` - Get current user info (requires authentication)

**Courses:**
- `GET /api/courses` - Get all courses
- `GET /api/courses/:id` - Get specific course
- `GET /api/courses/:id/units` - Get units for a course

**Units:**
- `GET /api/units/:id` - Get specific unit
- `GET /api/units/:id/concepts` - Get concepts for a unit

**Concepts:**
- `GET /api/concepts/:id` - Get concept with quiz cards
- `GET /api/concepts/:id/quiz-cards` - Get all quiz cards

**Quiz:**
- `GET /api/quiz-cards/:id` - Get quiz card with answers
- `POST /api/quiz-submit` - Submit answer

**Users:**
- `GET /api/users/:id` - Get user info
- `GET /api/users/:id/progress` - Get user progress

## Troubleshooting

Here are some common issues and their resolutions:

- **Port Already in Use**:
  - Stop any processes using the conflicting port or change the port in the `.env` file.

- **Database Connection Issues**:
  - Verify the `DATABASE_URL` is correct and the database is running.

- **Frontend Not Loading**:
  - Check the browser console for errors and ensure the frontend service is running.

- **Backend API Errors**:
  - Check the backend logs for detailed error messages.

- **Seed Data Not Loading**:
  - Ensure `AUTO_SEED_DATABASE=True` in the `.env` file or run the seed script manually:
    ```bash
    python backend/database/seed_data/seed.py
    ```

## Architecture Overview

The Gamify-HC application follows a modular architecture, with clear separation between the frontend, backend, and database layers. Below is a visual representation of how the components interact, including Docker for containerization:

```
┌─────────────────────────────────────────────────────────┐
│                    Docker Container                    │
│ ┌─────────────────────────────────────────────────────┐ │
│ │                Frontend (React)                    │ │
│ │  - User Interface                                  │ │
│ │  - API Communication via Services                 │ │
│ │  - State Management with Hooks                    │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │                Backend (Flask)                     │ │
│ │  - REST API Endpoints (/api/*)                     │ │
│ │  - Business Logic in Services                      │ │
│ │  - Authentication with JWT                         │ │
│ │  - Database Interaction via SQLAlchemy            │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │                Database (PostgreSQL)               │ │
│ │  - Stores Application Data                         │ │
│ │  - Auto-seeded with Initial Data                   │ │
│ │  - Managed via SQLAlchemy ORM                      │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Data Flow
1. **Frontend**: The React-based frontend sends HTTP requests to the backend API for data and displays the results to the user.
2. **Backend**: The Flask backend processes requests, applies business logic, and interacts with the database.
3. **Database**: PostgreSQL stores all application data, including user information, courses, units, and progress.

### Key Features
- **Frontend**:
  - Built with React, using hooks for state management.
  - Communicates with the backend via REST API.
  - Runs in a Docker container for consistent deployment.
- **Backend**:
  - Modular design with blueprints for different API routes.
  - Handles authentication, data validation, and business logic.
  - Runs in a Docker container for isolated execution.
- **Database**:
  - Relational database managed with SQLAlchemy ORM.
  - Automatically seeded with initial data on first run.
  - Runs in a Docker container for easy setup and scaling.







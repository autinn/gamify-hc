# gamify-hc

A gamified learning platform for Habits of Mind and Foundational Concepts.

## Quick Start (Docker)

The easiest way to run the application is with Docker.

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Run with Docker

**1. Set up environment variables:**
```bash
./scripts/check-env.sh
```
This script will:
- ✅ Check if you have a `.env` file
- 🚀 Create `.env` from `.env.example` if missing
- ⚠️ Warn you if using default/insecure values

**2. Start the application:**
```bash
docker compose up
```

That's it! The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5001

The database will be automatically created and seeded on first run.

### Making Changes and Switching Branches
Docker caches image layers, so when switching branches or making changes, Docker may use cached images that contain older code. To ensure you're running the latest code:

```bash
# Stop containers and remove volumes (use -v if you expect DB schema changes between branches)
docker compose down -v

# Rebuild images without cache to ensure fresh builds
docker compose build --no-cache

# Start services with rebuilt images
docker compose up
```

### Docker Commands

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

1. **Copy the example file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file** with your values (optional - defaults work for development):
   ```bash
   # Database Configuration
   DATABASE_URL=postgresql://gamify:gamify_secret@localhost:5432/gamify_hc
   
   # Flask Configuration
   FLASK_DEBUG=True
   FLASK_HOST=0.0.0.0
   FLASK_PORT=5001
   
   # JWT Configuration (CHANGE IN PRODUCTION!)
   JWT_SECRET_KEY=dev-secret-key-change-in-production
   ```

3. **For Docker**: Docker Compose automatically reads the `.env` file from the project root. You can also pass individual variables:
   ```bash
   # Option 1: Use .env file (recommended)
   cp .env.example .env
   # Edit .env with your values
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

## Development Setup (Without Docker)

For development, you may want to run the services directly on your machine instead of in Docker containers.

**Note**: This requires more setup than using Docker. The Docker approach (above) is recommended for simplicity.

### Prerequisites

1. **Start PostgreSQL** (required for backend):
   ```bash
   docker compose up postgres -d
   ```
   This starts only the PostgreSQL container. The backend and frontend will run directly on your machine.

2. **Set up environment variables** (optional):
   ```bash
   cp .env.example .env
   # Edit .env if you need to customize any values
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

**Or set environment variables explicitly**:
```bash
DATABASE_URL="postgresql://gamify:gamify_secret@localhost:5432/gamify_hc" python run.py
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

---

## Using API in React

```javascript
import * as api from '../services/api';

// Get courses
const courses = await api.getCourses();

// Get units
const units = await api.getCourseUnits(courseId);

// Submit quiz
const result = await api.submitQuizAnswer({
  user_id: 1,
  quiz_card_id: 5,
  answer_id: 12
});
```

---

## Project Structure

```
├── backend/
│   ├── app.py                    # Flask app factory with blueprint registration
│   ├── Dockerfile                # Backend Docker configuration
│   ├── routes/                   # API route blueprints (auth, courses, units, etc.)
│   ├── database/
│   │   ├── models.py            # SQLAlchemy database models
│   │   ├── setup.py             # Database initialization (PostgreSQL)
│   │   └── seed_data/           # Seed data scripts
│   ├── utils/
│   │   └── database_manager.py  # Database session management
│   └── tests/                   # Test suite
├── frontend/
│   ├── Dockerfile               # Frontend Docker configuration
│   ├── nginx.conf               # Nginx configuration for production
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── pages/               # Page components
│   │   └── services/api.js      # API helper functions
│   └── package.json
├── .github/
│   └── workflows/
│       └── ci.yaml              # GitHub Actions CI workflow
├── docker-compose.yml           # Docker Compose configuration
├── docs/                        # Project documentation
├── run.py                       # Start API server (for development)
└── requirements.txt             # Python packages
```

For detailed documentation, see:
- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Contributing: `docs/USING_GITHUB.md`

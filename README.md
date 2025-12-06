# gamify-hc

A gamified learning platform for Habits of Mind and Foundational Concepts.

## Quick Start (Docker)

The easiest way to run the application is with Docker.

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Run with Docker

```bash
docker-compose up
```

That's it! The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5001

The database will be automatically created and seeded on first run.

### Docker Commands

```bash
# Start services (foreground)
docker-compose up

# Start services (background)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after code changes
docker-compose up --build
```

### Environment Variables

You can customize the application with environment variables:

```bash
# Set JWT secret for production
JWT_SECRET_KEY=your-secure-secret docker-compose up
```

---

## Development Setup (Without Docker)

For development, you may want to run the services directly on your machine instead of in Docker containers.

**Note**: This requires more setup than using Docker. The Docker approach (above) is recommended for simplicity.

### Prerequisites

1. **Start PostgreSQL** (required for backend):
   ```bash
   docker-compose up postgres -d
   ```
   This starts only the PostgreSQL container. The backend and frontend will run directly on your machine.

### 1. Install Python Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Start Backend API
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

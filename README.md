# gamify-hc

A gamified learning platform for Habits of Mind and Foundational Concepts.

## Quick Start

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Backend API
```bash
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
│   ├── routes/                   # API route blueprints (auth, courses, units, etc.)
│   ├── database/
│   │   ├── models.py            # SQLAlchemy database models
│   │   ├── setup.py             # Database initialization
│   │   ├── gamify_hc.db         # SQLite database (auto-created)
│   │   └── seed_data/           # Seed data scripts
│   ├── utils/
│   │   └── database_manager.py  # Database session management
│   └── tests/                   # Test suite
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── pages/               # Page components
│   │   └── services/api.js      # API helper functions
│   └── package.json
├── docs/                        # Project documentation
├── run.py                       # Start API server
└── requirements.txt             # Python packages
```

For detailed documentation, see:
- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Contributing: `docs/USING_GITHUB.md`

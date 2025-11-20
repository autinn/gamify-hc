# gamify-hc

A gamified learning platform for Harvard College courses.

## Quick Start

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create Database
```bash
python backend/database/database.py
```

### 3. Start Backend API
```bash
python run.py
```
✅ API runs at: **http://localhost:5001**

Test it: Open http://localhost:5001/api/health in your browser

### 4. Start Frontend (in new terminal)
```bash
cd frontend
npm install  # first time only
npm start
```
✅ Frontend runs at: **http://localhost:3000**

---

## API Endpoints

All endpoints start with `/api/`:

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

**User:**
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

## Files

```
├── backend/
│   ├── app.py              # Flask API (all endpoints)
│   └── database/
│       ├── database.py     # Database models
│       └── test.db        # SQLite database (created after setup)
├── frontend/src/services/
│   └── api.js             # API helper functions
├── run.py                  # Start API server
└── requirements.txt        # Python packages
```

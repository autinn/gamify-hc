# Gamify HC — Running Notes

## 🧭 Project Overview
**Purpose:** Build a gamified version of the Habits of Mind & Foundational Concepts (HCs) handbook.  
**Tech Stack:** React (frontend) | Flask (backend) | SQL (database)

---

## 🗓️ Meetings

### Meeting 1 — 10/10/25
**Team Interests**
- **Backend:** Taher, Aldi, Merrick  
- **Frontend:** Rachael, Sophie, Autinn  

**Sprint Backlog: Starting the Project**
- [ ] Distribute labour — assign tasks  
- [ ] Design SRS content *(Rachael)*  
- [ ] Send HC content files *(Rachael)*  
- [ ] Initialize GitHub repo *(Autinn)*  
- [ ] Create timeline + MVP  
- [ ] Merrick: GitHub push workflow doc + PR template  
- [ ] Establish communication standards  

**Before Next Week**
- Backend → brainstorm database system  
- Frontend → meet for wireframe  

**Product Backlog**
- Initial architecture setup  
- Define MVP scope  

**Tech Stack (default unless otherwise needed)**
- React  
- Flask  
- SQL  

---

### Meeting 2 — 10/17/25
**Meeting Minutes**
- ✅ First PR merged  
- 📅 Backend + Frontend created internal subteam schedules  
- 🖼️ Reviewed Figma mockups and clarified layouts  

---

### Meeting 2.b.1 — Backend (10/19/25)
**Action Points**
- Access HC content for GitHub  
- Merrick: set up SQL DB for one HC chapter  
- Align backend with frontend for HC IDs + quiz schemas  
- Study Anki spaced repetition logic → [Anki Repo](https://github.com/ankitects/anki)

**Proposed Backend Structure**
```bash
backend/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── user.py, course.py, unit.py, concept.py, quiz.py, progress.py, badge.py
│   ├── routes/
│   │   ├── auth.py, courses.py, units.py, concepts.py, quiz.py
│   ├── services/
│   │   ├── quiz_generator.py, score_calculator.py
│   ├── utils/
│   │   ├── validators.py, decorators.py
│   └── config.py
├── migrations/
├── tests/
└── requirements.txt
```

**Minimum Endpoints for Demo**
```
GET /api/courses
GET /api/courses/:id/units
GET /api/units/:id/hcs
GET /api/hcs/:id
GET /api/hcs/:id/quizzes
POST /api/quiz/submit
GET /api/progress/me
POST /api/auth/login
```

**Example Return Shape**
```json
{
  "id": 1,
  "name": "EA50",
  "items": [],
  "pagination": { "page": 1, "total": 4 }
}
```

---

### Data Model (Draft)
| Table | Key Fields |
|--------|-------------|
| users | id, email, name, password_hash, total_points, streak, created_at |
| courses | id, code, name, semester |
| units | id, course_id, name, order_index |
| hcs | id, unit_id, name, tag, mission, cornerstone, link, is_unlocked |
| quizzes | id, hc_id, question, options_json, correct_index, explanation, points |
| challenges | id, scenario, options_json, correct_hc, cornerstone, points |
| progress | user_id, hc_id, score, completed, last_played |
| attempts | id, user_id, quiz_id, is_correct, created_at |

---

### Flask Backbone Tasks
1. Scaffold `app/` with Blueprints and stub routes.  
2. Add Alembic migrations + seed script (~100 quiz items).  
3. Implement SQLAlchemy models.  
4. Add JWT auth (`Flask-JWT-Extended`).  
5. Enforce pre-commit hooks (black, isort, flake8).  
6. Add one happy-path test per endpoint.  

---

### Meeting 2.f.1 — Frontend
**Frontend Claude Artifact:** [Claude Reference](https://claude.ai/public/artifacts/0701896b-1f72-4f59-8bc0-be9105420d12)

**Simplified Structure**
```bash
frontend/
├── src/
│   ├── components/
│   │   ├── common/ (Layout, UI, Charts)
│   │   ├── course/
│   │   ├── unit/
│   │   ├── concept/
│   │   └── quiz/
│   ├── pages/
│   │   ├── Dashboard.jsx, CoursePage.jsx, UnitPage.jsx, QuizPage.jsx
│   ├── hooks/
│   │   ├── useApi.js, useAuth.js, useQuiz.js
│   ├── api/
│   │   ├── client.js, courses.js, quiz.js, progress.js
│   ├── store/
│   │   ├── slices/, store.js
│   └── App.jsx
```

---

### Meeting 3 — 10/24/25
**Task Assignments**
- **Autinn:** Create all pages (add ConceptPage), integrate Rachael’s components  
- **Sophie:** Build quiz page with mock data  
- **Rachael:** Create shared components  
- **Merrick:** Convert SQL → SQLAlchemy, support Sophie with DB connections  
- **Taher:** Implement API routing logic  
- **Aldiyar:** Populate database with initial data  

---

## 📘 Reference Documents
- [Content Model for Gamified HC](https://docs.google.com/document/d/1nRAt4AXF9nVBPSisQoJmS3DDfrqllifTmLwbNBOROAo/edit?tab=t.0)
- [Cornerstone Example Questions](https://docs.google.com/document/d/1I9IVby8d04jzku9HsORTxh2cJsT-TvjvXp2MRarvtok/edit?tab=t.0)
- [Drive Folder](https://drive.google.com/drive/folders/1_OzpQb6egR9dreUbcy6e2HTYSBR_BVpQ)
- [GitHub Repo](https://github.com/autinn/gamify-hc)
- [Figma Board](https://www.figma.com/board/nocaEzzVgKNOBZaLVFWYyN/Gamify-HCs?node-id=0-1&t=AMfovwCndFghkmeU-1)

---

## 🧩 HC References (Empirical Analyses & Complex Systems)
Includes HC tags such as:
- `#dataviz`, `#heuristics`, `#constraints`, `#systemmapping`, `#ethicaljudgment`, `#emotionaliq`, etc.  
These connect directly to the backend’s HC schema and quiz content.

---

## 🧠 Next Steps
1. Finalize endpoint contracts + JSON schemas.  
2. Freeze API surface.  
3. Frontend integrates with Flask stubs.  
4. Create PR: **"backend: scaffold + stub API"**  
5. Backend + Frontend weekly sync.

---

*Last updated: 2025-11-06*

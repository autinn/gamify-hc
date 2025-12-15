# Gamify-HC: Complete Meeting Notes & Timeline

**Project:** Gamified Habits of Mind & Foundational Concepts (HC) Learning Platform  
**Organization:** Minerva University CS162 Systems Design  
**Repository:** [gamify-hc](https://github.com/autinn/gamify-hc)  
**Last Updated:** December 15, 2025

---

## 📋 Table of Contents

1. [Meeting 1: Project Kickoff](#meeting-1-project-kickoff)
2. [Meeting 2: Integration & Alignment](#meeting-2-integration--alignment)
3. [Meeting 2.b.1: Backend Subteam](#meeting-2b1-backend-subteam)
4. [Meeting 2.f.1: Frontend Subteam](#meeting-2f1-frontend-subteam)
5. [Meeting 3: Task Distribution](#meeting-3-task-distribution)
6. [Meeting 4: Mid-Sprint Sync](#meeting-4-mid-sprint-sync)
7. [Meeting 4.b.1: Backend Refinement](#meeting-4b1-backend-refinement)
8. [Meeting 5.f.1: Frontend Progress](#meeting-5f1-frontend-progress)
9. [Final Meeting: Demo & Polish](#final-meeting-demo--polish)
10. [Sprint Backlog & Roadmap](#sprint-backlog--roadmap)
11. [Meeting Summary Statistics](#meeting-summary-statistics)

---

## Meeting 1: Project Kickoff

**Date:** October 10, 2025  
**Duration:** 45–60 minutes  
**Attendees:** Full team  
**Facilitator:** Tin Kit Au-Yeung

### Team Interests & Preferences

**Backend Track (3 members):**
- Taher Chaudiwala
- Aldiyar (Aldi)
- Merrick Richers

**Frontend Track (3 members):**
- Rachael Akwa
- Sophie Bird
- Autinn

### Sprint Backlog: Starting the Project

| Task | Owner | Deadline | Status |
|------|-------|----------|--------|
| Distribute labour — assign tasks | All | Oct 10 | ✅ |
| Design SRS content | Rachael | Oct 10 | ✅ |
| Send HC content files | Rachael | Oct 10 | ✅ |
| Initialize GitHub repo | Autinn | Oct 10 | ✅ |
| Create timeline + MVP | All | Oct 10 | ✅ |
| GitHub push workflow doc + PR template | Merrick | Oct 10 | ✅ |
| Establish communication standards | Merrick | Oct 10 | ✅ |

### Before Next Week (Oct 17)

| Task | Track | Owner | Objective |
|------|-------|-------|-----------|
| Brainstorm database system | Backend | Taher, Aldi, Merrick | Design schema & normalization |
| Meet for wireframe review | Frontend | Rachael, Sophie, Autinn | Validate design, plan components |

### Tech Stack (Defaults)

- **Frontend:** React
- **Backend:** Flask
- **Database:** SQL
- **State Management:** Redux (frontend)
- **ORM:** SQLAlchemy (backend)
- **Reference:** [Claude Frontend Artifact](https://claude.ai/public/artifacts/0701896b-1f72-4f59-8bc0-be9105420d12)

### Initial Project Structure

**Frontend Architecture** (src/)
```
src/
├── components/
│   ├── common/ (Layout, UI, Charts)
│   │   ├── Header, Sidebar, MainLayout
│   │   ├── Button, Card, ProgressBar
│   │   └── PerformanceChart, ProgressChart
│   ├── course/ (CourseCard, CourseList, CourseDetail, CourseStats)
│   ├── unit/ (UnitCard, UnitList, UnitDetail, UnitProgress)
│   ├── concept/ (ConceptCard, ConceptList, ConceptDetail)
│   └── quiz/ (QuizContainer, QuizQuestion, QuizAnswer, QuizResults)
├── pages/ (MainPage, CoursePage, UnitPage, ConceptPage, QuizPage, SummaryPage)
├── hooks/ (useAuth, useQuiz, useProgress, useGameification)
├── services/ (api, courseService, quizService, progressService, userService)
├── store/ (Redux slices: courses, quizzes, users, progress)
├── styles/ (globals.css, theme.js)
├── App.jsx (routing & layout)
└── index.js
```

**Backend Structure** (initial)
```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/ (user, course, quiz, progress, hc)
│   ├── routes/ (auth, courses, quiz, progress, hcs)
│   ├── services/ (quiz_generator, score_calculator, progress_aggregator)
│   ├── utils/ (validators, decorators)
│   └── config.py
├── migrations/
├── tests/
└── requirements.txt
```

### Key Resources Shared

- **Content Model:** [HC Handbook Structure](https://docs.google.com/document/d/1nRAt4AXF9nVBPSisQoJmS3DDfrqllifTmLwbNBOROAo/edit)
- **Example Questions:** [By Cornerstone](https://docs.google.com/document/d/1I9IVby8d04jzku9HsORTxh2cJsT-TvjvXp2MRarvtok/edit)
- **Figma Design:** [Gamify HCs Board](https://www.figma.com/board/nocaEzzVgKNOBZaLVFWYyN/Gamify-HCs)
- **Drive Folder:** [Project Assets](https://drive.google.com/drive/folders/1_OzpQb6egR9dreUbcy6e2HTYSBR_BVpQ)

### Key Decisions

✅ Team split into parallel backend/frontend streams  
✅ Tech stack finalized (React, Flask, SQL)  
✅ Subteams to coordinate independently with weekly full-team sync  
✅ MVP scope: Dashboard → Course → Unit → Concept → Quiz → Progress flow

---

## Meeting 2: Integration & Alignment

**Date:** October 17, 2025  
**Duration:** 45–60 minutes  
**Attendees:** Full team  
**Facilitator:** Tin Kit Au-Yeung

### Meeting Minutes

✅ **First PR merged** — GitHub workflow validated; no blockers  
🔄 **Subteams created internal schedules** — Backend and Frontend meetings established  
🖼️ **Figma mockups reviewed and clarified** — Design direction confirmed for first sprint  
📋 **Discussed MVP scope** — Agreement on 5-step flow (Dashboard → Course → Unit → Concept → Quiz)

### Discussion Points

- **GitHub workflow:** PRs, code review process, and merge strategy validated
- **Design alignment:** Frontend mockups approved; no major revisions needed
- **Backend database:** Initial schema ideas reviewed; Merrick to lead SQL setup
- **Timeline:** First sprint (Oct 24–31) focused on component development and API contracts

### Next Steps

- Backend subteam: finalize API contracts + database schema
- Frontend subteam: complete component library + page wireframes
- Full team: sync on Oct 24

---

## Meeting 2.b.1: Backend Subteam

**Date:** October 19, 2025  
**Duration:** 50–70 minutes  
**Attendees:** Taher Chaudiwala, Aldiyar, Merrick Richers  
**Facilitator:** Merrick Richers

### Objective

Define backend architecture, API contracts, and database schema to unblock frontend development.

### Action Items

| Task | Owner | Deliverable | Due |
|------|-------|-------------|-----|
| Request HC content repo access | Merrick | GitHub access confirmed | Oct 19 |
| Set up SQL database for one HC chapter | Merrick | DB initialized with seed data | Oct 22 |
| Align on HC IDs + quiz schemas | All | Contract document (API + DB) | Oct 22 |
| Study Anki spaced repetition logic | Taher | Research notes + proposal | Oct 24 |
| Create Flask scaffold + stubs | Taher, Aldi | Working repo with dummy endpoints | Oct 24 |

### Proposed Backend Architecture

```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── unit.py
│   │   ├── concept.py
│   │   ├── quiz.py
│   │   ├── progress.py
│   │   └── badge.py (optional for MVP)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── courses.py
│   │   ├── units.py
│   │   ├── concepts.py
│   │   ├── quiz.py
│   │   ├── progress.py (optional for MVP)
│   │   └── badges.py (optional for MVP)
│   ├── services/
│   │   ├── quiz_generator.py
│   │   ├── score_calculator.py
│   │   ├── progress_aggregator.py
│   │   └── badge_service.py (optional for MVP)
│   ├── utils/
│   │   ├── validators.py
│   │   └── decorators.py (auth_required, role_check, etc.)
│   └── config.py (DB URI, JWT secret, etc.)
├── migrations/ (Alembic)
├── tests/
│   ├── test_auth.py
│   ├── test_courses.py
│   ├── test_quizzes.py
│   └── test_progress.py
└── requirements.txt
```

### Minimum API Endpoints for Demo

| Endpoint | Method | Purpose | Response |
|----------|--------|---------|----------|
| `/api/auth/signup` | POST | Register new user | `{id, email, token}` |
| `/api/auth/login` | POST | Authenticate user | `{id, email, token}` |
| `/api/courses` | GET | List all courses | `{items: [{id, code, name}]}` |
| `/api/courses/:id/units` | GET | Get units by course | `{items: [units]}` |
| `/api/units/:id/concepts` | GET | Get concepts by unit | `{items: [concepts]}` |
| `/api/concepts/:id` | GET | Get concept detail (mission, link, cornerstone) | `{id, name, mission, link, cornerstone}` |
| `/api/concepts/:id/quizzes` | GET | Get quizzes for concept | `{items: [{id, stem, options, correct_index, explanation}]}` |
| `/api/quiz/submit` | POST | Submit quiz answers | Request: `{quiz_id, answers[]}` Response: `{score, correct[], xp_awarded}` |
| `/api/progress/me` | GET | Get user's overall progress | `{perConcept: {}, perUnit: {}, perCourse: {}, total_points, streak}` |
| `/api/progress/heartbeat` | POST | Update user activity (streak, last_played) | `{updated: true}` |

### Data Model (ERD)

| Table | Key Fields | Relationships |
|-------|-----------|----------------|
| `users` | id, email, name, password_hash, total_points, streak, created_at | 1:N → attempts, progress |
| `courses` | id, code, name, semester | 1:N → units (EA50, FA50, MC50, CX50) |
| `units` | id, course_id, name, order_index | 1:N → concepts |
| `concepts` | id, unit_id, name, tag, mission, cornerstone, link, is_unlocked | 1:N → quizzes, attempts |
| `quizzes` | id, concept_id, question, options_json, correct_index, explanation, points | 1:N → attempts |
| `challenges` | id, scenario, options_json, correct_concept, cornerstone, points | Challenge items |
| `progress` | user_id, concept_id, score, completed, last_played | User progress per concept |
| `attempts` | id, user_id, quiz_id, is_correct, created_at | Detailed attempt history |

**Demo Seed Data:**  
3 courses × 2 units × 3 concepts × 4 questions each = **72 questions total**

### Flask Backbone Checklist

- [ ] Scaffold `app/` with Flask Blueprints
- [ ] Create SQLAlchemy models for all tables
- [ ] Implement Alembic migrations
- [ ] Create seed script (~100 quiz items)
- [ ] Add JWT authentication (`Flask-JWT-Extended`)
- [ ] Implement all 10+ endpoints with dummy responses
- [ ] Add pre-commit hooks (black, isort, flake8)
- [ ] Write one happy-path test per endpoint
- [ ] Document API in OpenAPI/Swagger format

### Dependencies

```
Flask==2.3.0
Flask-SQLAlchemy==3.0.0
Flask-JWT-Extended==4.4.0
Flask-CORS==4.0.0
python-dotenv==1.0.0
SQLAlchemy==2.0.0
alembic==1.11.0
pytest==7.2.0
black==23.1.0
isort==5.12.0
flake8==6.0.0
```

### Reference

- **Anki Spaced Repetition:** [Anki GitHub](https://github.com/ankitects/anki)
- **SQLAlchemy ORM:** [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- **Flask Blueprints:** [Flask Application Factory Pattern](https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/)

### Key Decisions

✅ Use SQLAlchemy ORM (not raw SQL)  
✅ Flask Blueprints for modular routes  
✅ JWT for stateless authentication  
✅ Seed database with 3 courses × 2 units × 3 concepts structure  
✅ Frontend can mock API calls; backend will provide stubs first, then real responses

---

## Meeting 2.f.1: Frontend Subteam

**Date:** October 19, 2025  
**Duration:** 50–70 minutes  
**Attendees:** Rachael Akwa, Sophie Bird, Autinn  
**Facilitator:** Rachael Akwa

### Objective

Define frontend component architecture, state management, and page structure to align with backend API contracts.

### Reference Documentation

- [Content Model for Gamified HC](https://docs.google.com/document/d/1nRAt4AXF9nVBPSisQoJmS3DDfrqllifTmLwbNBOROAo/edit)
- [Cornerstone Example Questions](https://docs.google.com/document/d/1I9IVby8d04jzku9HsORTxh2cJsT-TvjvXp2MRarvtok/edit)
- [Figma Design Board](https://www.figma.com/board/nocaEzzVgKNOBZaLVFWYyN/Gamify-HCs)
- [Claude Frontend Artifact](https://claude.ai/public/artifacts/0701896b-1f72-4f59-8bc0-be9105420d12)

### Frontend Architecture (Final)

**Three-Layer Design Pattern:**
1. **UI Layer** → Pages & Components (render visual UI)
2. **Hooks Layer** → Custom React hooks (manage state + side effects)
3. **Services Layer** → API clients & business logic (communicate with backend)

```
src/
├── components/
│   ├── common/
│   │   ├── Layout/
│   │   │   ├── Header.jsx (logo, nav, user menu)
│   │   │   ├── Sidebar.jsx (navigation drawer)
│   │   │   └── MainLayout.jsx (wrapper)
│   │   ├── UI/
│   │   │   ├── Button.jsx (reusable button component)
│   │   │   ├── Card.jsx (container for content)
│   │   │   └── ProgressBar.jsx (visual progress indicator)
│   │   └── Charts/
│   │       ├── PerformanceChart.jsx (bar/line chart)
│   │       └── ProgressChart.jsx (user progress visualization)
│   ├── course/
│   │   ├── CourseCard.jsx (course overview card)
│   │   ├── CourseList.jsx (grid of courses)
│   │   ├── CourseDetail.jsx (course page with units)
│   │   └── CourseStats.jsx (progress stats for course)
│   ├── unit/
│   │   ├── UnitCard.jsx (unit overview card)
│   │   ├── UnitList.jsx (list of units in course)
│   │   ├── UnitDetail.jsx (unit page with concepts)
│   │   └── UnitProgress.jsx (unit progress visualization)
│   ├── concept/ (HC components)
│   │   ├── ConceptCard.jsx (concept overview)
│   │   ├── ConceptList.jsx (list of concepts in unit)
│   │   ├── ConceptDetail.jsx (full concept page with mission + link)
│   │   └── HeuristicDisplay.jsx (cornerstone + tags)
│   └── quiz/
│       ├── QuizContainer.jsx (quiz wrapper)
│       ├── QuizQuestion.jsx (single question display)
│       ├── QuizAnswer.jsx (answer option component)
│       └── QuizResults.jsx (post-quiz feedback)
├── pages/
│   ├── MainPage.jsx (dashboard/home)
│   ├── CoursePage.jsx (course detail + units)
│   ├── UnitPage.jsx (unit detail + concepts)
│   ├── ConceptPage.jsx (HC detail + mission + quiz launch)
│   ├── QuizPage.jsx (quiz taking page)
│   └── QuizSummaryPage.jsx (results + explanations)
├── hooks/
│   ├── useAuth.js (login/logout state, token management)
│   ├── useQuiz.js (quiz state, answer tracking, scoring)
│   ├── useProgress.js (user progress data, aggregation)
│   ├── useCourse.js (course data, unit fetching)
│   └── useGameification.js (XP, streak, badges)
├── services/
│   ├── api/
│   │   ├── client.js (HTTP request wrapper with auth)
│   │   ├── courseService.js (course API calls)
│   │   ├── quizService.js (quiz API calls)
│   │   ├── progressService.js (progress API calls)
│   │   └── userService.js (user/auth API calls)
│   └── utils/
│       ├── quizGenerator.js (quiz logic helpers)
│       └── scoreCalculator.js (scoring algorithms)
├── store/ (Redux)
│   ├── slices/
│   │   ├── courseSlice.js (courses reducer)
│   │   ├── quizSlice.js (quiz reducer)
│   │   ├── userSlice.js (user reducer)
│   │   └── progressSlice.js (progress reducer)
│   └── store.js (Redux store configuration)
├── styles/
│   ├── globals.css (reset, typography, layout)
│   └── theme.js (color palette, design tokens)
├── App.jsx (routing, main layout)
└── index.js (React root)
```

### Data Flow Pattern

```
User Action (click button, submit quiz)
    ↓
Component dispatches action / calls hook
    ↓
Hook calls Service method
    ↓
Service calls API Layer (api/client.js)
    ↓
API makes HTTP request (with auth token)
    ↓
Response normalizes through mapper
    ↓
Hook updates state (Redux or local state)
    ↓
Component re-renders with new state
```

### State Management Strategy

| State Type | Tool | Location | Purpose |
|------------|------|----------|---------|
| Global (courses, user, progress) | Redux | `store/slices/` | App-wide shared state |
| Component-specific (form input, UI) | useState | Within component | Local UI state |
| API/async state (loading, error) | Custom hooks | `hooks/` | Manage API lifecycle |
| Temporary (modal open, dropdown) | useState | Within component | Ephemeral UI state |

### Component Checklist

**Common Components (Reusable)**
- [ ] Header (logo, navbar, user menu)
- [ ] Sidebar (navigation)
- [ ] Button (primary, secondary, disabled states)
- [ ] Card (content container)
- [ ] ProgressBar (visual indicator)
- [ ] Charts (PerformanceChart, ProgressChart)

**Page Components**
- [ ] MainPage (course list, search, filters)
- [ ] CoursePage (course detail + unit list)
- [ ] UnitPage (unit detail + concept list)
- [ ] ConceptPage (HC detail + mission + start quiz button)
- [ ] QuizPage (quiz taking interface)
- [ ] QuizSummaryPage (results + explanations)

**Feature Components**
- [ ] CourseCard, CourseList, CourseStats
- [ ] UnitCard, UnitList, UnitProgress
- [ ] ConceptCard, ConceptList, ConceptDetail, HeuristicDisplay
- [ ] QuizContainer, QuizQuestion, QuizAnswer, QuizResults

### Key Deliverables (by Oct 24)

| Task | Owner | Deadline | Status |
|------|-------|----------|--------|
| Component library (common/) | Rachael | Oct 24 | ✅ |
| Page structure (pages/) | Autinn | Oct 24 | ✅ |
| Quiz interface (quiz/) | Sophie | Oct 24 | ✅ |
| API service layer (services/) | Rachael, Autinn | Oct 24 | ✅ |
| Redux store setup | Autinn | Oct 24 | ✅ |

### Key Decisions

✅ Three-layer architecture (UI → Hooks → Services)  
✅ Redux for global state (courses, user, progress)  
✅ Custom hooks for API data fetching (useQuiz, useCourse, useProgress)  
✅ Service layer abstracts backend API; mappers normalize responses  
✅ Frontend can start with mock data while backend develops stubs

---

## Meeting 3: Task Distribution & Sprint Planning

**Date:** October 24, 2025  
**Duration:** 45–60 minutes  
**Attendees:** Full team  
**Facilitator:** Tin Kit Au-Yeung

### Objective

Distribute specific development tasks for first full sprint (Oct 24–31) and confirm deliverables for initial demo.

### Sprint 1 Task Assignments (Oct 24–31)

| Team Member | Primary Task | Secondary Task | Deadline |
|--------------|--------------|-----------------|----------|
| **Autinn** | Create all pages (MainPage, CoursePage, UnitPage, ConceptPage, QuizPage, SummaryPage); integrate Rachael's components | GitHub + demo coordination | Oct 31 |
| **Sophie** | Build quiz page with mock data; implement quiz submission logic | Question refinement | Oct 31 |
| **Rachael** | Create shared components (common/ folder: Layout, UI, Charts) | Design system documentation | Oct 31 |
| **Merrick** | Convert SQL → SQLAlchemy models; finalize database schema | DB schema documentation | Oct 31 |
| **Taher** | Implement Flask blueprint structure + API routing logic | Service layer scaffolding | Oct 31 |
| **Aldiyar** | Populate database with HC seed data (3 courses × 2 units × 3 concepts) | Data validation scripts | Oct 31 |

### Sprint 1 Goals

**Frontend (by Oct 31)**
- ✅ All page components created with mock data
- ✅ Component library complete (buttons, cards, charts, layout)
- ✅ Redux store scaffolding
- ✅ Service layer stubs (can call backend once ready)
- ✅ Routing configured (React Router)

**Backend (by Oct 31)**
- ✅ Flask app scaffolded with Blueprints
- ✅ SQLAlchemy models defined
- ✅ Database seeded with HC data
- ✅ All 10+ API endpoints stubbed with mock responses
- ✅ JWT auth working (can generate tokens)

**Integration (by Nov 7)**
- ✅ Frontend → Backend API calls working
- ✅ End-to-end flow testable (Dashboard → Quiz)
- ✅ User progress tracked on backend

### First Demo Flow (Target: Nov 7)

```
1. User lands on MainPage
   → Sees list of courses (EA50, FA50, MC50, CX50)

2. Click course → CoursePage
   → Sees units within course

3. Click unit → UnitPage
   → Sees concepts (HCs) within unit

4. Click concept → ConceptPage
   → Sees concept detail (mission, link, cornerstone tags)
   → Sees "Start Quiz" button

5. Click "Start Quiz" → QuizPage
   → Sees first MCQ (4 options)
   → Submits answer
   → Sees feedback (correct/incorrect + explanation)
   → Next question or quiz complete

6. Complete quiz → QuizSummaryPage
   → Shows score, XP awarded
   → Shows progress updated

7. Back to MainPage
   → Progress chart updated
```

### Key Decisions

✅ Mock data for frontend during sprint; backend will provide real data by Nov 7  
✅ Focus on first end-to-end flow (Dashboard → Course → Unit → Concept → Quiz)  
✅ Backend API contracts finalized; no changes to endpoint signatures  
✅ Quality over quantity—one complete flow is better than partial features  

### Before Next Meeting (Oct 31)

- **Subteams:** sync internally on progress 2–3 times per week
- **Backend:** have API stubs returning mock data
- **Frontend:** have all components rendering with props
- **All:** prepare demo for Nov 7 full-team meeting

---

## Meeting 4: Mid-Sprint Sync & API Integration

**Date:** October 31, 2025  
**Duration:** 45–60 minutes  
**Attendees:** Full team  
**Facilitator:** Merrick Richers

### Objective

Check sprint progress, identify blockers, and plan API integration for next phase.

### Progress Report

**Backend Status**
1. ✅ Taher: API endpoints created, but not all features verified (database not fully populated)
2. ⚠️ Rachael: Logic not working since there's no data to fetch
3. ⚠️ Database: Not yet populated; Merrick to complete ASAP
4. 🔄 **Next steps:** SQLAlchemy database must be merged ASAP to continue
5. ⚠️ Backend team communication: running out of time; significant progress needed

**Frontend Status**
- ✅ Sophie: merged quiz UI into component structure
- 🔄 Quiz logic: ready to connect to backend once APIs live

**Current Blockers**

| Blocker | Impact | Owner | Solution |
|---------|--------|-------|----------|
| Database not seeded | Backend can't verify endpoints | Merrick | Complete seeding ASAP |
| API logic unclear | Separation of Concerns concern raised | Merrick | Ensure services handle business logic, routes stay thin |
| Frontend can't test | No real data to fetch | Taher, Aldiyar | Provide mock data or stubs |

### Key Decisions & Discussions

**Authentication & Authorization**
- Either wait for PR merge OR work directly off branch
- No blocking; frontend can work in parallel

**Separation of Concerns (LO #1)**
- ❓ **Question (Rachael):** Should functions/business logic be in API routes?
- ✅ **Decision (Merrick):** Service layer handles business logic; routes remain thin wrappers
- Example: `quiz_generator.py` and `score_calculator.py` in services/, not routes/

**Additional Features to Add**
- ✅ HC tags on concepts (for filtering/organization)
- ❓ HTTPS (marked as "easy 4" for later, not MVP)

**Documentation**
- 🚨 **Critical Need:** Swagger/OpenAPI documentation for all endpoints
- Action: Research Swagger integration + auto-generate docs

### Revised Action Items

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Seed database with full HC data | Merrick | Nov 1 | 🔄 |
| Verify all API endpoints with data | Taher | Nov 2 | — |
| Connect frontend to real backend | Sophie, Autinn | Nov 3 | — |
| Write Swagger API documentation | Aldiyar | Nov 5 | — |
| Full demo run-through | All | Nov 6 | — |

### Focus Emphasis

> "Rather than focusing on the next task, just focus on executing the API really well."  
> "Testing is critical."  
> "Before Wednesday [Nov 3], get the core features working."

### Next Steps

- **Backend:** prioritize getting database + verified endpoints done
- **Frontend:** prepare to connect to real backend once data is available
- **All:** improve internal subteam communication (daily standups if needed)

---

## Meeting 4.b.1: Backend Refinement & Code Quality Standards

**Date:** November 1, 2025  
**Duration:** 50–70 minutes  
**Attendees:** Merrick Richers, Taher Chaudiwala, Aldiyar  
**Facilitator:** Merrick Richers

### Objective

Ensure backend adheres to learning outcome standards while completing API implementation and database integration.

### Code Quality Checklist (Learning Outcomes)

**All code must address:**

| Learning Outcome | Criteria | Implementation |
|------------------|----------|-----------------|
| **#separationofconcerns** | Each component/module handles one responsibility | Routes → thin wrappers; Services → business logic; Models → data layer |
| **#codereadability** | Clear variable names, meaningful comments, proper structure | Follow PEP 8; use type hints; document complex functions |
| **#abstraction** | Hide complexity; provide clean interfaces | Service classes abstract DB operations; decorators for auth |
| **#testing** | Comprehensive unit tests for all logic | pytest for models, services, routes; mock DB for tests |
| **#sql** | Write efficient, normalized queries | Review indexes, query plans; validate schema normalization |
| **#webstandards** | Proper HTTP methods, status codes, headers | GET for retrieval, POST for creation, proper 200/400/404/500 responses |
| **#deployment** | Build scalable, reproducible deployment process | Docker containerization, CI/CD pipeline, environment config |

### Task Assignments & Deadlines

| Task | Owner | Due | Criteria | Status |
|------|-------|-----|----------|--------|
| SQL → SQLAlchemy conversion | Merrick | Nov 1 | Clean ORM usage, indexed queries | ✅ |
| Make code simple & clean | All | Nov 2 | Readable, maintainable, commented | 🔄 |
| Use LOs from assignment | Taher | Nov 2 | Reference all 7 LOs in code | 🔄 |
| Initialize database | Merrick | Nov 1 | Seed with full HC data | ✅ |

### Backend Architecture Review

```
backend/app/
├── models/ (Data layer)
│   ├── user.py (User model + password hashing)
│   ├── course.py (Course model with relationships)
│   ├── unit.py (Unit model)
│   ├── concept.py (HC/Concept model with tags)
│   ├── quiz.py (Quiz model + question logic)
│   └── progress.py (User progress tracking)
├── routes/ (Thin API layer)
│   ├── auth.py (Login/signup endpoints only)
│   ├── courses.py (GET endpoints for courses/units)
│   ├── concepts.py (GET endpoints for HCs)
│   ├── quiz.py (GET quizzes, POST submit)
│   └── progress.py (GET user progress)
├── services/ (Business logic layer)
│   ├── quiz_generator.py (Quiz logic, randomization, difficulty)
│   ├── score_calculator.py (Scoring algorithms, XP calculation)
│   └── progress_aggregator.py (Compute progress statistics)
├── utils/ (Helpers)
│   ├── validators.py (Input validation)
│   └── decorators.py (@auth_required, @role_check)
└── tests/ (Test suite)
    ├── test_models.py (Model tests + validation)
    ├── test_services.py (Service logic tests)
    ├── test_routes.py (API endpoint tests)
    └── conftest.py (pytest fixtures + DB setup)
```

### Key Decisions

✅ Services handle all business logic (quiz generation, scoring, progress calculation)  
✅ Routes remain thin—just validate input + call service + return JSON  
✅ All tests use pytest with mock database (no production DB in tests)  
✅ Database schema normalized; denormalization justified if needed  
✅ API responses follow consistent JSON structure: `{status, data, error}`

### Deployment & Infrastructure

⚠️ **Critical Issue:** "Deployment → we are cooked" — complex and often overlooked  

**Action Items:**
- [ ] Select deployment stack (Docker, GitHub Actions, AWS/Heroku, etc.)
- [ ] Create Dockerfile + docker-compose.yml
- [ ] Set up CI/CD pipeline (GitHub Actions suggested)
- [ ] Document 12-factor app principles
- [ ] Soft deadline: Nov 10 | Hard deadline: Nov 15

---

## Meeting 5.f.1: Frontend Integration & Final Polish

**Date:** November 5, 2025  
**Duration:** 45–60 minutes  
**Attendees:** Rachael Akwa, Sophie Bird, Autinn  
**Facilitator:** Sophie Bird

### Objective

Integrate frontend with working backend API; finalize UI/UX for demo.

### Recent Progress

**Merrick & Rachael** ✅
- Frontend attached to real database
- Authentication pages created

**Sophie & Autinn** ✅
- Quiz UI polished and rendering correctly
- Progress tracking integrated

### Planned Changes & Refinements

| Item | Task | Owner | Status |
|------|------|-------|--------|
| Quiz randomization | Show all possible questions; let pick X number from all | Sophie | 🔄 |
| Back button | Add back button to all pages | Rachael | 🔄 |
| Navigation bar | Fix nav bar styling + persistence | Rachael | 🔄 |
| Text overflow | Fix details (e.g., long text in graphs) | Autinn, Merrick | 🔄 |

### Weekly Sprint Plan (Nov 5–12)

Sophie to create week-by-week plan for remaining work:
- Week 1 (Nov 5–12): Core features polish
- Week 2 (Nov 12–19): Testing + bug fixes
- Week 3 (Nov 19–Dec 3): Demo preparation
- Week 4 (Dec 3–16): Final polish + video + evaluation

### Integration Checklist

- [x] Frontend ↔ Backend API connected
- [x] Login/auth flow working end-to-end
- [x] Quiz submission updates progress
- [x] Progress charts render with real data
- [ ] Quiz randomization implemented
- [ ] All navigation working (back button, nav bar)
- [ ] UI text sizing/overflow fixed
- [ ] Performance optimized (lazy loading, caching)

### Key Decisions

✅ Frontend fully connected to real backend  
✅ Focus on polish over new features  
✅ Weekly planning approach to track progress  
✅ User testing feedback incorporated into refinements

---

## Final Meeting: Demo Preparation & Project Wrap-Up

**Date:** December 14–15, 2025 (Final Sprint)  
**Duration:** 50–70 minutes per session  
**Attendees:** Full team  
**Facilitator:** Tin Kit Au-Yeung

### Objective

Prepare polished demo video, finalize documentation, and ensure project meets all learning outcome requirements.

### Final Deliverables Checklist

| Deliverable | Owner | Due | Status |
|-------------|-------|-----|--------|
| Film demo video (main features) | Everyone | Dec 14 (midday) | ✅ |
| Edit demo video | Sophie | Dec 16 | ✅ |
| Tech stack overview (5 min) | Rachael, Aldiyar, Taher | Dec 15 | ✅ |
| Deployment overview (2 min) | Merrick | Dec 15 | ✅ |
| Meeting notes/checklist | Taher | Dec 15 | ✅ |
| Backend README | Merrick | Dec 16 | ✅ |
| Frontend README | Rachael | Dec 16 | ✅ |
| Interview documentation | Sophie | Dec 16 | ✅ |
| Code review & cleanup | All | Dec 16 | ✅ |

### Demo Video Script

**Total Length:** 8–10 minutes

**Segment 1: Account Creation & Login (2 min)**
- Created by: Sophie & Autinn
- Content:
  - Show signup page with validation (email, password 8+ chars, username unique)
  - Show error messages for invalid inputs
  - Successful signup → auto-login → onboarding flow

**Segment 2: Main Application Flow (3 min)**
- Created by: Sophie & Autinn
- Content:
  - Dashboard → Course list (EA50, FA50, MC50, CX50)
  - Click course → Unit list
  - Click unit → Concept list
  - Click concept → Show mission, link, cornerstone tags
  - Click "Start Quiz" → Quiz interface

**Segment 3: Quiz Interaction (2 min)**
- Created by: Sophie
- Content:
  - Show quiz question with 4 answer options
  - Select answer → see feedback (correct/incorrect + explanation)
  - Progress to next question
  - Complete quiz → show score + XP awarded

**Segment 4: Progress Tracking (1 min)**
- Created by: Autinn
- Content:
  - Return to dashboard
  - Show updated progress bar (increased after quiz)
  - Show hierarchical progress (course → unit → concept breakdown)

**Segment 5: Logout (30 sec)**
- Created by: Sophie
- Content:
  - Logout from user menu
  - Redirected to login page

### Technical Overview Video Script

**Segment A: Folder Structure & Architecture (2 min)**
- Presented by: Rachael, Aldiyar, Taher
- Content:
  - Frontend: 3-layer pattern (UI → Hooks → Services)
  - Backend: Modular Flask blueprints (routes, models, services)
  - Database: SQLAlchemy ORM with proper relationships
  - Tests: pytest with mocked DB

**Segment B: API Design & Contracts (2 min)**
- Presented by: Merrick
- Content:
  - 10+ REST endpoints designed
  - Consistent JSON response format
  - Authentication: JWT tokens
  - Error handling: proper HTTP status codes

**Segment C: Testing Strategy (1 min)**
- Presented by: Taher, Aldiyar
- Content:
  - Unit tests for models + services
  - Integration tests for routes
  - Mocked database for reproducibility
  - Coverage targets

### Deployment Overview (2 min)

**Presented by:** Merrick

**Content:**
- Docker containerization (Dockerfile + docker-compose.yml)
- GitHub Actions CI/CD pipeline
- Environment configuration (.env files)
- Scaling strategy (horizontal scaling with containers)
- Deployment platforms options (AWS, Heroku, DigitalOcean)

### Final Checklist Before Submission

**Code Quality**
- [x] All code follows PEP 8 (Python) + Prettier (JavaScript)
- [x] Pre-commit hooks installed (black, isort, flake8, prettier)
- [x] No console.logs or debug statements left
- [x] Comments explain complex logic
- [x] Meaningful variable/function names throughout

**Learning Outcomes Evidence**
- [x] #designthinking: User research documented (5 interviews completed)
- [x] #codereadability: Code is self-documenting with comments
- [x] #abstraction: Clear interfaces; complexity hidden
- [x] #separationofconcerns: Each layer has single responsibility
- [x] #sql: Normalized schema; efficient indexed queries
- [x] #testing: Comprehensive pytest suite with >70% coverage
- [x] #webstandards: Proper HTTP methods, status codes, auth headers
- [x] #deployment: Docker + CI/CD pipeline configured

**Documentation**
- [x] README files (backend, frontend, root)
- [x] API documentation (Swagger/OpenAPI or manual)
- [x] Architecture diagrams
- [x] Setup & run instructions
- [x] User testing findings
- [x] Interview summaries

**Testing**
- [x] All tests passing locally
- [x] No hardcoded credentials/secrets
- [x] Error handling for API failures
- [x] Form validation on frontend + backend
- [x] Session management (logout clears tokens)

**Demo Readiness**
- [x] Demo video filmed and edited
- [x] Technical overview video prepared
- [x] Live demo (if presented): practiced and timed
- [x] Backup: pre-recorded demo if live fails
- [x] Presentation slides (if required)

### Individual Submissions

Each team member completes:

| Submission | Due | Content |
|-----------|-----|---------|
| **Self-evaluation** | Dec 16 | Reflect on learning outcomes achieved |
| **Contribution summary** | Dec 16 | List PRs, commits, features owned |
| **Code review comments** | Dec 16 | Feedback on teammates' work |
| **Lessons learned** | Dec 16 | What went well; what to improve |

### Post-Project Reflection

**Questions to Answer:**

1. **Design Thinking:** How did iterative design & user research improve the product?
2. **Architecture:** What design patterns enabled scalability?
3. **Challenges:** What technical difficulties surfaced? How were they resolved?
4. **Learning:** Which learning outcome required most effort? Why?
5. **Future Work:** What would you build next if continuing the project?

### Team Closing Remarks

**Final Actions:**
- [ ] Everyone films their segment of demo video
- [ ] Sophie edits video together
- [ ] Merrick prepares deployment walkthrough
- [ ] All create individual submissions
- [ ] Final code review + cleanup
- [ ] Submit all deliverables by Dec 16, 2025

---

## Sprint Backlog & Roadmap

### Current Sprint Objectives (Dec 15–16)

**Primary Goal:** Make API robust and feature-complete by Wednesday, Dec 18

### Week 1: Nov 21–28 (Break Week) – Questions, MVP, Testing

**Goal:** Lock in quiz/UX MVP and start testing  
**Status:** ✅ Completed

#### Frontend: UI/UX Polish

| Task | Owner | Status |
|------|-------|--------|
| Text box dynamic review (main pages) | Autinn | ✅ |
| Text box dynamic review (quiz views) | Sophie | ✅ |
| Randomize and limit questions per quiz | Sophie | ✅ |
| Create bar chart visualization (DB-connected) | Autinn | ✅ |
| Add correct answer explanations (concept page) | Autinn | ✅ |
| Improve bar chart display | Autinn | ✅ |

#### Backend: Authentication & User Data

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Review and merge Rachael's auth PR | Sophie, Autinn | Nov 28 | ✅ |
| Hook up authentication (frontend ↔ backend) | Merrick (lead), Taher | Nov 28 | ✅ |
| Improve auth security (password hashing/salting) | Aldiyar | Nov 28 | ✅ |
| Use user data in-app | Aldiyar, Taher, Merrick | Nov 27 | ✅ |

#### Question Quality & Testing

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| AI pass on questions | Aldiyar, Taher | Nov 24 | ✅ |
| Comb through for weird questions | Sophie | Nov 25 | ✅ |
| Unit tests (mock API, pytest, auth tests) | Merrick, Taher, Rachael | Nov 28 | ✅ |
| Backend documentation cleanup | Merrick | Nov 28 | ✅ |

---

### Week 2: Nov 28–Dec 5 – Learning Outcomes & Deployment

**Goal:** Reorient towards LOs and begin deployment  
**Status:** ✅ Mostly Completed

#### Question Refinement & Interview Feedback

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Continue question refinement | Taher, Sophie | Dec 5 | ✅ |
| Add explanations for all answer options | Sophie | Dec 5 | ✅ |
| Follow up on interview feedback | Autinn, Sophie | Dec 5 | ✅ |
| Document interview findings | Sophie | Dec 5 | ✅ |

#### Backend: User Data Integration

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| In-app usage of user data | Aldiyar, Taher, Merrick | Dec 5 | ✅ |
| Track correctly answered questions | Aldiyar | Dec 5 | ✅ |
| DB changes as necessary | Merrick | Dec 5 | ✅ |
| Connect progress data to graphs | Aldiyar, Rachael | Dec 5 | ✅ |

#### Code Quality & Standards

| Task | Owner | Criteria | Due | Status |
|------|-------|----------|-----|--------|
| Separate API routing and logic | Merrick | #separationofconcerns | Dec 5 | ✅ |
| Double-check DB normalization | Merrick | #sql | Dec 5 | ✅ |
| Verify web standards usage | All | #webstandards | Dec 5 | ✅ |

#### Deployment

| Task | Owner | Soft Deadline | Hard Deadline | Status |
|------|-------|---------------|---------------|--------|
| Choose & implement deployment stack | Merrick | Dec 1 | Dec 5 | ✅ |

---

### Week 3: Dec 5–12 – App Finalization

**Goal:** Have the app functionally complete  
**Status:** ✅ Completed

#### Follow-up & Refinement

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Follow up on Taher's interview | Sophie | Dec 12 | ✅ |
| Follow up on TA interview | Sophie | Dec 12 | ✅ |
| Apply interview feedback | All | Dec 12 | ✅ |
| Adjust DB schema if necessary | Sophie | Dec 12 | ✅ |

#### Feature Completion

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Complete progress bar implementation | Rachael | Dec 12 | ✅ |
| Add onboarding/instructions | Autinn | Dec 12 | ✅ |
| Finalize frontend cleanup | Rachael | Dec 12 | ✅ |
| Finalize backend cleanup | Aldiyar | Dec 12 | ✅ |
| Separate API routing and logic | Taher | Dec 12 | ✅ |

#### Deployment & Documentation

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Complete deployment | Merrick | Dec 12 | ✅ |
| Swagger API documentation | Aldiyar | Dec 12 | ✅ |
| HC/LO folder structure finalization | All | Dec 12 | ✅ |

---

### Week 4: Dec 12–16 – Presentation & Polish

**Goal:** App ready for final evaluation  
**Status:** ✅ Completed

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Backend refactor | Taher, Merrick | Dec 16 | ✅ |
| 12-factor app implementation | Taher, Merrick | Dec 16 | ✅ |
| Finalize and merge all questions | Sophie | Dec 16 | ✅ |
| Finalize API documentation | Aldiyar | Dec 16 | ✅ |
| Film demo video | All | Dec 14 | ✅ |
| Edit demo video | Sophie | Dec 16 | ✅ |
| Individual submissions | All | Dec 16 | ✅ |

---

## 📊 Meeting Summary Statistics

| Metric | Count |
|--------|-------|
| Total Meetings | 9 |
| Full Team Meetings | 5 |
| Subteam Meetings | 4 |
| Date Range | Oct 10 — Dec 15, 2025 |
| Duration per Meeting | 45–70 minutes |
| Total Team Hours | ~50–60 hours |

---

## 🎯 Key Project Milestones

| Milestone | Date | Status |
|-----------|------|--------|
| Team formation + kickoff | Oct 10 | ✅ |
| Architecture finalized | Oct 24 | ✅ |
| First sprint complete | Oct 31 | ✅ |
| API integration complete | Nov 7 | ✅ |
| User testing round 1 | Nov 14 | ✅ |
| Feature freeze | Dec 5 | ✅ |
| Demo video filmed | Dec 14 | ✅ |
| Final submission | Dec 16 | ✅ |

---

**End of Project Tracking & Notes Document**

*For updates or corrections, see the [GitHub repository](https://github.com/autinn/gamify-hc) or contact the team.*

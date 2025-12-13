# Gamify-HC Frontend

A gamified learning platform for Habits of Mind and Foundational Concepts, built with React and Vitest.

## Quick Start

### With Docker (Recommended)

```bash
docker compose up
```

Frontend runs at: http://localhost:3000
Backend API at: http://localhost:5001

### Local Development

```bash
# Install dependencies
npm install

# Start development server
npm start
```

Opens at http://localhost:3000

## Available Scripts

```bash
npm start              # Development server on port 3000
npm run build          # Production build to `build/` folder
npm test               # Run all tests with Vitest
npm run test:ui        # Interactive test dashboard
npm run test:coverage  # Generate test coverage report
npm test -- --watch    # Watch mode for development
```

## Project Structure

```
src/
├── pages/              # 7 page components (Main, Login, Register, Course, Unit, Concept, Quiz)
├── components/         # Reusable UI components (common, course, unit, quiz, concept)
├── contexts/           # React Context providers (Onboarding)
├── hooks/              # 10 custom React hooks for state & logic
├── services/           # 8 API services (api.js + auth, course, unit, concept, quiz, progress, dataMappers)
├── __tests__/          # Test suite with Vitest setup
├── App.js              # Root component
└── index.js            # Entry point
```

## Architecture Overview

The Gamify-HC frontend uses a **layered architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────┐
│                    Pages (Route Components)              │
│  MainPage │ LoginPage │ CoursePage │ UnitPage │ QuizPage │
└────────────────────────┬────────────────────────────────┘
                         │ Use
┌────────────────────────▼────────────────────────────────┐
│              Custom React Hooks (State Logic)            │
│  useCourses │ useAuth │ useUnit │ useQuiz │ useProgress │
└────────────────────────┬────────────────────────────────┘
                         │ Call
┌────────────────────────▼────────────────────────────────┐
│            Services (API Communication)                  │
│  courseService │ authService │ quizService │ api.js     │
└────────────────────────┬────────────────────────────────┘
                         │ HTTP Requests
┌────────────────────────▼────────────────────────────────┐
│         Backend API (Flask - Port 5001)                  │
│  /api/auth │ /api/courses │ /api/units │ /api/quiz      │
└─────────────────────────────────────────────────────────┘
```

### How Data Flows Through the Architecture

#### 1. **Pages** - The UI Layer
Pages are route-based components that render the user interface. They compose custom hooks to manage state and display data.

**Key Pages:**
- `MainPage.js` - Dashboard showing all courses and global progress
- `LoginPage.js` / `RegisterPage.js` - Authentication
- `CoursePage.js` - Lists units in a course
- `UnitPage.js` - Shows concepts in a unit
- `QuizPage.js` - Quiz interface for answering questions

**Example Flow:**
```javascript
// MainPage.js
export default function MainPage() {
  const { courses, loading, error } = useCourses();
  const { globalProgress } = useProgress('global');
  
  return (
    <div>
      <h1>My Courses</h1>
      {courses.map(course => <CourseCard key={course.course_id} course={course} />)}
    </div>
  );
}
```

#### 2. **Custom Hooks** - The Business Logic Layer
Hooks encapsulate all state management, API communication, and data processing logic. This keeps pages clean and reusable.

**Hook Responsibilities:**
- Fetch data from services on mount
- Manage loading/error states
- Transform API responses into component-ready formats
- Handle user actions (submit, select, navigate)
- Provide state setters for UI interactions

**Key Hooks:**

| Hook | Purpose | Returns |
|------|---------|---------|
| `useCourses()` | Fetch all courses | `{ courses, loading, error }` |
| `useCourse(courseId)` | Fetch single course with units | `{ course, units, loading }` |
| `useUnit(courseId, unitId)` | Fetch unit with concepts | `{ unit, concepts, loading }` |
| `useConcept(courseId, unitId, conceptId)` | Fetch concept details | `{ concept, loading }` |
| `useQuiz(conceptId, unitId, courseId)` | Quiz state & handlers | `{ cards, score, handleNext, handleSelect }` |
| `useProgress(level)` | User progress metrics | `{ chartData, loading, refresh }` |
| `useAuth()` | Login/register logic | `{ login, register, loading, error }` |
| `useCurrentUser()` | Current user info | `{ user, loading, token }` |
| `useHeaderNavigation()` | Navigation structure | `{ courses, units, error }` |
| `useOnboarding()` | First-time user guide | `{ isFirstTime, startGuide, completeOnboarding }` |

**Example Hook:**
```javascript
// useQuiz.js
export function useQuiz(conceptId, unitId, courseId) {
  const [cards, setCards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [score, setScore] = useState(0);
  
  useEffect(() => {
    // Fetch quiz cards from API via quizService
    quizService.getQuizCards(conceptId).then(data => {
      setCards(quizService.shuffleAnswerOptions(data));
      setLoading(false);
    });
  }, [conceptId]);
  
  const handleSelect = (answer) => {
    // Submit answer via API, update score
    api.submitQuizAnswer({ answer_id: answer.id, ... });
    setScore(score + 1);
  };
  
  return { cards, loading, score, handleSelect };
}
```

#### 3. **Services** - The API Layer
Services handle all HTTP communication with the backend. They:
- Make API requests using fetch (via `api.js` wrapper)
- Transform API responses into frontend data structures
- Handle authentication tokens
- Manage error states

**Service Files (8 total):**

| Service | Endpoints | Purpose |
|---------|-----------|---------|
| `api.js` | All endpoints | Centralized HTTP client with auth & error handling |
| `authService.js` | `/api/auth/login`, `/api/auth/register` | User authentication & validation |
| `courseService.js` | `/api/courses`, `/api/courses/{id}` | Course data fetching |
| `unitService.js` | `/api/units`, `/api/units/{id}` | Unit and concept data |
| `quizService.js` | `/api/quiz` | Quiz card fetching & shuffling |
| `progressService.js` | `/api/progress` | User progress metrics |
| `conceptService.js` | `/api/concepts` | Concept details |
| `dataMappers.js` | (No API) | Data transformation utilities |

**Example Service:**
```javascript
// courseService.js
export async function fetchAllCourses() {
  const response = await api.getCourses(); // HTTP GET /api/courses
  return mapCoursesArray(response); // Transform to component format
}

export async function fetchCourseWithUnits(courseId) {
  const course = await api.getCourse(courseId);
  const units = await api.getCourseUnits(courseId);
  return { ...course, units }; // Combine related data
}
```

#### 4. **API Module** - The HTTP Client
`api.js` is a wrapper around Axios that handles:
- Setting authentication headers (JWT token from localStorage)
- Base URL configuration
- Error handling
- Response interceptors

**Example API Call:**
```javascript
// api.js
export async function getCourses() {
  const response = await axios.get('/api/courses', {
    headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
  });
  return response.data;
}
```

#### 5. **Data Transformation** - dataMappers.js
Services use data mappers to transform backend responses into component-expected formats:

```javascript
// dataMappers.js
export function mapCourseData(apiCourse) {
  return {
    course_id: apiCourse.id,           // Rename field
    title: apiCourse.name,              // Standardize format
    units: apiCourse.units || []        // Provide defaults
  };
}
```

## Complete Data Flow Example

**Scenario: User loads the MainPage dashboard**

```
1. LOAD MAINPAGE
   ↓
2. mainPage component mounts
   ↓
3. Calls two hooks:
   - useCourses()
   - useProgress('global')
   ↓
4. useCourses hook:
   - Sets loading = true
   - Calls courseService.fetchAllCourses()
   ↓
5. courseService:
   - Calls api.getCourses()
   - Makes HTTP GET /api/courses
   ↓
6. Backend API (Flask):
   - Queries database for user's courses
   - Returns: [{ id: 1, name: 'EA50', ... }, ...]
   ↓
7. courseService receives response:
   - Calls mapCoursesArray() to transform data
   - Returns: [{ course_id: 1, title: 'EA50', ... }, ...]
   ↓
8. Hook receives transformed data:
   - setLoading(false)
   - setCourses(transformedData)
   ↓
9. Component re-renders:
   - Displays courses in UI
   - Shows loading spinner gone
   - User sees dashboard
```

## Component Communication

**Props Flow (Down):**
```
MainPage
  ↓ passes course object
  ↓
CourseCard (component)
  ↓ passes course_id on click
  ↓
Navigation → CoursePage
```

**Data Flow (Up through Hooks):**
```
User clicks "Start Quiz"
  ↓
QuizPage mounts with conceptId
  ↓
useQuiz(conceptId) hook initializes
  ↓
Fetches quiz cards from API
  ↓
Returns { cards, score, handleSelect }
  ↓
QuizPage renders questions
```

## State Management Pattern

Gamify-HC uses **React Hooks for state** (no Redux/Context):

```javascript
// Local component state via hooks
const { courses, loading, error } = useCourses();
const { progress } = useProgress(courseId);
const { user } = useCurrentUser();
```

**Advantages:**
- Simpler, less boilerplate than Redux
- Direct API calls from hooks
- Co-located state and logic
- Easy to test (mock the services)

## Authentication Flow

```
1. User enters email/password on LoginPage
2. useAuth hook validates input
3. Calls authService.validateLoginForm()
4. Service calls api.login(email, password)
5. Backend verifies credentials
6. Returns JWT token
7. localStorage.setItem('token', response.access_token)
8. All future API calls include Authorization header
9. useCurrentUser() fetches user profile with token
10. Redirect to MainPage
```

## Onboarding System

New users are guided through an interactive onboarding tutorial that explains the platform's key features and navigation.

**How It Works:**

1. **First-Time Detection** — After login, `useOnboarding()` checks if the user has completed onboarding via `/api/users/{id}/onboarding`

2. **Onboarding Guide Trigger** — If `has_completed_onboarding` is false, `OnboardingGuide` component displays an interactive tutorial overlay

3. **Context Management** — `OnboardingContext` provides global access to onboarding state across all components:
   ```javascript
   const { isFirstTime, startGuide, completeOnboarding } = useOnboardingContext();
   ```

4. **Guide Completion** — When the user dismisses the guide, `completeOnboarding()` is called, which:
   - Updates backend via `api.updateOnboardingStatus(userId, true)`
   - Persists completion status to database
   - Prevents guide from showing again on future visits

5. **Components Involved:**
   - `OnboardingGuide.js` — Interactive tutorial component with step-by-step instructions
   - `OnboardingContext.js` — Global state provider for onboarding
   - `useOnboarding.js` — Hook managing onboarding lifecycle and API communication
   - `App.js` — Wraps app with `OnboardingProvider` and conditional `OnboardingGuide` rendering

**Key Features:**
- Non-intrusive overlay doesn't block core functionality
- Users can skip/dismiss at any time
- Only shown once per user (persistent via backend)
- Works seamlessly with authentication flow

## Error Handling

All services handle errors gracefully:

```javascript
// In useQuiz hook
useEffect(() => {
  quizService.getQuizCards(conceptId)
    .catch(error => {
      setError(`Failed to load quiz: ${error.message}`);
      setLoading(false);
    });
}, [conceptId]);
```

**Common Error Scenarios:**
- 401 Unauthorized → Redirect to login
- 404 Not Found → Show "Resource not found"
- 500 Server Error → Show "Server error, try again"
- Network timeout → Show "Connection lost"

## Technology Stack

- **React 19** - UI framework
- **React Router 7** - Client-side routing
- **Vitest** - Unit & integration test runner
- **React Testing Library** - Component testing utilities
- **Axios** - HTTP client (via api.js)

## Testing

The project has comprehensive test coverage across services, hooks, and pages.

```bash
npm test                  # Run all tests with watch mode
npm test -- --run         # Run once (CI mode)
npm run test:ui           # Interactive test dashboard
npm run test:coverage     # Generate coverage report
```

**Test Status: 146 tests passing (21 test files) ✅**

See [Testing.md](src/__tests__/Testing.md) for detailed testing architecture, patterns, and strategies.

## Backend Integration

The frontend communicates with the backend API at `/api`:
- Authentication: `/api/auth`
- Courses: `/api/courses`
- Units: `/api/units`
- Concepts: `/api/concepts`
- Quiz: `/api/quiz`
- Users: `/api/users`

See [Backend README](../backend/README.md) for API documentation.

## Development Tips

- Use `npm test -- --watch` for Test-Driven Development
- Mock API responses in tests with Vitest's `vi.mock()`
- Custom render function in `src/__tests__/testUtils.js` includes routing providers
- localStorage is mocked globally in `src/__tests__/setup.js`

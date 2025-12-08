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
├── hooks/              # 10 custom React hooks for state & logic
├── services/           # 7 API services (auth, course, unit, concept, quiz, progress, dataMappers)
├── __tests__/          # Test suite with Vitest setup
├── App.js              # Root component
└── index.js            # Entry point
```

## Technology Stack

- **React 19** - UI framework
- **React Router 7** - Client-side routing
- **Vitest** - Unit & integration test runner
- **React Testing Library** - Component testing utilities
- **Axios** - HTTP client (via api.js)

## Testing

See [Testing.md](src/__tests__/Testing.md) for comprehensive testing documentation.

**Test Structure:**
- Services (7): authService, courseService, unitService, conceptService, quizService, progressService, dataMappers
- Hooks (9): useAuth, useCourses, useCourse, useUnit, useConcept, useQuiz, useCurrentUser, useProgress, useHeaderNavigation, useGameification
- Pages (2): LoginPage, UnitPage (integration tests)
- Components: Quiz components

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

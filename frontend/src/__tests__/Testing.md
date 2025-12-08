# Frontend Testing Suite

This directory contains tests for the Gamify-HC frontend using **Vitest** and **React Testing Library**.

## Structure

```
src/__tests__/
├── setup.js              # Global test configuration (mocks localStorage, fetch)
├── testUtils.js          # Shared test utilities and custom render function
├── services/             # Service unit tests (7 files)
├── hooks/                # Hook unit tests (9 files)
├── pages/                # Page integration tests (5 files)
└── components/           # Component tests (quiz components)
```

## Running Tests

```bash
npm test              # Run all tests
npm run test:ui       # View with interactive UI dashboard
npm run test:coverage # Generate coverage report
npm test -- --watch   # Watch mode (auto-rerun on file changes)
npm test -- [file]    # Run specific test file
```

## Test Files

**Services (7)**: authService (19 tests), courseService (1), unitService (1), conceptService (1), quizService (18), progressService (12), dataMappers (5)

**Hooks (9)**: 
- useAuth (9 tests)
- useCourses (3 tests)
- useCourse (3 tests)
- useUnit (3 tests)
- useConcept (3 tests)
- useQuiz (13 tests)
- useCurrentUser (4 tests)
- useProgress (10 tests)
- useHeaderNavigation (12 tests)

**Pages (5)**: LoginPage (7 tests), UnitPage (5 tests), MainPage (5 tests), RegisterPage (7 tests), CoursePage (5 tests)

**Total: 21 test files, 146 tests, all passing ✅**

## Detailed Test Breakdown

### Services (7 test files, 59 tests)
Unit tests for API communication and data transformation.

- **authService.test.js (19 tests)** - Email/password/form validation
  - Email format and Minerva domain enforcement
  - Password strength validation
  - Username requirements
  - Complete form validation

- **quizService.test.js (18 tests)** - Quiz utilities
  - Answer shuffling and randomization
  - Quiz path navigation logic
  - Array handling edge cases

- **progressService.test.js (12 tests)** - Progress metrics
  - Global progress fetching
  - Course-level progress
  - Unit-level progress
  - Success rate calculations

- **dataMappers.test.js (5 tests)** - Data transformation
  - Course data mapping
  - Unit and concept mapping
  - Quiz card mapping

- **courseService, unitService, conceptService (1 test each)** - Service existence verification

### Hooks (9 test files, 70 tests)
Integration tests for hook state management and API integration.

- **useAuth.test.js (9 tests)** - Authentication
  - Login validation and API calls
  - Registration validation
  - Loading/error states

- **useQuiz.test.js (13 tests)** - Quiz state and interaction
  - Quiz card fetching
  - Answer submission and scoring
  - First correct answer tracking
  - Question navigation

- **useProgress.test.js (10 tests)** - Progress tracking
  - Global, course, unit, and concept level progress
  - Progress refresh functionality
  - Error handling

- **useHeaderNavigation.test.js (12 tests)** - Navigation structure
  - Course and unit fetching
  - Navigation data mapping
  - Error scenarios

- **useCourses.test.js (3 tests)**, **useCourse.test.js (3 tests)**, **useUnit.test.js (3 tests)**, **useConcept.test.js (3 tests)** - Data fetching hooks
  - Initial state
  - Loading states
  - Error handling

- **useCurrentUser.test.js (4 tests)** - User information
  - Current user fetching
  - Token handling
  - Missing token scenarios

### Pages (5 test files, 29 tests)
Integration tests verifying data flow from API to UI.

- **LoginPage.test.js (7 tests)** - Login validation
  - Email format validation
  - Minerva domain enforcement
  - Password requirements
  - Case-insensitive email handling

- **RegisterPage.test.js (7 tests)** - Registration form
  - Complete registration validation
  - Email domain restriction
  - Username requirements
  - Password strength and confirmation

- **MainPage.test.js (5 tests)** - Dashboard
  - Course fetching on mount
  - Global progress loading
  - Empty course lists
  - Error handling

- **CoursePage.test.js (5 tests)** - Course content
  - Course with units fetching
  - Course progress metrics
  - Empty course handling
  - Progress updates

- **UnitPage.test.js (5 tests)** - Unit content
  - Unit data fetching
  - Concept fetching
  - Composite data handling

## Testing Strategy

### Service Tests
Service tests mock the API layer and verify data transformation.

**Pattern:**
```javascript
vi.mock('../../services/api');
api.getCourses.mockResolvedValue([...]); // Mock API response
const result = await courseService.fetchAllCourses();
expect(result[0].course_id).toBe(1); // Verify transformation
```

**Focus Areas:**
- API request correctness
- Data transformation accuracy
- Error handling
- Edge cases (empty arrays, null values)

### Hook Tests
Hook tests mock services and verify state updates and side effects.

**Pattern:**
```javascript
vi.mock('../../services/courseService');
const { result } = renderHook(() => useCourses());
await waitFor(() => expect(result.current.loading).toBe(false));
expect(result.current.courses.length).toBe(2);
```

**Focus Areas:**
- State initialization
- Loading states during async operations
- Error state management
- Data updates after API calls
- User action handlers

### Page Tests
Page tests mock services and verify data integration in the UI.

**Pattern:**
```javascript
courseService.fetchAllCourses.mockResolvedValue([...]);
render(<MainPage />);
await waitFor(() => {
  expect(screen.getByText('Habits of Mind')).toBeInTheDocument();
});
```

**Focus Areas:**
- Data flow from hook to component
- Error message display
- Empty state handling
- User interactions
- Navigation

## Testing Setup

### Global Mocks (setup.js)
```javascript
// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
};
global.localStorage = localStorageMock;

// Mock fetch
global.fetch = vi.fn();
```

### Service Mocking Pattern
```javascript
import * as courseService from '../../services/courseService';
vi.mock('../../services/courseService');

// In tests:
courseService.fetchAllCourses.mockResolvedValue([...]);
```

### Custom Render with Providers
```javascript
// testUtils.js provides custom render with BrowserRouter
import { render } from '../testUtils';
render(<MainPage />); // Automatically wrapped with routing
```

## Common Test Patterns

### Async Operation Testing
```javascript
it('should fetch data on mount', async () => {
  service.fetch.mockResolvedValue(mockData);
  const { result } = renderHook(() => useHook());
  
  await waitFor(() => {
    expect(result.current.loading).toBe(false);
  });
  
  expect(result.current.data).toEqual(mockData);
});
```

### Error Handling Testing
```javascript
it('should handle API errors', async () => {
  const error = new Error('API failed');
  service.fetch.mockRejectedValue(error);
  
  const { result } = renderHook(() => useHook());
  
  await waitFor(() => {
    expect(result.current.error).toBeDefined();
  });
});
```

### Form Validation Testing
```javascript
it('should validate required fields', () => {
  const result = validateForm('', 'password');
  expect(result.valid).toBe(false);
  expect(result.error).toContain('required');
});
```

## Coverage

Run coverage reports with:
```bash
npm run test:coverage
```

Coverage is configured to exclude:
- `node_modules/`
- `src/__tests__/` (test files themselves)
- `src/setupTests.js`
- `src/reportWebVitals.js`
- `src/index.js`

View the HTML report in `coverage/index.html`

## Writing Tests

### Unit Test Example (Service)
```javascript
import { describe, it, expect, vi } from 'vitest';
import { validateEmail } from '../../../services/authService';

describe('authService', () => {
  it('should validate minerva emails', () => {
    const result = validateEmail('user@minerva.edu');
    expect(result.valid).toBe(true);
  });
});
```

### Hook Test Example
```javascript
import { renderHook, waitFor } from '@testing-library/react';
import { useCourses } from '../../../hooks/useCourses';
import * as api from '../../../services/api';
import { vi } from 'vitest';

vi.mock('../../../services/api');

describe('useCourses', () => {
  it('should fetch courses', async () => {
    api.getCourses.mockResolvedValueOnce({
      success: true,
      courses: [{ id: 1, name: 'Test Course' }]
    });
    
    const { result } = renderHook(() => useCourses());
    
    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
    
    expect(result.current.courses).toHaveLength(1);
  });
});
```

### Page Test Example (Integration)
```javascript
import { screen, waitFor } from '@testing-library/react';
import { render } from '../testUtils';
import LoginPage from '../../../pages/LoginPage';
import * as authService from '../../../services/authService';
import { vi } from 'vitest';

vi.mock('../../../services/authService');

describe('LoginPage', () => {
  it('should render login form', async () => {
    authService.validateEmail.mockReturnValue({ valid: true });
    
    render(<LoginPage />);
    
    await waitFor(() => {
      expect(screen.getByText('Login')).toBeInTheDocument();
    });
  });
});
```

## Test Utilities

**setup.js**:
- Global `localStorage` mock with `getItem`, `setItem`, `removeItem`, `clear`
- Global `fetch` mock
- jest-dom matchers for DOM assertions

**testUtils.js**:
- `render()` - Custom render with BrowserRouter provider for routing tests
- Mock API utilities
- Test data helpers

## Common Patterns

### Mocking API Calls
```javascript
import { vi } from 'vitest';
import * as api from '../services/api';

vi.mock('../services/api');

// In your test:
api.getCourses.mockResolvedValueOnce({ success: true, courses: [] });
```

### Testing Async Hooks
```javascript
import { renderHook, waitFor } from '@testing-library/react';

const { result } = renderHook(() => useMyHook());

await waitFor(() => {
  expect(result.current.loading).toBe(false);
});
```

### Testing Component Renders
```javascript
import { render } from '../testUtils';
import { screen } from '@testing-library/react';

render(<MyComponent />);

expect(screen.getByText('Expected Text')).toBeInTheDocument();
expect(screen.getByRole('button', { name: /submit/i })).toBeEnabled();
```

## Coverage

Run coverage with:
```bash
npm run test:coverage
```

Coverage excludes:
- `node_modules/`
- `src/__tests__/`
- `src/setupTests.js`
- `src/reportWebVitals.js`
- `src/index.js`

View HTML report in `coverage/` folder.

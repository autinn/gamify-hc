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

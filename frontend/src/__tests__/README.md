# Frontend Testing Suite

This directory contains tests for the Gamify-HC frontend using **Vitest** and **React Testing Library**.

## Structure

```
src/__tests__/
├── setup.js              # Global test configuration
├── testUtils.js          # Shared test utilities and mocks
├── services/             # Service unit tests (7 files)
├── hooks/                # Hook unit tests (8 files)
└── pages/                # Page integration tests (5 files)
```

## Running Tests

```bash
npm test              # Run all tests
npm run test:ui       # View with UI dashboard
npm run test:coverage # Generate coverage report
npm test -- --watch   # Watch mode
```

## Test Coverage

**Frontend unit & component tests** provide fast feedback during development and catch regressions early.

**Full end-to-end integration tests** are handled in the CI/CD pipeline via Docker Compose, which starts both frontend and backend services and validates the complete system workflow. See `.github/workflows/ci.yaml` for details.

## Test Files

**Services (7)**: authService, dataMappers, courseService, unitService, conceptService, progressService, quizService

**Hooks (8)**: useAuth, useCourses, useCourse, useUnit, useConcept, useQuiz, useCurrentUser, useProgress

**Pages (5)**: LoginPage, RegisterPage, CoursePage, UnitPage, MainPage

## Writing Tests

### Unit Test Example
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

vi.mock('../../../services/api');

describe('useCourses', () => {
  it('should fetch courses', async () => {
    api.getCourses.mockResolvedValueOnce(mockApiResponses.courses);
    const { result } = renderHook(() => useCourses());
    
    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });
});
```

### Page Test Example
```javascript
import { screen, waitFor } from '@testing-library/react';
import { render } from '../../testUtils';
import MainPage from '../../../pages/MainPage';

describe('MainPage', () => {
  it('should render user greeting', async () => {
    api.getCourses.mockResolvedValueOnce(mockApiResponses.courses);
    render(<MainPage />);
    
    await waitFor(() => {
      expect(screen.getByText('testuser')).toBeInTheDocument();
    });
  });
});
```

## Utilities

**mockApiCall()** - Mock successful API responses
**mockApiError()** - Mock API errors
**mockLocalStorage()** - Set up localStorage state
**render()** - Custom render with BrowserRouter provider

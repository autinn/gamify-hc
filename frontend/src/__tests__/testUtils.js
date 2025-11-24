/**
 * Test Utilities & Helpers
 * 
 * Shared utilities for testing:
 * - Custom render function with providers
 * - Mock API functions
 * - Test data builders
 */

import React from 'react';
import { render as rtlRender } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';

/**
 * Custom render function that includes providers (Router, etc)
 */
export function render(ui, options = {}) {
  function Wrapper({ children }) {
    return (
      <BrowserRouter>
        {children}
      </BrowserRouter>
    );
  }

  return rtlRender(ui, { wrapper: Wrapper, ...options });
}

// Re-export everything from React Testing Library
export * from '@testing-library/react';

/**
 * Mock API Responses
 */
export const mockApiResponses = {
  courses: [
    {
      course_id: 1,
      course_code: 'CS101',
      course_name: 'Intro to CS',
      title: 'Intro to CS',
      units: []
    },
    {
      course_id: 2,
      course_code: 'CS201',
      course_name: 'Data Structures',
      title: 'Data Structures',
      units: []
    }
  ],

  units: [
    {
      unit_id: 1,
      unit_code: 'CS101-U1',
      unit_name: 'Basics',
      title: 'Basics',
      concepts: []
    }
  ],

  concepts: [
    {
      concept_id: 1,
      concept_code: 'CS101-C1',
      concept_name: 'Variables',
      title: 'Variables'
    }
  ],

  quizCards: [
    {
      id: 1,
      question: 'What is a variable?',
      answers: [
        { id: 1, answer_text: 'Storage for data', is_correct: true, explanation: 'Correct!' },
        { id: 2, answer_text: 'A function', is_correct: false, explanation: 'Incorrect' }
      ]
    }
  ],

  user: {
    user_id: 1,
    username: 'testuser',
    email: 'test@minerva.edu',
    created_at: '2024-01-01T00:00:00'
  },

  loginResponse: {
    access_token: 'mock-jwt-token',
    user_id: 1,
    email: 'test@minerva.edu',
    username: 'testuser'
  }
};

/**
 * Mock localStorage helper
 */
export function mockLocalStorage(data = {}) {
  const defaultData = {
    token: 'mock-jwt-token',
    user_id: '1',
    user_email: 'test@minerva.edu',
    user_username: 'testuser',
    ...data
  };

  localStorage.getItem.mockImplementation(key => defaultData[key] || null);
  localStorage.setItem.mockImplementation((key, value) => {
    defaultData[key] = value;
  });

  return defaultData;
}

/**
 * Mock API fetch responses
 */
export function mockApiCall(endpoint, response, options = {}) {
  const { status = 200, headers = {} } = options;

  global.fetch.mockResolvedValueOnce({
    ok: status >= 200 && status < 300,
    status,
    json: async () => response,
    headers
  });
}

/**
 * Mock API error
 */
export function mockApiError(endpoint, error, status = 400) {
  global.fetch.mockResolvedValueOnce({
    ok: false,
    status,
    json: async () => ({ error })
  });
}

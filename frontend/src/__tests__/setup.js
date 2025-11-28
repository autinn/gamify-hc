/**
 * Test Setup File
 * 
 * Configuration and utilities for all tests using Vitest
 * - Mock localStorage
 * - Mock API responses
 * - Setup testing-library matchers
 */

import '@testing-library/jest-dom';
import { vi, beforeEach } from 'vitest';

// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
};

global.localStorage = localStorageMock;

// Reset mocks before each test
beforeEach(() => {
  localStorage.getItem.mockClear();
  localStorage.setItem.mockClear();
  localStorage.removeItem.mockClear();
  localStorage.clear.mockClear();
});

// Mock fetch globally
global.fetch = vi.fn();

// Reset fetch mock before each test
beforeEach(() => {
  fetch.mockClear();
});

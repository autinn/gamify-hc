/**
 * Test Setup File - Global Configuration for Vitest
 * 
 * This file is loaded before all tests and provides:
 * 1. Testing Library matchers (jest-dom)
 * 2. localStorage mock with real data persistence
 * 3. Fetch API mock for HTTP requests
 * 4. Test cleanup between test cases
 * 
 * Used by: All test files in src/__tests__/
 * Configuration: vitest.config.js (setupFiles field)
 */

import '@testing-library/jest-dom';
import { vi, beforeEach } from 'vitest';

// ============================================================================
// localStorage Mock with Real Data Persistence
// ============================================================================
/**
 * Creates a localStorage mock that maintains data across calls within a single test.
 * Unlike empty vi.fn() mocks, this actually stores and retrieves values.
 * 
 * Implementation:
 * - Encapsulates a `store` object to hold key-value pairs
 * - All operations (get/set/remove/clear) are spyable with vi.fn()
 * - Data persists across multiple calls within one test
 * - Cleared automatically by beforeEach hook before each test
 * 
 * Usage in tests:
 *   localStorage.setItem('token', 'abc123');
 *   expect(localStorage.getItem('token')).toBe('abc123');
 */
const localStorageMock = (() => {
  let store = {};

  return {
    /**
     * Retrieves value from mock storage
     * @param {string} key - Storage key
     * @returns {string|null} - Stored value or null if key doesn't exist
     */
    getItem: vi.fn((key) => {
      return store[key] || null;
    }),

    /**
     * Stores key-value pair in mock storage
     * @param {string} key - Storage key
     * @param {*} value - Value to store (converted to string)
     */
    setItem: vi.fn((key, value) => {
      store[key] = String(value);
    }),

    /**
     * Removes key from mock storage
     * @param {string} key - Storage key to remove
     */
    removeItem: vi.fn((key) => {
      delete store[key];
    }),

    /**
     * Clears all data from mock storage
     */
    clear: vi.fn(() => {
      store = {};
    }),
  };
})();

global.localStorage = localStorageMock;

// ============================================================================
// Test Cleanup Hooks
// ============================================================================
/**
 * Reset localStorage and fetch mocks before each test
 * Ensures tests are isolated and don't affect each other
 */
beforeEach(() => {
  // Clear storage data and reset all spy tracking
  localStorage.clear();
  localStorage.getItem.mockClear();
  localStorage.setItem.mockClear();
  localStorage.removeItem.mockClear();
  localStorage.clear.mockClear();
});

// ============================================================================
// Fetch API Mock
// ============================================================================
/**
 * Global fetch mock for intercepting HTTP requests in tests
 * 
 * Usage in tests:
 *   fetch.mockResolvedValue({ ok: true, json: async () => ({...}) });
 *   const response = await fetch('/api/users');
 */
global.fetch = vi.fn();

/**
 * Reset fetch mock before each test to prevent mock state leaking
 */
beforeEach(() => {
  fetch.mockClear();
});

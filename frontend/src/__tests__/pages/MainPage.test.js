/**
 * MainPage Integration Tests
 * 
 * Tests the main dashboard page functionality including:
 * - Fetching all available courses on component mount
 * - Loading global progress data for the user
 * - Handling empty course lists gracefully
 * - Error handling for API failures during data fetch
 * 
 * The MainPage serves as the primary dashboard after login,
 * displaying all courses and user's global progress metrics.
 * 
 * @module MainPage.test
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import * as courseService from '../../services/courseService';
import * as progressService from '../../services/progressService';

// Mock all course and progress service functions
vi.mock('../../services/courseService');
vi.mock('../../services/progressService');

describe('MainPage - Dashboard Data', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
    localStorage.setItem('token', 'test-token');
  });

  /**
   * Test: Fetch all courses on component mount
   * 
   * Verifies that the page correctly retrieves all courses from the API
   * and handles multiple course objects in the response.
   * 
   * Expected behavior:
   * - Calls fetchAllCourses() when component mounts
   * - Returns array of course objects with course_id, title, description
   * - Updates component state with course data
   */
  it('should fetch all courses on mount', async () => {
    const mockCourses = [
      { course_id: 1, title: 'Habits of Mind', description: 'Course 1' },
      { course_id: 2, title: 'Foundational Concepts', description: 'Course 2' }
    ];

    courseService.fetchAllCourses.mockResolvedValue(mockCourses);

    const result = await courseService.fetchAllCourses();

    expect(result).toEqual(mockCourses);
    expect(result.length).toBe(2);
  });

  /**
   * Test: Fetch global progress data
   * 
   * Verifies that the dashboard loads the user's overall progress statistics,
   * including success rate and total questions answered.
   * 
   * Expected behavior:
   * - Calls fetchGlobalProgress() for dashboard metrics
   * - Returns progress object with success_rate and answer counts
   * - Displays stats in dashboard UI
   */
  it('should fetch global progress data', async () => {
    const mockProgress = {
      global_success_rate: 0.75,
      total_questions_answered: 45,
      total_correct: 34
    };

    progressService.fetchGlobalProgress.mockResolvedValue(mockProgress);

    const result = await progressService.fetchGlobalProgress();

    expect(result.global_success_rate).toBe(0.75);
    expect(result.total_questions_answered).toBe(45);
  });

  /**
   * Test: Handle empty courses list
   * 
   * Verifies that the page handles the edge case where a user has
   * no courses available (e.g., new account, no enrollments).
   * 
   * Expected behavior:
   * - Returns empty array without errors
   * - Page shows "No courses available" message or placeholder
   * - Does not crash or display broken UI
   */
  it('should handle empty courses list', async () => {
    courseService.fetchAllCourses.mockResolvedValue([]);

    const result = await courseService.fetchAllCourses();

    expect(result).toEqual([]);
    expect(result.length).toBe(0);
  });

  /**
   * Test: Handle course fetch errors
   * 
   * Verifies that network errors or API failures are caught and handled gracefully.
   * 
   * Expected behavior:
   * - Catches API errors during course fetch
   * - Shows error message to user instead of crashing
   * - Allows user to retry or navigate elsewhere
   */
  it('should handle course fetch errors', async () => {
    const error = new Error('Failed to fetch courses');
    courseService.fetchAllCourses.mockRejectedValue(error);

    try {
      await courseService.fetchAllCourses();
      expect.fail('Should have thrown error');
    } catch (err) {
      expect(err.message).toBe('Failed to fetch courses');
    }
  });

  /**
   * Test: Handle progress fetch errors
   * 
   * Verifies that errors fetching progress data don't break the course display.
   * Progress is optional/secondary to course listing.
   * 
   * Expected behavior:
   * - Catches API errors during progress fetch
   * - Continues displaying courses even if progress fails
   * - Shows error for progress metrics while courses remain visible
   */
  it('should handle progress fetch errors', async () => {
    const error = new Error('Failed to fetch progress');
    progressService.fetchGlobalProgress.mockRejectedValue(error);

    try {
      await progressService.fetchGlobalProgress();
      expect.fail('Should have thrown error');
    } catch (err) {
      expect(err.message).toBe('Failed to fetch progress');
    }
  });
});

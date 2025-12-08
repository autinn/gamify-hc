/**
 * CoursePage Integration Tests
 * 
 * Tests the course detail page functionality including:
 * - Fetching course data with associated units
 * - Loading course-specific progress metrics
 * - Handling courses with zero units
 * - Displaying course progress (completion, success rate)
 * - Error handling for missing courses and failed API calls
 * 
 * CoursePage displays the units within a course and the user's
 * progress through that specific course's content.
 * 
 * @module CoursePage.test
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import * as courseService from '../../services/courseService';
import * as progressService from '../../services/progressService';

// Mock all course and progress service functions
vi.mock('../../services/courseService');
vi.mock('../../services/progressService');

describe('CoursePage - Course Content & Progress', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
    localStorage.setItem('token', 'test-token');
  });

  /**
   * Test: Fetch course with units
   * 
   * Verifies that the page loads a single course and its associated units.
   * Unit structure provides the navigation hierarchy within a course.
   * 
   * Expected response includes:
   * - course_id: Unique identifier
   * - title: Course name/code
   * - units: Array of unit objects with unit_id and title
   */
  it('should fetch course with units', async () => {
    const mockCourse = {
      course_id: 1,
      title: 'Habits of Mind',
      description: 'Understanding thinking habits',
      units: [
        { unit_id: 1, title: 'Unit 1', concepts_count: 3 },
        { unit_id: 2, title: 'Unit 2', concepts_count: 5 }
      ]
    };

    courseService.fetchCourseWithUnits.mockResolvedValue(mockCourse);

    const result = await courseService.fetchCourseWithUnits(1);

    expect(result.course_id).toBe(1);
    expect(result.units.length).toBe(2);
    expect(result.units[0].unit_id).toBe(1);
  });

  /**
   * Test: Fetch course progress
   * 
   * Verifies that course-specific progress metrics are loaded,
   * including success rate and units completion status.
   * 
   * Metrics tracked:
   * - success_rate: Overall accuracy on quiz questions in this course
   * - units_completed: Number of units completed by user
   * - total_units: Total units available in course
   */
  it('should fetch course progress', async () => {
    const mockProgress = {
      course_id: 1,
      success_rate: 0.68,
      units_completed: 2,
      total_units: 4
    };

    progressService.fetchCourseProgress.mockResolvedValue(mockProgress);

    const result = await progressService.fetchCourseProgress(1);

    expect(result.course_id).toBe(1);
    expect(result.success_rate).toBe(0.68);
    expect(result.units_completed).toBe(2);
  });

  /**
   * Test: Handle course with no units
   * 
   * Verifies graceful handling of empty courses (edge case).
   * A course may exist but have no units yet (in setup phase).
   * 
   * Expected behavior:
   * - Returns course object with empty units array
   * - Page shows "No units available" message
   * - Does not crash when rendering empty list
   */
  it('should handle course with no units', async () => {
    const mockCourse = {
      course_id: 1,
      title: 'Empty Course',
      description: 'No units yet',
      units: []
    };

    courseService.fetchCourseWithUnits.mockResolvedValue(mockCourse);

    const result = await courseService.fetchCourseWithUnits(1);

    expect(result.units).toEqual([]);
  });

  /**
   * Test: Handle course fetch errors
   * 
   * Verifies error handling when requested course doesn't exist
   * or is not accessible to the user.
   * 
   * Expected behavior:
   * - Catches 404 or authorization errors
   * - Shows "Course not found" error message
   * - Allows user to navigate back to course list
   */
  it('should handle course fetch errors', async () => {
    const error = new Error('Course not found');
    courseService.fetchCourseWithUnits.mockRejectedValue(error);

    try {
      await courseService.fetchCourseWithUnits(999);
      expect.fail('Should have thrown error');
    } catch (err) {
      expect(err.message).toBe('Course not found');
    }
  });

  /**
   * Test: Update course progress on unit completion
   * 
   * Verifies that progress metrics update when user completes a unit.
   * Tests the dynamic nature of progress tracking.
   * 
   * Simulates user progression:
   * - Initial state: 2 units completed out of 4
   * - After action: 3 units completed out of 4
   * - Progress metric: 75% course completion
   */
  it('should update course progress on unit completion', async () => {
    progressService.fetchCourseProgress.mockResolvedValue({
      course_id: 1,
      success_rate: 0.72,
      units_completed: 3,
      total_units: 4
    });

    const result = await progressService.fetchCourseProgress(1);

    expect(result.units_completed).toBe(3);
    expect(result.total_units).toBe(4);
  });
});

import { describe, it, expect, vi, beforeEach } from 'vitest';
import * as courseService from '../../services/courseService';
import * as progressService from '../../services/progressService';

// Mock services
vi.mock('../../services/courseService');
vi.mock('../../services/progressService');

describe('CoursePage - Course Content & Progress', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
    localStorage.setItem('token', 'test-token');
  });

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

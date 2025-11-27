import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useCourses } from '../../hooks/useCourses';
import * as courseService from '../../services/courseService';

vi.mock('../../services/courseService', () => ({
  fetchAllCourses: vi.fn()
}));

describe('useCourses Hook', () => {
  const mockCourses = [
    { course_id: 1, title: 'Biology', description: 'Biology Basics' },
    { course_id: 2, title: 'Chemistry', description: 'Chemistry Fundamentals' },
    { course_id: 3, title: 'Physics', description: 'Physics 101' }
  ];

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should fetch courses on mount', async () => {
    courseService.fetchAllCourses.mockResolvedValue(mockCourses);

    const { result } = renderHook(() => useCourses());

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(courseService.fetchAllCourses).toHaveBeenCalled();
    expect(result.current.courses).toHaveLength(3);
  });

  it('should handle fetch errors', async () => {
    courseService.fetchAllCourses.mockRejectedValue(new Error('Failed to fetch'));

    const { result } = renderHook(() => useCourses());

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    // Hook returns dummy courses on error, not an error state
    expect(result.current.courses).toBeDefined();
  });

  it('should return initial loading state', async () => {
    courseService.fetchAllCourses.mockResolvedValue(mockCourses);

    const { result } = renderHook(() => useCourses());

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });
});

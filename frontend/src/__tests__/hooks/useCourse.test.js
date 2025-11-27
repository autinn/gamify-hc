import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useCourse } from '../../hooks/useCourse';
import * as courseService from '../../services/courseService';

vi.mock('../../services/courseService', () => ({
  fetchCourseWithUnits: vi.fn()
}));

describe('useCourse Hook', () => {
  const mockCourse = {
    id: 1,
    name: 'Biology 101',
    units: [
      { id: 1, name: 'Unit 1' },
      { id: 2, name: 'Unit 2' }
    ]
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should fetch course on mount', async () => {
    courseService.fetchCourseWithUnits.mockResolvedValue({ course: mockCourse, units: [] });

    const { result } = renderHook(() => useCourse(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(courseService.fetchCourseWithUnits).toHaveBeenCalledWith(1);
    expect(result.current.course).toEqual(mockCourse);
  });

  it('should handle fetch errors', async () => {
    courseService.fetchCourseWithUnits.mockRejectedValue(new Error('Failed to fetch'));

    const { result } = renderHook(() => useCourse(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.error).toBeTruthy();
    expect(result.current.course).toBeNull();
  });

  it('should have initial loading state', async () => {
    courseService.fetchCourseWithUnits.mockResolvedValue({ course: mockCourse, units: [] });

    const { result } = renderHook(() => useCourse(1));

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });
});


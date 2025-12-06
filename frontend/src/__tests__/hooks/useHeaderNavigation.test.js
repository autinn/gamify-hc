import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, waitFor } from '@testing-library/react';
import { useHeaderNavigation } from '../../hooks/useHeaderNavigation';
import * as api from '../../services/api';

vi.mock('../../services/api');

describe('useHeaderNavigation Hook', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Course fetching', () => {
    it('should fetch courses on mount', async () => {
      const mockCourses = [
        { id: 1, name: 'EA50' },
        { id: 2, name: 'FA50' },
        { id: 3, name: 'MC50' }
      ];

      api.getCourses.mockResolvedValue(mockCourses);
      api.getCourseUnits.mockResolvedValue([]);

      const { result } = renderHook(() => useHeaderNavigation());

      expect(result.current.loading).toBe(true);

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(api.getCourses).toHaveBeenCalled();
      expect(result.current.courses).toHaveLength(3);
      expect(result.current.courses[0]).toEqual({ id: 1, label: 'EA50' });
    });

    it('should map course data correctly', async () => {
      const mockCourses = [
        { course_id: 1, code: 'EA50' },
        { course_id: 2, title: 'FA50' }
      ];

      api.getCourses.mockResolvedValue(mockCourses);
      api.getCourseUnits.mockResolvedValue([]);

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.courses).toEqual([
        { id: 1, label: 'EA50' },
        { id: 2, label: 'FA50' }
      ]);
    });

    it('should handle empty courses array', async () => {
      api.getCourses.mockResolvedValue([]);

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.courses).toEqual([]);
      expect(result.current.courseUnits).toEqual({});
    });
  });

  describe('Unit fetching', () => {
    it('should fetch units for each course', async () => {
      const mockCourses = [
        { id: 1, name: 'EA50' },
        { id: 2, name: 'FA50' }
      ];

      const mockUnits = [
        { id: 1, name: 'Unit 1' },
        { id: 2, name: 'Unit 2' }
      ];

      api.getCourses.mockResolvedValue(mockCourses);
      api.getCourseUnits.mockResolvedValue(mockUnits);

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(api.getCourseUnits).toHaveBeenCalledWith(1);
      expect(api.getCourseUnits).toHaveBeenCalledWith(2);
      expect(result.current.courseUnits[1]).toHaveLength(2);
      expect(result.current.courseUnits[2]).toHaveLength(2);
    });

    it('should map unit data correctly', async () => {
      const mockCourses = [{ id: 1, name: 'EA50' }];
      const mockUnits = [
        { unit_id: 1, title: 'Unit 1' },
        { unit_id: 2, name: 'Unit 2' }
      ];

      api.getCourses.mockResolvedValue(mockCourses);
      api.getCourseUnits.mockResolvedValue(mockUnits);

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.courseUnits[1]).toEqual([
        { id: 1, name: 'Unit 1' },
        { id: 2, name: 'Unit 2' }
      ]);
    });

    it('should handle unit fetch failure gracefully', async () => {
      const mockCourses = [
        { id: 1, name: 'EA50' },
        { id: 2, name: 'FA50' }
      ];

      api.getCourses.mockResolvedValue(mockCourses);
      api.getCourseUnits.mockImplementation((courseId) => {
        if (courseId === 1) {
          return Promise.resolve([{ id: 1, name: 'Unit 1' }]);
        }
        return Promise.reject(new Error('Failed to fetch units'));
      });

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      // Course 1 should have units, course 2 should have empty array
      expect(result.current.courseUnits[1]).toHaveLength(1);
      expect(result.current.courseUnits[2]).toEqual([]);
    });
  });

  describe('Error handling', () => {
    it('should handle course fetch error', async () => {
      api.getCourses.mockRejectedValue(new Error('API Error'));

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.error).toBe('API Error');
      expect(result.current.courses).toEqual([]);
      expect(result.current.courseUnits).toEqual({});
    });

    it('should handle invalid courses data format', async () => {
      api.getCourses.mockResolvedValue('not an array');

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.error).toBe('Invalid courses data format');
      expect(result.current.courses).toEqual([]);
    });

    it('should set error to null on success', async () => {
      const mockCourses = [{ id: 1, name: 'EA50' }];

      api.getCourses.mockResolvedValue(mockCourses);
      api.getCourseUnits.mockResolvedValue([]);

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.error).toBeNull();
    });
  });

  describe('Loading state', () => {
    it('should start with loading true', () => {
      api.getCourses.mockImplementation(
        () => new Promise(() => {}) // Never resolves
      );

      const { result } = renderHook(() => useHeaderNavigation());

      expect(result.current.loading).toBe(true);
    });

    it('should set loading to false after fetch completes', async () => {
      api.getCourses.mockResolvedValue([]);

      const { result } = renderHook(() => useHeaderNavigation());

      expect(result.current.loading).toBe(true);

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });
    });
  });

  describe('Return value structure', () => {
    it('should return correct structure', async () => {
      api.getCourses.mockResolvedValue([]);

      const { result } = renderHook(() => useHeaderNavigation());

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current).toHaveProperty('courses');
      expect(result.current).toHaveProperty('courseUnits');
      expect(result.current).toHaveProperty('loading');
      expect(result.current).toHaveProperty('error');
    });
  });
});

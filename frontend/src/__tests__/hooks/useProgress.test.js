import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useProgress } from '../../hooks/useProgress';
import * as progressService from '../../services/progressService';

vi.mock('../../services/progressService', () => ({
  fetchGlobalProgress: vi.fn(),
  fetchCourseProgress: vi.fn(),
  fetchUnitProgress: vi.fn(),
  fetchConceptProgress: vi.fn()
}));

describe('useProgress Hook', () => {
  const mockChartData = {
    labels: ['Item 1', 'Item 2', 'Item 3'],
    values: [10, 15, 8],
    metadata: { type: 'test', timestamp: Date.now() }
  };

  const emptyChartData = {
    labels: [],
    values: [],
    metadata: { error: true, timestamp: Date.now() }
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('global level', () => {
    it('should fetch global progress on mount', async () => {
      progressService.fetchGlobalProgress.mockResolvedValue(mockChartData);

      const { result } = renderHook(() => useProgress('global'));

      expect(result.current.loading).toBe(true);

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(progressService.fetchGlobalProgress).toHaveBeenCalled();
      expect(result.current.chartData).toEqual(mockChartData);
    });

    it('should handle errors gracefully', async () => {
      progressService.fetchGlobalProgress.mockRejectedValue(new Error('API error'));

      const { result } = renderHook(() => useProgress('global'));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.error).toBeTruthy();
      expect(result.current.chartData.metadata.error).toBe(true);
    });
  });

  describe('course level', () => {
    it('should fetch course progress with courseId', async () => {
      progressService.fetchCourseProgress.mockResolvedValue(mockChartData);

      const { result } = renderHook(() => useProgress('course', 1));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(progressService.fetchCourseProgress).toHaveBeenCalledWith(1);
      expect(result.current.chartData).toEqual(mockChartData);
    });

    it('should refetch when courseId changes', async () => {
      progressService.fetchCourseProgress.mockResolvedValue(mockChartData);

      const { result, rerender } = renderHook(
        ({ levelType, levelId }) => useProgress(levelType, levelId),
        { initialProps: { levelType: 'course', levelId: 1 } }
      );

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(progressService.fetchCourseProgress).toHaveBeenCalledWith(1);

      rerender({ levelType: 'course', levelId: 2 });

      await waitFor(() => {
        expect(progressService.fetchCourseProgress).toHaveBeenCalledWith(2);
      });
    });
  });

  describe('unit level', () => {
    it('should fetch unit progress with courseId and unitId', async () => {
      progressService.fetchUnitProgress.mockResolvedValue(mockChartData);

      const { result } = renderHook(() => useProgress('unit', 1, 1));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(progressService.fetchUnitProgress).toHaveBeenCalledWith(1, 1);
      expect(result.current.chartData).toEqual(mockChartData);
    });
  });

  describe('concept level', () => {
    it('should fetch concept progress with all IDs', async () => {
      progressService.fetchConceptProgress.mockResolvedValue(mockChartData);

      const { result } = renderHook(() => useProgress('concept', 1, 1));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(progressService.fetchConceptProgress).toHaveBeenCalledWith(1, 1, 1);
      expect(result.current.chartData).toEqual(mockChartData);
    });
  });

  describe('refresh function', () => {
    it('should allow manual refresh of progress data', async () => {
      progressService.fetchGlobalProgress.mockResolvedValue(mockChartData);

      const { result } = renderHook(() => useProgress('global'));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(progressService.fetchGlobalProgress).toHaveBeenCalledTimes(1);

      act(() => {
        result.current.refresh();
      });

      await waitFor(() => {
        expect(progressService.fetchGlobalProgress).toHaveBeenCalledTimes(2);
      });
    });

    it('should update chartData after refresh', async () => {
      const initialData = {
        labels: ['A', 'B'],
        values: [5, 10],
        metadata: { type: 'test' }
      };

      const updatedData = {
        labels: ['A', 'B', 'C'],
        values: [5, 10, 15],
        metadata: { type: 'test' }
      };

      progressService.fetchGlobalProgress.mockResolvedValueOnce(initialData);

      const { result } = renderHook(() => useProgress('global'));

      await waitFor(() => {
        expect(result.current.chartData).toEqual(initialData);
      });

      progressService.fetchGlobalProgress.mockResolvedValueOnce(updatedData);

      act(() => {
        result.current.refresh();
      });

      await waitFor(() => {
        expect(result.current.chartData).toEqual(updatedData);
      });
    });
  });

  describe('invalid level type', () => {
    it('should handle unknown level type', async () => {
      const { result } = renderHook(() => useProgress('invalid'));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.error).toBeTruthy();
      expect(result.current.chartData.metadata.error).toBe(true);
    });
  });

  describe('initial state', () => {
    it('should have correct initial state', () => {
      const { result } = renderHook(() => useProgress('global'));

      expect(result.current.loading).toBe(true);
      expect(result.current.error).toBe(null);
      expect(result.current.chartData).toEqual({
        labels: [],
        values: [],
        metadata: {}
      });
    });
  });
});

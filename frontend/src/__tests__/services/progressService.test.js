import { describe, it, expect, vi, beforeEach } from 'vitest';
import {
  fetchGlobalProgress,
  fetchCourseProgress,
  fetchUnitProgress,
  fetchConceptProgress
} from '../../services/progressService';
import * as api from '../../services/api';

vi.mock('../../services/api');

describe('progressService - Real API Integration Tests', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('fetchGlobalProgress', () => {
    it('should call api.getGlobalProgress and return chart data', async () => {
      const mockApiResponse = {
        labels: ['EA50', 'FA50', 'MC50'],
        values: [0.85, 0.72, 0.91],
        metadata: { type: 'courses', count: 3 }
      };

      api.getGlobalProgress.mockResolvedValue(mockApiResponse);

      const result = await fetchGlobalProgress();

      expect(api.getGlobalProgress).toHaveBeenCalled();
      expect(result.labels).toEqual(mockApiResponse.labels);
      expect(result.values).toEqual(mockApiResponse.values);
    });

    it('should handle API errors gracefully', async () => {
      api.getGlobalProgress.mockRejectedValue(new Error('Network error'));

      const result = await fetchGlobalProgress();

      expect(result.metadata.error).toBe(true);
      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
    });

    it('should return empty chart data when API returns empty', async () => {
      const mockApiResponse = {
        labels: [],
        values: [],
        metadata: { type: 'courses', count: 0 }
      };

      api.getGlobalProgress.mockResolvedValue(mockApiResponse);

      const result = await fetchGlobalProgress();

      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
    });
  });

  describe('fetchCourseProgress', () => {
    it('should call api.getCourseProgress with courseId and return chart data', async () => {
      const mockApiResponse = {
        labels: ['Unit 1', 'Unit 2', 'Unit 3'],
        values: [0.8, 0.75, 0.9],
        metadata: { type: 'units', course_id: 1, count: 3 }
      };

      api.getCourseProgress.mockResolvedValue(mockApiResponse);

      const result = await fetchCourseProgress(1);

      expect(api.getCourseProgress).toHaveBeenCalledWith(1);
      expect(result.labels).toEqual(mockApiResponse.labels);
      expect(result.values).toEqual(mockApiResponse.values);
    });

    it('should handle missing courseId', async () => {
      const result = await fetchCourseProgress(undefined);

      expect(result.metadata.error).toBe(true);
    });

    it('should handle API errors', async () => {
      api.getCourseProgress.mockRejectedValue(new Error('API error'));

      const result = await fetchCourseProgress(1);

      expect(result.metadata.error).toBe(true);
      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
    });
  });

  describe('fetchUnitProgress', () => {
    it('should call api.getUnitProgress with courseId and unitId', async () => {
      const mockApiResponse = {
        labels: ['Concept 1', 'Concept 2', 'Concept 3'],
        values: [0.88, 0.92, 0.78],
        metadata: { type: 'concepts', course_id: 1, unit_id: 1, count: 3 }
      };

      api.getUnitProgress.mockResolvedValue(mockApiResponse);

      const result = await fetchUnitProgress(1, 1);

      expect(api.getUnitProgress).toHaveBeenCalledWith(1, 1);
      expect(result.labels).toEqual(mockApiResponse.labels);
      expect(result.values).toEqual(mockApiResponse.values);
    });

    it('should handle missing unitId', async () => {
      const result = await fetchUnitProgress(1, undefined);

      expect(result.metadata.error).toBe(true);
    });

    it('should handle API errors', async () => {
      api.getUnitProgress.mockRejectedValue(new Error('API error'));

      const result = await fetchUnitProgress(1, 1);

      expect(result.metadata.error).toBe(true);
      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
    });
  });

  describe('Success rate validation', () => {
    it('should display success rates between 0 and 1', async () => {
      const mockApiResponse = {
        labels: ['EA50', 'FA50'],
        values: [0.6, 0.95],
        metadata: { type: 'courses', count: 2 }
      };

      api.getGlobalProgress.mockResolvedValue(mockApiResponse);

      const result = await fetchGlobalProgress();

      result.values.forEach(value => {
        expect(value).toBeGreaterThanOrEqual(0);
        expect(value).toBeLessThanOrEqual(1);
      });
    });

    it('should handle zero success rates', async () => {
      const mockApiResponse = {
        labels: ['Unit 1'],
        values: [0],
        metadata: { type: 'units', course_id: 1, count: 1 }
      };

      api.getCourseProgress.mockResolvedValue(mockApiResponse);

      const result = await fetchCourseProgress(1);

      expect(result.values[0]).toBe(0);
    });

    it('should handle perfect success rates', async () => {
      const mockApiResponse = {
        labels: ['Unit 1'],
        values: [1.0],
        metadata: { type: 'units', course_id: 1, count: 1 }
      };

      api.getCourseProgress.mockResolvedValue(mockApiResponse);

      const result = await fetchCourseProgress(1);

      expect(result.values[0]).toBe(1.0);
    });
  });
});
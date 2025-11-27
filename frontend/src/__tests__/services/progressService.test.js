import { describe, it, expect, vi, beforeEach } from 'vitest';
import {
  fetchGlobalProgress,
  fetchCourseProgress,
  fetchUnitProgress,
  fetchConceptProgress
} from '../../services/progressService';
import * as courseService from '../../services/courseService';
import * as unitService from '../../services/unitService';
import * as conceptService from '../../services/conceptService';

vi.mock('../../services/courseService');
vi.mock('../../services/unitService');
vi.mock('../../services/conceptService');

describe('progressService', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('fetchGlobalProgress', () => {
    it('should fetch all courses and return chart data', async () => {
      const mockCourses = [
        { course_id: 1, title: 'EA50' },
        { course_id: 2, title: 'FA50' },
        { course_id: 3, title: 'MC50' }
      ];

      courseService.fetchAllCourses.mockResolvedValue(mockCourses);

      const result = await fetchGlobalProgress();

      expect(result.labels).toEqual(['EA50', 'FA50', 'MC50']);
      expect(result.values).toHaveLength(3);
      expect(result.metadata.type).toBe('global');
      expect(result.metadata.count).toBe(3);
    });

    it('should return empty chart data when no courses exist', async () => {
      courseService.fetchAllCourses.mockResolvedValue([]);

      const result = await fetchGlobalProgress();

      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
      expect(result.metadata.error).toBe(true);
    });

    it('should return empty chart data on error', async () => {
      courseService.fetchAllCourses.mockRejectedValue(new Error('API error'));

      const result = await fetchGlobalProgress();

      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
      expect(result.metadata.error).toBe(true);
    });
  });

  describe('fetchCourseProgress', () => {
    it('should fetch units for a course and return chart data', async () => {
      const mockResponse = {
        course: { course_id: 1, title: 'EA50' },
        units: [
          { unit_id: 1, title: 'Unit 1', order_index: 0 },
          { unit_id: 2, title: 'Unit 2', order_index: 1 }
        ]
      };

      courseService.fetchCourseWithUnits.mockResolvedValue(mockResponse);

      const result = await fetchCourseProgress(1);

      expect(result.labels).toContain('Unit 1');
      expect(result.labels).toContain('Unit 2');
      expect(result.values).toHaveLength(2);
      expect(result.metadata.type).toBe('course');
      expect(result.metadata.courseId).toBe(1);
    });

    it('should return empty chart data when no units exist', async () => {
      const mockResponse = {
        course: { course_id: 1, title: 'EA50' },
        units: []
      };

      courseService.fetchCourseWithUnits.mockResolvedValue(mockResponse);

      const result = await fetchCourseProgress(1);

      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
    });

    it('should return empty chart data on error', async () => {
      courseService.fetchCourseWithUnits.mockRejectedValue(new Error('API error'));

      const result = await fetchCourseProgress(1);

      expect(result.metadata.error).toBe(true);
    });
  });

  describe('fetchUnitProgress', () => {
    it('should fetch concepts for a unit and return chart data', async () => {
      const mockResponse = {
        course: { course_id: 1, title: 'EA50' },
        unit: { unit_id: 1, title: 'Unit 1' },
        concepts: [
          { concept_id: 1, title: 'Problem Solving' },
          { concept_id: 2, title: 'Analysis' }
        ]
      };

      unitService.fetchCourseUnitWithConcepts.mockResolvedValue(mockResponse);

      const result = await fetchUnitProgress(1, 1);

      expect(result.labels).toContain('Problem Solving');
      expect(result.labels).toContain('Analysis');
      expect(result.values).toHaveLength(2);
      expect(result.metadata.type).toBe('unit');
      expect(result.metadata.courseId).toBe(1);
      expect(result.metadata.unitId).toBe(1);
    });

    it('should return empty chart data when no concepts exist', async () => {
      const mockResponse = {
        course: { course_id: 1, title: 'EA50' },
        unit: { unit_id: 1, title: 'Unit 1' },
        concepts: []
      };

      unitService.fetchCourseUnitWithConcepts.mockResolvedValue(mockResponse);

      const result = await fetchUnitProgress(1, 1);

      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
    });

    it('should return empty chart data on error', async () => {
      unitService.fetchCourseUnitWithConcepts.mockRejectedValue(new Error('API error'));

      const result = await fetchUnitProgress(1, 1);

      expect(result.metadata.error).toBe(true);
    });
  });

  describe('fetchConceptProgress', () => {
    it('should fetch quiz cards for a concept and return chart data', async () => {
      const mockResponse = {
        course: { course_id: 1, title: 'EA50' },
        unit: { unit_id: 1, title: 'Unit 1' },
        concept: { concept_id: 1, title: 'Problem Solving' },
        quizCards: [
          { quiz_card_id: 1, question: 'Q1' },
          { quiz_card_id: 2, question: 'Q2' },
          { quiz_card_id: 3, question: 'Q3' }
        ]
      };

      conceptService.fetchConceptWithAllData.mockResolvedValue(mockResponse);

      const result = await fetchConceptProgress(1, 1, 1);

      expect(result.labels).toHaveLength(3);
      expect(result.values).toHaveLength(3);
      expect(result.metadata.type).toBe('concept');
      expect(result.metadata.courseId).toBe(1);
      expect(result.metadata.unitId).toBe(1);
      expect(result.metadata.conceptId).toBe(1);
    });

    it('should return empty chart data when no quiz cards exist', async () => {
      const mockResponse = {
        course: { course_id: 1, title: 'EA50' },
        unit: { unit_id: 1, title: 'Unit 1' },
        concept: { concept_id: 1, title: 'Problem Solving' },
        quizCards: []
      };

      conceptService.fetchConceptWithAllData.mockResolvedValue(mockResponse);

      const result = await fetchConceptProgress(1, 1, 1);

      expect(result.labels).toEqual([]);
      expect(result.values).toEqual([]);
    });

    it('should return empty chart data on error', async () => {
      conceptService.fetchConceptWithAllData.mockRejectedValue(new Error('API error'));

      const result = await fetchConceptProgress(1, 1, 1);

      expect(result.metadata.error).toBe(true);
    });
  });
});

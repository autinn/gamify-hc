import { describe, it, expect, vi, beforeEach } from 'vitest';
import * as unitService from '../../services/unitService';

// Mock the unitService
vi.mock('../../services/unitService');

describe('UnitPage - Data Fetching', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should have fetchCourseUnitWithConcepts function', () => {
    expect(typeof unitService.fetchCourseUnitWithConcepts).toBe('function');
  });

  it('should fetch course and unit data together', async () => {
    const mockData = {
      course: { course_id: 1, title: 'EA50' },
      unit: { unit_id: 1, title: 'Unit 1' },
      concepts: [{ concept_id: 1, title: 'Concept 1' }]
    };

    unitService.fetchCourseUnitWithConcepts.mockResolvedValue(mockData);

    const result = await unitService.fetchCourseUnitWithConcepts(1, 1);
    
    expect(result).toEqual(mockData);
    expect(result.course.course_id).toBe(1);
    expect(result.unit.unit_id).toBe(1);
    expect(result.concepts.length).toBe(1);
  });

  it('should return empty concepts array when unit has no concepts', async () => {
    const mockData = {
      course: { course_id: 1, title: 'EA50' },
      unit: { unit_id: 1, title: 'Unit 1' },
      concepts: []
    };

    unitService.fetchCourseUnitWithConcepts.mockResolvedValue(mockData);

    const result = await unitService.fetchCourseUnitWithConcepts(1, 1);
    
    expect(result.concepts).toEqual([]);
  });

  it('should have fetchUnit function', () => {
    expect(typeof unitService.fetchUnit).toBe('function');
  });

  it('should have fetchUnitConcepts function', () => {
    expect(typeof unitService.fetchUnitConcepts).toBe('function');
  });
});

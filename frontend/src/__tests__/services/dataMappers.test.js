import { describe, it, expect } from 'vitest';
import {
  mapCourseData,
  mapUnitData,
  mapConceptData,
  mapQuizCardData
} from '../../services/dataMappers';

describe('dataMappers', () => {
  describe('mapCourseData', () => {
    it('should map course API response to component format', () => {
      const apiCourse = {
        id: 1,
        code: 'CS101',
        name: 'Intro to Computer Science',
        description: 'Introduction to computer science fundamentals'
      };

      const mapped = mapCourseData(apiCourse);

      expect(mapped.course_id).toBe(1);
      expect(mapped.title).toBe('Intro to Computer Science');
      expect(mapped.description).toBe('Introduction to computer science fundamentals');
    });

    it('should handle courses with units', () => {
      const apiCourse = {
        id: 1,
        code: 'CS101',
        name: 'Intro to CS',
        description: 'Basic computer science',
        units: [
          { id: 1, name: 'Basics', course_id: 1, description: 'Unit 1' }
        ]
      };

      const mapped = mapCourseData(apiCourse);

      expect(mapped.course_id).toBe(1);
      expect(mapped.title).toBe('Intro to CS');
    });
  });

  describe('mapUnitData', () => {
    it('should map unit API response to component format', () => {
      const apiUnit = {
        id: 1,
        name: 'Unit 1: Basics',
        course_id: 1,
        description: 'Basic concepts',
        order_index: 1
      };

      const mapped = mapUnitData(apiUnit);

      expect(mapped.unit_id).toBe(1);
      expect(mapped.course_id).toBe(1);
      expect(mapped.title).toBe('Unit 1: Basics');
      expect(mapped.description).toBe('Basic concepts');
    });
  });

  describe('mapConceptData', () => {
    it('should map concept API response to component format', () => {
      const apiConcept = {
        id: 1,
        name: 'Variables',
        unit_id: 1,
        definition: 'Named storage for data values'
      };

      const mapped = mapConceptData(apiConcept);

      expect(mapped.concept_id).toBe(1);
      expect(mapped.unit_id).toBe(1);
      expect(mapped.title).toBe('Variables');
      expect(mapped.definition).toBe('Named storage for data values');
    });
  });

  describe('mapQuizCardData', () => {
    it('should map quiz card API response to component format', () => {
      const apiCard = {
        id: 1,
        question: 'What is a variable?',
        answers: [
          { id: 1, answer_text: 'Storage for data', is_correct: true },
          { id: 2, answer_text: 'A function', is_correct: false }
        ]
      };

      const mapped = mapQuizCardData(apiCard);

      expect(mapped.text).toBe('What is a variable?');
      expect(mapped.options).toHaveLength(2);
      expect(mapped.options[0].text).toBe('Storage for data');
    });
  });
});

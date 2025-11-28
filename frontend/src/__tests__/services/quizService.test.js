import { describe, it, expect } from 'vitest';
import {
  getQuizBackPath,
  shuffleArray
} from '../../services/quizService';

describe('quizService', () => {
  describe('getQuizBackPath', () => {
    it('should return concept path when conceptId provided', () => {
      const path = getQuizBackPath(1, 2, 3);
      expect(path).toBe('/course/1/unit/2/concept/3');
    });

    it('should return unit path when only unitId provided', () => {
      const path = getQuizBackPath(1, 2);
      expect(path).toBe('/course/1/unit/2');
    });

    it('should return course path when only courseId provided', () => {
      const path = getQuizBackPath(1);
      expect(path).toBe('/course/1');
    });

    it('should return home path when no IDs provided', () => {
      const path = getQuizBackPath();
      expect(path).toBe('/');
    });
  });

  describe('shuffleArray', () => {
    it('should shuffle array of questions', () => {
      const questions = [
        { id: 1, text: 'Q1' },
        { id: 2, text: 'Q2' },
        { id: 3, text: 'Q3' }
      ];

      const shuffled = shuffleArray(questions);

      expect(shuffled).toHaveLength(3);
      expect(shuffled).toEqual(expect.arrayContaining(questions));
    });

    it('should return empty array for empty input', () => {
      const shuffled = shuffleArray([]);
      expect(shuffled).toEqual([]);
    });
  });
});

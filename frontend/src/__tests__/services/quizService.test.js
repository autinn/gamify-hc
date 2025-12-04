import { describe, it, expect } from 'vitest';
import {
  getQuizBackPath,
  shuffleArray,
  shuffleAnswerOptions
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

  describe('shuffleAnswerOptions', () => {
    it('should return an array', () => {
      const options = ['A', 'B', 'C', 'D'];
      const result = shuffleAnswerOptions(options);

      expect(Array.isArray(result)).toBe(true);
    });

    it('should preserve all options when shuffling', () => {
      const options = ['Answer A', 'Answer B', 'Answer C', 'Answer D'];
      const result = shuffleAnswerOptions(options);

      expect(result).toHaveLength(options.length);
      expect(result).toEqual(expect.arrayContaining(options));
    });

    it('should handle single element array', () => {
      const options = ['Only Option'];
      const result = shuffleAnswerOptions(options);

      expect(result).toEqual(['Only Option']);
    });

    it('should handle two element array', () => {
      const options = ['A', 'B'];
      const result = shuffleAnswerOptions(options);

      expect(result).toHaveLength(2);
      expect(result).toEqual(expect.arrayContaining(options));
    });

    it('should handle empty array', () => {
      const options = [];
      const result = shuffleAnswerOptions(options);

      expect(result).toEqual([]);
    });

    it('should not modify the original array', () => {
      const options = ['A', 'B', 'C', 'D'];
      const originalOptions = [...options];
      const result = shuffleAnswerOptions(options);

      expect(options).toEqual(originalOptions);
      expect(result).not.toBe(options);
    });

    it('should randomize order (statistical test)', () => {
      const options = ['A', 'B', 'C', 'D'];
      const results = [];

      // Shuffle multiple times
      for (let i = 0; i < 20; i++) {
        results.push(shuffleAnswerOptions(options).join(''));
      }

      // Check that we got different orderings (high probability)
      const uniqueResults = new Set(results);
      expect(uniqueResults.size).toBeGreaterThan(1);
    });

    it('should handle objects in array', () => {
      const options = [
        { id: 1, text: 'Option A' },
        { id: 2, text: 'Option B' },
        { id: 3, text: 'Option C' }
      ];
      const result = shuffleAnswerOptions(options);

      expect(result).toHaveLength(3);
      expect(result).toEqual(expect.arrayContaining(options));
    });

    it('should handle numbers in array', () => {
      const options = [1, 2, 3, 4, 5];
      const result = shuffleAnswerOptions(options);

      expect(result).toHaveLength(5);
      expect(result).toEqual(expect.arrayContaining(options));
    });

    it('should work with strings containing special characters', () => {
      const options = ['Option-A', 'Option_B', 'Option.C', 'Option/D'];
      const result = shuffleAnswerOptions(options);

      expect(result).toHaveLength(4);
      expect(result).toEqual(expect.arrayContaining(options));
    });

    it('should handle large arrays', () => {
      const options = Array.from({ length: 100 }, (_, i) => `Option ${i}`);
      const result = shuffleAnswerOptions(options);

      expect(result).toHaveLength(100);
      expect(result).toEqual(expect.arrayContaining(options));
    });

    it('should handle array with duplicate values', () => {
      const options = ['A', 'B', 'A', 'C', 'B'];
      const result = shuffleAnswerOptions(options);

      expect(result).toHaveLength(5);
      expect(result.filter(x => x === 'A')).toHaveLength(2);
      expect(result.filter(x => x === 'B')).toHaveLength(2);
      expect(result.filter(x => x === 'C')).toHaveLength(1);
    });
  });
});

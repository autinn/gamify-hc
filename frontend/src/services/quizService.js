/**
 * Quiz Service
 * 
 * Business logic for quiz-related data fetching, transformations, and utilities.
 * Handles quiz level detection, shuffling, and navigation.
 */

import * as api from './api';
import { mapQuizCardsArray } from './dataMappers';

/**
 * Fetch quiz cards based on level (course, unit, or concept)
 * @param {number} courseId - Course ID (optional)
 * @param {number} unitId - Unit ID (optional)
 * @param {number} conceptId - Concept ID (optional)
 * @returns {Promise<Array>} Array of mapped quiz cards
 * @throws {Error} If no valid quiz level provided
 */
export async function fetchQuizByLevel(courseId, unitId, conceptId) {
  let quizCards;

  if (conceptId) {
    quizCards = await api.getConceptQuizCards(parseInt(conceptId, 10));
  } else if (unitId) {
    quizCards = await api.getUnitQuizCards(parseInt(unitId, 10));
  } else if (courseId) {
    quizCards = await api.getCourseQuizCards(parseInt(courseId, 10));
  } else {
    throw new Error('No valid quiz level provided (courseId, unitId, or conceptId required)');
  }

  return mapQuizCardsArray(quizCards);
}

/**
 * Shuffle array of items randomly
 * @param {Array} array - Array to shuffle
 * @returns {Array} New shuffled array
 */
export function shuffleArray(array) {
  return [...array].sort(() => Math.random() - 0.5);
}

/**
 * Get back navigation path based on quiz context
 * @param {number} courseId - Course ID
 * @param {number} unitId - Unit ID (optional)
 * @param {number} conceptId - Concept ID (optional)
 * @returns {string} Navigation path
 */
export function getQuizBackPath(courseId, unitId, conceptId) {
  if (conceptId) {
    return `/course/${courseId}/unit/${unitId}/concept/${conceptId}`;
  } else if (unitId) {
    return `/course/${courseId}/unit/${unitId}`;
  } else if (courseId) {
    return `/course/${courseId}`;
  }
  return '/';
}

/**
 * Calculate quiz results percentage
 * @param {number} correctCount - Number of correct answers
 * @param {number} totalCount - Total number of questions
 * @returns {number} Percentage (0-100)
 */
export function calculateQuizPercentage(correctCount, totalCount) {
  if (totalCount === 0) return 0;
  return Math.round((correctCount / totalCount) * 100);
}

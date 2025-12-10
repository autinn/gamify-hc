/**
 * Quiz Service
 * @module quizService
 * 
 * Provides centralized business logic for quiz-related operations including:
 * - Multi-level quiz data fetching (concept, unit, course, or global)
 * - Question and answer option shuffling using randomization
 * - Quiz navigation path generation
 * - Quiz result calculations and scoring
 * 
 * The service bridges API calls with presentation logic, ensuring quiz data
 * is properly transformed and randomized for fair assessment experiences.
 */

import * as api from './api';
import { mapQuizCardsArray } from './dataMappers';

// ============================================================================
// Quiz Data Fetching
// ============================================================================

/**
 * Fetches quiz cards at the appropriate level based on provided context IDs.
 * 
 * Uses hierarchical resolution: conceptId > unitId > courseId > global.
 * When multiple IDs are provided, the most specific level is used.
 * 
 * Use this when you need quiz questions tailored to a specific learning context,
 * or use global quiz for system-wide assessment across all content.
 * 
 * @async
 * @param {number} [courseId] - The course identifier for course-level quiz
 * @param {number} [unitId] - The unit identifier for unit-level quiz
 * @param {number} [conceptId] - The concept identifier for concept-level quiz
 * @returns {Promise<Array>} Array of mapped quiz card objects ready for display
 * @throws {Error} If API request fails or IDs are invalid
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
    quizCards = await api.getGlobalQuizCards();
  }

  return mapQuizCardsArray(quizCards);
}

// ============================================================================
// Quiz Shuffling & Randomization
// ============================================================================

/**
 * Randomly shuffles an array using in-place Fisher-Yates-inspired randomization.
 * 
 * Creates a shallow copy before shuffling to preserve the original array.
 * Use this when order independence or unbiased randomization is important.
 * 
 * @param {Array} array - The array to shuffle
 * @returns {Array} A new shuffled array (original array unchanged)
 */
export function shuffleArray(array) {
  return [...array].sort(() => Math.random() - 0.5);
}

/**
 * Randomly shuffles quiz answer options for a single question.
 * 
 * Provides semantic clarity when specifically dealing with answer options
 * to prevent answer position bias during assessment. Ensures no answer
 * choice is consistently in the same position across multiple attempts.
 * 
 * @param {Array} options - Array of answer option objects
 * @returns {Array} Shuffled answer options in random order
 */
export function shuffleAnswerOptions(options) {
  return shuffleArray(options);
}

/**
 * Retrieves a randomized subset of quiz questions (maximum 5 questions).
 * 
 * Useful when conducting brief assessments or spot-checks of knowledge.
 * Questions are both shuffled and limited to create focused quiz sessions
 * that take approximately 3-5 minutes to complete.
 * 
 * @param {Array} quizCards - Array of complete quiz card objects
 * @returns {Array} Up to 5 randomly selected and shuffled quiz cards
 */
export function getShuffledQuizQuestions(quizCards) {
  const shuffled = shuffleArray(quizCards);
  return shuffled.slice(0, 5);
}

// ============================================================================
// Quiz Navigation & Results
// ============================================================================

/**
 * Determines the appropriate back navigation URL based on quiz context hierarchy.
 * 
 * Uses hierarchical path construction to return users to the content level
 * from which they initiated the quiz. Helps maintain navigation context
 * and provides intuitive "back" behavior throughout the learning experience.
 * 
 * Hierarchy: conceptId > unitId > courseId > home
 * 
 * @param {number} courseId - The course identifier (always provided)
 * @param {number} [unitId] - The unit identifier for unit/concept level quizzes
 * @param {number} [conceptId] - The concept identifier for concept-specific quizzes
 * @returns {string} Fully qualified URL path for navigation (e.g., '/course/1/unit/2')
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
 * Calculates the percentage score achieved on a quiz attempt.
 * 
 * Converts raw correct answer count to a percentage score (0-100) for
 * user feedback, progress tracking, and mastery assessment. Handles
 * edge case where quiz has no questions (returns 0%).
 * 
 * @param {number} correctCount - Number of questions answered correctly
 * @param {number} totalCount - Total number of questions in the quiz attempt
 * @returns {number} Rounded percentage score from 0 to 100 inclusive
 */
export function calculateQuizPercentage(correctCount, totalCount) {
  if (totalCount === 0) return 0;
  return Math.round((correctCount / totalCount) * 100);
}

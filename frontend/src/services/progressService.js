/**
 * Progress Service - User progress data fetching and aggregation
 *
 * Fetches user progress at different levels (global, course, unit, concept).
 * Returns standardized chart data format with labels, values, and metadata.
 * Includes error handling with graceful fallbacks to empty state.
 *
 * @module progressService
 */

import * as api from './api';

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

/**
 * Get empty chart data structure for graceful error handling
 *
 * Returns a standardized empty chart format when data is unavailable,
 * preventing null/undefined errors in chart components.
 *
 * @returns {Object} Empty chart data {labels: [], values: [], metadata: {error: true}}
 */
function getEmptyChartData() {
  return {
    labels: [],
    values: [],
    metadata: {
      timestamp: Date.now(),
      error: true
    }
  };
}

// ============================================================================
// GLOBAL PROGRESS
// ============================================================================

/**
 * Fetch global progress across all courses
 *
 * Aggregates success rates for all courses user is enrolled in.
 *
 * @async
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>} Chart data with course labels and success rates
 *
 * @example
 * const { labels, values } = await fetchGlobalProgress();
 * // labels: ['EA50', 'FA50', 'MC50', 'CX50']
 * // values: [0.75, 0.82, 0.68, 0.91]
 */
export async function fetchGlobalProgress() {
  try {
    const data = await api.getGlobalProgress();
    return {
      labels: data.labels || [],
      values: data.values || [],
      metadata: data.metadata || {}
    };
  } catch (err) {
    console.error('Error fetching global progress:', err);
    return getEmptyChartData();
  }
}

// ============================================================================
// COURSE PROGRESS
// ============================================================================

/**
 * Fetch progress for all units in a course
 *
 * Aggregates success rates for all units within a specific course.
 * Used to display unit-level progress on CoursePage.
 *
 * @async
 * @param {number} courseId - The course ID
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>} Chart data with unit labels and success rates
 *
 * @example
 * const { labels, values } = await fetchCourseProgress(1);
 * // labels: ['Unit 1: Problem-Solving', 'Unit 2: Analysis', ...]
 * // values: [0.75, 0.82, ...]
 */
export async function fetchCourseProgress(courseId) {
  try {
    if (!courseId) {
      return getEmptyChartData();
    }

    const data = await api.getCourseProgress(courseId);
    return {
      labels: data.labels || [],
      values: data.values || [],
      metadata: data.metadata || {}
    };
  } catch (err) {
    console.error('Error fetching course progress:', err);
    return getEmptyChartData();
  }
}

// ============================================================================
// UNIT PROGRESS
// ============================================================================

/**
 * Fetch progress for all concepts in a unit
 *
 * Aggregates success rates for all concepts within a specific unit.
 * Used to display concept-level progress on UnitPage.
 *
 * @async
 * @param {number} courseId - The parent course ID
 * @param {number} unitId - The unit ID
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>} Chart data with concept labels and success rates
 *
 * @example
 * const { labels, values } = await fetchUnitProgress(1, 2);
 * // labels: ['Concept A', 'Concept B', ...]
 * // values: [0.75, 0.82, ...]
 */
export async function fetchUnitProgress(courseId, unitId) {
  try {
    if (!courseId || !unitId) {
      return getEmptyChartData();
    }

    const data = await api.getUnitProgress(courseId, unitId);
    return {
      labels: data.labels || [],
      values: data.values || [],
      metadata: data.metadata || {}
    };
  } catch (err) {
    console.error('Error fetching unit progress:', err);
    return getEmptyChartData();
  }
}

// ============================================================================
// CONCEPT PROGRESS
// ============================================================================

/**
 * Fetch progress for all quiz cards in a concept
 *
 * Returns concept-level progress data. Currently returns empty data structure
 * but can be expanded to track individual quiz card success rates.
 * Used to display quiz card progress on ConceptPage.
 *
 * @async
 * @param {number} courseId - The parent course ID
 * @param {number} unitId - The parent unit ID
 * @param {number} conceptId - The concept ID
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>} Chart data with quiz labels and success rates
 *
 * @example
 * const { labels, values } = await fetchConceptProgress(1, 2, 3);
 * // labels: ['Quiz Card 1', 'Quiz Card 2', ...]
 * // values: [1, 0.5, ...] // 1 = correct, 0 = incorrect, 0.5 = partial
 */
export async function fetchConceptProgress(courseId, unitId, conceptId) {
  try {
    if (!courseId || !unitId || !conceptId) {
      return getEmptyChartData();
    }

    // Return empty data for concept level - can be expanded for individual quiz card progress
    return {
      labels: [],
      values: [],
      metadata: {
        type: 'concept',
        courseId,
        unitId,
        conceptId,
        timestamp: Date.now()
      }
    };
  } catch (err) {
    console.error('Error fetching concept progress:', err);
    return getEmptyChartData();
  }
}

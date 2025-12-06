/**
 * Progress Service
 * 
 * Handles fetching user progress data from the backend API.
 * Returns chart data aggregated by courses, units, or concepts.
 */

import * as api from './api';

/**
 * Fetch global progress (all courses)
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>}
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

/**
 * Fetch course progress (all units in a course)
 * @param {number} courseId - Course ID
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>}
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

/**
 * Fetch unit progress (all concepts in a unit)
 * @param {number} courseId - Course ID
 * @param {number} unitId - Unit ID
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>}
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

/**
 * Fetch concept progress (quiz cards for a concept)
 * @param {number} courseId - Course ID
 * @param {number} unitId - Unit ID
 * @param {number} conceptId - Concept ID
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>}
 */
export async function fetchConceptProgress(courseId, unitId, conceptId) {
  try {
    if (!courseId || !unitId || !conceptId) {
      return getEmptyChartData();
    }

    // For now, return empty data for concept level
    // This could be expanded to show individual quiz card progress
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

/**
 * Helper: Return empty chart data
 * @returns {object} Empty chart data structure
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

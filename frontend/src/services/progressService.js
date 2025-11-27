/**
 * Progress Service
 * 
 * Handles fetching and transforming user progress data at different levels:
 * - Global: All courses
 * - Course: All units in a course
 * - Unit: All concepts in a unit
 * - Concept: Quiz cards for a concept
 * 
 * Returns standardized chart data format with labels and values.
 */

import { fetchAllCourses, fetchCourseWithUnits } from './courseService';
import { fetchCourseUnitWithConcepts } from './unitService';
import { fetchConceptWithAllData } from './conceptService';

/**
 * Fetch global progress (all courses)
 * @returns {Promise<{labels: string[], values: number[], metadata: object}>}
 */
export async function fetchGlobalProgress() {
  try {
    const courses = await fetchAllCourses();
    
    if (!courses || courses.length === 0) {
      return getEmptyChartData();
    }

    return {
      labels: courses.map(c => c.title),
      values: courses.map(() => Math.floor(Math.random() * 21)), // 0-20 questions
      metadata: {
        type: 'global',
        count: courses.length,
        timestamp: Date.now()
      }
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

    const courseIdInt = parseInt(courseId, 10);
    const { units } = await fetchCourseWithUnits(courseIdInt);

    if (!units || units.length === 0) {
      return getEmptyChartData();
    }

    // Sort units by order_index
    const sortedUnits = [...units].sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

    return {
      labels: sortedUnits.map((u) => {
        // order_index is 0-based in DB, so add 1 for display
        if (u.order_index !== undefined && u.order_index !== null) {
          return `Unit ${u.order_index + 1}`;
        }
        return u.title;
      }),
      values: sortedUnits.map(() => Math.floor(Math.random() * 21)), // 0-20 questions
      metadata: {
        type: 'course',
        courseId: courseIdInt,
        count: sortedUnits.length,
        timestamp: Date.now()
      }
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

    const courseIdInt = parseInt(courseId, 10);
    const unitIdInt = parseInt(unitId, 10);
    const { concepts } = await fetchCourseUnitWithConcepts(courseIdInt, unitIdInt);

    if (!concepts || concepts.length === 0) {
      return getEmptyChartData();
    }

    return {
      labels: concepts.map(c => c.title),
      values: concepts.map(() => Math.floor(Math.random() * 21)), // 0-20 questions
      metadata: {
        type: 'unit',
        courseId: courseIdInt,
        unitId: unitIdInt,
        count: concepts.length,
        timestamp: Date.now()
      }
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

    const courseIdInt = parseInt(courseId, 10);
    const unitIdInt = parseInt(unitId, 10);
    const conceptIdInt = parseInt(conceptId, 10);
    const { quizCards } = await fetchConceptWithAllData(
      courseIdInt,
      unitIdInt,
      conceptIdInt
    );

    if (!quizCards || quizCards.length === 0) {
      return getEmptyChartData();
    }

    // For concept progress, we can show individual quiz cards or group them
    // For now, return placeholder data
    return {
      labels: quizCards.map((_, i) => `Question ${i + 1}`),
      values: quizCards.map(() => Math.floor(Math.random() * 21)), // 0-20 questions
      metadata: {
        type: 'concept',
        courseId: courseIdInt,
        unitId: unitIdInt,
        conceptId: conceptIdInt,
        count: quizCards.length,
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

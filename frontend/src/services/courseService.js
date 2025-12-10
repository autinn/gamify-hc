/**
 * Course Service - Manages course data fetching and transformations
 *
 * Handles all course-related API orchestration including fetching individual courses,
 * lists of courses, and composite data structures. Integrates with data mappers to
 * ensure consistent field naming and data structure across the application.
 *
 * @module courseService
 */

import * as api from './api';
import { mapCourseData, mapCoursesArray, mapUnitsArray } from './dataMappers';

// ============================================================================
// COURSE ENDPOINTS
// ============================================================================

/**
 * Fetches all available courses from the backend
 *
 * Retrieves complete list of courses accessible to the authenticated user.
 * Applies data mapping to ensure consistent component-expected field names.
 *
 * @async
 * @returns {Promise<Array<Object>>} Array of mapped course objects
 * @returns {number} result[].course_id - Course identifier
 * @returns {string} result[].title - Course name or code
 * @returns {string} result[].description - Course description
 *
 * @example
 * const courses = await fetchAllCourses();
 * courses.forEach(course => console.log(course.title));
 */
export async function fetchAllCourses() {
  const courses = await api.getCourses();
  return mapCoursesArray(courses);
}

/**
 * Fetches a single course by ID
 *
 * Retrieves detailed information for a specific course.
 * Applies data mapping to ensure consistent component-expected field names.
 *
 * @async
 * @param {number} courseId - Course identifier
 * @returns {Promise<Object>} Mapped course object
 * @returns {number} result.course_id - Course identifier
 * @returns {string} result.title - Course name or code
 * @returns {string} result.description - Course description
 *
 * @example
 * const course = await fetchCourse(42);
 * console.log(course.title); // "CS 101"
 */
export async function fetchCourse(courseId) {
  const course = await api.getCourse(courseId);
  return mapCourseData(course);
}

/**
 * Fetch course with all its units
 * @param {number} courseId - Course ID
 * @returns {Promise<Object>} {course: {...}, units: [...]}
 */
export async function fetchCourseWithUnits(courseId) {
  const [courseData, unitsData] = await Promise.all([
    api.getCourse(courseId),
    api.getCourseUnits(courseId)
  ]);

  return {
    course: mapCourseData(courseData),
    units: mapUnitsArray(unitsData)
  };
}

/**
 * Fetch course units
 * @param {number} courseId - Course ID
 * @returns {Promise<Array>} Array of mapped units
 */
export async function fetchCourseUnits(courseId) {
  const units = await api.getCourseUnits(courseId);
  return mapUnitsArray(units);
}

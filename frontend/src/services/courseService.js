/**
 * Course Service
 * 
 * Business logic for course-related data fetching and transformations.
 * Centralizes all course API orchestration and field mapping.
 */

import * as api from './api';
import { mapCourseData, mapCoursesArray, mapUnitsArray } from './dataMappers';

/**
 * Fetch all courses from API
 * @returns {Promise<Array>} Array of mapped courses
 */
export async function fetchAllCourses() {
  const courses = await api.getCourses();
  return mapCoursesArray(courses);
}

/**
 * Fetch single course by ID
 * @param {number} courseId - Course ID
 * @returns {Promise<Object>} Mapped course object
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

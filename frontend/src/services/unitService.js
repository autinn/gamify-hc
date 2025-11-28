/**
 * Unit Service
 * 
 * Business logic for unit-related data fetching and transformations.
 * Centralizes all unit API orchestration and field mapping.
 */

import * as api from './api';
import { mapCourseData, mapUnitData, mapConceptsArray } from './dataMappers';

/**
 * Fetch single unit by ID
 * @param {number} unitId - Unit ID
 * @returns {Promise<Object>} Mapped unit object
 */
export async function fetchUnit(unitId) {
  const unit = await api.getUnit(unitId);
  return mapUnitData(unit);
}

/**
 * Fetch unit concepts
 * @param {number} unitId - Unit ID
 * @returns {Promise<Array>} Array of mapped concepts
 */
export async function fetchUnitConcepts(unitId) {
  const concepts = await api.getUnitConcepts(unitId);
  return mapConceptsArray(concepts);
}

/**
 * Fetch unit with all its concepts
 * @param {number} unitId - Unit ID
 * @returns {Promise<Object>} {unit: {...}, concepts: [...]}
 */
export async function fetchUnitWithConcepts(unitId) {
  const [unitData, conceptsData] = await Promise.all([
    api.getUnit(unitId),
    api.getUnitConcepts(unitId)
  ]);

  return {
    unit: mapUnitData(unitData),
    concepts: mapConceptsArray(conceptsData)
  };
}

/**
 * Fetch course, unit, and concepts together (for UnitPage)
 * @param {number} courseId - Course ID
 * @param {number} unitId - Unit ID
 * @returns {Promise<Object>} {course: {...}, unit: {...}, concepts: [...]}
 */
export async function fetchCourseUnitWithConcepts(courseId, unitId) {
  const [courseData, unitData, conceptsData] = await Promise.all([
    api.getCourse(courseId),
    api.getUnit(unitId),
    api.getUnitConcepts(unitId)
  ]);

  return {
    course: mapCourseData(courseData),
    unit: mapUnitData(unitData),
    concepts: mapConceptsArray(conceptsData)
  };
}

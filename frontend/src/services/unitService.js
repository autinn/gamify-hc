/**
 * Unit Service
 * @module unitService
 * 
 * Provides business logic for unit-related data operations including:
 * - Individual unit fetching and data transformation
 * - Unit concept retrieval and aggregation
 * - Combined data fetching for page initialization
 * 
 * Centralizes all unit-level API orchestration, enabling efficient parallel
 * requests and consistent field mapping across the application. Use these
 * functions when rendering unit pages or loading unit content for users.
 */

import * as api from './api';
import { mapCourseData, mapUnitData, mapConceptsArray } from './dataMappers';

// ============================================================================
// Single Unit Operations
// ============================================================================

/**
 * Retrieves a single unit by ID with all fields transformed and mapped.
 * 
 * Use this when you need to display or work with a specific unit's metadata,
 * such as unit title, description, duration, or learning objectives.
 * Data is automatically transformed via mappers for consistent field names
 * and structure across the frontend.
 * 
 * @async
 * @param {number} unitId - The unique identifier for the unit to fetch
 * @returns {Promise<Object>} Mapped unit object with standardized field structure
 * @throws {Error} If the API request fails or unit ID is invalid
 */
export async function fetchUnit(unitId) {
  const unit = await api.getUnit(unitId);
  return mapUnitData(unit);
}

/**
 * Retrieves all concepts associated with a specific unit.
 * 
 * Concepts represent the individual learning topics within a unit. Use this
 * when you need to display a concept list, populate concept navigation menus,
 * or check available learning topics under a unit without fetching full
 * unit metadata.
 * 
 * @async
 * @param {number} unitId - The unique identifier for the parent unit
 * @returns {Promise<Array>} Array of mapped concept objects with consistent structure
 * @throws {Error} If the API request fails or unit ID is invalid
 */
export async function fetchUnitConcepts(unitId) {
  const concepts = await api.getUnitConcepts(unitId);
  return mapConceptsArray(concepts);
}

// ============================================================================
// Combined Data Operations
// ============================================================================

/**
 * Retrieves unit metadata and all associated concepts using parallel requests.
 * 
 * Optimized for unit detail views that need both unit information and concept
 * listings. Uses Promise.all() to fetch data in parallel, reducing total
 * network latency compared to sequential requests.
 * 
 * Use this when rendering a unit page that displays unit info alongside
 * its complete concept list for navigation or overview purposes.
 * 
 * @async
 * @param {number} unitId - The unique identifier for the unit
 * @returns {Promise<Object>} Object with structure: { unit: Object, concepts: Array }
 * @throws {Error} If any API request fails or unit ID is invalid
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
 * Retrieves complete hierarchical data for a unit page: course, unit, and concepts.
 * 
 * Fetches all necessary data for rendering a unit detail page in a single
 * call using parallel requests. Maintains the content hierarchy context
 * (course > unit > concepts) needed for navigation and breadcrumbs.
 * 
 * Use this for initializing UnitPage components or views that need full
 * content context and multiple levels of the learning hierarchy.
 * 
 * @async
 * @param {number} courseId - The parent course identifier for context and navigation
 * @param {number} unitId - The unit identifier for the main content
 * @returns {Promise<Object>} Object with structure: { course: Object, unit: Object, concepts: Array }
 * @throws {Error} If any API request fails or IDs are invalid
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

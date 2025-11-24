/**
 * Concept Service
 * 
 * Business logic for concept-related data fetching and transformations.
 * Centralizes all concept API orchestration and field mapping.
 */

import * as api from './api';
import { mapCourseData, mapUnitData, mapConceptData, mapQuizCardsArrayForConcept } from './dataMappers';

/**
 * Fetch single concept by ID
 * @param {number} conceptId - Concept ID
 * @returns {Promise<Object>} Mapped concept object
 */
export async function fetchConcept(conceptId) {
  const concept = await api.getConcept(conceptId);
  return mapConceptData(concept);
}

/**
 * Fetch concept quiz cards
 * @param {number} conceptId - Concept ID
 * @returns {Promise<Array>} Array of mapped quiz cards in concept format
 */
export async function fetchConceptQuizCards(conceptId) {
  const quizCards = await api.getConceptQuizCards(conceptId);
  return mapQuizCardsArrayForConcept(quizCards);
}

/**
 * Fetch course, unit, concept, and quiz cards together (for ConceptPage)
 * @param {number} courseId - Course ID
 * @param {number} unitId - Unit ID
 * @param {number} conceptId - Concept ID
 * @returns {Promise<Object>} {course: {...}, unit: {...}, concept: {...}, quizCards: [...]}
 */
export async function fetchConceptWithAllData(courseId, unitId, conceptId) {
  const [courseData, unitData, conceptData, quizCardsData] = await Promise.all([
    api.getCourse(courseId),
    api.getUnit(unitId),
    api.getConcept(conceptId),
    api.getConceptQuizCards(conceptId)
  ]);

  return {
    course: mapCourseData(courseData),
    unit: mapUnitData(unitData),
    concept: mapConceptData(conceptData),
    quizCards: mapQuizCardsArrayForConcept(quizCardsData)
  };
}

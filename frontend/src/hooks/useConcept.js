/**
 * useConcept Hook - Single concept data management
 *
 * Fetches a single concept with its parent course, unit, and all quiz cards.
 * Provides complete data structure for concept detail pages.
 *
 * @hook
 * @param {number} courseId - Parent course ID from URL
 * @param {number} unitId - Parent unit ID from URL
 * @param {number} conceptId - Concept ID from URL
 * @returns {Object} Concept data and state
 * @returns {Object|null} returns.course - Parent course object
 * @returns {Object|null} returns.unit - Parent unit object
 * @returns {Object|null} returns.concept - Concept object {concept_id, unit_id, title, definition}
 * @returns {Array} returns.quizCards - Array of quiz card objects for the concept
 * @returns {boolean} returns.loading - True while fetching
 * @returns {Error|null} returns.error - Error object if fetch failed
 *
 * @example
 * const { concept, quizCards, loading } = useConcept(courseId, unitId, conceptId);
 * if (loading) return <Loading />;
 * return <ConceptPage concept={concept} quizCards={quizCards} />;
 *
 * Used by: ConceptPage
 */

import { useState, useEffect } from 'react';
import { fetchConceptWithAllData } from '../services/conceptService';

export function useConcept(courseId, unitId, conceptId) {
  const [course, setCourse] = useState(null);
  const [unit, setUnit] = useState(null);
  const [concept, setConcept] = useState(null);
  const [quizCards, setQuizCards] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!courseId || !unitId || !conceptId) return;

    setLoading(true);
    setError(null);

    const courseIdInt = parseInt(courseId, 10);
    const unitIdInt = parseInt(unitId, 10);
    const conceptIdInt = parseInt(conceptId, 10);

    fetchConceptWithAllData(courseIdInt, unitIdInt, conceptIdInt)
      .then(({ course, unit, concept, quizCards }) => {
        setCourse(course);
        setUnit(unit);
        setConcept(concept);
        setQuizCards(quizCards);
      })
      .catch(err => {
        console.error('Error fetching concept data:', err);
        setError(err);
        // Keep null/empty state on error
      })
      .finally(() => setLoading(false));
  }, [courseId, unitId, conceptId]);

  return { course, unit, concept, quizCards, loading, error };
}

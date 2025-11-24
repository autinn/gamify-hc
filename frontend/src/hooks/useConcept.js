/**
 * useConcept Hook
 * 
 * Manages concept fetching with course, unit, and quiz cards.
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

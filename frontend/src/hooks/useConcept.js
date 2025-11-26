/**
 * useConcept Hook
 * 
 * Fetches a concept (Healing Circle) with its complete context: course, unit, and quiz cards.
 * Useful for displaying concept details with associated quiz questions and answers.
 * 
 * @component
 * @param {number|string} courseId - The ID of the course (required)
 * @param {number|string} unitId - The ID of the unit (required)
 * @param {number|string} conceptId - The ID of the concept to fetch (required)
 * @returns {Object} Concept data object
 * @returns {Object|null} returns.course - Parent course object {course_id, title, description} or null
 * @returns {Object|null} returns.unit - Parent unit object {unit_id, title, description} or null
 * @returns {Object|null} returns.concept - Concept object {concept_id, title, definition} or null
 * @returns {Array} returns.quizCards - Array of quiz card objects for this concept
 * @returns {boolean} returns.loading - True while concept data is being fetched
 * @returns {Error|null} returns.error - Error object if fetch failed
 * 
 * @example
 * const { course, unit, concept, quizCards, loading, error } = useConcept(courseId, unitId, conceptId);
 * 
 * if (loading) return <div>Loading...</div>;
 * return (
 *   <>
 *     <h2>{course.title}</h2>
 *     <h3>{unit.title}</h3>
 *     <h4>{concept.title}</h4>
 *     <p>{concept.definition}</p>
 *     {quizCards.map(card => <QuestionBlock key={card.quiz_card_id} card={card} />)}
 *   </>
 * );
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

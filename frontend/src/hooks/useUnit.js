/**
 * useUnit Hook
 * 
 * Fetches a single unit with its course context and all concepts.
 * Useful for displaying unit details with available concepts/healing circles.
 * 
 * @component
 * @param {number|string} courseId - The ID of the course (required)
 * @param {number|string} unitId - The ID of the unit to fetch (required)
 * @returns {Object} Unit data object
 * @returns {Object|null} returns.course - Parent course object {course_id, title, description} or null
 * @returns {Object|null} returns.unit - Unit object {unit_id, title, description} or null
 * @returns {Array} returns.concepts - Array of concept objects in this unit
 * @returns {boolean} returns.loading - True while unit data is being fetched
 * @returns {Error|null} returns.error - Error object if fetch failed
 * 
 * @example
 * const { course, unit, concepts, loading, error } = useUnit(courseId, unitId);
 * 
 * if (loading) return <div>Loading...</div>;
 * return (
 *   <>
 *     <h2>{course.title}</h2>
 *     <h3>{unit.title}</h3>
 *     {concepts.map(concept => <ConceptCard key={concept.concept_id} concept={concept} />)}
 *   </>
 * );
 * 
 * Used by: UnitPage
 */

import { useState, useEffect } from 'react';
import { fetchCourseUnitWithConcepts } from '../services/unitService';

export function useUnit(courseId, unitId) {
  const [course, setCourse] = useState(null);
  const [unit, setUnit] = useState(null);
  const [concepts, setConcepts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!courseId || !unitId) return;

    setLoading(true);
    setError(null);

    const courseIdInt = parseInt(courseId, 10);
    const unitIdInt = parseInt(unitId, 10);

    fetchCourseUnitWithConcepts(courseIdInt, unitIdInt)
      .then(({ course, unit, concepts }) => {
        setCourse(course);
        setUnit(unit);
        setConcepts(concepts);
      })
      .catch(err => {
        console.error('Error fetching unit data:', err);
        setError(err);
        // Keep null/empty state on error
      })
      .finally(() => setLoading(false));
  }, [courseId, unitId]);

  return { course, unit, concepts, loading, error };
}

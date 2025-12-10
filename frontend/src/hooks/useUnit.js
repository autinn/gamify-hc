/**
 * useUnit Hook - Single unit data management
 *
 * Fetches a single unit with its parent course and all concepts.
 * Provides hierarchical data structure for unit pages.
 *
 * @hook
 * @param {number} courseId - Parent course ID from URL
 * @param {number} unitId - Unit ID from URL
 * @returns {Object} Unit data and state
 * @returns {Object|null} returns.course - Parent course object {course_id, title, description}
 * @returns {Object|null} returns.unit - Unit object {unit_id, course_id, title, description, order_index}
 * @returns {Array} returns.concepts - Array of concept objects for the unit
 * @returns {boolean} returns.loading - True while fetching
 * @returns {Error|null} returns.error - Error object if fetch failed
 *
 * @example
 * const { course, unit, concepts, loading } = useUnit(courseId, unitId);
 * if (loading) return <Loading />;
 * return <UnitPage course={course} unit={unit} concepts={concepts} />;
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

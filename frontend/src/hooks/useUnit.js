/**
 * useUnit Hook
 * 
 * Manages unit fetching with course and concepts.
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

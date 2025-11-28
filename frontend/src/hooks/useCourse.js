/**
 * useCourse Hook
 * 
 * Manages single course fetching with its units.
 * Used by: CoursePage
 */

import { useState, useEffect } from 'react';
import { fetchCourseWithUnits } from '../services/courseService';

export function useCourse(courseId) {
  const [course, setCourse] = useState(null);
  const [units, setUnits] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!courseId) return;

    setLoading(true);
    setError(null);

    const courseIdInt = parseInt(courseId, 10);

    fetchCourseWithUnits(courseIdInt)
      .then(({ course, units }) => {
        setCourse(course);
        setUnits(units);
      })
      .catch(err => {
        console.error('Error fetching course data:', err);
        setError(err);
        // Keep null/empty state on error
      })
      .finally(() => setLoading(false));
  }, [courseId]);

  return { course, units, loading, error };
}

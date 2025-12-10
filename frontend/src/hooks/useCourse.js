/**
 * useCourse Hook - Single course data management
 *
 * Fetches a single course by ID along with all its units.
 * Provides loading and error states with graceful fallbacks.
 *
 * @hook
 * @param {number} courseId - Course ID from URL parameters
 * @returns {Object} Course data and state
 * @returns {Object|null} returns.course - Mapped course object {course_id, title, description}
 * @returns {Array} returns.units - Array of unit objects for the course
 * @returns {boolean} returns.loading - True while fetching
 * @returns {Error|null} returns.error - Error object if fetch failed
 *
 * @example
 * const { course, units, loading } = useCourse(courseId);
 * if (loading) return <Loading />;
 * return <CoursePage course={course} units={units} />;
 *
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

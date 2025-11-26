/**
 * useCourse Hook
 * 
 * Fetches a single course and all its units.
 * Useful for displaying course details with available units.
 * 
 * @component
 * @param {number|string} courseId - The ID of the course to fetch
 * @returns {Object} Course data object
 * @returns {Object|null} returns.course - Course object {course_id, title, description} or null
 * @returns {Array} returns.units - Array of unit objects for this course
 * @returns {boolean} returns.loading - True while course data is being fetched
 * @returns {Error|null} returns.error - Error object if fetch failed
 * 
 * @example
 * const { course, units, loading, error } = useCourse(courseId);
 * 
 * if (loading) return <div>Loading...</div>;
 * if (error) return <div>Error: {error.message}</div>;
 * return (
 *   <>
 *     <h1>{course.title}</h1>
 *     {units.map(unit => <UnitCard key={unit.unit_id} unit={unit} />)}
 *   </>
 * );
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

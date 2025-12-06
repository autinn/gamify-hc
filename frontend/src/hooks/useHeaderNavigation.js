import { useState, useEffect } from 'react';
import * as api from '../services/api';

/**
 * useHeaderNavigation - Manages header navigation data
 *
 * Fetches all courses and their units, handles errors gracefully.
 * All business logic for header data is isolated here.
 *
 * @returns {Object} { courses, courseUnits, loading, error }
 *   - courses: Array of { id, label }
 *   - courseUnits: Map of courseId -> Array of { id, name }
 *   - loading: Boolean indicating fetch state
 *   - error: Error message if fetch fails
 */
export const useHeaderNavigation = () => {
  const [courses, setCourses] = useState([]);
  const [courseUnits, setCourseUnits] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchNavigationData = async () => {
      try {
        setLoading(true);

        // Fetch all courses
        const courseData = await api.getCourses();
        if (!Array.isArray(courseData)) {
          throw new Error('Invalid courses data format');
        }

        // Map API response to component expectations
        const mappedCourses = courseData.map(c => ({
          id: c.id || c.course_id,
          label: c.name || c.code || c.title
        }));
        setCourses(mappedCourses);

        // Fetch units for each course in parallel
        const unitsMap = {};
        const unitPromises = mappedCourses.map(course =>
          api.getCourseUnits(course.id)
            .then(units => {
              if (Array.isArray(units)) {
                unitsMap[course.id] = units.map(u => ({
                  id: u.id || u.unit_id,
                  name: u.name || u.title
                }));
              }
            })
            .catch(err => {
              console.error(`Error fetching units for course ${course.id}:`, err);
              unitsMap[course.id] = [];
            })
        );

        await Promise.all(unitPromises);
        setCourseUnits(unitsMap);
        setError(null);
      } catch (err) {
        console.error('Error fetching navigation data:', err);
        setError(err.message);
        setCourses([]);
        setCourseUnits({});
      } finally {
        setLoading(false);
      }
    };

    fetchNavigationData();
  }, []);

  return { courses, courseUnits, loading, error };
};

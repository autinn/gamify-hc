import { useState, useEffect } from 'react';
import * as api from '../services/api';

/**
 * useHeaderNavigation Hook - Header navigation data management
 *
 * Fetches all courses and units for header navigation dropdown menus.
 * Organizes units by parent course ID for efficient dropdown filtering.
 * Handles loading and error states with user-friendly fallbacks.
 *
 * @hook
 * @returns {Object} Navigation data and state
 * @returns {Array} returns.courses - Array of course objects {id, label}
 * @returns {Object} returns.courseUnits - Map of courseId -> units {id, name}
 * @returns {boolean} returns.loading - True while fetching
 * @returns {string|null} returns.error - Error message if fetch failed
 *
 * @example
 * const { courses, courseUnits, loading } = useHeaderNavigation();
 * return courses.map(course => (
 *   <CourseDropdown
 *     course={course}
 *     units={courseUnits[course.id]}
 *   />
 * ));
 *
 * Used by: Header component
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

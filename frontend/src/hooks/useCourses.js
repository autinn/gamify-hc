/**
 * useCourses Hook
 * 
 * Fetches and manages the list of all available courses.
 * Falls back to dummy course data if API fails (graceful degradation).
 * 
 * @component
 * @returns {Object} Courses object
 * @returns {Array} returns.courses - Array of course objects with IDs and titles
 * @returns {boolean} returns.loading - True while courses are being fetched from API
 * 
 * @example
 * const { courses, loading } = useCourses();
 * 
 * if (loading) return <div>Loading...</div>;
 * return courses.map(course => <CourseCard key={course.course_id} course={course} />);
 * 
 * Used by: MainPage
 */

import { useState, useEffect } from 'react';
import { fetchAllCourses } from '../services/courseService';

const dummyCourses = [
  { course_id: 1, title: 'EA50', description: 'Problem Solving and Analysis' },
  { course_id: 2, title: 'FA50', description: 'Fundamental Analysis' },
  { course_id: 3, title: 'MC50', description: 'Metacognition and Critical Thinking' },
  { course_id: 4, title: 'CX50', description: 'Complex Systems and Design' },
];

export function useCourses() {
  const [courses, setCourses] = useState(dummyCourses);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);

    fetchAllCourses()
      .then(mappedCourses => {
        if (mappedCourses && mappedCourses.length > 0) {
          setCourses(mappedCourses);
        }
        // If empty, keep dummy data
      })
      .catch(err => {
        console.error('Error fetching courses:', err);
        // Keep dummy data on error
      })
      .finally(() => setLoading(false));
  }, []);

  return { courses, loading };
}

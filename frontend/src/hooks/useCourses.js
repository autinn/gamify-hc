/**
 * useCourses Hook
 * 
 * Manages course list fetching and state.
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

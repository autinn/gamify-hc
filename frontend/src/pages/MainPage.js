import React, { useEffect, useState } from 'react';
import PageLayout from '../components/common/layout/PageLayout';
import CourseList from '../components/course/CourseList';
import * as api from '../services/api';

/**
 * MainPage - Main dashboard page
 *
 * Displays a greeting, performance dashboard, and list of available courses.
 * Uses PageLayout for consistent two-column structure.
 */
const MainPage = () => {
  // Default dummy data for nice display
  const dummyCourses = [
    { course_id: 1, title: 'EA50', description: 'Problem Solving and Analysis' },
    { course_id: 2, title: 'FA50', description: 'Fundamental Analysis' },
    { course_id: 3, title: 'MC50', description: 'Metacognition and Critical Thinking' },
    { course_id: 4, title: 'CX50', description: 'Complex Systems and Design' },
  ];

  const [courses, setCourses] = useState(dummyCourses);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // CHANGED: Added field mapping to convert API response format to component expectations
    // Backend returns: {id, name/code, description} -> Component expects: {course_id, title, description}
    // Try to fetch real courses from API
    api.getCourses()
      .then(data => {
        if (data && data.length > 0) {
          // Map API response to component expectations
          const mappedCourses = data.map(c => ({
            course_id: c.id,
            title: c.name || c.code,
            description: c.description
          }));
          setCourses(mappedCourses);
        }
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching courses:', err);
        console.log('Using dummy data instead');
        // Keep dummy data if API fails
        setLoading(false);
      });
  }, []);

  // Chart data - shows performance across courses
  const chartData = {
    labels: courses.map(c => c.title),
    values: [65, 45, 55, 35], // Dummy performance values
  };

  return (
    <PageLayout
      greeting="Hello,"
      title="NAME"
      showButton={true}
      chartData={chartData}
      chartLabel="No. of questions answered"
      rightContent={<CourseList courses={courses} />}
    />
  );
};

export default MainPage;


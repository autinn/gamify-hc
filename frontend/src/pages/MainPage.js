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
    // Try to fetch real courses from API
    api.getCourses()
      .then(data => {
        if (data && data.length > 0) {
          setCourses(data);
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
      chartLabel="Questions you answered correctly (% correct answered)"
      rightContent={<CourseList courses={courses} />}
    />
  );
};

export default MainPage;


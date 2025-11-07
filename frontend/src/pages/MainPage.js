import React from 'react';
import PageLayout from '../components/common/layout/PageLayout';
import CourseList from '../components/course/CourseList';

/**
 * MainPage - Main dashboard page
 *
 * Displays a greeting, performance dashboard, and list of available courses.
 * Uses PageLayout for consistent two-column structure.
 */
const MainPage = () => {
  // Dummy data: 4 courses
  const courses = [
    { id: 'EA50', name: 'EA50' },
    { id: 'FA50', name: 'FA50' },
    { id: 'MC50', name: 'MC50' },
    { id: 'CX50', name: 'CX50' },
  ];

  // Dummy chart data - shows performance across courses
  const chartData = {
    labels: ['EA', 'FA', 'MC', 'CX'],
    values: [65, 45, 55, 35],
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


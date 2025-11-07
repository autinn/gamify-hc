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
  // Dummy data: 4 courses (aligned with DB schema)
  // Schema: course_id (int, PK), title (varchar), description (varchar)
  const courses = [
    { course_id: 1, title: 'EA50', description: 'Problem Solving and Analysis' },
    { course_id: 2, title: 'FA50', description: 'Fundamental Analysis' },
    { course_id: 3, title: 'MC50', description: 'Metacognition and Critical Thinking' },
    { course_id: 4, title: 'CX50', description: 'Complex Systems and Design' },
  ];

  // Dummy chart data - shows performance across courses
  const chartData = {
    labels: courses.map(c => c.title),
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


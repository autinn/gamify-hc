import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import UnitList from '../components/unit/UnitList';
import { useCourse } from '../hooks/useCourse';

/**
 * CoursePage - Course details page with units
 *
 * Displays course name, performance chart, and list of units for the course.
 * Uses URL parameter :courseId to determine which course to display.
 * Uses PageLayout for consistent two-column structure.
 */
const CoursePage = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  
  const { course, units } = useCourse(courseId);

  // Chart data - performance within this course
  const chartData = {
    labels: units.map(u => u.title),
    values: units.map(() => Math.floor(Math.random() * 100)), // TODO: Replace with real progress data
  };

  return (
    <PageLayout
      greeting="Welcome to"
      title={course ? course.title : courseId}
      showButton={true}
      startQuizPath={`/course/${courseId}/quiz`}
      chartData={chartData}
      chartLabel="Questions you answered correctly (% correct answered)"
      rightContent={<UnitList courseId={courseId} units={units} />}
      showBackButton={true}
      onBackClick={() => navigate('/')}
    />
  );
};

export default CoursePage;

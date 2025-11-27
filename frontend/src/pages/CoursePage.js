import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import UnitList from '../components/unit/UnitList';
import { useCourse } from '../hooks/useCourse';
import { useProgress } from '../hooks/useProgress';

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
  const { chartData } = useProgress('course', courseId);

  // Sort units by order_index for consistent display
  const sortedUnits = [...units].sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

  return (
    <PageLayout
      greeting="Welcome to"
      title={course ? course.title : courseId}
      showButton={true}
      startQuizPath={`/course/${courseId}/quiz`}
      chartData={chartData}
      chartLabel="No. of questions answered"
      rightContent={<UnitList courseId={courseId} units={sortedUnits} />}
      showBackButton={true}
      onBackClick={() => navigate('/')}
    />
  );
};

export default CoursePage;

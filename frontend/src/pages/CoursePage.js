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
  // Sort units by order_index and use order_index from DB (0-based, so add 1 for display)
  const sortedUnits = [...units].sort((a, b) => (a.order_index || 0) - (b.order_index || 0));
  const chartData = {
    labels: sortedUnits.map((u) => {
      // order_index is 0-based in DB (starts at 0), so add 1 for display (Unit 1, Unit 2, etc.)
      if (u.order_index !== undefined && u.order_index !== null) {
        return `Unit ${u.order_index + 1}`;
      }
      // Fallback if order_index is missing
      return u.title;
    }),
    values: sortedUnits.map(() => Math.floor(Math.random() * 21)), // 0-20 questions per unit
  };

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

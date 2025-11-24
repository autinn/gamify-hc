import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import ConceptList from '../components/concept/ConceptList';
import { useUnit } from '../hooks/useUnit';

/**
 * UnitPage - Unit details page with concepts
 *
 * Displays unit name, performance chart, and list of concepts for the unit.
 * Uses URL parameters :courseId and :unitId to determine which unit to display.
 * Uses PageLayout for consistent two-column structure.
 */
const UnitPage = () => {
  const { courseId, unitId } = useParams();
  const navigate = useNavigate();
  
  const { course, unit, concepts } = useUnit(courseId, unitId);

  // Chart data - concept performance within this unit
  const chartData = {
    labels: concepts.map(c => c.title),
    values: concepts.map(() => Math.floor(Math.random() * 21)), // 0-20 questions per concept
  };

  // Build greeting with course and unit number (using order_index + 1)
  const greeting = course && unit && unit.order_index !== undefined && unit.order_index !== null
    ? `${course.title} - Unit ${unit.order_index + 1}`
    : course && unit
    ? `${course.title} - ${unit.title}`
    : course 
    ? `${course.title} - Unit ${unitId}`
    : unit 
    ? `${courseId} - ${unit.title}`
    : `${courseId} - Unit ${unitId}`;

  return (
    <PageLayout
      greeting={greeting}
      title={unit ? unit.title : 'Unit'}
      showButton={true}
      startQuizPath={`/course/${courseId}/unit/${unitId}/quiz`}
      chartData={chartData}
      chartLabel="No. of questions answered"
      labelOffset={70}
      rightContent={<ConceptList concepts={concepts} courseId={courseId} unitId={unitId} />}
      showBackButton={true}
      onBackClick={() => navigate(`/course/${courseId}`)}
    />
  );
};

export default UnitPage;

import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import ConceptList from '../components/concept/ConceptList';
import { useUnit } from '../hooks/useUnit';
import { useProgress } from '../hooks/useProgress';

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
  const { chartData } = useProgress('unit', unitId, courseId);

  // Build greeting with course and unit names
  const greeting = course && unit 
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
      chartLabel="Success Rate (%)"
      labelOffset={70}
      rightContent={<ConceptList concepts={concepts} courseId={courseId} unitId={unitId} />}
      showBackButton={true}
      onBackClick={() => navigate(`/course/${courseId}`)}
    />
  );
};

export default UnitPage;

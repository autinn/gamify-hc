import React from 'react';
import { useParams } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import UnitList from '../components/unit/UnitList';

/**
 * CoursePage - Course details page with units
 *
 * Displays course name, performance chart, and list of units for the course.
 * Uses URL parameter :courseId to determine which course to display.
 * Uses PageLayout for consistent two-column structure.
 */
const CoursePage = () => {
  const { courseId } = useParams();

  // Dummy data: Units for a course
  // Replace this with actual API call when backend is ready
  const courseUnits = {
    EA50: [
      { id: 1, name: 'Scientific Method', questionCount: 8 },
      { id: 2, name: 'Problem Solving', questionCount: 7 },
    ],
    FA50: [
      { id: 1, name: 'Analysis Techniques', questionCount: 10 },
      { id: 2, name: 'Pattern Recognition', questionCount: 9 },
    ],
    MC50: [
      { id: 1, name: 'Metacognition Basics', questionCount: 6 },
      { id: 2, name: 'Self-Assessment', questionCount: 8 },
    ],
    CX50: [
      { id: 1, name: 'User Experience', questionCount: 7 },
      { id: 2, name: 'Design Thinking', questionCount: 9 },
    ],
  };

  const units = courseUnits[courseId] || [];

  // Dummy chart data - performance within this course
  const chartData = {
    labels: units.map(u => u.name),
    values: units.map(u => u.questionCount),
  };

  return (
    <PageLayout
      greeting="Welcome to"
      title={courseId}
      showButton={true}
      chartData={chartData}
      chartLabel="Questions you answered correctly (% correct answered)"
      rightContent={<UnitList courseId={courseId} units={units} />}
    />
  );
};

export default CoursePage;

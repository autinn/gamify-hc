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
  const courseIdInt = parseInt(courseId, 10);

  // Dummy data: Courses (aligned with DB schema)
  // Schema: course_id (int, PK), title (varchar), description (varchar)
  const courses = {
    1: { course_id: 1, title: 'EA50', description: 'Problem Solving and Analysis' },
    2: { course_id: 2, title: 'FA50', description: 'Fundamental Analysis' },
    3: { course_id: 3, title: 'MC50', description: 'Metacognition and Critical Thinking' },
    4: { course_id: 4, title: 'CX50', description: 'Complex Systems and Design' },
  };

  // Dummy data: Units for a course (aligned with DB schema)
  // Schema: unit_id (int, PK), course_id (int, FK), title (varchar), description (varchar), order_index (int)
  // Replace this with actual API call when backend is ready
  const courseUnits = {
    1: [ // EA50
      { unit_id: 1, course_id: 1, title: 'Scientific Method', description: 'Introduction to scientific methodology', order_index: 1 },
      { unit_id: 2, course_id: 1, title: 'Problem Solving', description: 'Problem-solving techniques and heuristics', order_index: 2 },
    ],
    2: [ // FA50
      { unit_id: 3, course_id: 2, title: 'Analysis Techniques', description: 'Methods for data analysis', order_index: 1 },
      { unit_id: 4, course_id: 2, title: 'Pattern Recognition', description: 'Identifying patterns in data', order_index: 2 },
    ],
    3: [ // MC50
      { unit_id: 5, course_id: 3, title: 'Metacognition Basics', description: 'Understanding thinking about thinking', order_index: 1 },
      { unit_id: 6, course_id: 3, title: 'Self-Assessment', description: 'Evaluating your own understanding', order_index: 2 },
    ],
    4: [ // CX50
      { unit_id: 7, course_id: 4, title: 'User Experience', description: 'Designing for user needs', order_index: 1 },
      { unit_id: 8, course_id: 4, title: 'Design Thinking', description: 'Creative problem-solving approach', order_index: 2 },
    ],
  };

  const course = courses[courseIdInt] || null;
  const units = courseUnits[courseIdInt] || [];

  // Dummy chart data - performance within this course
  const chartData = {
    labels: units.map(u => u.title),
    values: units.map(() => Math.floor(Math.random() * 100)), // Placeholder values
  };

  return (
    <PageLayout
      greeting="Welcome to"
      title={course ? course.title : courseId}
      showButton={true}
      chartData={chartData}
      chartLabel="Questions you answered correctly (% correct answered)"
      rightContent={<UnitList courseId={courseId} units={units} />}
    />
  );
};

export default CoursePage;

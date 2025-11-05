import React from 'react';
import { useParams } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import ConceptList from '../components/concept/ConceptList';

/**
 * UnitPage - Unit details page with concepts
 *
 * Displays unit name, performance chart, and list of concepts for the unit.
 * Uses URL parameters :courseId and :unitId to determine which unit to display.
 * Uses PageLayout for consistent two-column structure.
 */
const UnitPage = () => {
  const { courseId, unitId } = useParams();
  const courseIdInt = parseInt(courseId, 10);
  const unitIdInt = parseInt(unitId, 10);

  // Dummy data: Courses (aligned with DB schema)
  // Schema: course_id (int, PK), title (varchar), description (varchar)
  const courses = {
    1: { course_id: 1, title: 'EA50', description: 'Problem Solving and Analysis' },
    2: { course_id: 2, title: 'FA50', description: 'Fundamental Analysis' },
    3: { course_id: 3, title: 'MC50', description: 'Metacognition and Critical Thinking' },
    4: { course_id: 4, title: 'CX50', description: 'Complex Systems and Design' },
  };

  // Dummy data: Units (aligned with DB schema)
  // Schema: unit_id (int, PK), course_id (int, FK), title (varchar), description (varchar), order_index (int)
  const units = {
    1: { unit_id: 1, course_id: 1, title: 'Scientific Method', description: 'Introduction to scientific methodology', order_index: 1 },
    2: { unit_id: 2, course_id: 1, title: 'Problem Solving', description: 'Problem-solving techniques and heuristics', order_index: 2 },
    3: { unit_id: 3, course_id: 2, title: 'Analysis Techniques', description: 'Methods for data analysis', order_index: 1 },
    4: { unit_id: 4, course_id: 2, title: 'Pattern Recognition', description: 'Identifying patterns in data', order_index: 2 },
    5: { unit_id: 5, course_id: 3, title: 'Metacognition Basics', description: 'Understanding thinking about thinking', order_index: 1 },
    6: { unit_id: 6, course_id: 3, title: 'Self-Assessment', description: 'Evaluating your own understanding', order_index: 2 },
    7: { unit_id: 7, course_id: 4, title: 'User Experience', description: 'Designing for user needs', order_index: 1 },
    8: { unit_id: 8, course_id: 4, title: 'Design Thinking', description: 'Creative problem-solving approach', order_index: 2 },
  };

  // Dummy data: Concepts for each unit (aligned with DB schema)
  // Schema: concept_id (int, PK), unit_id (int, FK), title (varchar), definition (varchar)
  // Replace this with actual API call when backend is ready
  const unitConcepts = {
    1: [ // Scientific Method (unit_id: 1)
      { concept_id: 1, unit_id: 1, title: '#rightproblem', definition: 'Identifying the correct problem to solve' },
      { concept_id: 2, unit_id: 1, title: '#gapanalysis', definition: 'Analyzing gaps in knowledge or understanding' },
      { concept_id: 3, unit_id: 1, title: '#scienceoflearning', definition: 'Understanding how learning works' },
      { concept_id: 4, unit_id: 1, title: '#constraints', definition: 'Identifying and working within limitations' },
      { concept_id: 5, unit_id: 1, title: '#breakitdown', definition: 'Decomposing complex problems into smaller parts' },
      { concept_id: 6, unit_id: 1, title: '#heuristics', definition: 'Mental shortcuts for problem-solving' },
      { concept_id: 7, unit_id: 1, title: '#evidencebased', definition: 'Making decisions based on evidence' },
    ],
    2: [ // Problem Solving (unit_id: 2)
      { concept_id: 8, unit_id: 2, title: '#problem-analysis', definition: 'Analyzing problems systematically' },
      { concept_id: 9, unit_id: 2, title: '#solution-design', definition: 'Designing effective solutions' },
      { concept_id: 10, unit_id: 2, title: '#implementation', definition: 'Putting solutions into practice' },
    ],
    3: [ // Analysis Techniques (unit_id: 3)
      { concept_id: 11, unit_id: 3, title: '#regression', definition: 'Statistical regression analysis' },
      { concept_id: 12, unit_id: 3, title: '#clustering', definition: 'Grouping similar data points' },
    ],
    4: [ // Pattern Recognition (unit_id: 4)
      { concept_id: 13, unit_id: 4, title: '#pattern-recognition', definition: 'Identifying patterns in data' },
      { concept_id: 14, unit_id: 4, title: '#analysis', definition: 'Systematic examination of data' },
    ],
    5: [ // Metacognition Basics (unit_id: 5)
      { concept_id: 15, unit_id: 5, title: '#designthinking', definition: 'Human-centered design approach' },
      { concept_id: 16, unit_id: 5, title: '#interpretivelens', definition: 'Frameworks for interpretation' },
    ],
    6: [ // Self-Assessment (unit_id: 6)
      { concept_id: 17, unit_id: 6, title: '#metacognition', definition: 'Thinking about thinking' },
      { concept_id: 18, unit_id: 6, title: '#self-assessment', definition: 'Evaluating your own understanding' },
    ],
    7: [ // User Experience (unit_id: 7)
      { concept_id: 19, unit_id: 7, title: '#systemmapping', definition: 'Mapping system structures' },
      { concept_id: 20, unit_id: 7, title: '#levelsofanalysis', definition: 'Different levels of system analysis' },
    ],
    8: [ // Design Thinking (unit_id: 8)
      { concept_id: 21, unit_id: 8, title: '#userexperience', definition: 'User-centered design approach' },
      { concept_id: 22, unit_id: 8, title: '#design', definition: 'Principles of effective design' },
    ],
  };

  const course = courses[courseIdInt] || null;
  const unit = units[unitIdInt] || null;
  const concepts = unitConcepts[unitIdInt] || [];

  // Dummy chart data - concept performance within this unit
  const chartData = {
    labels: concepts.map(c => c.title.replace('#', '')),
    values: concepts.map(() => Math.floor(Math.random() * 100)), // Random values for now
  };

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
      chartData={chartData}
      chartLabel="Problem Solving HCs"
      rightContent={<ConceptList concepts={concepts} courseId={courseId} unitId={unitId} />}
    />
  );
};

export default UnitPage;

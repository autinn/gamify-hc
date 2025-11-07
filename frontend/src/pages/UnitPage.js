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

  // Dummy data: Concepts for each unit (keyed by courseId-unitId combination)
  // Replace this with actual API call when backend is ready
  const unitConcepts = {
    'EA50-1': [
      { id: 1, name: '#rightproblem' },
      { id: 2, name: '#gapanalysis' },
      { id: 3, name: '#scienceoflearning' },
      { id: 4, name: '#constraints' },
      { id: 5, name: '#breakitdown' },
      { id: 6, name: '#heuristics' },
      { id: 7, name: '#evidencebased' },
    ],
    'EA50-2': [
      { id: 8, name: '#problem-analysis' },
      { id: 9, name: '#solution-design' },
      { id: 10, name: '#implementation' },
    ],
    'FA50-1': [
      { id: 11, name: '#regression' },
      { id: 12, name: '#clustering' },
    ],
    'FA50-2': [
      { id: 13, name: '#pattern-recognition' },
      { id: 14, name: '#analysis' },
    ],
    'MC50-1': [
      { id: 15, name: '#designthinking' },
      { id: 16, name: '#interpretivelens' },
    ],
    'MC50-2': [
      { id: 17, name: '#metacognition' },
      { id: 18, name: '#self-assessment' },
    ],
    'CX50-1': [
      { id: 19, name: '#systemmapping' },
      { id: 20, name: '#levelsofanalysis' },
    ],
    'CX50-2': [
      { id: 21, name: '#userexperience' },
      { id: 22, name: '#design' },
    ],
  };

  // Unit names for display
  const unitNames = {
    'EA50-1': 'Scientific Method',
    'EA50-2': 'Problem Solving',
    'FA50-1': 'Analysis Techniques',
    'FA50-2': 'Pattern Recognition',
    'MC50-1': 'Metacognition Basics',
    'MC50-2': 'Self-Assessment',
    'CX50-1': 'User Experience',
    'CX50-2': 'Design Thinking',
  };

  const concepts = unitConcepts[`${courseId}-${unitId}`] || [];
  const unitName = unitNames[`${courseId}-${unitId}`] || 'Unit';

  // Dummy chart data - concept performance within this unit
  const chartData = {
    labels: concepts.map(c => c.name.replace('#', '')),
    values: concepts.map(() => Math.floor(Math.random() * 100)), // Random values for now
  };

  return (
    <PageLayout
      greeting={`${courseId} - Unit ${unitId}`}
      title={unitName}
      showButton={true}
      chartData={chartData}
      chartLabel="Problem Solving HCs"
      rightContent={<ConceptList concepts={concepts} />}
    />
  );
};

export default UnitPage;

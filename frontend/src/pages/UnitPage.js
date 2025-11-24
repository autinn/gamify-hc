import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import ConceptList from '../components/concept/ConceptList';
import * as api from '../services/api';

/**
 * UnitPage - Unit details page with concepts
 *
 * Displays unit name, performance chart, and list of concepts for the unit.
 * Uses URL parameters :courseId and :unitId to determine which unit to display.
 * Uses PageLayout for consistent two-column structure.
 * 
 * CHANGES: Replaced dummy data (hardcoded courses, units, and unitConcepts objects)
 * with API calls to fetch real data from the backend. Added useState/useEffect hooks
 * to manage API data fetching and state.
 */
const UnitPage = () => {
  const { courseId, unitId } = useParams();
  const navigate = useNavigate();
  const courseIdInt = parseInt(courseId, 10);
  const unitIdInt = parseInt(unitId, 10);

  // State for course, unit, and concepts data fetched from API
  // Previously: Used hardcoded dummy data objects (courses, units, unitConcepts)
  const [course, setCourse] = useState(null);
  const [unit, setUnit] = useState(null);
  const [concepts, setConcepts] = useState([]);

  useEffect(() => {
    // CHANGED: Replaced dummy data lookup with API calls to fetch real course, unit, and concepts
    // Previously: const course = courses[courseIdInt] || null;
    // Previously: const unit = units[unitIdInt] || null;
    // Previously: const concepts = unitConcepts[unitIdInt] || [];
    // Fetch course, unit, and concepts
    Promise.all([
      api.getCourse(courseIdInt),
      api.getUnit(unitIdInt),
      api.getUnitConcepts(unitIdInt)
    ])
      .then(([courseData, unitData, conceptsData]) => {
        // Map API response fields to component expectations
        // Backend returns: {id, name/code, description} -> Component expects: {course_id, title, description}
        setCourse({
          course_id: courseData.id,
          title: courseData.name || courseData.code,
          description: courseData.description
        });

        // Map API response fields to component expectations
        // Backend returns: {id, name, ...} -> Component expects: {unit_id, title, ...}
        setUnit({
          unit_id: unitData.id,
          course_id: unitData.course_id,
          title: unitData.name,
          description: unitData.description,
          order_index: unitData.order_index
        });

        // Map API response fields to component expectations
        // Backend returns: {id, name/tag, ...} -> Component expects: {concept_id, title, ...}
        const mappedConcepts = conceptsData.map(c => ({
          concept_id: c.id,
          unit_id: c.unit_id,
          title: c.name || c.tag,
          definition: c.definition
        }));
        setConcepts(mappedConcepts);
      })
      .catch(err => {
        console.error('Error fetching unit data:', err);
      });
  }, [courseIdInt, unitIdInt]);

  // Chart data - concept performance within this unit
  const chartData = {
    labels: concepts.map(c => c.title.replace('#', '')),
    values: concepts.map(() => Math.floor(Math.random() * 100)), // TODO: Replace with real progress data
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
      startQuizPath={`/course/${courseId}/unit/${unitId}/quiz`}
      chartData={chartData}
      chartLabel="No. of questions answered"
      rightContent={<ConceptList concepts={concepts} courseId={courseId} unitId={unitId} />}
      showBackButton={true}
      onBackClick={() => navigate(`/course/${courseId}`)}
    />
  );
};

export default UnitPage;

import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import ConceptList from '../components/concept/ConceptList';
import { useUnit } from '../hooks/useUnit';
import { useProgress } from '../hooks/useProgress';

/**
 * UnitPage - Unit detail page with concepts and progress dashboard
 *
 * Displays specific unit name, unit-level progress chart, and list of concepts within the unit.
 * Gets courseId and unitId from URL parameters (/course/:courseId/unit/:unitId) to fetch unit-specific data.
 * Uses PageLayout component for consistent two-column layout structure.
 *
 * @component
 * @returns {React.ReactNode} Unit dashboard with concepts list and progress chart
 *
 * Route Parameters:
 * - courseId: Parent course identifier (from URL /course/:courseId/unit/:unitId)
 * - unitId: Unique unit identifier (from URL /course/:courseId/unit/:unitId)
 *
 * Data Requirements:
 * - useUnit hook: Fetches course, unit, and associated concepts (using courseId and unitId)
 *   - Returns: { course: { title, ... }, unit: { title, ... }, concepts: [...] }
 * - useProgress hook: Fetches unit-specific progress metrics (success rate for this unit)
 *   - Called with 'unit' level, unitId, and courseId parameters
 *
 * Layout Structure (via PageLayout):
 * - Left Column:
 *   - Greeting: Hierarchical path (e.g., "Biology 101 - Unit 1: Cells")
 *   - Title: Unit title or "Unit" fallback
 *   - Chart: Unit success rate progress chart
 *   - "Start Quiz" button: Navigates to /course/:courseId/unit/:unitId/quiz
 *   - Back button: Returns to CoursePage (/course/:courseId)
 * - Right Column:
 *   - ConceptList: Grid of concepts in this unit as clickable cards
 *
 * Greeting Logic:
 * - Prefers full path: "Course Title - Unit Title" when both available
 * - Falls back to course name if unit not loaded
 * - Falls back to course/unit IDs if neither loaded
 * - Ensures greeting always shows context up to parent course
 *
 * Navigation:
 * - Clicking concept card: Navigates to /course/:courseId/unit/:unitId/concept/:conceptId
 * - "Start Quiz" button: Navigates to /course/:courseId/unit/:unitId/quiz
 * - Back button: Returns to CoursePage (/course/:courseId)
 *
 * CSS & Layout:
 * - Uses PageLayout component for responsive two-column structure
 * - Left content shows unit info and progress (sidebar on desktop, collapsed on mobile)
 * - Right content shows concept list taking remaining space
 * - labelOffset=70: Adjusts chart label positioning for longer text
 * - showBackButton=true ensures navigation control is visible
 *
 * @example
 * <UnitPage />
 * // URL: /course/3/unit/7
 * // Displays: "Biology 101 - Unit 1: Cells" with unit progress chart and all concepts
 *
 * Used by: Router for unit detail navigation (/:courseId/unit/:unitId route)
 */
const UnitPage = () => {
  const { courseId, unitId } = useParams();
  const navigate = useNavigate();
  
  const { course, unit, concepts } = useUnit(courseId, unitId);
  const { chartData } = useProgress('unit', unitId, courseId);

  // Build greeting showing full hierarchical path: "Course Title - Unit Title"
  // Provides context showing which course the unit belongs to
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

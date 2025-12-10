import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import UnitList from '../components/unit/UnitList';
import { useCourse } from '../hooks/useCourse';
import { useProgress } from '../hooks/useProgress';

/**
 * CoursePage - Course detail page with units and progress dashboard
 *
 * Displays specific course name, course-level progress chart, and list of units within the course.
 * Gets courseId from URL parameters (/course/:courseId) to fetch course-specific data.
 * Uses PageLayout component for consistent two-column layout structure.
 *
 * @component
 * @returns {React.ReactNode} Course dashboard with units list and progress chart
 *
 * Route Parameters:
 * - courseId: Unique course identifier (from URL /course/:courseId)
 *
 * Data Requirements:
 * - useCourse hook: Fetches course object and associated units (using courseId)
 *   - Returns: { course: { title, ... }, units: [...] }
 * - useProgress hook: Fetches course-specific progress metrics (success rate for this course)
 *   - Called with 'course' level and courseId parameter
 *
 * Layout Structure (via PageLayout):
 * - Left Column:
 *   - Greeting: "Welcome to"
 *   - Title: Course title (e.g., "Chemistry 101")
 *   - Chart: Course success rate progress chart
 *   - "Start Quiz" button: Navigates to /course/:courseId/quiz
 *   - Back button: Returns to MainPage (/)
 * - Right Column:
 *   - UnitList: Grid of units in this course as clickable cards
 *
 * Data Processing:
 * - Units are sorted by order_index before display to match course structure
 * - If course object not loaded yet, displays courseId as fallback title
 *
 * Navigation:
 * - Clicking unit card: Navigates to /course/:courseId/unit/:unitId
 * - "Start Quiz" button: Navigates to /course/:courseId/quiz
 * - Back button: Returns to MainPage (/)
 *
 * CSS & Layout:
 * - Uses PageLayout component for responsive two-column structure
 * - Left content shows course info and progress (sidebar on desktop, collapsed on mobile)
 * - Right content shows unit list taking remaining space
 * - showBackButton=true ensures navigation control is visible
 *
 * @example
 * <CoursePage />
 * // URL: /course/3
 * // Displays: "Welcome to Biology 101" with course progress chart and all units
 *
 * Used by: Router for course detail navigation (/:courseId route)
 */
const CoursePage = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  
  const { course, units } = useCourse(courseId);
  const { chartData } = useProgress('course', courseId);

  // Sort units by order_index to ensure consistent display matching course structure
  // This is important because API response may not always return units in order
  const sortedUnits = [...units].sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

  return (
    <PageLayout
      greeting="Welcome to"
      title={course ? course.title : courseId}
      showButton={true}
      startQuizPath={`/course/${courseId}/quiz`}
      chartData={chartData}
      chartLabel="Success Rate (%)"
      rightContent={<UnitList courseId={courseId} units={sortedUnits} />}
      showBackButton={true}
      onBackClick={() => navigate('/')}
    />
  );
};

export default CoursePage;

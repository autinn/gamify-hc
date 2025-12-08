import React from 'react';
import PageLayout from '../components/common/layout/PageLayout';
import CourseList from '../components/course/CourseList';
import { useCourses } from '../hooks/useCourses';
import { useCurrentUser } from '../hooks/useCurrentUser';
import { useProgress } from '../hooks/useProgress';

/**
 * MainPage - Main dashboard page for authenticated users
 *
 * Displays personalized greeting, global progress dashboard, and available courses.
 * Uses PageLayout component for consistent two-column layout structure.
 * Fetches user profile, course list, and global progress metrics.
 *
 * @component
 * @returns {React.ReactNode} Dashboard with user greeting, progress chart, and course list
 *
 * Data Requirements:
 * - useCourses hook: Fetches array of all available courses (from courseService)
 * - useCurrentUser hook: Fetches current user profile (username from API or localStorage fallback)
 * - useProgress hook: Fetches global progress metrics (success rate across all courses/units)
 *
 * Layout Structure (via PageLayout):
 * - Left Column:
 *   - Greeting: "Hello,"
 *   - Title: User's username
 *   - Chart: Global success rate progress chart with percentage data
 * - Right Column:
 *   - CourseList: Grid of all available courses as clickable cards
 *
 * Data Fallback:
 * - If useCurrentUser cannot fetch user data, falls back to localStorage.getItem('user_username')
 * - If localStorage also unavailable, displays "Guest"
 * - Ensures page never breaks even if user data endpoint fails
 *
 * Navigation:
 * - Clicking any course card navigates to /course/:courseId
 * - "Start Quiz" button (if showButton=true in PageLayout) may navigate to quiz
 *
 * Chart Data:
 * - chartData: Array of labels and values for global success rate
 * - chartLabel: "Success Rate (%)" shown in chart
 *
 * CSS & Layout:
 * - Uses PageLayout component for responsive two-column structure
 * - Left content adapts for desktop (sidebar) vs mobile (collapsed)
 * - Right content takes remaining space
 *
 * @example
 * <MainPage />
 * // Displays: "Hello, John" with global progress chart and all courses
 *
 * Used by: Router as the default authenticated dashboard page (usually at /)
 */
const MainPage = () => {
  const { courses } = useCourses();
  const { user } = useCurrentUser();
  const { chartData } = useProgress('global');

  // Get user name from API response or localStorage fallback for display
  // This ensures the greeting works even if user fetch fails
  const userName = user?.username || localStorage.getItem('user_username') || 'Guest';

  return (
    <PageLayout
      greeting="Hello,"
      title={userName}
      showButton={true}
      chartData={chartData}
      chartLabel="Success Rate (%)"
      rightContent={<CourseList courses={courses} />}
    />
  );
};

export default MainPage;


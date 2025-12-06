import React from 'react';
import PageLayout from '../components/common/layout/PageLayout';
import CourseList from '../components/course/CourseList';
import { useCourses } from '../hooks/useCourses';
import { useCurrentUser } from '../hooks/useCurrentUser';
import { useProgress } from '../hooks/useProgress';

/**
 * MainPage - Main dashboard page
 *
 * Displays a greeting, performance dashboard, and list of available courses.
 * Uses PageLayout for consistent two-column structure.
 */
const MainPage = () => {
  const { courses } = useCourses();
  const { user } = useCurrentUser();
  const { chartData } = useProgress('global');

  // Use API user data if available, otherwise fall back to stored username
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


import React, { useEffect, useRef } from 'react';
import PageLayout from '../components/common/layout/PageLayout';
import CourseList from '../components/course/CourseList';
import { useCourses } from '../hooks/useCourses';
import { useCurrentUser } from '../hooks/useCurrentUser';
import { useProgress } from '../hooks/useProgress';
import { useOnboardingContext } from '../contexts/OnboardingContext';

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
  const { user, loading: userLoading } = useCurrentUser();
  const { chartData } = useProgress('global');
  const { isFirstTime, startGuide, loading: onboardingLoading, refreshStatus } = useOnboardingContext();

  // Force refresh onboarding status when MainPage mounts (e.g., after registration/login)
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      console.log('[MainPage] Mounted with token, refreshing onboarding status...');
      refreshStatus();
    }
  }, [refreshStatus]);

  // Get user name from API response or localStorage fallback for display
  // This ensures the greeting works even if user fetch fails
  const userName = user?.username || localStorage.getItem('user_username') || 'Guest';

  // Auto-trigger onboarding for first-time users
  // Use a ref to track if we've already triggered to avoid multiple triggers
  const hasTriggeredRef = useRef(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    console.log('[MainPage] Onboarding check:', {
      isFirstTime,
      onboardingLoading,
      userLoading,
      hasToken: !!token,
      hasTriggered: hasTriggeredRef.current
    });

    // Only trigger if:
    // 1. We have a token
    // 2. Loading is complete
    // 3. User is first-time
    // 4. We haven't already triggered
    if (token && !onboardingLoading && !userLoading && isFirstTime && !hasTriggeredRef.current) {
      console.log('[MainPage] ✅ Conditions met! Auto-triggering onboarding guide for first-time user');
      hasTriggeredRef.current = true;
      
      // Delay to ensure page is fully rendered and all elements are available
      const timer = setTimeout(() => {
        console.log('[MainPage] Calling startGuide()...');
        startGuide();
      }, 1200);
      return () => clearTimeout(timer);
    } else if (!isFirstTime) {
      // Reset trigger flag if user is not first-time (e.g., after completing onboarding)
      hasTriggeredRef.current = false;
    }
  }, [isFirstTime, onboardingLoading, userLoading, startGuide]);

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


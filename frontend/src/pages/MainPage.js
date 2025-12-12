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

  // Get user name from API response or localStorage fallback for display
  // This ensures the greeting works even if user fetch fails
  const userName = user?.username || localStorage.getItem('user_username') || 'Guest';

  /**
   * Auto-triggers onboarding guide for first-time users.
   * 
   * Uses refs to prevent multiple triggers:
   * - hasTriggeredRef: Prevents duplicate triggers in same component mount
   * - timerRef: Stores timer ID to prevent premature cleanup when effect re-runs
   * 
   * The database flag (has_completed_onboarding) is the single source of truth
   * for whether a user should see onboarding.
   */
  const hasTriggeredRef = useRef(false);
  const timerRef = useRef(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    // Use user_id directly (primitive) instead of entire user object to avoid unnecessary re-renders
    const userId = user?.user_id || localStorage.getItem('user_id');

    // DEBUG: Log current state for debugging
    console.log('[MainPage] Onboarding check:', {
      isFirstTime,
      onboardingLoading,
      userLoading,
      hasToken: !!token,
      userId,
      hasTriggered: hasTriggeredRef.current,
      hasCompletedOnboarding: user?.has_completed_onboarding
    });

    // Trigger conditions (all must be true):
    // 1. Token exists
    // 2. Onboarding status check complete
    // 3. User data loaded
    // 4. User is first-time (has_completed_onboarding = false)
    // 5. Not already triggered in this mount
    // 6. Valid user_id exists
    if (token && !onboardingLoading && !userLoading && isFirstTime && !hasTriggeredRef.current && userId) {
      console.log('[MainPage] ✅ Conditions met! Auto-triggering onboarding guide for first-time user');
      hasTriggeredRef.current = true;
      
      // Clear any existing timer before setting new one
      if (timerRef.current) {
        console.log('[MainPage] Clearing existing timer before setting new one');
        clearTimeout(timerRef.current);
      }
      
      console.log('[MainPage] ⚡ About to call startGuide() in 1200ms...');
      
      // Delay to ensure page is fully rendered and all DOM elements are available
      timerRef.current = setTimeout(() => {
        console.log('[MainPage] ⚡ Calling startGuide() NOW');
        timerRef.current = null; // Clear ref when timer fires
        startGuide();
      }, 1200);
      
      return () => {
        // Only clear timer if it hasn't fired yet
        if (timerRef.current) {
          console.log('[MainPage] Cleanup: clearing startGuide timer (timer not yet fired)');
          clearTimeout(timerRef.current);
          timerRef.current = null;
        } else {
          console.log('[MainPage] Cleanup: timer already fired, no cleanup needed');
        }
      };
    } else if (!isFirstTime) {
      // Reset trigger flag if user is not first-time (e.g., after completing onboarding)
      hasTriggeredRef.current = false;
      // Clear any pending timer
      if (timerRef.current) {
        clearTimeout(timerRef.current);
        timerRef.current = null;
      }
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


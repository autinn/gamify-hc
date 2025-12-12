/**
 * useOnboarding Hook - Manages onboarding guide state and database persistence
 *
 * Provides functions to check if user is first-time, trigger guide manually,
 * and mark onboarding as completed. Uses PostgreSQL database to persist
 * completion status across devices.
 *
 * @hook
 * @returns {Object} Onboarding state and methods
 * @returns {boolean} returns.isFirstTime - True if user hasn't completed onboarding
 * @returns {boolean} returns.isActive - True if guide is currently active
 * @returns {Function} returns.startGuide - Trigger guide manually
 * @returns {Function} returns.completeOnboarding - Mark onboarding as completed
 * @returns {Function} returns.skipOnboarding - Mark onboarding as skipped (same as completed)
 * @returns {boolean} returns.loading - True while checking/updating status
 *
 * @example
 * const { isFirstTime, startGuide, completeOnboarding } = useOnboarding();
 * if (isFirstTime) startGuide();
 *
 * Used by: MainPage, Header, OnboardingGuide
 */

import { useState, useEffect, useCallback } from 'react';
import { updateOnboardingStatus, getCurrentUser } from '../services/api';
import { getStoredToken } from '../services/authService';

export function useOnboarding() {
  const [isFirstTime, setIsFirstTime] = useState(false);
  const [isActive, setIsActive] = useState(false);
  const [loading, setLoading] = useState(true);

  /**
   * Checks onboarding status by fetching user data from /auth/me endpoint.
   * The user object includes has_completed_onboarding flag which determines if user is first-time.
   * 
   * @returns {Promise<void>}
   */
  const checkOnboardingStatus = useCallback(async () => {
    try {
      setLoading(true);
      const token = getStoredToken();
      console.log('[Onboarding] Checking status. Token exists:', !!token);
      
      if (!token) {
        console.log('[Onboarding] No token found, setting loading to false');
        setLoading(false);
        setIsFirstTime(false);
        return;
      }

      console.log('[Onboarding] Fetching current user from /auth/me...');
      const currentUser = await getCurrentUser();
      console.log('[Onboarding] Current user data:', currentUser);
      
      if (currentUser && currentUser.has_completed_onboarding !== undefined) {
        // User is first-time if they haven't completed onboarding
        const isFirst = !currentUser.has_completed_onboarding;
        console.log('[Onboarding] has_completed_onboarding:', currentUser.has_completed_onboarding);
        console.log('[Onboarding] Setting isFirstTime to:', isFirst);
        setIsFirstTime(isFirst);
        setLoading(false);
        console.log('[Onboarding] Status check complete. isFirstTime:', isFirst, 'loading: false');
        return;
      } else {
        // Missing field - assume not first-time for safety
        console.warn('[Onboarding] User data missing has_completed_onboarding field. Assuming not first-time.');
        setIsFirstTime(false);
        setLoading(false);
        return;
      }
    } catch (error) {
      console.error('[Onboarding] Error checking onboarding status:', error);
      setIsFirstTime(false);
      setLoading(false);
    }
  }, []);

  /**
   * Checks onboarding status on mount and when token becomes available.
   * Uses multiple strategies to catch token storage after login/registration:
   * - Immediate check on mount
   * - Polling at 500ms, 1000ms, 2000ms intervals
   * - Listening for localStorage storage events (cross-tab)
   * - Listening for custom 'token-stored' event (same-tab)
   */
  useEffect(() => {
    let mounted = true;
    
    const performCheck = async () => {
      const token = getStoredToken();
      if (token) {
        console.log('[Onboarding] Token available, checking status...');
        if (mounted) {
          await checkOnboardingStatus();
        }
      } else {
        console.log('[Onboarding] No token yet, will check again...');
        if (mounted) {
          setLoading(false);
          setIsFirstTime(false);
        }
      }
    };

    // Check immediately
    performCheck();

    // Poll at intervals to catch async token storage (important after login)
    const timers = [
      setTimeout(() => mounted && performCheck(), 500),
      setTimeout(() => mounted && performCheck(), 1000),
      setTimeout(() => mounted && performCheck(), 2000),
    ];

    // Listen for localStorage changes (cross-tab only - storage event doesn't fire in same tab)
    const handleStorageChange = (e) => {
      if (e.key === 'token' && e.newValue && mounted) {
        console.log('[Onboarding] Token detected via storage event, checking status...');
        performCheck();
      }
    };
    window.addEventListener('storage', handleStorageChange);

    // Listen for custom event triggered after login/registration (same-tab)
    const handleTokenSet = () => {
      if (mounted) {
        console.log('[Onboarding] Token set event received, checking status...');
        performCheck();
      }
    };
    window.addEventListener('token-stored', handleTokenSet);

    return () => {
      mounted = false;
      timers.forEach(timer => clearTimeout(timer));
      window.removeEventListener('storage', handleStorageChange);
      window.removeEventListener('token-stored', handleTokenSet);
    };
  }, [checkOnboardingStatus]);

  /**
   * Marks onboarding as completed in the database.
   * Updates the has_completed_onboarding flag to true, which persists globally across devices.
   * Also updates local state and refreshes status to confirm the update.
   * 
   * @returns {Promise<void>}
   */
  const completeOnboarding = useCallback(async () => {
    try {
      const token = getStoredToken();
      if (!token) {
        console.warn('[Onboarding] Cannot complete: no token');
        return;
      }

      const currentUser = await getCurrentUser();
      if (!currentUser || !currentUser.user_id) {
        console.warn('[Onboarding] Cannot complete: no user_id');
        return;
      }

      const userId = currentUser.user_id;
      
      // Update database: set has_completed_onboarding = true (global, persistent)
      await updateOnboardingStatus(userId, true);
      
      // Update local state immediately for responsive UI
      setIsFirstTime(false);
      setIsActive(false);
      
      // Refresh status from database to confirm update
      await checkOnboardingStatus();
    } catch (error) {
      console.error('[Onboarding] Error updating onboarding status:', error);
    }
  }, [checkOnboardingStatus]);

  /**
   * Skips onboarding (same as completing it).
   * Marks onboarding as completed in the database.
   * 
   * @returns {Promise<void>}
   */
  const skipOnboarding = useCallback(async () => {
    await completeOnboarding();
  }, [completeOnboarding]);

  /**
   * Starts the onboarding guide manually.
   * Works regardless of first-time status (can be triggered via help button).
   * 
   * @returns {void}
   */
  const startGuide = useCallback(() => {
    console.log('[Onboarding] 🚀 startGuide() called - setting isActive to true');
    setIsActive(true);
  }, []);

  return {
    isFirstTime,
    isActive,
    startGuide,
    completeOnboarding,
    skipOnboarding,
    loading,
    setIsActive, // Allow component to control active state
    refreshStatus: checkOnboardingStatus, // Allow manual refresh
  };
}


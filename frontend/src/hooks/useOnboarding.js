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

  // Simple check: get user data from /auth/me which includes has_completed_onboarding
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
        const isFirst = !currentUser.has_completed_onboarding;
        console.log('[Onboarding] has_completed_onboarding:', currentUser.has_completed_onboarding);
        console.log('[Onboarding] Setting isFirstTime to:', isFirst);
        setIsFirstTime(isFirst);
      } else {
        console.warn('[Onboarding] User data missing has_completed_onboarding field. Assuming not first-time.');
        setIsFirstTime(false);
      }
    } catch (error) {
      console.error('[Onboarding] Error checking onboarding status:', error);
      console.error('[Onboarding] Error details:', error.message, error.stack);
      setIsFirstTime(false);
    } finally {
      setLoading(false);
      console.log('[Onboarding] Status check complete. Final state - loading: false, isFirstTime:', isFirstTime);
    }
  }, []);

  // Check status on mount and whenever token becomes available
  // This handles both initial load and after login/registration
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

    // Also check after delays to catch async token storage (important after login)
    const timers = [
      setTimeout(() => mounted && performCheck(), 500),
      setTimeout(() => mounted && performCheck(), 1000),
      setTimeout(() => mounted && performCheck(), 2000),
    ];

    // Listen for localStorage changes (when token is set)
    // Note: storage event only fires for OTHER tabs, so we also poll
    const handleStorageChange = (e) => {
      if (e.key === 'token' && e.newValue && mounted) {
        console.log('[Onboarding] Token detected via storage event, checking status...');
        performCheck();
      }
    };
    window.addEventListener('storage', handleStorageChange);

    // Also listen for custom event we can trigger after login
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

  // Mark onboarding as completed in database
  const completeOnboarding = useCallback(async () => {
    try {
      const token = getStoredToken();
      if (!token) {
        console.warn('[Onboarding] Cannot complete: no token');
        return;
      }

      // Get user_id from current user
      const currentUser = await getCurrentUser();
      if (!currentUser || !currentUser.user_id) {
        console.warn('[Onboarding] Cannot complete: no user_id');
        return;
      }

      const userId = currentUser.user_id;
      console.log('[Onboarding] Marking onboarding as completed for user:', userId);
      await updateOnboardingStatus(userId, true);
      
      setIsFirstTime(false);
      setIsActive(false);
      console.log('[Onboarding] Onboarding marked as completed');
    } catch (error) {
      console.error('[Onboarding] Error updating onboarding status:', error);
    }
  }, []);

  // Skip onboarding (same as complete)
  const skipOnboarding = useCallback(async () => {
    await completeOnboarding();
  }, [completeOnboarding]);

  // Start guide manually (works regardless of first-time status)
  const startGuide = useCallback(() => {
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


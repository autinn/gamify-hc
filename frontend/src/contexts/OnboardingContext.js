/**
 * OnboardingContext - Context for managing onboarding guide state globally
 *
 * Provides shared state and methods for triggering and managing the onboarding guide
 * across all components in the application.
 *
 * @module OnboardingContext
 */

import React, { createContext, useContext } from 'react';
import { useOnboarding } from '../hooks/useOnboarding';

const OnboardingContext = createContext(null);

/**
 * OnboardingProvider - Context provider for onboarding state
 *
 * Wraps the application and provides onboarding state and methods to all children.
 *
 * @component
 * @param {React.ReactNode} children - Child components
 * @returns {React.ReactNode} Context provider
 */
export function OnboardingProvider({ children }) {
  const onboarding = useOnboarding();

  return (
    <OnboardingContext.Provider value={onboarding}>
      {children}
    </OnboardingContext.Provider>
  );
}

/**
 * useOnboardingContext - Hook to access onboarding context
 *
 * @returns {Object} Onboarding state and methods
 * @throws {Error} If used outside OnboardingProvider
 */
export function useOnboardingContext() {
  const context = useContext(OnboardingContext);
  if (!context) {
    throw new Error('useOnboardingContext must be used within OnboardingProvider');
  }
  return context;
}


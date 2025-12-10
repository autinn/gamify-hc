/**
 * OnboardingGuide - Interactive onboarding tour using react-joyride
 *
 * Provides a step-by-step guide through the application's key features.
 * Can be triggered automatically for first-time users or manually via help button.
 *
 * @component
 * @param {boolean} isActive - Whether the guide should be active
 * @param {Function} onComplete - Callback when guide is completed
 * @param {Function} onSkip - Callback when guide is skipped
 * @param {Function} setIsActive - Function to control active state
 * @returns {React.ReactNode} Joyride component with tour steps
 *
 * Tour Steps:
 * 1. Main Page: Home button and course navigation
 * 2. Main Page: Course cards
 * 3. Main Page: Start Quiz button
 * 4. Main Page: Progress chart
 * 5. Course Page: Unit navigation
 * 6. Unit Page: Concept navigation
 * 7. Concept Page: Content structure
 * 8. Header: Navigation bar
 *
 * Used by: MainPage, App (or PageLayout)
 */

import React, { useState, useEffect } from 'react';
import Joyride from 'react-joyride';
import { useLocation } from 'react-router-dom';
import './OnboardingGuide.css';

const OnboardingGuide = ({ isActive, onComplete, onSkip, setIsActive }) => {
  const location = useLocation();
  const [run, setRun] = useState(false);
  const [resetKey, setResetKey] = useState(0);

  // DEBUG: Log when isActive prop changes
  useEffect(() => {
    console.log('[OnboardingGuide] 🔔 isActive prop changed to:', isActive);
  }, [isActive]);

  /**
   * Generates tour steps based on the current page path.
   * Each page type (main, course, unit, concept) has its own set of steps.
   * The welcome step is shown first on the main page.
   * 
   * @returns {Array} Array of step objects for react-joyride
   */
  const getSteps = () => {
    const path = location.pathname;
    
    // Welcome step (shown first on all pages)
    const welcomeStep = {
      target: 'body',
      content: 'Welcome to Gamify HC, an app with scenario-based questions to help you understand Minerva HCs better.',
      placement: 'center',
      disableBeacon: true,
    };
    
    // Main page steps
    if (path === '/') {
      return [
        welcomeStep,
        {
          target: '.header__home-button',
          content: 'Use the Home button to return to the main dashboard anytime.',
          placement: 'bottom',
          disableBeacon: true,
        },
        {
          target: '.course-card',
          content: 'Click on any card to explore the units and concepts within that course.',
          placement: 'right',
          disableBeacon: true,
        },
        {
          target: '.page-layout__button-container',
          content: 'The "Start Quiz" button lets you test your knowledge. You can take quizzes at the course, unit, or concept level. You can also take quizzes for all courses at once.',
          placement: 'left',
          disableBeacon: true,
        },
        {
            target: '.page-layout__button-container',
            content: 'The quiz is not timed, so take it easy! You have unlimited attempts to get the questions right but only your first attempt will be counted for your progress.',
            placement: 'left',
            disableBeacon: true,
        },
        {
          target: '.performance-chart',
          content: 'This progress chart shows your success rate. It displays how well you\'re performing across courses, units, or concepts. The higher the bar, the better your performance!',
          placement: 'left',
          disableBeacon: true,
        },
        {
          target: '.header__course-nav',
          content: 'Use the navigation bar at the top to quickly jump between courses and units. Hover over a course to see its units.',
          placement: 'bottom',
          disableBeacon: true,
        },
      ];
    }
    
    // Course page steps
    if (path.match(/^\/course\/\d+$/)) {
      return [
        {
          target: '.unit-card',
          content: 'Click on a unit card to explore the concepts within that unit.',
          placement: 'right',
          disableBeacon: true,
        },
        {
          target: '.page-layout__button-container',
          content: 'Start a quiz for this specific course to test your knowledge across all units.',
          placement: 'left',
          disableBeacon: true,
        },
        {
          target: '.performance-chart',
          content: 'This chart shows your success rate for this course across all units.',
          placement: 'left',
          disableBeacon: true,
        },
      ];
    }
    
    // Unit page steps
    if (path.match(/^\/course\/\d+\/unit\/\d+$/)) {
      return [
        {
          target: '.concept-card',
          content: 'Click on a concept card to study the materials and questions for that concept.',
          placement: 'right',
          disableBeacon: true,
        },
        {
          target: '.page-layout__button-container',
          content: 'Start a quiz for this unit to test your knowledge of all concepts.',
          placement: 'left',
          disableBeacon: true,
        },
        {
          target: '.performance-chart',
          content: 'This chart shows your success rate for this unit across all concepts.',
          placement: 'left',
          disableBeacon: true,
        },
      ];
    }
    
    // Concept page steps
    if (path.match(/^\/course\/\d+\/unit\/\d+\/concept\/\d+$/)) {
      return [
        {
          target: '.concept-page__content',
          content: 'Here you can study the questions and answers for this concept. Review the materials before taking the quiz.',
          placement: 'top',
          disableBeacon: true,
        },
        {
          target: '.concept-page__button-container',
          content: 'When you\'re ready, click "Start Quiz" to test your understanding of this concept.',
          placement: 'left',
          disableBeacon: true,
        },
      ];
    }
    
    // Default: no steps for other pages
    return [];
  };

  const steps = getSteps();
  
  // DEBUG: Log steps for current page
  useEffect(() => {
    console.log('[OnboardingGuide] Steps for current page:', steps.length, 'path:', location.pathname);
    if (steps.length === 0) {
      console.warn('[OnboardingGuide] ⚠️ No steps available for path:', location.pathname);
    }
  }, [steps.length, location.pathname]);

  /**
   * Starts/stops the guide based on isActive prop.
   * When starting, increments resetKey to force react-joyride to remount and start from step 0.
   * Uses a brief delay to ensure clean reset before starting.
   */
  useEffect(() => {
    console.log('[OnboardingGuide] Effect triggered - isActive:', isActive, 'steps.length:', steps.length);
    if (isActive && steps.length > 0) {
      console.log('[OnboardingGuide] ✅ Starting guide! Resetting and will run in 100ms');
      // Increment resetKey to force react-joyride to remount and start from step 0
      setResetKey(prev => prev + 1);
      setRun(false);
      // Restart after a brief delay to ensure clean reset
      const timer = setTimeout(() => {
        console.log('[OnboardingGuide] ⚡ Setting run=true NOW');
        setRun(true);
      }, 100);
      return () => {
        console.log('[OnboardingGuide] Cleanup: clearing start timer');
        clearTimeout(timer);
      };
    } else {
      if (isActive && steps.length === 0) {
        console.warn('[OnboardingGuide] ❌ Cannot start: isActive=true but steps.length=0');
      } else if (!isActive) {
        console.log('[OnboardingGuide] ❌ Not starting: isActive=false');
      }
      setRun(false);
    }
  }, [isActive, steps.length, location.pathname]);

  /**
   * Resets the tour when location changes (user navigates to different page).
   * Increments resetKey to force react-joyride to reset to the first step with new steps.
   */
  useEffect(() => {
    if (run && steps.length > 0) {
      setResetKey(prev => prev + 1);
      setRun(false);
      const timer = setTimeout(() => {
        setRun(true);
      }, 100);
      return () => clearTimeout(timer);
    }
  }, [location.pathname, run, steps.length]);

  /**
   * Handles react-joyride callback events.
   * Manages guide state when user closes, completes, or skips the tour.
   * 
   * @param {Object} data - Callback data from react-joyride
   * @param {string} data.action - Action type (e.g., 'close')
   * @param {string} data.status - Status (e.g., 'finished', 'skipped')
   */
  const handleJoyrideCallback = (data) => {
    const { action, status } = data;

    // Handle close button (X button)
    if (action === 'close') {
      setRun(false);
      setIsActive(false);
      if (onSkip) {
        onSkip();
      }
      return;
    }

    // Handle completion or skip
    if (status === 'finished' || status === 'skipped') {
      setRun(false);
      setIsActive(false);
      
      if (status === 'finished' && onComplete) {
        onComplete();
      } else if (status === 'skipped' && onSkip) {
        onSkip();
      }
      return;
    }
  };

  // Don't render if no steps available for current page
  if (steps.length === 0) {
    return null;
  }

  return (
    <Joyride
      key={resetKey}
      steps={steps}
      run={run}
      continuous={true}
      showProgress={true}
      showSkipButton={true}
      disableScrolling={true}
      scrollToFirstStep={false}
      callback={handleJoyrideCallback}
      styles={{
        options: {
          primaryColor: '#333',
          zIndex: 10000,
        },
        tooltip: {
          borderRadius: 8,
          fontSize: 14,
        },
        buttonNext: {
          backgroundColor: '#333',
          color: '#fff',
          borderRadius: 4,
          padding: '8px 16px',
        },
        buttonBack: {
          color: '#333',
          marginRight: 8,
        },
        buttonSkip: {
          color: '#666',
        },
      }}
      floaterProps={{
        disableAnimation: false,
      }}
      locale={{
        back: 'Back',
        close: 'Close',
        last: 'Got it!',
        next: 'Next',
        skip: 'Skip',
      }}
    />
  );
};

export default OnboardingGuide;


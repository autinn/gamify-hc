import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import MainPage from './pages/MainPage';
import CoursePage from './pages/CoursePage';
import UnitPage from './pages/UnitPage';
import ConceptPage from './pages/ConceptPage';
import QuizPage from './pages/QuizPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import ProtectedRoute from './components/common/ProtectedRoute';
import { OnboardingProvider, useOnboardingContext } from './contexts/OnboardingContext';
import OnboardingGuide from './components/common/OnboardingGuide';
import { getAuthToken } from './services/api';
import './App.css';

/**
 * App - Root application component with routing configuration
 *
 * Defines all application routes with authentication protection via ProtectedRoute.
 * Routes organized into public (login/register) and protected (authenticated user only) paths.
 * Supports hierarchical quiz paths: course-level, unit-level, and concept-level quizzes.
 *
 * @component
 * @returns {React.ReactNode} Router with all application routes
 *
 * Route Structure:
 *
 * PUBLIC ROUTES (no authentication required):
 * - /login: LoginPage component for existing users
 * - /register: RegisterPage component for new user registration
 *
 * PROTECTED ROUTES (authentication required via ProtectedRoute wrapper):
 *
 * Hierarchy Routes:
 * - / : MainPage - Main dashboard with course list
 * - /course/:courseId : CoursePage - Course details with units
 * - /course/:courseId/unit/:unitId : UnitPage - Unit details with concepts
 * - /course/:courseId/unit/:unitId/concept/:conceptId : ConceptPage - Concept study materials
 *
 * Quiz Routes (support all hierarchy levels):
 * - /quiz : All courses quiz (full course assessment)
 * - /course/:courseId/quiz : Course-level quiz
 * - /course/:courseId/unit/:unitId/quiz : Unit-level quiz
 * - /course/:courseId/unit/:unitId/concept/:conceptId/quiz : Concept-level quiz
 *
 * Default Route:
 * - * (wildcard): Redirects based on authentication status
 *   - If authenticated (getAuthToken() returns true): Redirect to /
 *   - If not authenticated: Redirect to /login
 *
 * Authentication:
 * - ProtectedRoute wrapper checks JWT token validity
 * - Redirects unauthenticated users to /login
 * - Automatic token refresh handled by API service
 *
 * URL Parameter Types:
 * - courseId: Numeric or string course identifier from database
 * - unitId: Numeric or string unit identifier (unique within course)
 * - conceptId: Numeric or string concept identifier (unique within unit)
 *
 * @example
 * <App />
 * // Sets up BrowserRouter with complete navigation structure
 * // Public users see login/register pages
 * // Authenticated users see full course/unit/concept/quiz hierarchy
 */

function App() {
  return (
    <OnboardingProvider>
      <Router>
        <Routes>
        {/* ============================================================================ */}
        {/* PUBLIC ROUTES - No authentication required */}
        {/* ============================================================================ */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        
        {/* ============================================================================ */}
        {/* PROTECTED ROUTES - Require valid authentication token */}
        {/* ============================================================================ */}
        
        {/* Main Page - Dashboard with course list */}
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <MainPage />
            </ProtectedRoute>
          }
        />
        
        {/* Course Details - Shows units for specific course */}
        <Route
          path="/course/:courseId"
          element={
            <ProtectedRoute>
              <CoursePage />
            </ProtectedRoute>
          }
        />
        
        {/* Unit Details - Shows concepts for specific unit */}
        <Route
          path="/course/:courseId/unit/:unitId"
          element={
            <ProtectedRoute>
              <UnitPage />
            </ProtectedRoute>
          }
        />
        
        {/* Concept Details - Shows study materials (questions/answers) for concept */}
        <Route
          path="/course/:courseId/unit/:unitId/concept/:conceptId"
          element={
            <ProtectedRoute>
              <ConceptPage />
            </ProtectedRoute>
          }
        />
        
        {/* ============================================================================ */}
        {/* QUIZ ROUTES - Support multiple hierarchy levels */}
        {/* ============================================================================ */}
        
        {/* All courses quiz */}
        <Route
          path="/quiz"
          element={
            <ProtectedRoute>
              <QuizPage />
            </ProtectedRoute>
          }
        />
        
        {/* Course-level quiz */}
        <Route
          path="/course/:courseId/quiz"
          element={
            <ProtectedRoute>
              <QuizPage />
            </ProtectedRoute>
          }
        />
        
        {/* Unit-level quiz */}
        <Route
          path="/course/:courseId/unit/:unitId/quiz"
          element={
            <ProtectedRoute>
              <QuizPage />
            </ProtectedRoute>
          }
        />
        
        {/* Concept-level quiz */}
        <Route
          path="/course/:courseId/unit/:unitId/concept/:conceptId/quiz"
          element={
            <ProtectedRoute>
              <QuizPage />
            </ProtectedRoute>
          }
        />
        
        {/* ============================================================================ */}
        {/* DEFAULT ROUTE - Redirect based on authentication status */}
        {/* ============================================================================ */}
        <Route
          path="*"
          element={
            getAuthToken() ? <Navigate to="/" replace /> : <Navigate to="/login" replace />
          }
        />
      </Routes>
      <OnboardingGuideWrapper />
      </Router>
    </OnboardingProvider>
  );
}

/**
 * OnboardingGuideWrapper - Wrapper component to access onboarding context
 * 
 * Renders OnboardingGuide with access to the onboarding context.
 * Must be inside Router to use useLocation hook in OnboardingGuide.
 */
function OnboardingGuideWrapper() {
  const { isActive, setIsActive, completeOnboarding, skipOnboarding } = useOnboardingContext();
  
  return (
    <OnboardingGuide
      isActive={isActive}
      setIsActive={setIsActive}
      onComplete={completeOnboarding}
      onSkip={skipOnboarding}
    />
  );
}

export default App;

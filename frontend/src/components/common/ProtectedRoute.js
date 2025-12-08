import React from 'react';
import { Navigate } from 'react-router-dom';
import { getAuthToken } from '../../services/api';

/**
 * ProtectedRoute - Route guard component for authenticated-only pages
 *
 * Checks authentication status before rendering protected content.
 * Redirects unauthenticated users to login page. Preserves return path
 * in URL for post-login redirect (if implemented).
 *
 * @component
 * @param {React.ReactNode} children - Page component to render if authenticated
 * @returns {React.ReactNode} Protected page or redirect to login
 *
 * @example
 * <Route
 *   path="/dashboard"
 *   element={
 *     <ProtectedRoute>
 *       <DashboardPage />
 *     </ProtectedRoute>
 *   }
 * />
 *
 * Used by: App.js route definitions
 */
const ProtectedRoute = ({ children }) => {
  const token = getAuthToken();

  // Redirect to login if user is not authenticated
  if (!token) {
    return <Navigate to="/login" replace />;
  }

  // Render protected component if authenticated
  return children;
};

export default ProtectedRoute;


import React from 'react';
import { Navigate } from 'react-router-dom';
import { getAuthToken } from '../../services/api';

/**
 * ProtectedRoute - Route protection component
 *
 * Checks if user is authenticated by verifying token in localStorage.
 * If not authenticated, redirects to login page.
 * If authenticated, renders the protected component.
 */
const ProtectedRoute = ({ children }) => {
  const token = getAuthToken();

  if (!token) {
    // Redirect to login if not authenticated
    return <Navigate to="/login" replace />;
  }

  // Render protected component if authenticated
  return children;
};

export default ProtectedRoute;


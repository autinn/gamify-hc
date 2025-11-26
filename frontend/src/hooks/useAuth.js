/**
 * useAuth Hook
 * 
 * Manages authentication state and login/register logic.
 * Handles form validation, API communication, and token storage.
 * 
 * @component
 * @returns {Object} Auth object
 * @returns {Function} returns.login - Login function(email, password) - validates email/password, calls API, stores token
 * @returns {Function} returns.register - Register function(username, email, password, passwordConfirm) - validates form, calls API, stores token
 * @returns {string} returns.error - Current error message (empty string if no error)
 * @returns {boolean} returns.loading - Loading state (true while API call is in progress)
 * @returns {Function} returns.setError - Function to manually set error message
 * 
 * @example
 * const { login, register, error, loading } = useAuth();
 * 
 * // Login
 * await login('user@minerva.edu', 'password123');
 * 
 * // Register
 * await register('username', 'user@minerva.edu', 'password123', 'password123');
 * 
 * Used by: LoginPage, RegisterPage
 */

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import * as api from '../services/api';
import {
  validateLoginForm,
  validateRegisterForm,
  storeAuthData
} from '../services/authService';

export function useAuth() {
  const navigate = useNavigate();
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const login = async (email, password) => {
    setError('');
    setLoading(true);

    try {
      const normalizedEmail = email.trim().toLowerCase();

      // Validate form
      const validation = validateLoginForm(normalizedEmail, password);
      if (!validation.valid) {
        setError(validation.error);
        setLoading(false);
        return;
      }

      // Call login API - backend accepts email in username field
      const data = await api.login(normalizedEmail, password);

      // Store token and user data
      storeAuthData(data);

      // Navigate to home
      navigate('/');
    } catch (err) {
      const errorMessage = err.data?.error || err.message || 'Login failed. Please try again.';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const register = async (username, email, password, passwordConfirm) => {
    setError('');
    setLoading(true);

    try {
      const normalizedEmail = email.trim().toLowerCase();

      // Validate form
      const validation = validateRegisterForm(username, normalizedEmail, password, passwordConfirm);
      if (!validation.valid) {
        setError(validation.error);
        setLoading(false);
        return;
      }

      // Call register API
      const data = await api.register(username, normalizedEmail, password);

      // Store token and user data
      storeAuthData(data);

      // Navigate to home
      navigate('/');
    } catch (err) {
      const errorMessage = err.data?.error || err.message || 'Registration failed. Please try again.';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return {
    login,
    register,
    error,
    loading,
    setError
  };
}

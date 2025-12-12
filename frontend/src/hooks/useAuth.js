/**
 * useAuth Hook - Authentication state management
 *
 * Manages user login and registration with form validation and token handling.
 * Provides error reporting and loading states for async operations.
 *
 * @hook
 * @returns {Object} Auth methods and state
 * @returns {Function} returns.login - Async login function(email, password)
 * @returns {Function} returns.register - Async register function(username, email, password, passwordConfirm)
 * @returns {string} returns.error - Error message if login/register failed
 * @returns {boolean} returns.loading - True while request in flight
 * @returns {Function} returns.setError - Manually clear error message
 *
 * @example
 * const { login, error, loading } = useAuth();
 * await login('user@minerva.edu', 'password123');
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
      console.log('[Auth] Login response:', {
        hasAccessToken: !!data.access_token,
        userId: data.user_id,
        username: data.username
      });

      // Store token and user data
      storeAuthData(data);
      console.log('[Auth] Token stored in localStorage:', !!localStorage.getItem('token'));

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
      console.log('[Auth] Registration response:', {
        hasAccessToken: !!data.access_token,
        userId: data.user_id,
        username: data.username,
        email: data.email
      });

      // Note: We don't store the token here since user needs to manually log in
      // The backend returns a token, but we'll let user log in manually
      // Navigate to login page for manual login
      navigate('/login');
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

/**
 * useCurrentUser Hook - Current logged-in user data management
 *
 * Fetches and caches the authenticated user's profile information from the backend.
 * Validates token presence before making request. Falls back gracefully if fetch fails.
 *
 * @hook
 * @returns {Object} User data and state
 * @returns {Object|null} returns.user - User object {user_id, username, email, ...}
 * @returns {boolean} returns.loading - True while fetching (initial load only)
 * @returns {string|null} returns.error - Error message if fetch failed, null on success
 *
 * @example
 * const { user, loading, error } = useCurrentUser();
 * if (loading) return <Loading />;
 * if (error) return <Error message={error} />;
 * return <UserGreeting name={user.username} />;
 *
 * Used by: MainPage, Header, and authenticated pages
 */

import { useState, useEffect } from 'react';
import * as api from '../services/api';

export function useCurrentUser() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCurrentUser = async () => {
      try {
        setLoading(true);
        const token = localStorage.getItem('token');
        console.log('Token in hook:', token ? 'exists' : 'missing');
        
        if (!token) {
          console.warn('No token found in localStorage');
          setUser(null);
          setLoading(false);
          return;
        }

        const userData = await api.getCurrentUser();
        console.log('Current user data:', userData);
        setUser(userData);
        setError(null);
      } catch (err) {
        console.error('Error fetching current user:', err);
        setError(err.message || 'Failed to fetch user data');
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

    fetchCurrentUser();
  }, []);

  return {
    user,
    loading,
    error
  };
}

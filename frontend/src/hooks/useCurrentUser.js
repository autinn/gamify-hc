/**
 * useCurrentUser Hook
 * 
 * Fetches the currently logged-in user's profile data from the database.
 * Uses the JWT token from localStorage to identify and authenticate the user.
 * Returns null if no token is found (user is not logged in).
 * 
 * @component
 * @returns {Object} Current user data object
 * @returns {Object|null} returns.user - Current user object {user_id, username, email, created_at} or null if not logged in
 * @returns {boolean} returns.loading - True while user data is being fetched
 * @returns {Error|null} returns.error - Error object if fetch failed or user not authenticated
 * 
 * @example
 * const { user, loading, error } = useCurrentUser();
 * 
 * if (loading) return <div>Loading...</div>;
 * if (error) return <div>Not authenticated</div>;
 * if (!user) return <div>Please log in</div>;
 * 
 * return <div>Welcome, {user.username}!</div>;
 * 
 * Used by: MainPage, Header, and other authenticated pages
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

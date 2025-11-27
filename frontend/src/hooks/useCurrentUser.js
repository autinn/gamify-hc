/**
 * useCurrentUser Hook
 * 
 * Fetches the current logged-in user's data from the database.
 * Returns user information including username, email, etc.
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

import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import './AuthPage.css';

/**
 * LoginPage - User authentication login page
 *
 * Displays email and password form for user login. Integrates with useAuth hook
 * for authentication logic and error handling. On successful login, user is redirected
 * to MainPage (dashboard). New users are directed to RegisterPage.
 *
 * @component
 * @returns {React.ReactNode} Login form with email/password inputs and submit button
 *
 * Form Inputs:
 * - Email field: type="email", placeholder shows example format
 * - Password field: type="password" with bullet placeholder
 * - Submit button: "Log In" (or "Logging in..." while request in progress)
 *
 * Features:
 * - Uses useAuth hook for login(email, password) function
 * - Displays error messages from authentication failures
 * - Disables inputs and button while login request is processing (loading state)
 * - Link to /register for new user registration
 * - Clear error on each submit attempt
 *
 * Auth Integration:
 * - Calls login(email, password) from useAuth hook
 * - Displays error message if authentication fails
 * - Automatic redirect to MainPage on successful login (handled by ProtectedRoute)
 *
 * CSS Classes:
 * - auth-container: Main page wrapper
 * - auth-card: Centered card with form
 * - auth-title: "Gamify-HC" branding
 * - auth-subtitle: "Log In" heading
 * - auth-error: Error message display
 * - auth-form: Form container
 * - form-group: Input field wrapper
 * - form-label: Input labels
 * - form-input: Text/password inputs (disabled during loading)
 * - auth-button: Submit button (disabled during loading)
 * - auth-footer: "Sign up" link area
 * - auth-link: Styled link to register page
 *
 * @example
 * <LoginPage />
 * // Displays: Email/password form with Gamify-HC branding
 *
 * Navigation:
 * - Success: Automatic redirect to MainPage
 * - New user: Link to /register (RegisterPage)
 *
 * Used by: AuthPage route configuration (usually at /login)
 */
const LoginPage = () => {
  const { login, error, loading, setError } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Clear any previous error messages
    await login(email, password); // Attempt authentication with provided credentials
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h1 className="auth-title">Gamify-HC</h1>
        <h2 className="auth-subtitle">Log In</h2>

        {error && <div className="auth-error">{error}</div>}

        <form onSubmit={handleSubmit} className="auth-form">
          <div className="form-group">
            <label htmlFor="email" className="form-label">Email</label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="email@uni.minerva.edu"
              className="form-input"
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password" className="form-label">Password</label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              className="form-input"
              disabled={loading}
            />
          </div>

          <button
            type="submit"
            className="auth-button"
            disabled={loading}
          >
            {loading ? 'Logging in...' : 'Log In'}
          </button>
        </form>

        <p className="auth-footer">
          Don't have an account?{' '}
          <Link to="/register" className="auth-link">
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;

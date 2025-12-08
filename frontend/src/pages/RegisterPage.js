import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import './AuthPage.css';

/**
 * RegisterPage - User registration/account creation page
 *
 * Displays form for new users to create an account. Requires username, email,
 * password, and password confirmation. Integrates with useAuth hook for registration logic.
 * On successful registration, user is redirected to MainPage (dashboard).
 * Existing users are directed to LoginPage.
 *
 * @component
 * @returns {React.ReactNode} Registration form with username, email, and password inputs
 *
 * Form Fields:
 * - Username: text input for account username
 * - Email: email input validated by server (checked for uniqueness)
 * - Password: password input with bullet placeholder
 * - Confirm Password: password confirmation for verification
 * - Submit button: "Sign Up" (or "Creating account..." while processing)
 *
 * Features:
 * - Uses useAuth hook for register(username, email, password, confirmPassword) function
 * - Client-side password confirmation field included for UX
 * - Server performs actual validation (email uniqueness, password requirements)
 * - Displays error messages from registration failures
 * - Disables inputs and button while registration request is processing (loading state)
 * - Link to /login for existing users
 * - Clear error on each submit attempt
 *
 * Form Handling:
 * - Uses formData state object to manage all four input fields
 * - handleChange updates formData for any input field change
 * - handleSubmit extracts fields and calls register function
 *
 * Auth Integration:
 * - Calls register(username, email, password, confirmPassword) from useAuth hook
 * - Displays error message if registration fails (duplicate email, password mismatch, etc.)
 * - Automatic redirect to MainPage on successful registration (handled by ProtectedRoute)
 *
 * CSS Classes:
 * - auth-container: Main page wrapper
 * - auth-card: Centered card with form
 * - auth-title: "Gamify-HC" branding
 * - auth-subtitle: "Create Account" heading
 * - auth-error: Error message display
 * - auth-form: Form container
 * - form-group: Input field wrapper
 * - form-label: Input labels
 * - form-input: Text/email/password inputs (disabled during loading)
 * - auth-button: Submit button (disabled during loading)
 * - auth-footer: "Sign in" link area
 * - auth-link: Styled link to login page
 *
 * @example
 * <RegisterPage />
 * // Displays: Username, email, password form with Gamify-HC branding
 *
 * Navigation:
 * - Success: Automatic redirect to MainPage
 * - Existing user: Link to /login (LoginPage)
 *
 * Used by: AuthPage route configuration (usually at /register)
 */
const RegisterPage = () => {
  const { register, error, loading, setError } = useAuth();
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    // Update formData object for whichever field changed
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Clear any previous error messages
    const { username, email, password, confirmPassword } = formData;
    // Attempt registration with provided credentials (server validates password matching)
    await register(username, email, password, confirmPassword);
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h1 className="auth-title">Gamify-HC</h1>
        <h2 className="auth-subtitle">Create Account</h2>

        {error && <div className="auth-error">{error}</div>}

        <form onSubmit={handleSubmit} className="auth-form">
          <div className="form-group">
            <label htmlFor="username" className="form-label">Username</label>
            <input
              id="username"
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              placeholder="Choose a username"
              className="form-input"
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="email" className="form-label">Email</label>
            <input
              id="email"
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
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
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="••••••••"
              className="form-input"
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="confirmPassword" className="form-label">Confirm Password</label>
            <input
              id="confirmPassword"
              type="password"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
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
            {loading ? 'Creating account...' : 'Sign Up'}
          </button>
        </form>

        <p className="auth-footer">
          Already have an account?{' '}
          <Link to="/login" className="auth-link">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
};

export default RegisterPage;

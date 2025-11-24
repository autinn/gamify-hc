import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import './AuthPage.css';

/**
 * LoginPage - User login page
 *
 * Allows users to log in with email and password.
 * On successful login, redirects to the main dashboard.
 * Includes link to register page for new users.
 */
const LoginPage = () => {
  const { login, error, loading, setError } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    await login(email, password);
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

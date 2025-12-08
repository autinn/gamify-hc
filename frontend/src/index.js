import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

/**
 * Application Entry Point
 *
 * Initializes React 18 root and renders the App component into the DOM.
 * Enables React StrictMode for development warnings and checks.
 * Optionally tracks web performance metrics via reportWebVitals.
 *
 * React StrictMode Benefits:
 * - Identifies potential problems in development
 * - Warns about deprecated lifecycle methods
 * - Detects unexpected side effects
 * - Only active in development mode (stripped in production build)
 *
 * Performance Monitoring:
 * - reportWebVitals() can be called with a callback (e.g., console.log or analytics)
 * - Tracks metrics: LCP, FID, TTFB, CLS, INP
 * - Uncomment below to enable: reportWebVitals(console.log);
 */
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Optional: Measure and track application performance metrics
// Useful for analytics, monitoring, or debugging performance issues
// reportWebVitals(console.log);
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

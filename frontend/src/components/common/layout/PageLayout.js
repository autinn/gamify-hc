import React from 'react';
import Header from './Header.js';
import Button from '../UI/Button';
import { useNavigate } from 'react-router-dom';
import PerformanceChart from '../Charts/PerformanceChart';
import './PageLayout.css';

/**
 * PageLayout - Reusable two-column layout component
 *
 * Provides consistent spacing and structure across MainPage, CoursePage, and UnitPage.
 * Left column contains greeting text, title, Start Quiz button, and chart.
 * Right column contains dynamic content (courses, units, or concepts).
 *
 * @param {string} greeting - Small greeting text (e.g., "Hello,", "Welcome to")
 * @param {string} title - Main title text (e.g., "NAME", "EA50", "Problem-Solving")
 * @param {boolean} showButton - Whether to display the Start Quiz button
 * @param {object} chartData - Data object for PerformanceChart (label, values, etc.)
 * @param {string} chartLabel - Label/description for the chart (e.g., "EA FA MC CX")
 * @param {React.ReactNode} rightContent - Content for right column (CourseList, UnitList, ConceptList, etc.)
 */
const PageLayout = ({
  greeting,
  title,
  showButton = true,
  chartData,
  chartLabel,
  rightContent,
  // optional path to navigate to when Start Quiz is clicked
  startQuizPath,
  // optional custom left-side content to render instead of the PerformanceChart
  leftContent,
  // optional back button configuration
  showBackButton = false,
  onBackClick,
}) => {
  const navigate = useNavigate();
  return (
    <>
      <div className="page-layout__header-wrapper">
        <Header />
      </div>
      {/* Back Button - Separate container between header and page */}
      {showBackButton && (
        <div className="page-layout__back-button-bar">
          <Button
            label="← Back"
            variant="secondary"
            onClick={onBackClick || (() => navigate(-1))}
          />
        </div>
      )}
      <div className="page-layout">
      {/* Left Column: Greeting, Title, Button, Chart */}
      <div className="page-layout__left-column">
        {/* Greeting and Title Section */}
        <div className="page-layout__header">
          <p className="page-layout__greeting">{greeting}</p>
          <h1 className="page-layout__title">{title}</h1>
        </div>

        {/* Start Quiz Button */}
        {showButton && (
          <div className="page-layout__button-container">
            <Button
              label="Start Quiz"
              variant="primary"
              onClick={() => navigate(startQuizPath || '/quiz')}
            />
          </div>
        )}

        {/* Performance Chart Placeholder or custom leftContent (used by QuizPage) */}
        <div className="page-layout__chart-container">
          {leftContent ? leftContent : <PerformanceChart data={chartData} label={chartLabel} />}
        </div>
      </div>

      {/* Right Column: Dynamic Content */}
      <div className="page-layout__right-column">
        {rightContent}
      </div>
      </div>
    </>
  );
};

export default PageLayout;

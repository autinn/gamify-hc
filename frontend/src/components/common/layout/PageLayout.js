import React from 'react';
import Header from './Header.js';
import Button from '../UI/Button';
import { useNavigate } from 'react-router-dom';
import PerformanceChart from '../Charts/PerformanceChart';
import './PageLayout.css';

/**
 * PageLayout - Reusable two-column application layout component
 *
 * Provides consistent page structure across the application with:
 * - Header navigation at top
 * - Optional back button between header and content
 * - Left column: greeting, title, quiz button, performance chart
 * - Right column: dynamic content (courses, units, concepts, quiz results)
 *
 * The layout adapts based on props to support different page types:
 * - MainPage: Shows global progress + course list
 * - CoursePage: Shows course progress + unit list + back button
 * - UnitPage: Shows unit progress + concept list + back button
 * - QuizPage: Uses leftContent to show quiz UI instead of chart
 *
 * @component
 * @param {string} greeting - Greeting text (e.g., "Hello,", "Welcome to")
 * @param {string} title - Page title (e.g., username, course name, unit name)
 * @param {boolean} [showButton=true] - Show "Start Quiz" button in left column
 * @param {Object} [chartData] - Chart data object {labels: [], values: []} for PerformanceChart
 * @param {string} [chartLabel] - X-axis label for chart (e.g., "Success Rate (%)")
 * @param {number} [labelOffset=50] - Pixel offset for chart label positioning
 * @param {React.ReactNode} rightContent - Content for right column (required)
 * @param {string} [startQuizPath] - Navigation path for quiz button (default: '/quiz')
 * @param {React.ReactNode} [leftContent] - Custom left-column content instead of chart
 * @param {boolean} [showBackButton=false] - Show back button (for hierarchical pages)
 * @param {Function} [onBackClick] - Back button click handler (defaults to navigate(-1))
 * @returns {React.ReactNode} Full page layout
 *
 * CSS Layout:
 * - page-layout__header-wrapper: Header container
 * - page-layout__back-button-bar: Back button bar
 * - page-layout: Main grid container (two columns)
 * - page-layout__left-column: Left section (greeting, title, button, chart)
 * - page-layout__right-column: Right section (dynamic content)
 *
 * @example
 * <PageLayout
 *   greeting="Hello,"
 *   title={userName}
 *   showButton={true}
 *   chartData={progressData}
 *   chartLabel="Success Rate (%)"
 *   rightContent={<CourseList courses={courses} />}
 * />
 *
 * Used by: MainPage, CoursePage, UnitPage, QuizPage
 */
const PageLayout = ({
  greeting,
  title,
  showButton = true,
  chartData,
  chartLabel,
  rightContent,
  labelOffset,
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
          {leftContent ? leftContent : <PerformanceChart data={chartData} label={chartLabel} labelOffset={labelOffset} />}
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

import React, { useState, useEffect, useRef } from 'react';
import './PerformanceChart.css';

/**
 * PerformanceChart - Interactive bar chart for displaying progress data
 *
 * Renders a responsive bar chart with:
 * - Rotated x-axis labels to prevent overlap
 * - Hover tooltips showing percentage values
 * - Dynamic padding calculation based on longest label
 * - Graceful handling of empty data states
 *
 * Designed for displaying success rates at different levels:
 * - Global: Course-level success rates
 * - Course: Unit-level success rates
 * - Unit: Concept-level success rates
 *
 * @component
 * @param {Object} data - Chart data object
 * @param {string[]} data.labels - X-axis category labels (e.g., course names, unit names)
 * @param {number[]} data.values - Y-axis values (0-1 range for percentages)
 * @param {string} [label] - Chart description/axis label
 * @param {number} [labelOffset=50] - CSS pixel offset for rotated labels from axis
 * @returns {React.ReactNode} Rendered bar chart
 *
 * Features:
 * - Auto-scales bars based on max value (assumes 0-1 range)
 * - Tooltip shows (value * 100).toFixed(1)% on hover
 * - Dynamic padding prevents label text overflow
 * - Empty state message when no data available
 *
 * CSS Classes:
 * - performance-chart: Main container
 * - performance-chart__content: Chart wrapper
 * - performance-chart__bars: Bar container with dynamic padding
 * - performance-chart__bar-wrapper: Individual bar container
 * - performance-chart__bar: Bar element (height-based)
 * - performance-chart__label: Rotated x-axis label
 * - performance-chart__tooltip: Hover tooltip
 * - performance-chart__description: Chart description text
 * - performance-chart__empty-state: No data message
 *
 * @example
 * <PerformanceChart
 *   data={{
 *     labels: ['EA50', 'FA50', 'MC50'],
 *     values: [0.75, 0.82, 0.68]
 *   }}
 *   label="Course Success Rates"
 *   labelOffset={70}
 * />
 *
 * Used by: MainPage, CoursePage, UnitPage (via PageLayout)
 */
const PerformanceChart = ({ data, label, labelOffset = 50 }) => {
  const [hoveredIndex, setHoveredIndex] = useState(null);
  const [dynamicPadding, setDynamicPadding] = useState(120);
  const measureRef = useRef(null);
  
  // Chart scaling: values are success rates (0-1), max bar height in pixels
  const maxValue = 1;
  const maxBarHeight = 150;
  
  // Calculate dynamic bottom padding based on longest label to prevent text overflow
  // when labels are rotated 45 degrees
  useEffect(() => {
    if (!data || !data.labels || !measureRef.current) return;

    // Measure text width by temporarily rendering invisible text
    const measureLabelWidth = (text) => {
      const span = document.createElement('span');
      span.style.visibility = 'hidden';
      span.style.position = 'absolute';
      span.style.fontSize = '10px';
      span.style.fontWeight = '600';
      span.style.whiteSpace = 'nowrap';
      span.style.fontFamily = 'inherit';
      span.textContent = text;
      measureRef.current.appendChild(span);
      const width = span.offsetWidth;
      measureRef.current.removeChild(span);
      return width;
    };

    // Find longest label to calculate required padding
    let maxLabelWidth = 0;
    data.labels.forEach((labelText) => {
      const width = measureLabelWidth(labelText);
      maxLabelWidth = Math.max(maxLabelWidth, width);
    });

    // Calculate padding: label height + gap + axis label space
    // Clamp between 80px (short labels) and 150px (very long labels)
    const calculatedPadding = Math.min(Math.max(maxLabelWidth + 30, 80), 150);
    setDynamicPadding(calculatedPadding);
  }, [data]);
  
  return (
    <div className="performance-chart">
      {/* Invisible measurement container for label width calculation */}
      <div ref={measureRef} style={{ visibility: 'hidden', position: 'absolute', top: '-9999px' }} />
      
      {data && data.labels && data.labels.length > 0 ? (
        <div className="performance-chart__content">
          <div 
            className="performance-chart__bars"
            style={{ paddingBottom: `${dynamicPadding}px` }}
          >
            {data.labels.map((labelItem, index) => {
              const value = data.values[index] || 0;
              const percentage = (value / maxValue);
              const barHeight = Math.min(percentage * maxBarHeight, maxBarHeight);
              
              return (
                <div 
                  key={index} 
                  className="performance-chart__bar-wrapper"
                  onMouseEnter={() => setHoveredIndex(index)}
                  onMouseLeave={() => setHoveredIndex(null)}
                >
                  {/* Hover tooltip showing the value as percentage */}
                  {hoveredIndex === index && (
                    <div className="performance-chart__tooltip">
                      {`${(value * 100).toFixed(1)}%`}
                    </div>
                  )}
                  <div
                    className="performance-chart__bar"
                    style={{
                      height: `${barHeight}px`,
                    }}
                  />
                  <p 
                    className="performance-chart__label" 
                    title={labelItem}
                    style={{ bottom: `-${dynamicPadding - labelOffset}px` }}
                  >
                    {labelItem}
                  </p>
                </div>
              );
            })}
          </div>
          {label && (
            <p className="performance-chart__description">
              {label}
            </p>
          )}
        </div>
      ) : (
        <div className="performance-chart__empty-state">
          <p className="performance-chart__empty-message">Start taking quizzes to see your progress!</p>
        </div>
      )}
    </div>
  );
};

export default PerformanceChart;
import React, { useState, useEffect, useRef } from 'react';
import './PerformanceChart.css';

/**
 * PerformanceChart - Bar chart component with hover tooltips and dynamic padding
 *
 * Displays a bar chart with rotated labels and hover functionality to show values.
 * Dynamically adjusts padding based on longest label to prevent overlap.
 *
 * @param {object} data - Chart data object { labels, values }
 * @param {string} label - Chart title/description (x-axis label)
 * @param {number} labelOffset - Offset for label positioning (default: 10). Use higher values (e.g., 70) for more space from axis
 */
const PerformanceChart = ({ data, label, labelOffset = 50 }) => {
  const [hoveredIndex, setHoveredIndex] = useState(null);
  const [dynamicPadding, setDynamicPadding] = useState(120);
  const measureRef = useRef(null);
  
  // Simple bar chart visualization using divs
  const maxValue = 1; // Success rates are between 0 and 1
  const maxBarHeight = 150; // Maximum height for bars in pixels
  
  // Calculate dynamic padding based on longest label
  useEffect(() => {
    if (!data || !data.labels || !measureRef.current) return;

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

    // Find the maximum label width (becomes height when rotated)
    let maxLabelWidth = 0;
    data.labels.forEach((labelText) => {
      const width = measureLabelWidth(labelText);
      maxLabelWidth = Math.max(maxLabelWidth, width);
    });

    // Calculate padding: label height + gap + axis label space
    // Min 80px for short labels, max 150px for very long labels
    const calculatedPadding = Math.min(Math.max(maxLabelWidth + 30, 80), 150);
    setDynamicPadding(calculatedPadding);
  }, [data]);
  
  return (
    <div className="performance-chart">
      {/* Hidden element for measuring text width */}
      <div ref={measureRef} style={{ visibility: 'hidden', position: 'absolute', top: '-9999px' }} />
      
      {data && data.labels ? (
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
        <p className="performance-chart__placeholder">Chart data not available</p>
      )}
    </div>
  );
};

export default PerformanceChart;
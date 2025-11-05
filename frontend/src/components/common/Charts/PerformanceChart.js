import React from 'react';
import './PerformanceChart.css';

/**
 * PerformanceChart - Placeholder chart component
 *
 * Currently a placeholder - will be replaced with actual chart visualization
 * (e.g., bar chart, line chart using charting library)
 *
 * @param {object} data - Chart data object { labels, values }
 * @param {string} label - Chart title/description
 */
const PerformanceChart = ({ data, label }) => {
  // Simple bar chart visualization using divs (placeholder)
  const maxValue = data && data.values ? Math.max(...data.values, 1) : 100;
  const maxBarHeight = 150; // Maximum height for bars in pixels
  
  return (
    <div className="performance-chart">
      {data && data.labels ? (
        <div className="performance-chart__content">
          <div className="performance-chart__bars">
            {data.labels.map((labelItem, index) => {
              const value = data.values[index] || 0;
              const percentage = (value / maxValue);
              const barHeight = Math.min(percentage * maxBarHeight, maxBarHeight);
              
              return (
                <div key={index} className="performance-chart__bar-wrapper" style={{ position: 'relative' }}>
                  <div
                    className="performance-chart__bar"
                    style={{
                      height: `${barHeight}px`,
                    }}
                  />
                  <p className="performance-chart__label">{labelItem}</p>
                </div>
              );
            })}
          </div>
          {label && <p className="performance-chart__description">{label}</p>}
        </div>
      ) : (
        <p className="performance-chart__placeholder">Chart data not available</p>
      )}
    </div>
  );
};

export default PerformanceChart;

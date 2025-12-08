/**
 * Web Vitals Reporting Module
 *
 * Measures and reports Core Web Vitals - key metrics for user experience.
 * Lazily imports web-vitals library only when needed (callback provided).
 * Metrics are sent to provided callback function for analytics, monitoring, or logging.
 *
 * @param {Function} onPerfEntry - Callback function to receive performance metrics
 *   Called for each metric with object: { name: string, value: number, ... }
 *   Example: onPerfEntry({ name: 'LCP', value: 2500, ... })
 *
 * Core Web Vitals Measured:
 *
 * 1. CLS (Cumulative Layout Shift)
 *    - Measures visual stability during page load
 *    - Good: < 0.1, Needs Improvement: 0.1-0.25, Poor: > 0.25
 *    - Caused by: Unexpected layout changes, ad injections, web fonts
 *
 * 2. FID (First Input Delay)
 *    - Measures responsiveness to user input (deprecated, replaced by INP in web-vitals v4)
 *    - Good: < 100ms, Needs Improvement: 100-300ms, Poor: > 300ms
 *    - Caused by: Long JavaScript execution, heavy main thread work
 *
 * 3. FCP (First Contentful Paint)
 *    - Measures when first content appears on page
 *    - Good: < 1.8s, Needs Improvement: 1.8-3s, Poor: > 3s
 *    - Caused by: Slow server response, render-blocking JavaScript/CSS
 *
 * 4. LCP (Largest Contentful Paint)
 *    - Measures when largest visible content loads
 *    - Good: < 2.5s, Needs Improvement: 2.5-4s, Poor: > 4s
 *    - Caused by: Slow server response, large images, JavaScript execution
 *
 * 5. TTFB (Time to First Byte)
 *    - Measures server response time
 *    - Good: < 600ms, Needs Improvement: 600-1800ms, Poor: > 1800ms
 *    - Caused by: Slow server, unoptimized backend, poor hosting location
 *
 * Usage:
 * - For console logging: reportWebVitals(console.log)
 * - For analytics: reportWebVitals((metric) => { analytics.track(metric); })
 * - Lazy loading: Only imports web-vitals if callback provided (saves bundle size)
 *
 * @example
 * // Log metrics to console
 * reportWebVitals(console.log);
 *
 * // Send to analytics service
 * reportWebVitals((metric) => {
 *   // metric: { name: 'LCP', value: 2500, rating: 'good', ... }
 *   fetch('/api/metrics', { method: 'POST', body: JSON.stringify(metric) });
 * });
 */
const reportWebVitals = onPerfEntry => {
  // Only initialize if callback is provided and is a function
  if (onPerfEntry && onPerfEntry instanceof Function) {
    // Lazy import web-vitals library (only when metrics are needed)
    // Reduces initial bundle size if metrics not enabled
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      // Measure and report each Core Web Vital metric
      getCLS(onPerfEntry);  // Cumulative Layout Shift
      getFID(onPerfEntry);  // First Input Delay (deprecated)
      getFCP(onPerfEntry);  // First Contentful Paint
      getLCP(onPerfEntry);  // Largest Contentful Paint
      getTTFB(onPerfEntry); // Time to First Byte
    });
  }
};

export default reportWebVitals;

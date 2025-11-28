/**
 * useProgress Hook
 * 
 * Manages progress data fetching at different levels (global, course, unit, concept).
 * Returns standardized chart data with labels and values.
 * Handles loading and error states with graceful fallbacks.
 * 
 * @component
 * @param {string} levelType - Level type: 'global' | 'course' | 'unit' | 'concept'
 * @param {number} [levelId] - ID for the specific level (not needed for 'global')
 * @param {number} [parentId] - Parent ID (courseId for unit, unitId for concept)
 * @returns {Object} Progress data object
 * @returns {Object} returns.chartData - Chart data {labels, values, metadata}
 * @returns {boolean} returns.loading - True while data is being fetched
 * @returns {Error|null} returns.error - Error object if fetch failed
 * @returns {Function} returns.refresh - Function to manually refresh progress data
 * 
 * @example
 * // Global progress
 * const { chartData, loading } = useProgress('global');
 * 
 * // Course progress
 * const { chartData, loading } = useProgress('course', courseId);
 * 
 * // Unit progress
 * const { chartData, loading } = useProgress('unit', unitId, courseId);
 * 
 * // Concept progress
 * const { chartData, loading } = useProgress('concept', conceptId, unitId);
 * 
 * Used by: MainPage, CoursePage, UnitPage
 */

import { useState, useEffect } from 'react';
import {
  fetchGlobalProgress,
  fetchCourseProgress,
  fetchUnitProgress,
  fetchConceptProgress
} from '../services/progressService';

export function useProgress(levelType, levelId, parentId) {
  const [chartData, setChartData] = useState({
    labels: [],
    values: [],
    metadata: {}
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;

    const fetchProgress = async () => {
      try {
        setLoading(true);
        setError(null);

        let data;

        switch (levelType) {
          case 'global':
            data = await fetchGlobalProgress();
            break;
          case 'course':
            data = await fetchCourseProgress(levelId);
            break;
          case 'unit':
            data = await fetchUnitProgress(parentId, levelId);
            break;
          case 'concept':
            data = await fetchConceptProgress(parentId, levelId, levelId);
            break;
          default:
            throw new Error(`Unknown level type: ${levelType}`);
        }

        if (isMounted) {
          setChartData(data);
        }
      } catch (err) {
        console.error(`Error fetching ${levelType} progress:`, err);
        if (isMounted) {
          setError(err);
          setChartData({ labels: [], values: [], metadata: { error: true } });
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    fetchProgress();

    return () => {
      isMounted = false;
    };
  }, [levelType, levelId, parentId]);

  const refresh = async () => {
    setLoading(true);
    setError(null);

    try {
      let data;

      switch (levelType) {
        case 'global':
          data = await fetchGlobalProgress();
          break;
        case 'course':
          data = await fetchCourseProgress(levelId);
          break;
        case 'unit':
          data = await fetchUnitProgress(parentId, levelId);
          break;
        case 'concept':
          data = await fetchConceptProgress(parentId, levelId, levelId);
          break;
        default:
          throw new Error(`Unknown level type: ${levelType}`);
      }

      setChartData(data);
    } catch (err) {
      console.error(`Error refreshing ${levelType} progress:`, err);
      setError(err);
      setChartData({ labels: [], values: [], metadata: { error: true } });
    } finally {
      setLoading(false);
    }
  };

  return {
    chartData,
    loading,
    error,
    refresh
  };
}

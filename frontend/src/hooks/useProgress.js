/**
 * useProgress Hook - User progress chart data management
 *
 * Fetches user progress data at different hierarchical levels:
 * - Global: Across all courses
 * - Course: Across all units in a course
 * - Unit: Across all concepts in a unit
 * - Concept: For individual quiz cards (expansion-ready)
 *
 * Returns standardized chart data format suitable for PerformanceChart components.
 * Includes manual refresh capability and graceful error handling.
 *
 * @hook
 * @param {string} levelType - Progress aggregation level: 'global' | 'course' | 'unit' | 'concept'
 * @param {number} [levelId] - ID for the specific level (required for non-global levels)
 * @param {number} [parentId] - Parent ID for nested levels (courseId for unit, unitId for concept)
 * @returns {Object} Progress data and state
 * @returns {Object} returns.chartData - Chart data {labels: string[], values: number[], metadata: object}
 * @returns {boolean} returns.loading - True while fetching
 * @returns {Error|null} returns.error - Error object if fetch failed
 * @returns {Function} returns.refresh - Manual refresh function to re-fetch data
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

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useUnit } from '../../hooks/useUnit';
import * as unitService from '../../services/unitService';

vi.mock('../../services/unitService', () => ({
  fetchCourseUnitWithConcepts: vi.fn()
}));

describe('useUnit Hook', () => {
  const mockUnit = {
    id: 1,
    name: 'Cell Structure',
    concepts: [
      { id: 1, name: 'Concept 1' },
      { id: 2, name: 'Concept 2' }
    ]
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should have loading state', async () => {
    unitService.fetchCourseUnitWithConcepts.mockResolvedValue(mockUnit);

    const { result } = renderHook(() => useUnit(1, 1));

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });

  it('should handle fetch errors', async () => {
    unitService.fetchCourseUnitWithConcepts.mockRejectedValue(new Error('Failed to fetch'));

    const { result } = renderHook(() => useUnit(1, 1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.error).toBeTruthy();
    expect(result.current.unit).toBeNull();
  });

  it('should have initial loading state', async () => {
    unitService.fetchCourseUnitWithConcepts.mockResolvedValue(mockUnit);

    const { result } = renderHook(() => useUnit(1, 1));

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });
});


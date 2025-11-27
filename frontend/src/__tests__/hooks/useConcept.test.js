import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useConcept } from '../../hooks/useConcept';
import * as conceptService from '../../services/conceptService';

vi.mock('../../services/conceptService', () => ({
  fetchConceptWithAllData: vi.fn()
}));

describe('useConcept Hook', () => {
  const mockConcept = {
    id: 1,
    name: 'Prokaryotic Cells',
    questions: [
      { id: 1, text: 'What is a prokaryote?' },
      { id: 2, text: 'Name examples' }
    ]
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should have loading state', async () => {
    conceptService.fetchConceptWithAllData.mockResolvedValue({
      course: { course_id: 1 },
      unit: { unit_id: 1 },
      concept: mockConcept,
      quizCards: []
    });

    const { result } = renderHook(() => useConcept(1, 1, 1));

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });

  it('should handle fetch errors', async () => {
    conceptService.fetchConceptWithAllData.mockRejectedValue(new Error('Failed to fetch'));

    const { result } = renderHook(() => useConcept(1, 1, 1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.error).toBeTruthy();
    expect(result.current.concept).toBeNull();
  });

  it('should have initial loading state', async () => {
    conceptService.fetchConceptWithAllData.mockResolvedValue({
      course: { course_id: 1 },
      unit: { unit_id: 1 },
      concept: mockConcept,
      quizCards: []
    });

    const { result } = renderHook(() => useConcept(1, 1, 1));

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });
});

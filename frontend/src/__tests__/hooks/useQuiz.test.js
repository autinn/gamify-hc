import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useQuiz } from '../../hooks/useQuiz';
import * as quizService from '../../services/quizService';

vi.mock('../../services/quizService', () => ({
  fetchQuizByLevel: vi.fn(),
  getShuffledQuizQuestions: vi.fn()
}));

describe('useQuiz Hook', () => {
  const mockQuestions = [
    { id: 1, text: 'Q1', options: [{ id: 1, is_correct: true }] },
    { id: 2, text: 'Q2', options: [{ id: 2, is_correct: true }] },
    { id: 3, text: 'Q3', options: [{ id: 3, is_correct: true }] },
    { id: 4, text: 'Q4', options: [{ id: 4, is_correct: true }] },
    { id: 5, text: 'Q5', options: [{ id: 5, is_correct: true }] }
  ];

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should fetch quiz on mount', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(quizService.fetchQuizByLevel).toHaveBeenCalledWith(1, undefined, undefined);
  });

  it('should fetch unit-level quiz', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1, 2));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(quizService.fetchQuizByLevel).toHaveBeenCalledWith(1, 2, undefined);
  });

  it('should increment correctCount on handleSelect with correct option', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    act(() => {
      result.current.handleSelect({ id: 1, is_correct: true, text: 'Correct' });
    });

    expect(result.current.correctCount).toBe(1);
  });

  it('should move to next question on handleNext', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    const initialIndex = result.current.currentIndex;

    act(() => {
      result.current.handleNext();
    });

    expect(result.current.currentIndex).toBe(initialIndex + 1);
  });

  it('should handle fetch errors', async () => {
    quizService.fetchQuizByLevel.mockRejectedValue(new Error('Fetch failed'));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.error).toBeTruthy();
  });

  it('should only score first correct answer on a question', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    act(() => {
      result.current.handleSelect({ id: 1, is_correct: true, text: 'Correct' });
    });

    expect(result.current.correctCount).toBe(1);

    // User selects a wrong answer after the first correct one
    act(() => {
      result.current.handleSelect({ id: 2, is_correct: false, text: 'Wrong' });
    });

    // Score should remain 1 (not incremented again)
    expect(result.current.correctCount).toBe(1);
  });

  it('should not increment score if first selection is incorrect', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    act(() => {
      result.current.handleSelect({ id: 2, is_correct: false, text: 'Wrong' });
    });

    expect(result.current.correctCount).toBe(0);
  });

  it('should mark isAnsweredCorrectly when any correct option is selected', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    act(() => {
      result.current.handleSelect({ id: 1, is_correct: true, text: 'Correct' });
    });

    expect(result.current.isAnsweredCorrectly).toBe(true);
  });

  it('should reset firstSelection on handleNext', async () => {
    quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
    quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

    const { result } = renderHook(() => useQuiz(1));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    act(() => {
      result.current.handleSelect({ id: 1, is_correct: true, text: 'Correct' });
      result.current.handleNext();
    });

    expect(result.current.isAnsweredCorrectly).toBe(false);
  });
});

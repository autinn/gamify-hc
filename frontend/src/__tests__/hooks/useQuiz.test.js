import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useQuiz } from '../../hooks/useQuiz';
import * as quizService from '../../services/quizService';
import * as api from '../../services/api';

vi.mock('../../services/quizService', () => ({
  fetchQuizByLevel: vi.fn(),
  getShuffledQuizQuestions: vi.fn()
}));

vi.mock('../../services/api', () => ({
  submitQuizAnswer: vi.fn()
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
    localStorage.clear();
  });

  afterEach(() => {
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

  describe('Database Persistence - quiz-submit endpoint', () => {
    it('should submit answer with is_first_attempt flag', async () => {
      api.submitQuizAnswer.mockResolvedValue({});
      quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
      quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

      const { result } = renderHook(() => useQuiz(1, 2, 3));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      // First attempt
      act(() => {
        result.current.handleSelect({ id: 1, is_correct: false, text: 'Wrong' });
      });

      await waitFor(() => {
        expect(api.submitQuizAnswer).toHaveBeenCalledWith(
          expect.objectContaining({
            is_first_attempt: true
          })
        );
      });

      // Second attempt
      act(() => {
        result.current.handleSelect({ id: 1, is_correct: true, text: 'Correct' });
      });

      await waitFor(() => {
        const lastCall = api.submitQuizAnswer.mock.calls[api.submitQuizAnswer.mock.calls.length - 1];
        expect(lastCall[0].is_first_attempt).toBe(false);
      });
    });

    it('should include quiz_card_id, answer_id in submission', async () => {
      api.submitQuizAnswer.mockResolvedValue({});
      quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
      quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

      const { result } = renderHook(() => useQuiz(1, 2, 3));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      act(() => {
        result.current.handleSelect({ id: 42, is_correct: true, text: 'Correct' });
      });

      await waitFor(() => {
        expect(api.submitQuizAnswer).toHaveBeenCalledWith(
          expect.objectContaining({
            quiz_card_id: mockQuestions[0].id,
            answer_id: 42,
            is_first_attempt: true
          })
        );
      });
    });

    it('should handle submission errors gracefully', async () => {
      const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

      api.submitQuizAnswer.mockRejectedValueOnce(new Error('Network error'));

      quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
      quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

      const { result } = renderHook(() => useQuiz(1, 2, 3));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      act(() => {
        result.current.handleSelect({ id: 1, is_correct: true, text: 'Correct' });
      });

      await waitFor(() => {
        expect(consoleErrorSpy).toHaveBeenCalled();
      });

      consoleErrorSpy.mockRestore();
    });

    it('should track correctCount only on first correct attempt per question', async () => {
      api.submitQuizAnswer.mockResolvedValue({});

      quizService.fetchQuizByLevel.mockResolvedValue(mockQuestions);
      quizService.getShuffledQuizQuestions.mockReturnValue(mockQuestions.slice(0, 5));

      const { result } = renderHook(() => useQuiz(1, 2, 3));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      // Wrong first, correct second
      act(() => {
        result.current.handleSelect({ id: 1, is_correct: false, text: 'Wrong' });
      });
      expect(result.current.correctCount).toBe(0);

      act(() => {
        result.current.handleSelect({ id: 1, is_correct: true, text: 'Correct' });
      });
      expect(result.current.correctCount).toBe(0); // Still 0 because first was wrong

      // Move to next question
      act(() => {
        result.current.handleNext();
      });

      // Correct on first try
      act(() => {
        result.current.handleSelect({ id: 2, is_correct: true, text: 'Correct' });
      });
      expect(result.current.correctCount).toBe(1);
    });
  });
});

/**
 * useQuiz Hook - Quiz game state management
 *
 * Manages quiz progression, question shuffling, answer selection, and scoring.
 * Tracks first attempt for progress scoring (only first correct answer counts).
 * Allows multiple attempts per question for learning reinforcement.
 *
 * Scoring Logic:
 * - firstSelection tracks the user's first chosen answer
 * - Score only increments on first-attempt correct answers
 * - User can try again after wrong answer (no score penalty)
 * - isAnsweredCorrectly controls Next button visibility
 *
 * @hook
 * @param {number} courseId - Course ID (optional, for level-based quiz)
 * @param {number} unitId - Unit ID (optional, for level-based quiz)
 * @param {number} conceptId - Concept ID (optional, for level-based quiz)
 * @returns {Object} Quiz state and handlers
 * @returns {Array} returns.questions - Shuffled array of up to 5 quiz cards
 * @returns {Object} returns.currentQuestion - Current quiz card {id, text, options[]}
 * @returns {number} returns.currentIndex - Current question index (0-based)
 * @returns {number} returns.correctCount - Number of first-attempt correct answers
 * @returns {number} returns.totalCount - Total questions in this quiz session
 * @returns {boolean} returns.isAnsweredCorrectly - True if current question answered correctly
 * @returns {boolean} returns.isQuizDone - True when all questions completed
 * @returns {boolean} returns.loading - True while fetching questions
 * @returns {Error|null} returns.error - Error object if fetch failed
 * @returns {Function} returns.handleSelect - Answer selection handler(option)
 * @returns {Function} returns.handleNext - Move to next question handler()
 *
 * @example
 * const { currentQuestion, handleSelect, handleNext, isQuizDone } = useQuiz(1, 2, 3);
 * return isQuizDone ? <Results /> : <QuizUI question={currentQuestion} />;
 *
 * Used by: QuizPage
 */

import { useState, useEffect } from 'react';
import { fetchQuizByLevel, getShuffledQuizQuestions } from '../services/quizService';

export function useQuiz(courseId, unitId, conceptId) {
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [isAnsweredCorrectly, setIsAnsweredCorrectly] = useState(false);

  // Tracks the user's first answer selection to determine scoring
  const [firstSelection, setFirstSelection] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Load and initialize quiz on component mount or when quiz level changes
  useEffect(() => {
    setLoading(true);
    setError(null);

    // Reset quiz state
    setCurrentIndex(0);
    setCorrectCount(0);
    setIsAnsweredCorrectly(false);
    setFirstSelection(null);

    // Fetch quiz cards at appropriate level (concept > unit > course > global)
    fetchQuizByLevel(courseId, unitId, conceptId)
      .then((quizCards) => {
        if (quizCards && quizCards.length > 0) {
          // Shuffle and limit to 5 questions for reasonable session length
          const selected = getShuffledQuizQuestions(quizCards);
          setQuestions(selected);
        }
      })
      .catch((err) => {
        console.error("Error fetching quiz cards:", err);
        setError(err);
      })
      .finally(() => setLoading(false));
  }, [courseId, unitId, conceptId]);

  // Derived state for component rendering
  const currentQuestion = questions[currentIndex];
  const totalCount = questions.length;
  const isQuizDone = !loading && currentIndex >= totalCount;

  /**
   * Handle user answer selection
   *
   * Implements first-attempt scoring: only the first correct answer
   * increments the score. Subsequent attempts (whether correct or incorrect)
   * don't affect scoring. Submits selection to backend for persistence.
   *
   * @param {Object} option - Selected answer option {id, text, is_correct, explanation}
   */
  const handleSelect = async (option) => {
    // Determine if this is the first answer selection for this question
    const isFirstAttempt = firstSelection === null;
    
    // Track first selection to prevent multiple score increments
    if (isFirstAttempt) {
      setFirstSelection(option.id);

      // Only increment score on first-attempt correct answers
      if (option.is_correct) {
        setCorrectCount((prev) => prev + 1);
      }
    }

    // Show Next button once any correct answer is selected
    // (allows user to try multiple times, but move on when correct)
    if (option.is_correct) {
      setIsAnsweredCorrectly(true);
    }

    // Persist answer to backend for progress tracking and user card updates
    try {
      const token = localStorage.getItem('token');

      const apiUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5001/api';
      const response = await fetch(`${apiUrl}/quiz-submit`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token && { 'Authorization': `Bearer ${token}` })
        },
        body: JSON.stringify({
          quiz_card_id: currentQuestion.id,
          answer_id: option.id,
          is_first_attempt: isFirstAttempt
        })
      });
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        console.error('Quiz submission error:', errorData);
      }
    } catch (err) {
      console.error('Error submitting quiz answer:', err);
    }
  };

  /**
   * Move to next question
   *
   * Increments question index and resets state for the new question.
   * Resets firstSelection so next question can track its own first attempt.
   */
  const handleNext = () => {
    setCurrentIndex((i) => i + 1);
    setIsAnsweredCorrectly(false);
    setFirstSelection(null); // Reset first-attempt tracking for new question
  };

  return {
    questions,
    currentQuestion,
    currentIndex,
    correctCount,
    totalCount,
    isAnsweredCorrectly,
    isQuizDone,
    loading,
    error,
    handleSelect,
    handleNext,
  };
}
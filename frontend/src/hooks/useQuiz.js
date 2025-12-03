/**
 * useQuiz Hook (Updated)
 *
 * - Tracks first selection to score only if first attempt is correct
 * - Allows multiple tries
 * - Marks question correct so Next button appears
 * - Resets properly on each question
 */

import { useState, useEffect } from 'react';
import { fetchQuizByLevel, getShuffledQuizQuestions } from '../services/quizService';

export function useQuiz(courseId, unitId, conceptId) {
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [isAnsweredCorrectly, setIsAnsweredCorrectly] = useState(false);

  // NEW: track the first option the user clicks
  const [firstSelection, setFirstSelection] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Load quiz
  useEffect(() => {
    setLoading(true);
    setError(null);

    setCurrentIndex(0);
    setCorrectCount(0);
    setIsAnsweredCorrectly(false);
    setFirstSelection(null);

    fetchQuizByLevel(courseId, unitId, conceptId)
      .then((quizCards) => {
        if (quizCards && quizCards.length > 0) {
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

  // Derived state
  const currentQuestion = questions[currentIndex];
  const totalCount = questions.length;
  const isQuizDone = !loading && currentIndex >= totalCount;

  /**
   * MAIN LOGIC:
   * Called by QuizAnswers every time user clicks an option.
   * Submits answer to backend with first-attempt flag for progress tracking.
   */
  const handleSelect = async (option) => {
    // Determine if this is first attempt
    const isFirstAttempt = firstSelection === null;
    
    // Only record first attempt locally
    if (isFirstAttempt) {
      setFirstSelection(option.id);

      // FIRST TRY CORRECT → increase score
      if (option.is_correct) {
        setCorrectCount((prev) => prev + 1);
      }
    }

    // Eventually correct → show next button
    if (option.is_correct) {
      setIsAnsweredCorrectly(true);
    }

    // Submit to backend for persistence (quiz answers, UserCard tracking)
    try {
      const token = localStorage.getItem('token');
      const response = await fetch('http://localhost:5001/api/quiz-submit', {
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

  const handleNext = () => {
    setCurrentIndex((i) => i + 1);
    setIsAnsweredCorrectly(false);
    setFirstSelection(null); // reset first-attempt tracking
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
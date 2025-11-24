/**
 * useQuiz Hook
 * 
 * Manages quiz state including questions, current index, answers tracking.
 * Handles multi-level quizzes (course, unit, concept).
 * Used by: QuizPage
 */

import { useState, useEffect } from 'react';
import { fetchQuizByLevel, shuffleArray } from '../services/quizService';

export function useQuiz(courseId, unitId, conceptId) {
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [isAnsweredCorrectly, setIsAnsweredCorrectly] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Determine which level of quiz to fetch
    if (!courseId && !unitId && !conceptId) return;

    setLoading(true);
    setError(null);
    setCurrentIndex(0);
    setCorrectCount(0);
    setIsAnsweredCorrectly(false);

    fetchQuizByLevel(courseId, unitId, conceptId)
      .then(quizCards => {
        if (quizCards && quizCards.length > 0) {
          const shuffled = shuffleArray(quizCards);
          setQuestions(shuffled);
        }
      })
      .catch(err => {
        console.error('Error fetching quiz cards:', err);
        setError(err);
      })
      .finally(() => setLoading(false));
  }, [courseId, unitId, conceptId]);

  // Quiz state calculations
  const currentQuestion = questions[currentIndex];
  const totalCount = questions.length;
  const isQuizDone = currentIndex >= totalCount;

  // Handlers
  const handleCorrect = () => {
    setIsAnsweredCorrectly(true);
    setCorrectCount(prev => prev + 1);
  };

  const handleNext = () => {
    setIsAnsweredCorrectly(false);
    setCurrentIndex(i => i + 1);
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
    handleCorrect,
    handleNext
  };
}

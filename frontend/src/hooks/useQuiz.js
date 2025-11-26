/**
 * useQuiz Hook
 * 
 * Manages quiz state including questions, current index, answers tracking, and scoring.
 * Handles multi-level quizzes: course-level, unit-level, concept-level, and global random quizzes.
 * Questions are automatically shuffled and limited to 5 per quiz.
 * 
 * @component
 * @param {number} [courseId] - Course ID for course-level quiz (optional)
 * @param {number} [unitId] - Unit ID for unit-level quiz (optional)
 * @param {number} [conceptId] - Concept ID for concept-level quiz (optional)
 * @returns {Object} Quiz object with state and handlers
 * @returns {Array} returns.questions - Array of shuffled quiz questions (max 5)
 * @returns {Object} returns.currentQuestion - Currently displayed question object
 * @returns {number} returns.currentIndex - Index of current question (0-based)
 * @returns {number} returns.correctCount - Number of correctly answered questions
 * @returns {number} returns.totalCount - Total number of questions in quiz
 * @returns {boolean} returns.isAnsweredCorrectly - Whether current question was answered correctly
 * @returns {boolean} returns.isQuizDone - True when all questions have been answered
 * @returns {boolean} returns.loading - True while quiz data is being fetched
 * @returns {Error|null} returns.error - Error object if quiz loading failed
 * @returns {Function} returns.handleCorrect - Handler to mark current question as correct
 * @returns {Function} returns.handleNext - Handler to move to next question
 * 
 * @example
 * // Global random quiz
 * const quiz = useQuiz();
 * 
 * // Course-level quiz
 * const quiz = useQuiz(courseId);
 * 
 * // Unit-level quiz
 * const quiz = useQuiz(courseId, unitId);
 * 
 * // Concept-level quiz
 * const quiz = useQuiz(courseId, unitId, conceptId);
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
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch quiz - works for both specific level (course/unit/concept) and global quiz
    setLoading(true);
    setError(null);
    setCurrentIndex(0);
    setCorrectCount(0);
    setIsAnsweredCorrectly(false);

    fetchQuizByLevel(courseId, unitId, conceptId)
      .then(quizCards => {
        if (quizCards && quizCards.length > 0) {
          // Shuffle and limit to 5 questions
          const selected = getShuffledQuizQuestions(quizCards);
          setQuestions(selected);
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

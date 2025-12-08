import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Quiz.css'; // reuse same base styling for consistency

/**
 * QuizResults - Quiz completion summary and navigation screen
 *
 * Displays final quiz score and provides navigation back to home page.
 * Shown after user completes all questions in a quiz.
 * Displays the number of correct answers and percentage score.
 *
 * @component
 * @param {number} correctCount - Number of questions answered correctly
 * @param {number} totalCount - Total number of questions in the quiz
 * @returns {React.ReactNode} Results display with score and return button
 *
 * Display Format:
 * - "You answered {correctCount} out of {totalCount} questions correctly ({percent}%)."
 * - "Return Home" button navigates to /
 *
 * Score Calculation:
 * - Percentage = Math.round((correctCount / totalCount) * 100)
 * - Calculated client-side for display purposes
 *
 * CSS Classes:
 * - quiz-results: Main results container
 * - quiz-results__score: Score text display
 * - quiz-results__button: Return button styled like answer options
 *
 * @example
 * <QuizResults
 *   correctCount={8}
 *   totalCount={10}
 * />
 * // Displays: "You answered 8 out of 10 questions correctly (80%)."
 * // With Return Home button
 *
 * Used by: QuizPage component (after quiz completion)
 */
const QuizResults = ({ correctCount, totalCount }) => {
  const navigate = useNavigate();
  // Calculate percentage score for display
  const percent = Math.round((correctCount / totalCount) * 100);

  return (
    <div className="quiz-results">

      <p className="quiz-results__score">
        You answered <strong>{correctCount}</strong> out of <strong>{totalCount}</strong> questions correctly
        ({percent}%).
      </p>

      <button
        className="quiz-results__button quiz-answers__option"
        onClick={() => navigate('/')}
      >
        Return Home
      </button>
    </div>
  );
};

export default QuizResults;
import React from 'react';
import './Quiz.css';

/**
 * QuizQuestion - Displays current quiz question with progress indicator
 *
 * Shows the question text and current progress (e.g., "Question 3 / 10").
 * Part of the two-column quiz layout: question on left, answers on right.
 * Renders nothing if question prop is null/undefined.
 *
 * @component
 * @param {Object} question - Current quiz question object
 *   @param {number} question.id - Question identifier (quiz_card_id)
 *   @param {string} question.text - Question text to display
 * @param {Object} progress - Quiz progress tracking
 *   @param {number} progress.current - Current question number (1-based)
 *   @param {number} progress.total - Total number of questions in quiz
 * @returns {React.ReactNode} Question display with progress or null
 *
 * Display Layout:
 * - Progress meta: "Question X / Y"
 * - Question text: Large heading with the question
 * - Hint text: "Select the best answer from the right."
 *
 * CSS Classes:
 * - quiz-question: Main container
 * - quiz-question__meta: Progress indicator (Question 1 / 5)
 * - quiz-question__text: Question text heading
 * - quiz-question__hint: Helper text for user
 *
 * @example
 * <QuizQuestion
 *   question={{ id: 1, text: "What is the capital of France?" }}
 *   progress={{ current: 1, total: 10 }}
 * />
 * // Displays: "Question 1 / 10" and the question text
 *
 * Used by: QuizPage component (left column of quiz layout)
 */
const QuizQuestion = ({ question, progress }) => {
  if (!question) return null;

  return (
    <div className="quiz-question">
      <div className="quiz-question__meta">
        Question {progress.current} / {progress.total}
      </div>
      <h2 className="quiz-question__text">{question.text}</h2>
      <div className="quiz-question__hint">
        Select the best answer from the right.
      </div>
    </div>
  );
};

export default QuizQuestion;
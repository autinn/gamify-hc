import React from 'react';
import { useNavigate } from 'react-router-dom';
import './QuizAnswers.css'; // reuse same base styling for consistency

/**
 * QuizResults - shows quiz summary and return button.
 * Props:
 *  - correctCount: number
 *  - totalCount: number
 */
const QuizResults = ({ correctCount, totalCount }) => {
  const navigate = useNavigate();
  const percent = Math.round((correctCount / totalCount) * 100);

  return (
    <div className="quiz-results">
      <h2 className="quiz-results__title">Quiz Complete!</h2>

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
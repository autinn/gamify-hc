import React from 'react';
import './QuizAnswers.css'; // you might later rename this to Quiz.css for both question & answers

/**
 * QuizQuestion - displays current quiz question and progress.
 * Props:
 *  - question: { id, text }
 *  - progress: { current, total }
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
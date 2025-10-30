import React from 'react';
import './QuizAnswers.css';

/**
 * QuizQuestion - simple question display used on the left column of the quiz page.
 * Shows the question text, optional metadata (progress / points), and a small hint area.
 * Props:
 *  - question: { id, text }
 *  - progress: { current, total }
 */
const QuizQuestion = ({ question = { id: 1, text: 'What is 2 + 2?' }, progress = { current: 1, total: 10 } }) => {
  return (
    <div className="quiz-question">
      <div className="quiz-question__meta">Question {progress.current} / {progress.total}</div>
      <h2 className="quiz-question__text">{question.text}</h2>
      <div className="quiz-question__hint">Select the best answer from the right.</div>
    </div>
  );
};

export default QuizQuestion;

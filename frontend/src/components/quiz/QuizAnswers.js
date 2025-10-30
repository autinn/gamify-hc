import React from 'react';
import './QuizAnswers.css';

/**
 * QuizAnswers - displays four answer options stacked vertically.
 * Each option is styled as a selectable card. Currently there is no
 * state/selection persistence; this component focuses on layout and styling
 * to match the `rightContent` area of `PageLayout`.
 *
 * Props (future):
 *  - options: array of { id, text }
 *  - onSelect: function(id)
 */
const defaultOptions = [
  { id: 'A', text: 'Answer option A' },
  { id: 'B', text: 'Answer option B' },
  { id: 'C', text: 'Answer option C' },
  { id: 'D', text: 'Answer option D' },
];

const QuizAnswers = ({ options = defaultOptions, onSelect }) => {
  return (
    <div className="quiz-answers">
      {options.map((opt) => (
        <button
          key={opt.id}
          className="quiz-answers__option"
          onClick={() => onSelect && onSelect(opt.id)}
          type="button"
        >
          <div className="quiz-answers__label">{opt.id}</div>
          <div className="quiz-answers__text">{opt.text}</div>
        </button>
      ))}
    </div>
  );
};

export default QuizAnswers;

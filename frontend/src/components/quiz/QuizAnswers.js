import React, { useState, useEffect } from 'react';
import './Quiz.css';

/**
 * QuizAnswers - displays multiple-choice options for a given question.
 * Props:
 *  - options: [{ id, text, is_correct, explanation }]
 *  - questionId: string or number (used to reset between questions)
 *  - onCorrect: callback when user selects the correct answer
 */
const QuizAnswers = ({ options, questionId, onCorrect }) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [isLocked, setIsLocked] = useState(false);
  const [attempted, setAttempted] = useState(false);

  // ✅ Reset state when question changes
  useEffect(() => {
    setSelectedOption(null);
    setIsLocked(false);
    setAttempted(false);
  }, [questionId]);

  const handleSelect = (option) => {
    if (isLocked) return; // stop after correct answer
    setSelectedOption(option.id);

    if (option.is_correct) {
      const isFirstAttempt = !attempted;
      setIsLocked(true);
      onCorrect?.(isFirstAttempt);
    } else if (!option.is_correct) {
      setAttempted(true);
    }
  };

  return (
    <div className="quiz-answers">
      {options.map((option) => {
        const isSelected = selectedOption === option.id;
        const isCorrect = option.is_correct && isSelected;
        const isIncorrect = !option.is_correct && isSelected;

        return (
          <div key={option.id} className="quiz-answers__block">
            <div
              className={`quiz-answers__option ${
                isCorrect
                  ? 'quiz-answers__option--correct'
                  : isIncorrect
                  ? 'quiz-answers__option--incorrect'
                  : ''
              }`}
              onClick={() => handleSelect(option)}
            >
              <div className="quiz-answers__label">
                {String.fromCharCode(65 + options.indexOf(option))}
              </div>
              <div className="quiz-answers__text">{option.text}</div>
            </div>

            {isSelected && option.explanation && (
              <div className="quiz-answers__explanation">
                {option.explanation}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};

export default QuizAnswers;

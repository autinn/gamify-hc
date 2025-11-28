import React, { useState, useEffect, useMemo } from 'react';
import './Quiz.css';

const QuizAnswers = ({ options, questionId, onCorrect }) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [isLocked, setIsLocked] = useState(false);

  // 🔀 Shuffle options only when the question changes
  const shuffledOptions = useMemo(() => {
    if (!options) return [];
    const copy = [...options];
    return copy.sort(() => Math.random() - 0.5);
  }, [questionId]); // re-randomize when a *new question* arrives

  useEffect(() => {
    setSelectedOption(null);
    setIsLocked(false);
  }, [questionId]);

  const handleSelect = (option) => {
    if (isLocked) return;
    setSelectedOption(option.id);

    if (option.is_correct) {
      setIsLocked(true);
      onCorrect?.();
    }
  };

  return (
    <div className="quiz-answers">
      {shuffledOptions.map((option) => {
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
              } ${isSelected ? 'quiz-answers__option--expanded' : ''}`}
              onClick={() => handleSelect(option)}
            >
              <div className="quiz-answers__text">{option.text}</div>

              {isSelected && option.explanation && (
                <>
                  <div className="quiz-answers__divider" />
                  <div className="quiz-answers__explanation">
                    {option.explanation}
                  </div>
                </>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default QuizAnswers;
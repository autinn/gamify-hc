import React, { useState, useEffect, useMemo } from 'react';
import './Quiz.css';

const QuizAnswers = ({ options, questionId, onSelect, isAnsweredCorrectly }) => {
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [isLocked, setIsLocked] = useState(false);
  const [attempted, setAttempted] = useState(false);

  // Shuffle once per question
  const shuffledOptions = useMemo(() => {
    if (!options) return [];
    return [...options].sort(() => Math.random() - 0.5);
  }, [questionId]);

  useEffect(() => {
    setSelectedOptions([]);
    setIsLocked(false);
    setAttempted(false);
  }, [questionId]);

  const handleSelect = (option) => {
    if (isLocked) return;

    setSelectedOptions((prev) => [...prev, option.id]);

    // report selection upward
    onSelect(option);

    // lock after correct
    if (option.is_correct) {
      const isFirstAttempt = !attempted;
      setIsLocked(true);
    }
  };

  return (
    <div className="quiz-answers">
      {shuffledOptions.map((option) => {
        const wasSelected = selectedOptions.includes(option.id);

        const isCorrect = option.is_correct && wasSelected;
        const isIncorrect = !option.is_correct && wasSelected;

        return (
          <div key={option.id} className="quiz-answers__block">
            <div
              className={`quiz-answers__option ${
                isCorrect
                  ? 'quiz-answers__option--correct'
                  : isIncorrect
                  ? 'quiz-answers__option--incorrect'
                  : ''
              } ${wasSelected ? 'quiz-answers__option--expanded' : ''}`}
              onClick={() => handleSelect(option)}
            >
              <div className="quiz-answers__text">{option.text}</div>

              {wasSelected && option.explanation && (
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

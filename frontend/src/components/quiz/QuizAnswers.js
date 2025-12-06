import React, { useState, useEffect, useMemo } from 'react';
import { shuffleAnswerOptions } from '../../services/quizService';
import './Quiz.css';

/**
 * QuizAnswers - Component for displaying and handling quiz answer selection
 *
 * Displays shuffled answer options, tracks selection state, and provides feedback.
 * All business logic (shuffling) is delegated to quizService.
 *
 * @param {Array} options - Array of answer option objects with { id, text, is_correct, explanation }
 * @param {number} questionId - ID of current question (used to reset state on question change)
 * @param {Function} onSelect - Callback when option is selected
 * @param {boolean} isAnsweredCorrectly - Whether current question was answered correctly
 */
const QuizAnswers = ({ options, questionId, onSelect, isAnsweredCorrectly }) => {
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [isLocked, setIsLocked] = useState(false);
  const [attempted, setAttempted] = useState(false);

  // Shuffle answers once per question using service function
  const shuffledOptions = useMemo(() => {
    return shuffleAnswerOptions(options);
  }, [questionId, options]);

  // Reset state when question changes
  useEffect(() => {
    setSelectedOptions([]);
    setIsLocked(false);
    setAttempted(false);
  }, [questionId]);

  const handleSelect = (option) => {
    if (isLocked) return;

    setSelectedOptions((prev) => [...prev, option.id]);

    // Report selection upward
    onSelect(option);

    // Lock after correct answer
    if (option.is_correct) {
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

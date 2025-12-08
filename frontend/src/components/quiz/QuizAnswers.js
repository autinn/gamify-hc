import React, { useState, useEffect, useMemo } from 'react';
import { shuffleAnswerOptions } from '../../services/quizService';
import './Quiz.css';

/**
 * QuizAnswers - Answer selection and feedback component for quiz questions
 *
 * Displays answer options (shuffled), tracks selection state, and provides immediate feedback.
 * Shows correct/incorrect indicators and explanations when answers are selected.
 * Part of two-column quiz layout: question on left, answers on right.
 *
 * @component
 * @param {Array<Object>} options - Array of answer option objects
 *   @param {number} options[].id - Answer option ID (quiz_answer_id)
 *   @param {string} options[].text - Answer text to display
 *   @param {boolean} options[].is_correct - Whether this is the correct answer
 *   @param {string} options[].explanation - Explanation shown after selection (if provided)
 * @param {number} questionId - Current question ID (triggers reset on change)
 * @param {Function} onSelect - Callback when user selects an option, receives selected option object
 * @param {boolean} isAnsweredCorrectly - Whether current question was already answered correctly (provided by parent for styling)
 * @returns {React.ReactNode} Answer options with selection and feedback UI
 *
 * Features:
 * - Answers are shuffled per question (using shuffleAnswerOptions from quizService)
 * - Selection tracking: tracks which options user clicked
 * - Feedback: Shows correct/incorrect styling immediately on selection
 * - Explanation: Displays explanation if selected option has one
 * - Locking: Locks answers after correct answer selected (prevents multiple selections)
 * - State reset: Clears selection state when question changes (via questionId dependency)
 *
 * CSS Classes:
 * - quiz-answers: Main container
 * - quiz-answers__block: Individual answer wrapper
 * - quiz-answers__option: Clickable option with variants:
 *   - quiz-answers__option--correct: Green styling for correct answer when selected
 *   - quiz-answers__option--incorrect: Red styling for incorrect answer when selected
 *   - quiz-answers__option--expanded: Expanded state to show explanation
 * - quiz-answers__text: Answer text element
 * - quiz-answers__divider: Separator between answer and explanation
 * - quiz-answers__explanation: Explanation text styling
 *
 * State Management:
 * - selectedOptions: Array of option IDs user has selected (usually 1)
 * - isLocked: Boolean preventing further selections after correct answer
 * - attempted: Boolean tracking if answer attempt was made (for styling)
 *
 * @example
 * <QuizAnswers
 *   options={[
 *     { id: 1, text: "Paris", is_correct: true, explanation: "Paris is the capital of France" },
 *     { id: 2, text: "London", is_correct: false, explanation: "London is the capital of UK" },
 *   ]}
 *   questionId={5}
 *   onSelect={handleAnswerSelected}
 *   isAnsweredCorrectly={false}
 * />
 *
 * Used by: QuizPage component (right column of quiz layout)
 */
const QuizAnswers = ({ options, questionId, onSelect, isAnsweredCorrectly }) => {
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [isLocked, setIsLocked] = useState(false);
  const [attempted, setAttempted] = useState(false);

  // Shuffle answers once per question using service function
  // Prevents answer order from influencing user behavior
  const shuffledOptions = useMemo(() => {
    return shuffleAnswerOptions(options);
  }, [questionId, options]);

  // Clear selection state when question changes to prevent stale feedback
  useEffect(() => {
    setSelectedOptions([]);
    setIsLocked(false);
    setAttempted(false);
  }, [questionId]);

  const handleSelect = (option) => {
    // Don't allow selection if already answered correctly (locked)
    if (isLocked) return;

    // Track this selection in local state for UI feedback
    setSelectedOptions((prev) => [...prev, option.id]);

    // Report selection upward to parent for scoring logic
    onSelect(option);

    // Lock interface after correct answer selected to prevent changing answer
    if (option.is_correct) {
      setIsLocked(true);
    }
  };

  return (
    <div className="quiz-answers">
      {shuffledOptions.map((option) => {
        // Check if this option was selected by the user
        const wasSelected = selectedOptions.includes(option.id);

        // Determine styling based on correctness and selection
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

              {/* Show explanation only if this option was selected */}
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

import React from 'react';
import './ConceptDetail.css';

/**
 * ConceptDetail - Concept learning display with alternating question/answer blocks
 *
 * Displays quiz cards in an alternating pattern: question block followed by answer block.
 * This creates a learning view where students can read questions and see correct answers with explanations.
 * Used on ConceptPage for concept study/review.
 *
 * @component
 * @param {Array<Object>} quizCards - Array of quiz card objects with questions and answers
 *   @param {number} quizCards[].quiz_card_id - Unique card identifier
 *   @param {string} quizCards[].question - Question text to display
 *   @param {Array<Object>} quizCards[].quiz_answers - Array of answer objects for this question
 *     @param {number} quiz_answers[].quiz_answer_id - Answer identifier
 *     @param {string} quiz_answers[].answer_text - Answer text to display
 *     @param {boolean} quiz_answers[].is_correct - Whether this is the correct answer
 *     @param {string} quiz_answers[].explanation - Optional explanation of why answer is correct
 * @returns {React.ReactNode} Alternating question and answer blocks or "No questions" message
 *
 * Layout Pattern:
 * 1. Question block (narrow horizontal rectangle with question text)
 * 2. Answer block (taller rectangle with answer text and explanation)
 * 3. Repeat for each quiz card
 *
 * CSS Classes:
 * - concept-detail: Main container
 * - concept-detail__question: Question block wrapper
 * - concept-detail__answer: Answer block wrapper
 * - concept-detail__text: Text element with variants:
 *   - concept-detail__text--question: Question text styling
 *   - concept-detail__text--answer: Correct answer styling
 *   - concept-detail__text--explanation: Explanation text styling
 *
 * @example
 * const quizCards = [
 *   {
 *     quiz_card_id: 1,
 *     question: "What is photosynthesis?",
 *     quiz_answers: [
 *       {
 *         quiz_answer_id: 1,
 *         answer_text: "Process by which plants convert light to chemical energy",
 *         is_correct: true,
 *         explanation: "This is the correct definition of photosynthesis"
 *       }
 *     ]
 *   }
 * ];
 * <ConceptDetail quizCards={quizCards} />
 *
 * Used by: ConceptPage component
 */
const ConceptDetail = ({ quizCards }) => {
  if (!quizCards || quizCards.length === 0) {
    return (
      <div className="concept-detail">
        <p>No questions available for this concept.</p>
      </div>
    );
  }

  // Find the correct answer object for this quiz card (marked with is_correct: true in API)
  const getCorrectAnswer = (quizCard) => {
    return quizCard.quiz_answers?.find(answer => answer.is_correct === true);
  };

  return (
    <div className="concept-detail">
      {quizCards.map((quizCard) => {
        const correctAnswer = getCorrectAnswer(quizCard);
        
        return (
          <React.Fragment key={quizCard.quiz_card_id}>
            {/* Question Block - displays the quiz question */}
            <div className="concept-detail__question">
              <p className="concept-detail__text concept-detail__text--question">{quizCard.question}</p>
            </div>
            
            {/* Answer Block - displays the correct answer with optional explanation */}
            {correctAnswer && (
              <div className="concept-detail__answer">
                <div className="concept-detail__answer-content">
                  <p className="concept-detail__text concept-detail__text--answer">{correctAnswer.answer_text}</p>
                  {correctAnswer.explanation && (
                    <p className="concept-detail__text concept-detail__text--explanation">{correctAnswer.explanation}</p>
                  )}
                </div>
              </div>
            )}
          </React.Fragment>
        );
      })}
    </div>
  );
};

export default ConceptDetail;


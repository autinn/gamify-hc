import React from 'react';
import './QuestionAnswerBlocks.css';

/**
 * QuestionAnswerBlocks - Displays alternating Question and Answer blocks
 *
 * Displays quiz cards with their corresponding answers in an alternating pattern.
 * Question blocks are narrow horizontal rectangles, Answer blocks are taller.
 *
 * @param {array} quizCards - Array of quiz card objects with question and quiz_answers
 */
const QuestionAnswerBlocks = ({ quizCards }) => {
  if (!quizCards || quizCards.length === 0) {
    return (
      <div className="question-answer-blocks">
        <p>No questions available for this concept.</p>
      </div>
    );
  }

  // Find the correct answer for each quiz card
  const getCorrectAnswer = (quizCard) => {
    return quizCard.quiz_answers?.find(answer => answer.is_correct === true);
  };

  return (
    <div className="question-answer-blocks">
      {quizCards.map((quizCard) => {
        const correctAnswer = getCorrectAnswer(quizCard);
        
        return (
          <React.Fragment key={quizCard.quiz_card_id}>
            {/* Question Block */}
            <div className="question-answer-blocks__question">
              <p className="question-answer-blocks__text question-answer-blocks__text--question">{quizCard.question}</p>
            </div>
            
            {/* Answer Block */}
            {correctAnswer && (
              <div className="question-answer-blocks__answer">
                <p className="question-answer-blocks__text question-answer-blocks__text--answer">{correctAnswer.answer_text}</p>
              </div>
            )}
          </React.Fragment>
        );
      })}
    </div>
  );
};

export default QuestionAnswerBlocks;


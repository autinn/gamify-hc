import React from 'react';
import './ConceptDetail.css';

/**
 * ConceptDetail - Displays concept details with alternating Question and Answer blocks
 *
 * Displays quiz cards with their corresponding answers in an alternating pattern.
 * Question blocks are narrow horizontal rectangles, Answer blocks are taller.
 *
 * @param {array} quizCards - Array of quiz card objects with question and quiz_answers
 */
const ConceptDetail = ({ quizCards }) => {
  if (!quizCards || quizCards.length === 0) {
    return (
      <div className="concept-detail">
        <p>No questions available for this concept.</p>
      </div>
    );
  }

  // Find the correct answer for each quiz card
  const getCorrectAnswer = (quizCard) => {
    return quizCard.quiz_answers?.find(answer => answer.is_correct === true);
  };

  return (
    <div className="concept-detail">
      {quizCards.map((quizCard) => {
        const correctAnswer = getCorrectAnswer(quizCard);
        
        return (
          <React.Fragment key={quizCard.quiz_card_id}>
            {/* Question Block */}
            <div className="concept-detail__question">
              <p className="concept-detail__text concept-detail__text--question">{quizCard.question}</p>
            </div>
            
            {/* Answer Block */}
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


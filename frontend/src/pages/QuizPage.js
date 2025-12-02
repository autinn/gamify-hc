import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import QuizAnswers from '../components/quiz/QuizAnswers';
import QuizQuestion from '../components/quiz/QuizQuestion';
import QuizResults from '../components/quiz/QuizResults';
import { useQuiz } from '../hooks/useQuiz';
import { useConcept } from '../hooks/useConcept';
import { useUnit } from '../hooks/useUnit';
import { useCourse } from '../hooks/useCourse';
import { getQuizBackPath } from '../services/quizService';
import '../components/quiz/Quiz.css';

const QuizPage = () => {
  const { courseId, unitId, conceptId } = useParams();
  const navigate = useNavigate();
  
  const {
    currentQuestion,
    currentIndex,
    correctCount,
    totalCount,
    isAnsweredCorrectly,
    isQuizDone,
    handleSelect,
    handleNext
  } = useQuiz(courseId, unitId, conceptId);

  const { concept } = useConcept(courseId, unitId, conceptId);
  const { unit } = useUnit(courseId, unitId);
  const { course } = useCourse(courseId);

  const greeting = conceptId 
    ? `Quiz for ${concept?.title || 'Concept'}`
    : unitId 
    ? `Quiz for ${unit?.title || 'Unit'}`
    : courseId 
    ? `Quiz for ${course?.title || courseId}`
    : 'Quiz';

  return (
    <PageLayout
      greeting={greeting}
      showButton={false}
      showBackButton={true}
      onBackClick={() => navigate(getQuizBackPath(courseId, unitId, conceptId))}
      leftContent={
        isQuizDone ? (
          <h2 className="quiz-results__title">Quiz Complete!</h2>
        ) : (
          <QuizQuestion
            question={currentQuestion}
            progress={{ current: currentIndex + 1, total: totalCount }}
          />
        )
      }
      rightContent={
        isQuizDone ? (
          <QuizResults 
            correctCount={correctCount} 
            totalCount={totalCount} 
          />
        ) : (
          <>
            <QuizAnswers
              key={currentQuestion?.id}
              questionId={currentQuestion?.id}
              options={currentQuestion?.options || []}
              onSelect={handleSelect}
              isAnsweredCorrectly={isAnsweredCorrectly}
            />

            {isAnsweredCorrectly && (
              <div className="quiz-next-container">
                <button className="quiz-next-button" onClick={handleNext}>
                  Next Question →
                </button>
              </div>
            )}
          </>
        )
      }
    />
  );
};

export default QuizPage;
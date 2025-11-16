import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import QuizAnswers from '../components/quiz/QuizAnswers';
import QuizQuestion from '../components/quiz/QuizQuestion';
import QuizResults from '../components/quiz/QuizResults';
import * as api from '../services/api';
import '../components/quiz/Quiz.css';

/**
 * QuizPage - Quiz interface for course, unit, or concept level quizzes
 * 
 * CHANGES: Replaced dummy data (hardcoded dummyQuestions array) with API calls
 * to fetch real quiz cards from the backend based on URL parameters (courseId, unitId, conceptId).
 * Added useEffect hook to fetch quiz cards when component mounts or URL parameters change.
 */
const QuizPage = () => {
  const { courseId, unitId, conceptId } = useParams();
  // State for quiz questions fetched from API
  // Previously: Used hardcoded dummyQuestions array
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [isAnsweredCorrectly, setIsAnsweredCorrectly] = useState(false);

  useEffect(() => {
    // CHANGED: Replaced dummy data with API calls to fetch quiz cards based on quiz level
    // Previously: const currentQuestion = dummyQuestions[currentIndex];
    // Fetches quiz cards for concept, unit, or course level based on URL parameters
    let fetchPromise;
    if (conceptId) {
      fetchPromise = api.getConceptQuizCards(parseInt(conceptId, 10));
    } else if (unitId) {
      fetchPromise = api.getUnitQuizCards(parseInt(unitId, 10));
    } else if (courseId) {
      fetchPromise = api.getCourseQuizCards(parseInt(courseId, 10));
    } else {
      return;
    }

    fetchPromise.then(quizCards => {
      if (quizCards && quizCards.length > 0) {
        // Shuffle and map API response to component question format
        // Backend returns: {id, question, answers: [{id, answer_text, ...}]}
        // Component expects: {id, text, options: [{id, text, ...}]}
        const shuffled = [...quizCards].sort(() => Math.random() - 0.5);
        setQuestions(shuffled.map(qc => ({
          id: qc.id,
          text: qc.question,
          options: qc.answers.map(a => ({
            id: a.id,
            text: a.answer_text,
            is_correct: a.is_correct,
            explanation: a.explanation
          }))
        })));
      }
    }).catch(err => console.error('Error fetching quiz cards:', err));
  }, [courseId, unitId, conceptId]);

  const currentQuestion = questions[currentIndex];
  const totalCount = questions.length;
  const isQuizDone = currentIndex >= totalCount;
  const greeting = courseId ? `Quiz for ${courseId}` : 'Quiz';
  const title = unitId ? `Unit ${unitId}` : courseId ? courseId : 'Practice';

  const handleCorrect = () => {
    // ✅ Mark as correct but wait for the user to click “Next Question”
    setIsAnsweredCorrectly(true);
    setCorrectCount((prev) => prev + 1);
  };

  const handleNext = () => {
    setIsAnsweredCorrectly(false);
    setCurrentIndex((i) => i + 1);
  };

  return (
    <PageLayout
      greeting={greeting}
      title={title}
      showButton={false}
      leftContent={
        isQuizDone ? (
          <QuizResults correctCount={correctCount} totalCount={totalCount} />
        ) : (
          <QuizQuestion
            question={currentQuestion}
            progress={{ current: currentIndex + 1, total: totalCount }}
          />
        )
      }
      rightContent={
        !isQuizDone && (
          <>
            <QuizAnswers
              key={currentQuestion?.id}
              questionId={currentQuestion?.id}
              options={currentQuestion?.options || []}
              onCorrect={handleCorrect}
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
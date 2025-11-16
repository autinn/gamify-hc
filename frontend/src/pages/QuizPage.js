import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import QuizAnswers from '../components/quiz/QuizAnswers';
import QuizQuestion from '../components/quiz/QuizQuestion';
import QuizResults from '../components/quiz/QuizResults';
import '../components/quiz/Quiz.css';

const dummyQuestions = [
  {
    id: 1,
    text: 'What is 2 + 2?',
    options: [
      { id: 'A', text: '3', is_correct: false, explanation: '2 + 2 equals 4.' },
      { id: 'B', text: '4', is_correct: true, explanation: 'Correct! 2 + 2 = 4.' },
      { id: 'C', text: '5', is_correct: false, explanation: 'No, that’s too high.' },
      { id: 'D', text: '22', is_correct: false, explanation: 'That’s concatenation, not addition.' },
    ],
  },
  {
    id: 2,
    text: 'Which planet is known as the Red Planet?',
    options: [
      { id: 'A', text: 'Venus', is_correct: false, explanation: 'Venus is yellowish-white.' },
      { id: 'B', text: 'Mars', is_correct: true, explanation: 'Mars is often called the Red Planet.' },
      { id: 'C', text: 'Jupiter', is_correct: false, explanation: 'That’s a gas giant, not red.' },
      { id: 'D', text: 'Mercury', is_correct: false, explanation: 'Mercury is grey.' },
    ],
  },
  {
    id: 3,
    text: 'What is the capital of South Korea?',
    options: [
      { id: 'A', text: 'Busan', is_correct: false, explanation: 'Busan is the second-largest city.' },
      { id: 'B', text: 'Tokyo', is_correct: false, explanation: 'Tokyo is in Japan.' },
      { id: 'C', text: 'Seoul', is_correct: true, explanation: 'Correct! Seoul is the capital.' },
      { id: 'D', text: 'Pyongyang', is_correct: false, explanation: 'That’s the capital of North Korea.' },
    ],
  },
];

const QuizPage = () => {
  const { courseId, unitId } = useParams();
  const greeting = courseId ? `Quiz for ${courseId}` : 'Quiz';
  const title = unitId ? `Unit ${unitId}` : courseId ? courseId : 'Practice';

  const [currentIndex, setCurrentIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [isAnsweredCorrectly, setIsAnsweredCorrectly] = useState(false);

  const currentQuestion = dummyQuestions[currentIndex];
  const totalCount = dummyQuestions.length;
  const isQuizDone = currentIndex >= totalCount;

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
              key={currentQuestion.id}
              questionId={currentQuestion.id}
              options={currentQuestion.options}
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
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

/**
 * QuizPage - Interactive quiz assessment page
 *
 * Displays quiz questions and answer options in two-column layout.
 * Left column shows current question with progress. Right column shows answer options.
 * Supports quizzes at three levels: course, unit, or concept.
 * Shows results screen after quiz completion.
 *
 * @component
 * @returns {React.ReactNode} Two-column quiz layout or results screen
 *
 * Route Parameters (URL-based quiz determination):
 * - courseId: Required - identifies which course quiz
 * - unitId: Optional - if present, quiz is for specific unit within course
 * - conceptId: Optional - if present, quiz is for specific concept within unit
 *
 * Quiz Level Logic:
 * - Concept-level quiz: /course/:courseId/unit/:unitId/concept/:conceptId/quiz
 * - Unit-level quiz: /course/:courseId/unit/:unitId/quiz
 * - Course-level quiz: /course/:courseId/quiz
 *
 * Data Requirements:
 * - useQuiz hook: Main quiz logic (question progression, scoring, state management)
 *   - Parameters: courseId, unitId, conceptId
 *   - Returns: currentQuestion, currentIndex, correctCount, totalCount, isAnsweredCorrectly, isQuizDone, handleSelect, handleNext
 * - useConcept/useUnit/useCourse hooks: For title display (lazy-loaded based on quiz level)
 *
 * Page State Transitions:
 * 1. Quiz In Progress: Shows QuizQuestion (left) and QuizAnswers (right)
 *    - User selects answer → handleSelect updates state
 *    - Correct answer → isAnsweredCorrectly = true, unlock "Next Question" button
 *    - User clicks "Next Question" → handleNext moves to next question
 * 2. Quiz Complete: Shows "Quiz Complete!" (left) and QuizResults (right)
 *    - Displays final score and percentage
 *    - "Return Home" button navigates back to /(default) or previous page
 *
 * Layout Structure (via PageLayout):
 * - Left Column:
 *   - Greeting: "Quiz for"
 *   - Title: Concept/Unit/Course name depending on quiz level
 *   - Content: QuizQuestion during quiz, "Quiz Complete!" after quiz
 *   - Back button: Returns to previous page (quiz start location)
 * - Right Column:
 *   - Content: QuizAnswers during quiz, QuizResults after quiz
 *   - "Next Question" button: Appears only after correct answer selection
 *
 * Navigation:
 * - Back button: Uses getQuizBackPath() to determine correct return path based on quiz level
 * - "Next Question" button: Advances to next question (appears after correct answer)
 * - "Return Home" (in QuizResults): Returns to MainPage (/)
 *
 * CSS Classes:
 * - quiz-next-container: Container for "Next Question" button
 * - quiz-next-button: Styled button with arrow → (appears conditionally)
 * - quiz-results__title: "Quiz Complete!" title
 *
 * Title Determination:
 * - Prefers loaded names from hooks: concept title, unit title, or course title
 * - Falls back to IDs if data not loaded yet (e.g., "Concept 5")
 * - Handles any combination of available data gracefully
 *
 * @example
 * <QuizPage />
 * // URL: /course/3/unit/7/concept/12/quiz
 * // Displays: Two-column layout with quiz questions and answer options
 * // Title: Name of concept (or "Concept 12" if loading)
 *
 * Used by: Router for quiz pages at different hierarchy levels (course/unit/concept)
 */

const QuizPage = () => {
  const { courseId, unitId, conceptId } = useParams();
  const navigate = useNavigate();
  
  // Fetch quiz data and state management (question progression, scoring)
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

  // Fetch context data for title display (lazy-loaded as needed)
  const { concept } = useConcept(courseId, unitId, conceptId);
  const { unit } = useUnit(courseId, unitId);
  const { course } = useCourse(courseId);

  // Quiz greeting (prefix for title)
  const greeting = 'Quiz for'

  // Determine quiz title based on available data (concept > unit > course)
  // Prefers actual names from API but falls back to IDs if still loading
  const title = conceptId 
    ? concept?.title || `Concept ${conceptId}`
    : unitId 
    ? unit?.title || `Unit ${unitId}`
    : courseId 
    ? course?.title || courseId
    : 'All Courses';

  return (
    <PageLayout
      greeting={greeting}
      title={title}
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

            {/* Show "Next Question" button only after correct answer selected */}
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
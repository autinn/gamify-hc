import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Button from '../components/common/UI/Button';
import ConceptDetail from '../components/concept/ConceptDetail';
import Header from '../components/common/layout/Header';
import { useConcept } from '../hooks/useConcept';
import './ConceptPage.css';

/**
 * ConceptPage - Concept learning page with study materials (questions and answers)
 *
 * Displays concept name, definition, and quiz questions/answers in study format.
 * Gets courseId, unitId, and conceptId from URL parameters to fetch concept-specific data.
 * Provides navigation to concept-specific quiz for assessment.
 *
 * @component
 * @returns {React.ReactNode} Concept study page with questions/answers and navigation
 *
 * Route Parameters:
 * - courseId: Parent course identifier
 * - unitId: Parent unit identifier
 * - conceptId: Concept identifier
 *
 * Data Requirements:
 * - useConcept hook: Fetches course, unit, concept, and quiz cards (questions/answers)
 *   - Returns: {
 *       course: { title, ... },
 *       unit: { title, ... },
 *       concept: { title, definition, ... },
 *       quizCards: [{ quiz_card_id, question, quiz_answers: [...] }, ...]
 *     }
 *
 * Page Structure:
 * 1. Header Component: App navigation with course dropdown
 * 2. Back Button Bar: "← Back" button to return to UnitPage
 * 3. Header Section:
 *    - Greeting: Hierarchical path (e.g., "Biology 101 - Unit 1: Cells")
 *    - Title: Concept title
 *    - Definition: Concept definition text (if available)
 *    - "Start Quiz" button: Navigates to concept-specific quiz
 * 4. Content Section:
 *    - ConceptDetail: Displays quiz questions and correct answers in study format
 *
 * Navigation:
 * - Back button: Returns to UnitPage (/course/:courseId/unit/:unitId)
 * - "Start Quiz" button: Navigates to /course/:courseId/unit/:unitId/concept/:conceptId/quiz
 * - Header: Allows navigation to other courses via dropdown
 *
 * Greeting Logic:
 * - Prefers full path: "Course Title - Unit Title" when both available
 * - Falls back to course name or ID pairs if data loading
 * - Maintains context showing concept location in hierarchy
 *
 * CSS Classes:
 * - concept-page: Main page container
 * - concept-page__back-button-bar: Back button wrapper
 * - concept-page__header: Header section (greeting, title, buttons)
 * - concept-page__greeting: Hierarchical path text
 * - concept-page__header-row: Title and button row
 * - concept-page__title: Concept title heading
 * - concept-page__button-container: Start Quiz button wrapper
 * - concept-page__definition: Concept definition text
 * - concept-page__content: Content section with ConceptDetail
 *
 * @example
 * <ConceptPage />
 * // URL: /course/3/unit/7/concept/12
 * // Displays: Concept title, definition, and questions/answers for study
 *
 * Used by: Router for concept detail navigation (/:courseId/unit/:unitId/concept/:conceptId route)
 */
const ConceptPage = () => {
  const { courseId, unitId, conceptId } = useParams();
  const navigate = useNavigate();
  
  const { course, unit, concept, quizCards } = useConcept(courseId, unitId, conceptId);

  // Build greeting showing full hierarchical path: "Course Title - Unit Title"
  // Provides context showing where this concept is located in the course structure
  const greeting = course && unit 
    ? `${course.title} - ${unit.title}`
    : course 
    ? `${course.title} - Unit ${unitId}`
    : unit 
    ? `${courseId} - ${unit.title}`
    : `${courseId} - Unit ${unitId}`;

  // Handle quiz button click - navigate to concept-specific quiz
  const handleStartQuiz = () => {
    navigate(`/course/${courseId}/unit/${unitId}/concept/${conceptId}/quiz`);
  };

  return (
    <>
      <Header />

      <div className="concept-page">
        {/* Back Button Bar */}
        <div className="concept-page__back-button-bar">
          <Button 
            label="← Back" 
            variant="secondary" 
            onClick={() => navigate(`/course/${courseId}/unit/${unitId}`)} 
          />
        </div>

        {/* Header Section */}
        <div className="concept-page__header">
        <p className="concept-page__greeting">{greeting}</p>
        <div className="concept-page__header-row">
          <h1 className="concept-page__title">{concept ? concept.title : ''}</h1>
          <div className="concept-page__button-container">
            <Button label="Start Quiz" variant="primary" onClick={handleStartQuiz} />
          </div>
        </div>
        {concept && concept.definition && (
          <p className="concept-page__definition">{concept.definition}</p>
        )}
      </div>

      {/* Content Section */}
      <div className="concept-page__content">
        <ConceptDetail quizCards={quizCards} />
      </div>
      </div>
    </>
  );
};

export default ConceptPage;


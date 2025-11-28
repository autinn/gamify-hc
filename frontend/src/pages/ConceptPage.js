import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Button from '../components/common/UI/Button';
import ConceptDetail from '../components/concept/ConceptDetail';
import Header from '../components/common/layout/Header';
import { useConcept } from '../hooks/useConcept';
import './ConceptPage.css';

/**
 * ConceptPage - Concept details page with quiz cards (questions and answers)
 *
 * Displays concept name, quiz questions and answers.
 * Uses URL parameters :courseId, :unitId, and :conceptId to determine which concept to display.
 */
const ConceptPage = () => {
  const { courseId, unitId, conceptId } = useParams();
  const navigate = useNavigate();
  
  const { course, unit, concept, quizCards } = useConcept(courseId, unitId, conceptId);

  // Build greeting with course and unit names
  const greeting = course && unit 
    ? `${course.title} - ${unit.title}`
    : course 
    ? `${course.title} - Unit ${unitId}`
    : unit 
    ? `${courseId} - ${unit.title}`
    : `${courseId} - Unit ${unitId}`;

  // Handle quiz button click
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


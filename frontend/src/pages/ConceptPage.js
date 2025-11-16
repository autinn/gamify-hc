import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Button from '../components/common/UI/Button';
import QuestionAnswerBlocks from '../components/concept/QuestionAnswerBlocks';
import Header from '../components/common/layout/Header';
import * as api from '../services/api';
import './ConceptPage.css';

/**
 * ConceptPage - Concept details page with quiz cards (questions and answers)
 *
 * Displays concept name, quiz questions and answers.
 * Uses URL parameters :courseId, :unitId, and :conceptId to determine which concept to display.
 * Uses PageLayout for consistent two-column structure.
 * 
 * CHANGES: Replaced dummy data (hardcoded conceptData, courses, and units objects)
 * with API calls to fetch real data from the backend. Added useState/useEffect hooks
 * to manage API data fetching and state.
 */
const ConceptPage = () => {
  const { courseId, unitId, conceptId } = useParams();
  const navigate = useNavigate();
  const courseIdInt = parseInt(courseId, 10);
  const unitIdInt = parseInt(unitId, 10);
  const conceptIdInt = parseInt(conceptId, 10);

  // State for course, unit, concept, and quiz cards data fetched from API
  // Previously: Used hardcoded dummy data objects (conceptData, courses, units)
  const [course, setCourse] = useState(null);
  const [unit, setUnit] = useState(null);
  const [concept, setConcept] = useState(null);
  const [quizCards, setQuizCards] = useState([]);

  useEffect(() => {
    // CHANGED: Replaced dummy data lookup with API calls to fetch real course, unit, concept, and quiz cards
    // Previously: const concept = conceptData[conceptIdInt] || null;
    // Previously: const course = courses[courseIdInt] || null;
    // Previously: const unit = units[unitIdInt] || null;
    // Fetch course, unit, concept, and quiz cards
    Promise.all([
      api.getCourse(courseIdInt),
      api.getUnit(unitIdInt),
      api.getConcept(conceptIdInt),
      api.getConceptQuizCards(conceptIdInt)
    ])
      .then(([courseData, unitData, conceptData, quizCardsData]) => {
        // Map API response fields to component expectations
        // Backend returns: {id, name/code, description} -> Component expects: {course_id, title, description}
        setCourse({
          course_id: courseData.id,
          title: courseData.name || courseData.code,
          description: courseData.description
        });

        // Map API response fields to component expectations
        // Backend returns: {id, name, ...} -> Component expects: {unit_id, title, ...}
        setUnit({
          unit_id: unitData.id,
          course_id: unitData.course_id,
          title: unitData.name,
          description: unitData.description
        });

        // Map API response fields to component expectations
        // Backend returns: {id, name/tag, ...} -> Component expects: {concept_id, title, ...}
        setConcept({
          concept_id: conceptData.id,
          unit_id: conceptData.unit_id,
          title: conceptData.name || conceptData.tag,
          definition: conceptData.definition
        });

        // Map quiz cards - backend returns array of quiz cards with answers
        // Previously: Used hardcoded quiz_cards from conceptData object
        // Backend returns: {id, hc_id, question, answers: [{id, answer_text, ...}]}
        // Component expects: {quiz_card_id, concept_id, question, quiz_answers: [{answer_id, ...}]}
        const mappedQuizCards = quizCardsData.map(qc => ({
          quiz_card_id: qc.id,
          concept_id: qc.hc_id,
          question: qc.question,
          quiz_answers: qc.answers.map(a => ({
            answer_id: a.id,
            quiz_card_id: qc.id,
            answer_text: a.answer_text,
            is_correct: a.is_correct,
            explanation: a.explanation
          }))
        }));
        setQuizCards(mappedQuizCards);
      })
      .catch(err => {
        console.error('Error fetching concept data:', err);
      });
  }, [courseIdInt, unitIdInt, conceptIdInt]);

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
        <QuestionAnswerBlocks quizCards={quizCards} />
      </div>
      </div>
    </>
  );
};

export default ConceptPage;


import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ConceptCard.css';

/**
 * ConceptCard - Individual concept card component
 *
 * Displays a single concept as a clickable card.
 * Navigates to the ConceptPage when clicked using hierarchical routing.
 *
 * @param {object} concept - Concept object with concept_id and title (from DB schema)
 * @param {string} courseId - Parent course ID (course_id from URL)
 * @param {string} unitId - Parent unit ID (unit_id from URL)
 */
const ConceptCard = ({ concept, courseId, unitId }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/course/${courseId}/unit/${unitId}/concept/${concept.concept_id}`);
  };

  return (
    <div className="concept-card" onClick={handleClick} role="button" tabIndex={0}>
      <p className="concept-card__name">{concept.title}</p>
    </div>
  );
};

export default ConceptCard;

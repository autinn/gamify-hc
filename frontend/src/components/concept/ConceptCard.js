import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ConceptCard.css';

/**
 * ConceptCard - Individual concept card component
 *
 * Displays a single concept as a clickable card.
 * Navigates to the ConceptPage when clicked using hierarchical routing.
 *
 * @param {object} concept - Concept object with id and name/title
 * @param {string} courseId - Parent course ID (e.g., "EA50")
 * @param {string} unitId - Parent unit ID (e.g., "1")
 */
const ConceptCard = ({ concept, courseId, unitId }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/course/${courseId}/unit/${unitId}/concept/${concept.id}`);
  };

  return (
    <div className="concept-card" onClick={handleClick} role="button" tabIndex={0}>
      <p className="concept-card__name">{concept.name}</p>
    </div>
  );
};

export default ConceptCard;

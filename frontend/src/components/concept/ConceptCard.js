import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ConceptCard.css';

/**
 * ConceptCard - Individual concept card component
 *
 * Displays a single concept as a clickable card showing concept title.
 * When clicked, navigates to the concept detail page with hierarchical routing.
 *
 * @component
 * @param {Object} concept - Concept object
 *   @param {number} concept.concept_id - Unique concept identifier (from DB)
 *   @param {string} concept.title - Concept name/title to display
 * @param {number} courseId - Parent course ID (for navigation path)
 * @param {number} unitId - Parent unit ID (for navigation path)
 * @returns {React.ReactNode} Clickable concept card
 *
 * Navigation Path:
 * /course/:courseId/unit/:unitId/concept/:conceptId
 *
 * CSS Classes:
 * - concept-card: Main card container (clickable, hover effect)
 * - concept-card__name: Concept title text element
 *
 * @example
 * const concept = { concept_id: 3, title: "Data Analysis" };
 * <ConceptCard
 *   concept={concept}
 *   courseId={1}
 *   unitId={5}
 * />
 * // Displays: "Data Analysis" (clickable)
 *
 * Used by: ConceptList component
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

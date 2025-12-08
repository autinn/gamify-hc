import React from 'react';
import ConceptCard from './ConceptCard';
import './ConceptList.css';

/**
 * ConceptList - Container for concept cards with grid layout
 *
 * Renders an array of ConceptCard components in a flexible grid.
 * Each concept is displayed as a clickable card that navigates to concept detail page.
 *
 * @component
 * @param {Array<Object>} concepts - Array of concept objects from API
 *   @param {number} concepts[].concept_id - Unique concept identifier
 *   @param {string} concepts[].title - Concept name to display
 * @param {number} courseId - Parent course ID (for navigation)
 * @param {number} unitId - Parent unit ID (for navigation)
 * @returns {React.ReactNode} Grid container of ConceptCard components
 *
 * Grid Layout:
 * - CSS class: concept-list (flex container with responsive grid)
 * - Adapts column count based on screen size
 * - Each child is a ConceptCard component
 *
 * Data Flow:
 * - Typically receives concepts from useConcept hook (parent) filtered by unit_id
 * - Passes through concept object and parent IDs to each ConceptCard for navigation
 *
 * @example
 * const concepts = [
 *   { concept_id: 1, title: "Concept One", ... },
 *   { concept_id: 2, title: "Concept Two", ... }
 * ];
 * <ConceptList concepts={concepts} courseId={1} unitId={5} />
 *
 * Used by: UnitPage component
 */
const ConceptList = ({ concepts, courseId, unitId }) => {
  return (
    <div className="concept-list">
      {concepts.map((concept) => (
        <ConceptCard 
            key={concept.concept_id} 
            concept={concept}
            courseId={courseId}
            unitId={unitId}
        />
      ))}
    </div>
  );
};

export default ConceptList;
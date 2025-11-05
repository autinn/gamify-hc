import React from 'react';
import ConceptCard from './ConceptCard';
import './ConceptList.css';

/**
 * ConceptList - List of concept cards
 *
 * Displays a list of concepts as clickable cards.
 *
 * @param {array} concepts - Array of concept objects
 * @param {string} courseId - Parent course ID
 * @param {string} unitId - Parent unit ID
 */
const ConceptList = ({ concepts, courseId, unitId }) => {
  return (
    <div className="concept-list">
      {concepts.map((concept) => (
        <ConceptCard 
            key={concept.id} 
            concept={concept}
            courseId={courseId}
            unitId={unitId}
        />
      ))}
    </div>
  );
};

export default ConceptList;
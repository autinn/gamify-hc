import React from 'react';
import ConceptCard from './ConceptCard';
import './ConceptList.css';

const ConceptList = ({ concepts }) => {
  return (
    <div className="concept-list">
      {concepts.map((concept) => (
        <ConceptCard 
            key={concept.id} 
            concept={concept} 
        />
      ))}
    </div>
  );
};

export default ConceptList;
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ConceptCard.css';

const ConceptCard = ({ concept }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/concept/${concept.id}`);
  };

  return (
    <div className="concept-card" onClick={handleClick} role="button" tabIndex={0}>
      <p className="concept-card__name">{concept.name}</p>
    </div>
  );
};

export default ConceptCard;

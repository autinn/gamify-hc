import React from 'react';
import { useNavigate } from 'react-router-dom';
import './UnitCard.css';

/**
 * UnitCard - Individual unit card component
 *
 * Displays a single unit as a clickable card.
 * Navigates to the UnitPage when clicked.
 *
 * @param {string} courseId - Parent course ID (e.g., "EA50")
 * @param {number} unitNumber - Unit number (1, 2, 3...)
 * @param {string} unitName - Unit name (e.g., "Problem-Solving")
 * @param {number} questionCount - Number of questions in this unit
 */
const UnitCard = ({ courseId, unitNumber, unitName, questionCount }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/course/${courseId}/unit/${unitNumber}`);
  };

  return (
    <div className="unit-card" onClick={handleClick} role="button" tabIndex={0}>
      <p className="unit-card__number">Unit {unitNumber}:</p>
      <p className="unit-card__name">{unitName}</p>
    </div>
  );
};

export default UnitCard;


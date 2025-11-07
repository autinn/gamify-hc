import React from 'react';
import { useNavigate } from 'react-router-dom';
import './UnitCard.css';

/**
 * UnitCard - Individual unit card component
 *
 * Displays a single unit as a clickable card.
 * Navigates to the UnitPage when clicked.
 *
 * @param {string} courseId - Parent course ID (course_id from URL)
 * @param {number} unitId - Unit ID (unit_id from DB schema)
 * @param {string} unitTitle - Unit title (e.g., "Problem-Solving")
 */
const UnitCard = ({ courseId, unitId, unitTitle }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/course/${courseId}/unit/${unitId}`);
  };

  return (
    <div className="unit-card" onClick={handleClick} role="button" tabIndex={0}>
      <p className="unit-card__name">{unitTitle}</p>
    </div>
  );
};

export default UnitCard;


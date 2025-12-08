import React from 'react';
import { useNavigate } from 'react-router-dom';
import './UnitCard.css';

/**
 * UnitCard - Individual unit card component
 *
 * Displays a single unit as a clickable card. Shows unit number and title.
 * When clicked, navigates to the unit detail page showing concepts.
 *
 * @component
 * @param {number} courseId - Parent course ID (from URL for navigation)
 * @param {number} unitId - Unit ID (unit_id from DB)
 * @param {string} unitTitle - Unit title/name to display
 * @param {number} orderIndex - Unit order index (0-based, displayed as Unit 1, Unit 2, etc.)
 * @returns {React.ReactNode} Clickable unit card
 *
 * Display Format:
 * - If orderIndex provided: "Unit {orderIndex + 1}: {unitTitle}"
 * - If no orderIndex: Just "{unitTitle}"
 *
 * CSS Classes:
 * - unit-card: Main card container (clickable, hover effect)
 * - unit-card__name: Unit name text element
 *
 * @example
 * <UnitCard
 *   courseId={1}
 *   unitId={5}
 *   unitTitle="Problem-Solving"
 *   orderIndex={0}
 * />
 * // Displays: "Unit 1: Problem-Solving"
 *
 * Used by: UnitList component
 */
const UnitCard = ({ courseId, unitId, unitTitle, orderIndex }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/course/${courseId}/unit/${unitId}`);
  };

  return (
    <div className="unit-card" onClick={handleClick} role="button" tabIndex={0}>
      <p className="unit-card__name">
        {orderIndex !== undefined && orderIndex !== null 
          ? `Unit ${orderIndex + 1}: ${unitTitle}`
          : unitTitle}
      </p>
    </div>
  );
};

export default UnitCard;


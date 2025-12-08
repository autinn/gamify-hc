import React from 'react';
import UnitCard from './UnitCard';
import './UnitList.css';

/**
 * UnitList - Container for unit cards with dynamic responsive grid
 *
 * Renders an array of UnitCard components in a flexible grid layout.
 * Grid automatically adjusts based on screen size and number of items.
 * Units are sorted by order_index before display to ensure consistent ordering.
 *
 * @component
 * @param {string} courseId - Parent course ID for navigation to UnitPage
 * @param {Array<Object>} units - Array of unit objects from API
 *   @param {number} units[].unit_id - Unique unit identifier
 *   @param {string} units[].title - Unit name/title
 *   @param {number} units[].order_index - Sort order (0-based, displayed as Unit 1, Unit 2, etc.)
 *
 * @returns {React.ReactNode} Grid container of UnitCard components
 *
 * Example Unit Object:
 * {
 *   unit_id: 5,
 *   title: "Problem-Solving Techniques",
 *   order_index: 2,
 *   // ... other properties
 * }
 *
 * Grid Layout:
 * - CSS class: unit-list (flex container with responsive grid)
 * - Adapts column count based on screen size
 * - Each child is a UnitCard component
 *
 * @example
 * const units = [
 *   { unit_id: 1, title: "Unit One", order_index: 0, ... },
 *   { unit_id: 2, title: "Unit Two", order_index: 1, ... }
 * ];
 * <UnitList courseId={5} units={units} />
 *
 * Used by: CoursePage component
 */
const UnitList = ({ courseId, units }) => {
  // Sort units by order_index to ensure consistent display order matching course structure
  // This is necessary because API response may not always return units in order
  const sortedUnits = [...units].sort((a, b) => (a.order_index || 0) - (b.order_index || 0));
  
  return (
    <div className="unit-list">
      {sortedUnits.map((unit) => (
        <UnitCard
          key={unit.unit_id}
          courseId={courseId}
          unitId={unit.unit_id}
          unitTitle={unit.title}
          orderIndex={unit.order_index}
        />
      ))}
    </div>
  );
};

export default UnitList;


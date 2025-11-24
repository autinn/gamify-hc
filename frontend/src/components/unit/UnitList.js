import React from 'react';
import UnitCard from './UnitCard';
import './UnitList.css';

/**
 * UnitList - Container for unit cards with dynamic responsive grid
 *
 * Renders an array of UnitCard components in a flexible grid layout.
 * Grid automatically adjusts based on screen size and number of items.
 *
 * @param {string} courseId - Parent course ID for navigation
 * @param {array} units - Array of unit objects with id, name, and questionCount properties
 *   Example: [
 *     { id: 1, name: "Scientific Method", questionCount: 8 },
 *     { id: 2, name: "Problem Solving", questionCount: 7 }
 *   ]
 */
const UnitList = ({ courseId, units }) => {
  // Sort units by order_index to ensure consistent display order
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


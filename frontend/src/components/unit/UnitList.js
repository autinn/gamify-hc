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
  return (
    <div className="unit-list">
      {units.map((unit) => (
        <UnitCard
          key={unit.unit_id}
          courseId={courseId}
          unitId={unit.unit_id}
          unitTitle={unit.title}
        />
      ))}
    </div>
  );
};

export default UnitList;


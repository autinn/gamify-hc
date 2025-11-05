import React from 'react';
import CourseCard from './CourseCard';
import './CourseList.css';

/**
 * CourseList - Container for course cards with dynamic responsive grid
 *
 * Renders an array of CourseCard components in a flexible grid layout.
 * Grid automatically adjusts based on screen size and number of items.
 *
 * @param {array} courses - Array of course objects with id and name properties
 *   Example: [{ id: 'EA50', name: 'EA50' }, { id: 'FA50', name: 'FA50' }]
 */
const CourseList = ({ courses }) => {
  return (
    <div className="course-list">
      {courses.map((course) => (
        <CourseCard
          key={course.id}
          id={course.id}
          name={course.name}
        />
      ))}
    </div>
  );
};

export default CourseList;


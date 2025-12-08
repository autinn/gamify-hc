import React from 'react';
import CourseCard from './CourseCard';
import './CourseList.css';

/**
 * CourseList - Container for course cards with responsive grid layout
 *
 * Renders multiple CourseCard components in a flexible grid that adapts
 * to available space. Used on MainPage to display all available courses.
 *
 * @component
 * @param {Array<Object>} courses - Array of course objects
 * @param {number} courses[].course_id - Course identifier
 * @param {string} courses[].title - Course name/code to display
 * @param {string} [courses[].description] - Course description (optional, not displayed)
 * @returns {React.ReactNode} Grid of course cards
 *
 * CSS Classes:
 * - course-list: Main container (flex grid layout)
 * - Individual CourseCard components inside
 *
 * Grid Layout:
 * - Responsive: Adapts columns based on viewport width
 * - Flexible gap spacing: Maintains consistent spacing
 * - Card aspect ratio: Maintains consistent card proportions
 *
 * @example
 * const courses = [
 *   { course_id: 1, title: 'EA50' },
 *   { course_id: 2, title: 'FA50' }
 * ];
 * <CourseList courses={courses} />
 *
 * Used by: MainPage
 */
const CourseList = ({ courses }) => {
  return (
    <div className="course-list">
      {courses.map((course) => (
        <CourseCard
          key={course.course_id}
          id={course.course_id}
          name={course.title}
        />
      ))}
    </div>
  );
};

export default CourseList;


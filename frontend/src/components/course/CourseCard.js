import React from 'react';
import { useNavigate } from 'react-router-dom';
import './CourseCard.css';

/**
 * CourseCard - Individual course card component
 *
 * Displays a single course as a clickable card. When clicked, navigates
 * to the course detail page showing units and course progress.
 *
 * @component
 * @param {number} id - Course ID (course_id from DB)
 * @param {string} name - Course title/code to display (e.g., "EA50", "FA50")
 * @returns {React.ReactNode} Clickable course card
 *
 * CSS Classes:
 * - course-card: Main card container (clickable, hover effect)
 * - course-card__name: Course name text element
 *
 * @example
 * <CourseCard id={1} name="EA50" />
 *
 * Used by: CourseList component
 */
const CourseCard = ({ id, name }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/course/${id}`);
  };

  return (
    <div className="course-card" onClick={handleClick} role="button" tabIndex={0}>
      <p className="course-card__name">{name}</p>
    </div>
  );
};

export default CourseCard;


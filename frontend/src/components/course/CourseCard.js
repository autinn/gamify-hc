import React from 'react';
import { useNavigate } from 'react-router-dom';
import './CourseCard.css';

/**
 * CourseCard - Individual course card component
 *
 * Displays a single course (e.g., EA50, FA50) as a clickable card.
 * Navigates to the CoursePage when clicked.
 *
 * @param {string} id - Course ID (e.g., "EA50", "FA50")
 * @param {string} name - Course name/display text (e.g., "EA50")
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


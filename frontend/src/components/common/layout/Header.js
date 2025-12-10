import React, { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useHeaderNavigation } from '../../../hooks/useHeaderNavigation';
import * as api from '../../../services/api';
import './Header.css';

/**
 * Header - App navigation header with course dropdowns
 *
 * Renders top navigation bar with:
 * - Home button to return to main dashboard
 * - Course dropdown menus showing units for each course
 * - Logout button for authenticated users
 *
 * Uses useHeaderNavigation hook to fetch and organize navigation data.
 * Tracks active course from URL to highlight current location.
 *
 * @component
 * @returns {React.ReactNode} Header navigation element
 *
 * CSS Structure:
 * - header: Main header container (flex, sticky/fixed)
 * - header__home-button: Home navigation link
 * - header__course-nav: Course list container
 * - header__course-item: Individual course with dropdown
 * - header__course-link: Course link (active state when current)
 * - header__dropdown: Unit dropdown menu (shows on hover)
 * - header__dropdown-item: Individual unit link
 * - header__logout-button: Logout button (icon-based)
 *
 * Used by: PageLayout, ConceptPage (as primary app navigation)
 */
const isAuthenticated = () => {
  return localStorage.getItem('token') !== null;
};

const Header = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const pathParts = location.pathname.split('/');
  const courseId = pathParts[2];
  
  // UI state: which course dropdown is open
  const [openDropdown, setOpenDropdown] = useState(null);
  
  // Navigation data from hook
  const { courses, courseUnits } = useHeaderNavigation();

  const handleMouseEnter = (courseId) => {
    setOpenDropdown(courseId);
  };

  const handleMouseLeave = () => {
    setOpenDropdown(null);
  };

  const handleLogout = () => {
    api.logout();
    navigate('/login');
  };

  return (
    <header className="header">
      <Link to="/" className="header__home-button">
        Home
      </Link>
      <nav className="header__course-nav">
        {courses.map((course) => (
          <div
            key={course.id}
            className="header__course-item"
            onMouseEnter={() => handleMouseEnter(course.id)}
            onMouseLeave={handleMouseLeave}
          >
            <Link
              to={`/course/${course.id}`}
              className={`header__course-link ${String(course.id) === courseId ? 'header__course-link--active' : ''}`}
            >
              {course.label}
            </Link>
            {openDropdown === course.id && (
              <div className="header__dropdown">
                {courseUnits[course.id]?.map((unit) => (
                  <Link
                    key={unit.id}
                    to={`/course/${course.id}/unit/${unit.id}`}
                    className="header__dropdown-item"
                  >
                    {unit.name}
                  </Link>
                ))}
              </div>
            )}
          </div>
        ))}
      </nav>
      {isAuthenticated() && (
        <button className="header__logout-button" onClick={handleLogout}>
          <span className="material-symbols-outlined">logout</span>
        </button>
      )}
    </header>
  );
};

export default Header;

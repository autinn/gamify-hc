import React, { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useHeaderNavigation } from '../../../hooks/useHeaderNavigation';
import * as api from '../../../services/api';
import './Header.css';

const isAuthenticated = () => {
  return localStorage.getItem('token') !== null;
};

const Header = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const pathParts = location.pathname.split('/');
  const courseId = pathParts[2];
  
  // UI state only
  const [openDropdown, setOpenDropdown] = useState(null);
  
  // Data from hook
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

import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Header.css';

const Header = () => {
  const location = useLocation();
  const pathParts = location.pathname.split('/');
  const courseId = pathParts[2];
  
  const [openDropdown, setOpenDropdown] = useState(null);

  const courseUnits = {
    EA50: [
      { id: 1, name: 'Scientific Method' },
      { id: 2, name: 'Problem Solving' },
    ],
    FA50: [
      { id: 1, name: 'Logical Thinking' },
      { id: 2, name: 'Pattern Recognition' },
    ],
    MC50: [
      { id: 1, name: 'Close Reading: How does language shape and represent reality?' },
      { id: 2, name: 'Self-Assessment' },
    ],
    CX50: [
      { id: 1, name: 'Characteristics of Complex Systems' },
      { id: 2, name: 'Design Thinking' },
    ],
  };

  const courses = [
    { id: 'EA50', label: 'EA50' },
    { id: 'FA50', label: 'FA50' },
    { id: 'MC50', label: 'MC50' },
    { id: 'CX50', label: 'CX50' },
  ];

  const handleMouseEnter = (courseId) => {
    setOpenDropdown(courseId);
  };

  const handleMouseLeave = () => {
    setOpenDropdown(null);
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
              className={`header__course-link ${courseId === course.id ? 'header__course-link--active' : ''}`}
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
    </header>
  );
};

export default Header;
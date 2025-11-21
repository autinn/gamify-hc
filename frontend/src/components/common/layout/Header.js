import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import * as api from '../../../services/api';
import './Header.css';

const Header = () => {
  const location = useLocation();
  const pathParts = location.pathname.split('/');
  const courseId = pathParts[2];
  
  const [openDropdown, setOpenDropdown] = useState(null);
  const [courses, setCourses] = useState([]);
  const [courseUnits, setCourseUnits] = useState({});

  useEffect(() => {
    // Fetch all courses from API
    api.getCourses()
      .then(data => {
        if (data && Array.isArray(data)) {
          // Map API response to component expectations
          const mappedCourses = data.map(c => ({
            id: c.id || c.course_id,
            label: c.name || c.code || c.title
          }));
          setCourses(mappedCourses);
          
          // Fetch units for each course
          const unitsMap = {};
          Promise.all(
            mappedCourses.map(course =>
              api.getCourseUnits(course.id)
                .then(units => {
                  if (Array.isArray(units)) {
                    unitsMap[course.id] = units.map(u => ({
                      id: u.id || u.unit_id,
                      name: u.name || u.title
                    }));
                  }
                })
                .catch(err => {
                  console.error(`Error fetching units for course ${course.id}:`, err);
                  unitsMap[course.id] = [];
                })
            )
          ).then(() => {
            setCourseUnits(unitsMap);
          });
        }
      })
      .catch(err => {
        console.error('Error fetching courses:', err);
        setCourses([]);
      });
  }, []);

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
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import PageLayout from '../components/common/layout/PageLayout';
import UnitList from '../components/unit/UnitList';
import * as api from '../services/api';

/**
 * CoursePage - Course details page with units
 *
 * Displays course name, performance chart, and list of units for the course.
 * Uses URL parameter :courseId to determine which course to display.
 * Uses PageLayout for consistent two-column structure.
 * 
 * CHANGES: Replaced dummy data (hardcoded courses and units objects) with API calls
 * to fetch real data from the backend. Added useState/useEffect hooks to manage
 * API data fetching and state.
 */
const CoursePage = () => {
  const { courseId } = useParams();
  const courseIdInt = parseInt(courseId, 10);

  // State for course and units data fetched from API
  // Previously: Used hardcoded dummy data objects (courses, courseUnits)
  const [course, setCourse] = useState(null);
  const [units, setUnits] = useState([]);

  useEffect(() => {
    // CHANGED: Replaced dummy data lookup with API calls to fetch real course and units
    // Previously: const course = courses[courseIdInt] || null;
    // Previously: const units = courseUnits[courseIdInt] || [];
    // Fetch course and units in parallel
    Promise.all([
      api.getCourse(courseIdInt),
      api.getCourseUnits(courseIdInt)
    ])
      .then(([courseData, unitsData]) => {
        // Map API response fields to component expectations
        // Backend returns: {id, name/code, description} -> Component expects: {course_id, title, description}
        setCourse({
          course_id: courseData.id,
          title: courseData.name || courseData.code,
          description: courseData.description
        });

        // Map API response fields to component expectations
        // Backend returns: {id, name, ...} -> Component expects: {unit_id, title, ...}
        const mappedUnits = unitsData.map(u => ({
          unit_id: u.id,
          course_id: u.course_id,
          title: u.name,
          description: u.description,
          order_index: u.order_index
        }));
        setUnits(mappedUnits);
      })
      .catch(err => {
        console.error('Error fetching course data:', err);
      });
  }, [courseIdInt]);

  // Chart data - performance within this course
  const chartData = {
    labels: units.map(u => u.title),
    values: units.map(() => Math.floor(Math.random() * 100)), // TODO: Replace with real progress data
  };

  return (
    <PageLayout
      greeting="Welcome to"
      title={course ? course.title : courseId}
      showButton={true}
      startQuizPath={`/course/${courseId}/quiz`}
      chartData={chartData}
      chartLabel="Questions you answered correctly (% correct answered)"
      rightContent={<UnitList courseId={courseId} units={units} />}
    />
  );
};

export default CoursePage;

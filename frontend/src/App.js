import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './pages/MainPage';
import CoursePage from './pages/CoursePage';
import UnitPage from './pages/UnitPage';
import ConceptPage from './pages/ConceptPage';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/course/:courseId" element={<CoursePage />} />
        <Route path="/course/:courseId/unit/:unitId" element={<UnitPage />} />
        <Route path="/course/:courseId/unit/:unitId/concept/:conceptId" element={<ConceptPage />} />
      </Routes>
  
    </Router>
  );
}

export default App;

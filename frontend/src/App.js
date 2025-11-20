import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './pages/MainPage';
import CoursePage from './pages/CoursePage';
import UnitPage from './pages/UnitPage';
import ConceptPage from './pages/ConceptPage';
import QuizPage from './pages/QuizPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/" element={<MainPage />} />
        <Route path="/course/:courseId" element={<CoursePage />} />
        <Route path="/course/:courseId/unit/:unitId" element={<UnitPage />} />
        <Route path="/course/:courseId/unit/:unitId/concept/:conceptId" element={<ConceptPage />} />
        <Route path="/quiz" element={<QuizPage />} />
        <Route path="/course/:courseId/quiz" element={<QuizPage />} />
        <Route path="/course/:courseId/unit/:unitId/quiz" element={<QuizPage />} />
        {/* CHANGED: Added route for concept-level quiz to support quiz functionality at concept level */}
        <Route path="/course/:courseId/unit/:unitId/concept/:conceptId/quiz" element={<QuizPage />} />
      </Routes>
    </Router>
  );
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './components/common/layout/MainLayout';
import MainPage from './pages/MainPage';
import CoursePage from './pages/CoursePage';
import UnitPage from './pages/UnitPage';
import ConceptPage from './pages/ConceptPage';
import QuizPage from './pages/QuizPage';
import './App.css';

function App() {
  return (
    <Router>
       <MainLayout>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/course/:courseId" element={<CoursePage />} />
        <Route path="/course/:courseId/unit/:unitId" element={<UnitPage />} />
        <Route path="/course/:courseId/unit/:unitId/concept/:conceptId" element={<ConceptPage />} />
        <Route path="/quiz" element={<QuizPage />} />
        <Route path="/course/:courseId/quiz" element={<QuizPage />} />
        <Route path="/course/:courseId/unit/:unitId/quiz" element={<QuizPage />} />
      </Routes>
      </MainLayout>
    </Router>
  );
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './components/common/layout/MainLayout';
import MainPage from './pages/MainPage';
import CoursePage from './pages/CoursePage';
import UnitPage from './pages/UnitPage';
import './App.css';

function App() {
  return (
    <Router>
       <MainLayout>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/course/:courseId" element={<CoursePage />} />
        <Route path="/course/:courseId/unit/:unitId" element={<UnitPage />} />
      </Routes>
      </MainLayout>
    </Router>
  );
}

export default App;

import React from 'react';
import Header from './Header.js';
import './MainLayout.css';

/**
 * MainLayout - Root layout wrapper for the entire application
 * 
 * Provides:
 * - Global header navigation
 * - Consistent spacing and structure
 * - Route content rendering
 */
const MainLayout = ({ children }) => {
  return (
    <div className="main-layout">
      <Header />
      <main className="main-layout__content">
        {children}
      </main>
    </div>
  );
};

export default MainLayout;
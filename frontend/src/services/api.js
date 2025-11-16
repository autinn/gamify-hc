/**
 * API Service for Gamify-HC
 * Use these functions in your React components to fetch data from the backend
 */

const API_BASE_URL = 'http://localhost:5001/api';

// Helper function for API calls
async function apiRequest(endpoint, options = {}) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      throw new Error(`API Error: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error(`API Error (${endpoint}):`, error);
    throw error;
  }
}

// ========================================
// COURSES
// ========================================

export async function getCourses() {
  return apiRequest('/courses');
}

export async function getCourse(courseId) {
  return apiRequest(`/courses/${courseId}`);
}

export async function getCourseUnits(courseId) {
  return apiRequest(`/courses/${courseId}/units`);
}

// ========================================
// UNITS
// ========================================

export async function getUnit(unitId) {
  return apiRequest(`/units/${unitId}`);
}

export async function getUnitConcepts(unitId) {
  return apiRequest(`/units/${unitId}/concepts`);
}

// ========================================
// CONCEPTS
// ========================================

export async function getConcept(conceptId) {
  return apiRequest(`/concepts/${conceptId}`);
}

export async function getConceptQuizCards(conceptId) {
  return apiRequest(`/concepts/${conceptId}/quiz-cards`);
}

// ========================================
// QUIZ CARDS
// ========================================

export async function getQuizCard(quizCardId) {
  return apiRequest(`/quiz-cards/${quizCardId}`);
}

// CHANGED: Added new API functions to fetch quiz cards filtered by course or unit
// These endpoints were added to the backend to support quiz functionality at different levels
export async function getCourseQuizCards(courseId) {
  return apiRequest(`/courses/${courseId}/quiz-cards`);
}

export async function getUnitQuizCards(unitId) {
  return apiRequest(`/units/${unitId}/quiz-cards`);
}

export async function submitQuizAnswer(data) {
  return apiRequest('/quiz-submit', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

// ========================================
// USERS
// ========================================

export async function getUser(userId) {
  return apiRequest(`/users/${userId}`);
}

export async function getUserProgress(userId) {
  return apiRequest(`/users/${userId}/progress`);
}

// ========================================
// HEALTH CHECK
// ========================================

export async function checkHealth() {
  return apiRequest('/health');
}

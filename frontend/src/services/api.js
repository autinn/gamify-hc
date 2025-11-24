/**
 * API Service for Gamify-HC
 * Use these functions in your React components to fetch data from the backend
 */

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5001/api';

// Helper function to get auth token from localStorage
export function getAuthToken() {
  return localStorage.getItem('token');
}

// Helper function for API calls
async function apiRequest(endpoint, options = {}) {
  try {
    const token = getAuthToken();
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    };

    // Automatically include Authorization header if token exists
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers,
      ...options,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      const error = new Error(errorData.error || `API Error: ${response.status}`);
      error.status = response.status;
      error.data = errorData;
      throw error;
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

/**
 * Fetch random quiz cards from all courses
 * Used for global practice quiz without a specific course context
 * @returns {Promise<Array>} Array of random quiz cards from all courses
 */
export async function getGlobalQuizCards() {
  return apiRequest('/quiz-cards/random');
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
// AUTHENTICATION
// ========================================

export async function register(username, email, password) {
  return apiRequest('/auth/register', {
    method: 'POST',
    body: JSON.stringify({ username, email, password }),
  });
}

export async function login(username, password) {
  return apiRequest('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ username, password }),
  });
}

export async function getCurrentUser() {
  return apiRequest('/auth/me');
}

/**
 * Logout function - client-side only
 * 
 * How it works:
 * - Removes the JWT token from localStorage, preventing authenticated API requests
 * - Clears all user data from localStorage
 * - The token itself remains valid until expiration (24 hours), but without it in
 *   localStorage, the user cannot make authenticated requests
 */
export function logout() {
  localStorage.removeItem('token');
  localStorage.removeItem('user_id');
  localStorage.removeItem('user_email');
  localStorage.removeItem('user_username');
}

// ========================================
// HEALTH CHECK
// ========================================

export async function checkHealth() {
  return apiRequest('/health');
}

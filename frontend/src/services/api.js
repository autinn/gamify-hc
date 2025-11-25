/**
 * API Service for Gamify-HC
 * 
 * Centralized API client for all backend communication.
 * - Automatically includes authentication tokens in requests
 * - Handles error formatting and logging
 * - Provides typed endpoints for courses, units, concepts, quizzes, and users
 * 
 * Use these functions in your React components to fetch data from the backend.
 */

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5001/api';

/**
 * Get authentication token from localStorage
 * @returns {string|null} JWT token or null if not authenticated
 */
export function getAuthToken() {
  return localStorage.getItem('token');
}

/**
 * Make an API request with automatic authentication header handling
 * @param {string} endpoint - API endpoint path (e.g., '/courses', '/quiz-cards/1')
 * @param {Object} options - Fetch options (method, body, headers, etc.)
 * @returns {Promise<Object>} Parsed JSON response from the API
 * @throws {Error} If the API request fails or returns an error status
 */
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

/**
 * Fetch all available courses
 * @returns {Promise<Array>} Array of course objects {id, name, code, description}
 */
export async function getCourses() {
  return apiRequest('/courses');
}

/**
 * Fetch a single course by ID
 * @param {number} courseId - The course ID
 * @returns {Promise<Object>} Course object {id, name, code, description, units}
 */
export async function getCourse(courseId) {
  return apiRequest(`/courses/${courseId}`);
}

/**
 * Fetch all units within a course
 * @param {number} courseId - The course ID
 * @returns {Promise<Array>} Array of unit objects for the course
 */
export async function getCourseUnits(courseId) {
  return apiRequest(`/courses/${courseId}/units`);
}

// ========================================
// UNITS
// ========================================

/**
 * Fetch a single unit by ID
 * @param {number} unitId - The unit ID
 * @returns {Promise<Object>} Unit object {id, name, course_id, description, order_index}
 */
export async function getUnit(unitId) {
  return apiRequest(`/units/${unitId}`);
}

/**
 * Fetch all concepts within a unit
 * @param {number} unitId - The unit ID
 * @returns {Promise<Array>} Array of concept objects for the unit
 */
export async function getUnitConcepts(unitId) {
  return apiRequest(`/units/${unitId}/concepts`);
}

// ========================================
// CONCEPTS (Healing Circles)
// ========================================

/**
 * Fetch a single concept (Healing Circle) by ID
 * @param {number} conceptId - The concept ID
 * @returns {Promise<Object>} Concept object {id, name, unit_id, definition}
 */
export async function getConcept(conceptId) {
  return apiRequest(`/concepts/${conceptId}`);
}

/**
 * Fetch all quiz cards (questions and answers) for a concept
 * @param {number} conceptId - The concept ID
 * @returns {Promise<Array>} Array of quiz card objects for the concept
 */
export async function getConceptQuizCards(conceptId) {
  return apiRequest(`/concepts/${conceptId}/quiz-cards`);
}

// ========================================
// QUIZ CARDS
// ========================================

/**
 * Fetch a single quiz card by ID
 * @param {number} quizCardId - The quiz card ID
 * @returns {Promise<Object>} Quiz card object {id, question, answers, concept_id}
 */
export async function getQuizCard(quizCardId) {
  return apiRequest(`/quiz-cards/${quizCardId}`);
}

/**
 * Fetch all quiz cards for a specific course
 * @param {number} courseId - The course ID
 * @returns {Promise<Array>} Array of quiz cards from all units and concepts in the course
 */
export async function getCourseQuizCards(courseId) {
  return apiRequest(`/courses/${courseId}/quiz-cards`);
}

/**
 * Fetch all quiz cards for a specific unit
 * @param {number} unitId - The unit ID
 * @returns {Promise<Array>} Array of quiz cards from all concepts in the unit
 */
export async function getUnitQuizCards(unitId) {
  return apiRequest(`/units/${unitId}/quiz-cards`);
}

/**
 * Fetch random quiz cards from all courses for global practice
 * Useful for practice quizzes that aren't tied to a specific course/unit
 * @returns {Promise<Array>} Array of random quiz cards from all courses
 */
export async function getGlobalQuizCards() {
  return apiRequest('/quiz-cards/random');
}

/**
 * Submit an answer to a quiz question
 * Tracks user's answer choice and evaluates correctness
 * @param {Object} data - Answer submission data {quiz_card_id, answer_id, user_id}
 * @returns {Promise<Object>} Response with answer evaluation {is_correct, explanation}
 */
export async function submitQuizAnswer(data) {
  return apiRequest('/quiz-submit', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

// ========================================
// USERS
// ========================================

/**
 * Fetch a single user by ID
 * @param {number} userId - The user ID
 * @returns {Promise<Object>} User object {id, username, email, created_at}
 */
export async function getUser(userId) {
  return apiRequest(`/users/${userId}`);
}

/**
 * Fetch the current authenticated user's profile
 * Uses the JWT token from localStorage to identify the user
 * @returns {Promise<Object>} Current user object {id, username, email, created_at}
 */
export async function getCurrentUser() {
  return apiRequest('/auth/me');
}

/**
 * Fetch user's progress data across courses/units
 * @param {number} userId - The user ID
 * @returns {Promise<Object>} Progress object with completion rates and stats
 */
export async function getUserProgress(userId) {
  return apiRequest(`/users/${userId}/progress`);
}

// ========================================
// AUTHENTICATION
// ========================================

/**
 * Register a new user account
 * @param {string} username - Username for the account (min 3 characters)
 * @param {string} email - User's email address (must be @minerva.edu)
 * @param {string} password - User's password (min 6 characters)
 * @returns {Promise<Object>} Response with JWT token and user data {access_token, user_id, email, username}
 * @throws {Error} If email is already registered or validation fails
 */
export async function register(username, email, password) {
  return apiRequest('/auth/register', {
    method: 'POST',
    body: JSON.stringify({ username, email, password }),
  });
}

/**
 * Login with email and password
 * @param {string} username - User's email address (used as username in login)
 * @param {string} password - User's password
 * @returns {Promise<Object>} Response with JWT token and user data {access_token, user_id, email, username}
 * @throws {Error} If credentials are invalid
 */
export async function login(username, password) {
  return apiRequest('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ username, password }),
  });
}

/**
 * Logout the current user (client-side only)
 * 
 * How it works:
 * - Removes the JWT token from localStorage, preventing authenticated API requests
 * - Clears all user data from localStorage (user_id, user_email, user_username)
 * - The JWT token itself remains valid on the backend until expiration (24 hours),
 *   but without it in localStorage, the user cannot make authenticated requests
 * - On next login, a new token will be issued
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

/**
 * Check backend API health status
 * Useful for verifying the API is running before making other requests
 * @returns {Promise<Object>} Health status object {status: 'ok'} or error
 */
export async function checkHealth() {
  return apiRequest('/health');
}

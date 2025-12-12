/**
 * Authentication Service - Manages auth validation, token storage, and user data
 *
 * Provides comprehensive authentication logic including email and password validation,
 * form validation, token management, and localStorage handling for persisting user sessions.
 * Enforces Minerva-specific business rules and ensures consistent auth state across the app.
 *
 * @module authService
 */

// ============================================================================
// VALIDATION FUNCTIONS
// ============================================================================

/**
 * Validates email format and enforces Minerva institution requirement
 *
 * Email must be non-empty, contain @, and end with @minerva.edu to comply
 * with organization security policies.
 *
 * @param {string} email - Email address to validate
 * @returns {Object} Validation result with status and error message
 * @returns {boolean} result.valid - Whether validation passed
 * @returns {string|null} result.error - Error message if validation failed, null on success
 *
 * @example
 * const result = validateEmail('user@minerva.edu');
 * if (!result.valid) console.error(result.error);
 */
export function validateEmail(email) {
  const trimmedEmail = email.trim().toLowerCase();

  if (!trimmedEmail) {
    return { valid: false, error: 'Email is required' };
  }

  if (!trimmedEmail.includes('@')) {
    return { valid: false, error: 'Please enter a valid email' };
  }

  // Enforce Minerva institutional email requirement
  if (!trimmedEmail.endsWith('minerva.edu')) {
    return { valid: false, error: 'Please use your @minerva.edu email' };
  }

  return { valid: true, error: null };
}

/**
 * Validates password meets minimum security requirements
 *
 * Checks that password is provided and meets minimum length threshold.
 * Additional complexity requirements can be added here as needed.
 *
 * @param {string} password - Password to validate
 * @returns {Object} Validation result with status and error message
 * @returns {boolean} result.valid - Whether validation passed
 * @returns {string|null} result.error - Error message if validation failed, null on success
 */
export function validatePassword(password) {
  const MIN_LENGTH = 8;

  if (!password) {
    return { valid: false, error: 'Password is required' };
  }

  // Enforce minimum password length for basic security
  if (password.length < MIN_LENGTH) {
    return { valid: false, error: `Password must be at least ${MIN_LENGTH} characters long` };
  }

  return { valid: true, error: null };
}

/**
 * Validates username meets minimum requirements
 *
 * Ensures username is provided and meets minimum length to prevent
 * trivial or empty usernames in the system.
 *
 * @param {string} username - Username to validate
 * @returns {Object} Validation result with status and error message
 * @returns {boolean} result.valid - Whether validation passed
 * @returns {string|null} result.error - Error message if validation failed, null on success
 */
export function validateUsername(username) {
  const MIN_LENGTH = 3;

  if (!username) {
    return { valid: false, error: 'Username is required' };
  }

  // Enforce minimum username length for meaningful user identification
  if (username.length < MIN_LENGTH) {
    return { valid: false, error: `Username must be at least ${MIN_LENGTH} characters` };
  }

  return { valid: true, error: null };
}

/**
 * Validates that password confirmation matches the original password
 *
 * Prevents user registration/password reset errors by ensuring both
 * password fields contain identical values before submission.
 *
 * @param {string} password - Original password
 * @param {string} confirmation - Password confirmation field
 * @returns {Object} Validation result with status and error message
 * @returns {boolean} result.valid - Whether passwords match
 * @returns {string|null} result.error - Error message if mismatch, null on success
 */
export function validatePasswordMatch(password, confirmation) {
  // Compare passwords for user confirmation errors (typos, etc.)
  if (password !== confirmation) {
    return { valid: false, error: 'Passwords do not match' };
  }

  return { valid: true, error: null };
}

/**
 * Validates complete login form with all required fields
 *
 * Performs comprehensive validation of login credentials by checking
 * both email and password. Returns on first validation failure to provide
 * clear user feedback.
 *
 * @param {string} email - Email address
 * @param {string} password - Password
 * @returns {Object} Validation result with status and error message
 * @returns {boolean} result.valid - Whether all fields are valid
 * @returns {string|null} result.error - First validation error found, null on success
 */
export function validateLoginForm(email, password) {
  // Check email validity first
  const emailValidation = validateEmail(email);
  if (!emailValidation.valid) {
    return emailValidation;
  }

  // Then check password validity
  const passwordValidation = validatePassword(password);
  if (!passwordValidation.valid) {
    return passwordValidation;
  }

  return { valid: true, error: null };
}

/**
 * Validates complete registration form with all required fields
 *
 * Performs comprehensive validation of registration credentials including
 * username, email, password, and password confirmation. Returns on first
 * validation failure to provide clear, actionable user feedback.
 *
 * @param {string} username - Desired username
 * @param {string} email - Email address
 * @param {string} password - Password
 * @param {string} passwordConfirm - Password confirmation field
 * @returns {Object} Validation result with status and error message
 * @returns {boolean} result.valid - Whether all fields are valid
 * @returns {string|null} result.error - First validation error found, null on success
 *
 * @example
 * const result = validateRegisterForm('john_doe', 'john@minerva.edu', 'pass123', 'pass123');
 * if (!result.valid) showError(result.error);
 */
export function validateRegisterForm(username, email, password, passwordConfirm) {
  // Check username validity first
  const usernameValidation = validateUsername(username);
  if (!usernameValidation.valid) {
    return usernameValidation;
  }

  // Then check email validity
  const emailValidation = validateEmail(email);
  if (!emailValidation.valid) {
    return emailValidation;
  }

  // Then check password validity
  const passwordValidation = validatePassword(password);
  if (!passwordValidation.valid) {
    return passwordValidation;
  }

  // Finally check password match before committing
  const matchValidation = validatePasswordMatch(password, passwordConfirm);
  if (!matchValidation.valid) {
    return matchValidation;
  }

  return { valid: true, error: null };
}

// ============================================================================
// TOKEN AND USER DATA MANAGEMENT
// ============================================================================

/**
 * Stores authentication tokens and user data in localStorage for persistent sessions
 *
 * Persists API-provided credentials and user information locally to maintain
 * authentication state across page reloads and browser sessions. Data is stored
 * as individual items for granular access control.
 *
 * @param {Object} data - Authentication response from server
 * @param {string} data.access_token - JWT token for API authentication
 * @param {number} data.user_id - Unique user identifier
 * @param {string} data.email - User's email address
 * @param {string} data.username - User's display name
 *
 * @example
 * storeAuthData({ access_token: 'jwt...', user_id: 123, email: 'user@minerva.edu', username: 'john' });
 */
export function storeAuthData(data) {
  // Persist API credentials for subsequent authenticated requests
  localStorage.setItem('token', data.access_token);
  localStorage.setItem('user_id', data.user_id);
  localStorage.setItem('user_email', data.email);
  localStorage.setItem('user_username', data.username);
  
  // Dispatch custom event to notify that token was stored
  // This helps onboarding check trigger after login/registration
  window.dispatchEvent(new Event('token-stored'));
}

/**
 * Retrieves stored authentication token from localStorage
 *
 * Used to attach JWT token to API requests for authentication.
 * Returns null if user is not currently authenticated.
 *
 * @returns {string|null} JWT token if authenticated, null otherwise
 */
export function getStoredToken() {
  return localStorage.getItem('token');
}

/**
 * Retrieves all stored user data from localStorage
 *
 * Returns user identification and account information stored during
 * authentication. Values may be null if user is not authenticated.
 *
 * @returns {Object} User data object
 * @returns {string|null} result.user_id - Unique user identifier
 * @returns {string|null} result.user_email - User's email address
 * @returns {string|null} result.user_username - User's display name
 */
export function getStoredUserData() {
  return {
    user_id: localStorage.getItem('user_id'),
    user_email: localStorage.getItem('user_email'),
    user_username: localStorage.getItem('user_username')
  };
}

/**
 * Checks if user is currently authenticated
 *
 * Simple check for token existence to determine authentication state.
 * Use before making authenticated API requests.
 *
 * @returns {boolean} True if valid token exists, false otherwise
 */
export function isAuthenticated() {
  return getStoredToken() !== null;
}

/**
 * Clears all authentication data from localStorage (logout operation)
 *
 * Removes all stored tokens and user data to securely sign out the user.
 * Should be called when user explicitly logs out or when token becomes invalid.
 */
export function clearAuthData() {
  // Remove all auth-related data to prevent unauthorized access after logout
  localStorage.removeItem('token');
  localStorage.removeItem('user_id');
  localStorage.removeItem('user_email');
  localStorage.removeItem('user_username');
}

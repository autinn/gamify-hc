/**
 * Auth Service
 * 
 * Business logic for authentication including validation, token management, and user data handling.
 * Centralizes all auth-related transformations and business rules.
 */

/**
 * Email validation - must be Minerva email
 * @param {string} email - Email to validate
 * @returns {Object} {valid: boolean, error: string|null}
 */
export function validateEmail(email) {
  const trimmedEmail = email.trim().toLowerCase();

  if (!trimmedEmail) {
    return { valid: false, error: 'Email is required' };
  }

  if (!trimmedEmail.includes('@')) {
    return { valid: false, error: 'Please enter a valid email' };
  }

  if (!trimmedEmail.endsWith('minerva.edu')) {
    return { valid: false, error: 'Please use your @minerva.edu email' };
  }

  return { valid: true, error: null };
}

/**
 * Password validation - minimum length checks
 * @param {string} password - Password to validate
 * @returns {Object} {valid: boolean, error: string|null}
 */
export function validatePassword(password) {
  const MIN_LENGTH = 6;

  if (!password) {
    return { valid: false, error: 'Password is required' };
  }

  if (password.length < MIN_LENGTH) {
    return { valid: false, error: `Password must be at least ${MIN_LENGTH} characters` };
  }

  return { valid: true, error: null };
}

/**
 * Username validation
 * @param {string} username - Username to validate
 * @returns {Object} {valid: boolean, error: string|null}
 */
export function validateUsername(username) {
  const MIN_LENGTH = 3;

  if (!username) {
    return { valid: false, error: 'Username is required' };
  }

  if (username.length < MIN_LENGTH) {
    return { valid: false, error: `Username must be at least ${MIN_LENGTH} characters` };
  }

  return { valid: true, error: null };
}

/**
 * Validate password confirmation match
 * @param {string} password - Password
 * @param {string} confirmation - Password confirmation
 * @returns {Object} {valid: boolean, error: string|null}
 */
export function validatePasswordMatch(password, confirmation) {
  if (password !== confirmation) {
    return { valid: false, error: 'Passwords do not match' };
  }

  return { valid: true, error: null };
}

/**
 * Validate login form
 * @param {string} email - Email address
 * @param {string} password - Password
 * @returns {Object} {valid: boolean, error: string|null}
 */
export function validateLoginForm(email, password) {
  const emailValidation = validateEmail(email);
  if (!emailValidation.valid) {
    return emailValidation;
  }

  const passwordValidation = validatePassword(password);
  if (!passwordValidation.valid) {
    return passwordValidation;
  }

  return { valid: true, error: null };
}

/**
 * Validate registration form
 * @param {string} username - Username
 * @param {string} email - Email address
 * @param {string} password - Password
 * @param {string} passwordConfirm - Password confirmation
 * @returns {Object} {valid: boolean, error: string|null}
 */
export function validateRegisterForm(username, email, password, passwordConfirm) {
  const usernameValidation = validateUsername(username);
  if (!usernameValidation.valid) {
    return usernameValidation;
  }

  const emailValidation = validateEmail(email);
  if (!emailValidation.valid) {
    return emailValidation;
  }

  const passwordValidation = validatePassword(password);
  if (!passwordValidation.valid) {
    return passwordValidation;
  }

  const matchValidation = validatePasswordMatch(password, passwordConfirm);
  if (!matchValidation.valid) {
    return matchValidation;
  }

  return { valid: true, error: null };
}

/**
 * Store authentication tokens and user data in localStorage
 * @param {Object} data - API response with {access_token, user_id, email, username}
 */
export function storeAuthData(data) {
  localStorage.setItem('token', data.access_token);
  localStorage.setItem('user_id', data.user_id);
  localStorage.setItem('user_email', data.email);
  localStorage.setItem('user_username', data.username);
}

/**
 * Get stored auth token
 * @returns {string|null} JWT token or null
 */
export function getStoredToken() {
  return localStorage.getItem('token');
}

/**
 * Get stored user data
 * @returns {Object} {user_id, user_email, user_username}
 */
export function getStoredUserData() {
  return {
    user_id: localStorage.getItem('user_id'),
    user_email: localStorage.getItem('user_email'),
    user_username: localStorage.getItem('user_username')
  };
}

/**
 * Check if user is authenticated
 * @returns {boolean} True if token exists
 */
export function isAuthenticated() {
  return getStoredToken() !== null;
}

/**
 * Clear all auth data from localStorage (logout)
 */
export function clearAuthData() {
  localStorage.removeItem('token');
  localStorage.removeItem('user_id');
  localStorage.removeItem('user_email');
  localStorage.removeItem('user_username');
}

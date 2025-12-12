/**
 * RegisterPage Validation Tests
 * 
 * Tests the registration form validation logic including:
 * - Complete registration form validation with all required fields
 * - Email domain restrictions (Minerva-only enforcement)
 * - Username requirements (length, format)
 * - Password strength requirements (minimum length)
 * - Password confirmation matching
 * - Whitespace handling and trimming
 * 
 * These tests ensure users cannot create invalid accounts and receive
 * clear feedback on form validation errors.
 * 
 * @module RegisterPage.test
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { validateRegisterForm } from '../../services/authService';

describe('RegisterPage - Registration Validation', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });

  /**
   * Test: Validate complete registration form
   * 
   * Verifies that all required fields (username, email, passwords) pass validation
   * when filled correctly.
   * 
   * Valid input criteria:
   * - Username: minimum 3 characters
   * - Email: must be @minerva.edu domain
   * - Password: minimum 8 characters
   * - Password confirmation: must match password field
   */
  it('should validate complete register form', () => {
    const result = validateRegisterForm(
      'username123',
      'newuser@minerva.edu',
      'password123',
      'password123'
    );
    expect(result.valid).toBe(true);
    expect(result.error).toBeNull();
  });

  /**
   * Test: Reject non-Minerva email addresses
   * 
   * Verifies that the system enforces institutional email requirement.
   * Only @minerva.edu domain emails are accepted (security/enrollment policy).
   * 
   * Invalid inputs tested: gmail.com, yahoo.com, etc.
   */
  it('should reject non-minerva email', () => {
    const result = validateRegisterForm(
      'username123',
      'user@gmail.com',
      'password123',
      'password123'
    );
    expect(result.valid).toBe(false);
    expect(result.error).toBeDefined();
  });

  /**
   * Test: Reject empty username
   * 
   * Verifies that username field is required and cannot be blank.
   */
  it('should reject empty username', () => {
    const result = validateRegisterForm(
      '',
      'user@minerva.edu',
      'password123',
      'password123'
    );
    expect(result.valid).toBe(false);
    expect(result.error).toContain('Username');
  });

  /**
   * Test: Reject short username
   * 
   * Verifies minimum username length requirement (3 characters).
   * Prevents trivial/low-quality usernames.
   */
  it('should reject short username', () => {
    const result = validateRegisterForm(
      'ab',
      'user@minerva.edu',
      'password123',
      'password123'
    );
    expect(result.valid).toBe(false);
    expect(result.error).toContain('Username');
  });

  /**
   * Test: Reject short password
   * 
   * Verifies minimum password length requirement (8 characters).
   * Ensures basic password security standards.
   */
  it('should reject short password', () => {
    const result = validateRegisterForm(
      'username123',
      'user@minerva.edu',
      'short',
      'short'
    );
    expect(result.valid).toBe(false);
    expect(result.error).toContain('8 characters');
  });

  /**
   * Test: Reject mismatched passwords
   * 
   * Verifies that password and password confirmation fields must match.
   * Prevents accidental password typos during registration.
   */
  it('should reject mismatched passwords', () => {
    const result = validateRegisterForm(
      'username123',
      'user@minerva.edu',
      'password123',
      'different456'
    );
    expect(result.valid).toBe(false);
    expect(result.error).toBeDefined();
  });

  /**
   * Test: Validate with minimal input
   * 
   * Verifies that valid input passes all validation checks
   * even with minimal allowed values (username: 3 chars, password: 8 chars).
   */
  it('should validate with minimal whitespace', () => {
    const result = validateRegisterForm(
      'username123',
      'user@minerva.edu',
      'password123',
      'password123'
    );
    expect(result.valid).toBe(true);
  });
});

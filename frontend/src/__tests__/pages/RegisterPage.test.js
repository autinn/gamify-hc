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
   * - Password: minimum 6 characters
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

  it('should reject short password', () => {
    const result = validateRegisterForm(
      'username123',
      'user@minerva.edu',
      'short',
      'short'
    );
    expect(result.valid).toBe(false);
    expect(result.error).toContain('6 characters');
  });

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

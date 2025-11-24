import { describe, it, expect } from 'vitest';
import {
  validateEmail,
  validatePassword,
  validateUsername,
  validatePasswordMatch,
  validateLoginForm,
  validateRegisterForm
} from '../../services/authService';

describe('authService - Validation Functions', () => {
  describe('validateEmail', () => {
    it('should validate correct minerva emails', () => {
      const result = validateEmail('user@minerva.edu');
      expect(result.valid).toBe(true);
      expect(result.error).toBeNull();
    });

    it('should reject non-minerva emails', () => {
      const result = validateEmail('user@gmail.com');
      expect(result.valid).toBe(false);
      expect(result.error).toBe('Please use your @minerva.edu email');
    });

    it('should reject emails without @', () => {
      const result = validateEmail('invalidemail');
      expect(result.valid).toBe(false);
      expect(result.error).toBe('Please enter a valid email');
    });

    it('should reject empty email', () => {
      const result = validateEmail('');
      expect(result.valid).toBe(false);
      expect(result.error).toBe('Email is required');
    });

    it('should handle whitespace and case', () => {
      const result = validateEmail('  USER@MINERVA.EDU  ');
      expect(result.valid).toBe(true);
    });
  });

  describe('validatePassword', () => {
    it('should validate password with minimum length', () => {
      const result = validatePassword('password123');
      expect(result.valid).toBe(true);
      expect(result.error).toBeNull();
    });

    it('should reject password below minimum length', () => {
      const result = validatePassword('pass');
      expect(result.valid).toBe(false);
      expect(result.error).toContain('at least 6 characters');
    });

    it('should reject empty password', () => {
      const result = validatePassword('');
      expect(result.valid).toBe(false);
      expect(result.error).toBe('Password is required');
    });
  });

  describe('validateUsername', () => {
    it('should validate username with minimum length', () => {
      const result = validateUsername('validuser');
      expect(result.valid).toBe(true);
      expect(result.error).toBeNull();
    });

    it('should reject username below minimum length', () => {
      const result = validateUsername('ab');
      expect(result.valid).toBe(false);
      expect(result.error).toContain('at least 3 characters');
    });

    it('should reject empty username', () => {
      const result = validateUsername('');
      expect(result.valid).toBe(false);
      expect(result.error).toBe('Username is required');
    });
  });

  describe('validatePasswordMatch', () => {
    it('should validate matching passwords', () => {
      const result = validatePasswordMatch('password123', 'password123');
      expect(result.valid).toBe(true);
      expect(result.error).toBeNull();
    });

    it('should reject non-matching passwords', () => {
      const result = validatePasswordMatch('password123', 'different');
      expect(result.valid).toBe(false);
      expect(result.error).toBe('Passwords do not match');
    });
  });

  describe('validateLoginForm', () => {
    it('should validate complete login form', () => {
      const result = validateLoginForm('user@minerva.edu', 'password123');
      expect(result.valid).toBe(true);
    });

    it('should fail on invalid email', () => {
      const result = validateLoginForm('invalid@gmail.com', 'password123');
      expect(result.valid).toBe(false);
    });

    it('should fail on invalid password', () => {
      const result = validateLoginForm('user@minerva.edu', 'short');
      expect(result.valid).toBe(false);
    });
  });

  describe('validateRegisterForm', () => {
    it('should validate complete register form', () => {
      const result = validateRegisterForm(
        'newuser',
        'user@minerva.edu',
        'password123',
        'password123'
      );
      expect(result.valid).toBe(true);
    });

    it('should fail on invalid username', () => {
      const result = validateRegisterForm(
        'ab',
        'user@minerva.edu',
        'password123',
        'password123'
      );
      expect(result.valid).toBe(false);
    });

    it('should fail on non-matching passwords', () => {
      const result = validateRegisterForm(
        'newuser',
        'user@minerva.edu',
        'password123',
        'different'
      );
      expect(result.valid).toBe(false);
    });
  });
});

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { validateLoginForm } from '../../services/authService';

describe('LoginPage - Auth Validation', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });

  it('should validate correct login credentials', () => {
    const result = validateLoginForm('user@minerva.edu', 'password123');
    expect(result.valid).toBe(true);
    expect(result.error).toBeNull();
  });

  it('should reject login with non-minerva email', () => {
    const result = validateLoginForm('user@gmail.com', 'password123');
    expect(result.valid).toBe(false);
    expect(result.error).toContain('minerva.edu');
  });

  it('should reject login with empty email', () => {
    const result = validateLoginForm('', 'password123');
    expect(result.valid).toBe(false);
    expect(result.error).toBe('Email is required');
  });

  it('should reject login with empty password', () => {
    const result = validateLoginForm('user@minerva.edu', '');
    expect(result.valid).toBe(false);
    expect(result.error).toBe('Password is required');
  });

  it('should reject login with short password', () => {
    const result = validateLoginForm('user@minerva.edu', 'short');
    expect(result.valid).toBe(false);
    expect(result.error).toContain('8 characters');
  });

  it('should handle whitespace in email', () => {
    const result = validateLoginForm('  USER@MINERVA.EDU  ', 'password123');
    expect(result.valid).toBe(true);
  });

  it('should be case-insensitive for email', () => {
    const result = validateLoginForm('USER@MINERVA.EDU', 'password123');
    expect(result.valid).toBe(true);
  });
});

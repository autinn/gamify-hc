import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useAuth } from '../../hooks/useAuth';
import * as api from '../../services/api';
import * as authService from '../../services/authService';

vi.mock('../../services/api', () => ({
  login: vi.fn(),
  register: vi.fn()
}));

vi.mock('../../services/authService', () => ({
  validateLoginForm: vi.fn(),
  validateRegisterForm: vi.fn(),
  storeAuthData: vi.fn()
}));

vi.mock('react-router-dom', () => ({
  useNavigate: vi.fn(() => vi.fn())
}));

describe('useAuth Hook', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });

  describe('login()', () => {
    it('should validate email and password before API call', async () => {
      authService.validateLoginForm.mockReturnValue({
        valid: false,
        error: 'Email must be a minerva.edu address'
      });

      const { result } = renderHook(() => useAuth());

      await act(async () => {
        await result.current.login('invalid@gmail.com', 'password123');
      });

      expect(result.current.error).toContain('minerva.edu');
      expect(api.login).not.toHaveBeenCalled();
    });

    it('should reject login with short password', async () => {
      authService.validateLoginForm.mockReturnValue({
        valid: false,
        error: 'Password must be at least 8 characters long'
      });

      const { result } = renderHook(() => useAuth());

      await act(async () => {
        await result.current.login('user@minerva.edu', 'short');
      });

      expect(result.current.error).toContain('8 characters');
      expect(api.login).not.toHaveBeenCalled();
    });

    it('should call API and store token on valid credentials', async () => {
      const mockResponse = {
        access_token: 'test-token-123',
        user_id: 1,
        email: 'user@minerva.edu',
        username: 'testuser'
      };

      authService.validateLoginForm.mockReturnValue({ valid: true });
      api.login.mockResolvedValue(mockResponse);
      authService.storeAuthData.mockImplementation(() => {});

      const { result } = renderHook(() => useAuth());

      await act(async () => {
        await result.current.login('user@minerva.edu', 'password123');
      });

      expect(api.login).toHaveBeenCalledWith('user@minerva.edu', 'password123');
      expect(authService.storeAuthData).toHaveBeenCalledWith(mockResponse);
    });

    it('should display error on API failure', async () => {
      const error = new Error('Invalid credentials');
      error.data = { error: 'Email or password is incorrect' };
      api.login.mockRejectedValue(error);

      const { result } = renderHook(() => useAuth());

      await act(async () => {
        await result.current.login('user@minerva.edu', 'wrongpassword');
      });

      expect(result.current.error).toContain('Email or password');
    });
  });

  describe('register()', () => {
    it('should validate all register fields', async () => {
      authService.validateRegisterForm.mockReturnValue({
        valid: false,
        error: 'Username must be at least 3 characters'
      });

      const { result } = renderHook(() => useAuth());

      await act(async () => {
        await result.current.register('ab', 'user@minerva.edu', 'password123', 'password123');
      });

      expect(result.current.error).toContain('3 characters');
      expect(api.register).not.toHaveBeenCalled();
    });

    it('should reject mismatched passwords', async () => {
      authService.validateRegisterForm.mockReturnValue({
        valid: false,
        error: 'Passwords do not match'
      });

      const { result } = renderHook(() => useAuth());

      await act(async () => {
        await result.current.register('testuser', 'user@minerva.edu', 'password123', 'different');
      });

      expect(result.current.error).toContain('do not match');
      expect(api.register).not.toHaveBeenCalled();
    });

    it('should call API on valid registration', async () => {
      const mockResponse = {
        access_token: 'test-token-123',
        user_id: 2,
        email: 'newuser@minerva.edu',
        username: 'newuser'
      };

      authService.validateRegisterForm.mockReturnValue({ valid: true });
      api.register.mockResolvedValue(mockResponse);
      authService.storeAuthData.mockImplementation(() => {});

      const { result } = renderHook(() => useAuth());

      await act(async () => {
        await result.current.register('newuser', 'newuser@minerva.edu', 'password123', 'password123');
      });

      expect(api.register).toHaveBeenCalledWith('newuser', 'newuser@minerva.edu', 'password123');
      expect(authService.storeAuthData).toHaveBeenCalledWith(mockResponse);
    });
  });

  describe('loading and error state', () => {
    it('should set loading to true during API call', async () => {
      const mockResponse = {
        access_token: 'test-token',
        user_id: 1,
        email: 'user@minerva.edu',
        username: 'testuser'
      };

      api.login.mockImplementation(() => new Promise(resolve => setTimeout(() => resolve(mockResponse), 100)));
      authService.storeAuthData.mockImplementation(() => {});

      const { result } = renderHook(() => useAuth());

      expect(result.current.loading).toBe(false);

      act(() => {
        result.current.login('user@minerva.edu', 'password123');
      });

      expect(result.current.loading).toBe(true);

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });
    });

    it('should allow setError to update error state', async () => {
      const { result } = renderHook(() => useAuth());

      expect(result.current.error).toBe('');

      act(() => {
        result.current.setError('Custom error message');
      });

      expect(result.current.error).toBe('Custom error message');
    });
  });
});

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useCurrentUser } from '../../hooks/useCurrentUser';
import * as api from '../../services/api';

vi.mock('../../services/api', () => ({
  getCurrentUser: vi.fn()
}));

// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn()
};
global.localStorage = localStorageMock;

describe('useCurrentUser Hook', () => {
  const mockUser = {
    user_id: 1,
    username: 'testuser',
    email: 'test@example.com',
    created_at: '2024-01-01T00:00:00Z'
  };

  beforeEach(() => {
    vi.clearAllMocks();
    localStorageMock.getItem.mockReturnValue('test-token');
  });

  it('should fetch current user on mount', async () => {
    api.getCurrentUser.mockResolvedValue(mockUser);

    const { result } = renderHook(() => useCurrentUser());

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(api.getCurrentUser).toHaveBeenCalled();
    expect(result.current.user).toEqual(mockUser);
  });

  it('should return loading state', async () => {
    api.getCurrentUser.mockResolvedValue(mockUser);

    const { result } = renderHook(() => useCurrentUser());

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
  });

  it('should handle fetch errors', async () => {
    api.getCurrentUser.mockRejectedValue(new Error('Failed to fetch'));

    const { result } = renderHook(() => useCurrentUser());

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.error).toBeTruthy();
    expect(result.current.user).toBeNull();
  });

  it('should handle missing token', async () => {
    localStorageMock.getItem.mockReturnValue(null);

    const { result } = renderHook(() => useCurrentUser());

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.user).toBeNull();
    expect(api.getCurrentUser).not.toHaveBeenCalled();
  });
});

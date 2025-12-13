import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useOnboarding } from '../../hooks/useOnboarding';
import * as api from '../../services/api';
import * as authService from '../../services/authService';

vi.mock('../../services/api', () => ({
  getCurrentUser: vi.fn(),
  updateOnboardingStatus: vi.fn(),
}));

vi.mock('../../services/authService', () => ({
  getStoredToken: vi.fn(),
}));

describe('useOnboarding Hook', { timeout: 15000 }, () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });

  afterEach(() => {
    // Ensure real timers are used
    vi.useRealTimers();
  });

  it('should initialize with correct default state', () => {
    authService.getStoredToken.mockReturnValue(null);

    const { result } = renderHook(() => useOnboarding());

    expect(result.current.isFirstTime).toBe(false);
    expect(result.current.isActive).toBe(false);
  });

  it('should detect first-time user when has_completed_onboarding is false', async () => {
    authService.getStoredToken.mockReturnValue('test-token');
    api.getCurrentUser.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: false,
    });

    const { result } = renderHook(() => useOnboarding());

    // Wait for the polling timers to fire and set the state
    await waitFor(
      () => {
        expect(result.current.isFirstTime).toBe(true);
      },
      { timeout: 3000 }
    );
  });

  it('should detect returning user when has_completed_onboarding is true', async () => {
    authService.getStoredToken.mockReturnValue('test-token');
    api.getCurrentUser.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: true,
    });

    const { result } = renderHook(() => useOnboarding());

    await waitFor(
      () => {
        expect(result.current.isFirstTime).toBe(false);
      },
      { timeout: 3000 }
    );
  });

  it('should handle missing token gracefully', () => {
    authService.getStoredToken.mockReturnValue(null);

    const { result } = renderHook(() => useOnboarding());

    expect(result.current.isFirstTime).toBe(false);
    expect(api.getCurrentUser).not.toHaveBeenCalled();
  });

  it('should allow manual guide start', () => {
    authService.getStoredToken.mockReturnValue(null);

    const { result } = renderHook(() => useOnboarding());

    expect(result.current.isActive).toBe(false);

    act(() => {
      result.current.startGuide();
    });

    expect(result.current.isActive).toBe(true);
  });

  it('should complete onboarding and update database', async () => {
    authService.getStoredToken.mockReturnValue('test-token');
    api.getCurrentUser.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: false,
    });
    api.updateOnboardingStatus.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: true,
    });

    const { result } = renderHook(() => useOnboarding());

    // Wait for initial status check
    await waitFor(
      () => {
        expect(result.current.isFirstTime).toBe(true);
      },
      { timeout: 3000 }
    );

    // Update mock to return completed status after calling completeOnboarding
    api.getCurrentUser.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: true,
    });

    // Complete onboarding
    await act(async () => {
      await result.current.completeOnboarding();
    });

    expect(api.updateOnboardingStatus).toHaveBeenCalledWith(1, true);
    expect(result.current.isFirstTime).toBe(false);
  });

  it('should skip onboarding (same as completing)', async () => {
    authService.getStoredToken.mockReturnValue('test-token');
    api.getCurrentUser.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: false,
    });
    api.updateOnboardingStatus.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: true,
    });

    const { result } = renderHook(() => useOnboarding());

    await waitFor(
      () => {
        expect(result.current.isFirstTime).toBe(true);
      },
      { timeout: 3000 }
    );

    // Skip onboarding
    await act(async () => {
      await result.current.skipOnboarding();
    });

    expect(api.updateOnboardingStatus).toHaveBeenCalledWith(1, true);
  });

  it('should handle API errors gracefully when checking status', async () => {
    const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
    authService.getStoredToken.mockReturnValue('test-token');
    api.getCurrentUser.mockRejectedValue(new Error('API Error'));

    const { result } = renderHook(() => useOnboarding());

    await waitFor(
      () => {
        expect(result.current.loading).toBe(false);
      },
      { timeout: 3000 }
    );

    expect(result.current.isFirstTime).toBe(false);

    consoleErrorSpy.mockRestore();
  });

  it('should handle missing user_id when completing onboarding', async () => {
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    authService.getStoredToken.mockReturnValue('test-token');
    api.getCurrentUser.mockResolvedValue({
      user_id: undefined,
      has_completed_onboarding: false,
    });

    const { result } = renderHook(() => useOnboarding());

    await waitFor(
      () => {
        expect(result.current.loading).toBe(false);
      },
      { timeout: 3000 }
    );

    await act(async () => {
      await result.current.completeOnboarding();
    });

    expect(consoleWarnSpy).toHaveBeenCalledWith(
      expect.stringContaining('Cannot complete: no user_id')
    );
    expect(api.updateOnboardingStatus).not.toHaveBeenCalled();

    consoleWarnSpy.mockRestore();
  });

  it('should set isActive to false when completing onboarding', async () => {
    authService.getStoredToken.mockReturnValue('test-token');
    api.getCurrentUser.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: false,
    });
    api.updateOnboardingStatus.mockResolvedValue({
      user_id: 1,
      has_completed_onboarding: true,
    });

    const { result } = renderHook(() => useOnboarding());

    await waitFor(
      () => {
        expect(result.current.isFirstTime).toBe(true);
      },
      { timeout: 3000 }
    );

    // Start guide
    act(() => {
      result.current.startGuide();
    });
    expect(result.current.isActive).toBe(true);

    // Complete onboarding
    await act(async () => {
      await result.current.completeOnboarding();
    });

    expect(result.current.isActive).toBe(false);
  });
});


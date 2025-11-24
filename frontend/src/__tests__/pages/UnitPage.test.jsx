import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { screen, waitFor } from '@testing-library/react';
import { render } from '../testUtils';
import UnitPage from '../../pages/UnitPage';
import * as unitService from '../../services/unitService';

vi.mock('../../services/unitService');
vi.mock('react-router-dom', async () => {
  const actual = await vi.importActual('react-router-dom');
  return {
    ...actual,
    useParams: () => ({ courseId: '1', unitId: '1' }),
    useNavigate: () => vi.fn()
  };
});

describe('UnitPage Integration', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render unit details', async () => {
    unitService.getUnit = vi.fn().mockResolvedValue({
      unit_id: 1,
      title: 'Unit 1: Basics',
      description: 'Basic concepts'
    });

    render(<UnitPage />);

    await waitFor(() => {
      expect(screen.getByText(/Unit 1/i)).toBeInTheDocument();
    });
  });
});

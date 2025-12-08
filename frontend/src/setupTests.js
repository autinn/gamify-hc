/**
 * Test Environment Configuration
 *
 * Configures testing environment with jest-dom matchers for DOM assertions.
 * Runs once before test suite starts, setting up reusable testing utilities.
 *
 * jest-dom Matchers Enabled:
 * - Custom DOM matchers for more readable assertions
 * - toHaveTextContent(): Check if element contains specific text
 * - toBeVisible(): Check if element is visible
 * - toBeDisabled()/toBeEnabled(): Check button/input disabled state
 * - toHaveClass(): Check element CSS classes
 * - toHaveAttribute(): Check element attributes
 * - And many more for DOM testing
 *
 * Example Usage:
 * - expect(screen.getByText('Hello')).toBeInTheDocument()
 * - expect(button).toBeDisabled()
 * - expect(input).toHaveValue('test')
 *
 * References:
 * - https://github.com/testing-library/jest-dom
 * - https://github.com/testing-library/react-testing-library
 *
 * Used by: Vitest/Jest test runner for all test files
 */
import '@testing-library/jest-dom';

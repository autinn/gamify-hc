import React from 'react';
import './Button.css';

/**
 * Button - Reusable styled button component
 *
 * Versatile button component supporting multiple variants and states.
 * Used throughout the app for consistent button styling and behavior.
 *
 * @component
 * @param {string} label - Button text content
 * @param {string} [variant='primary'] - Visual style variant ('primary' | 'secondary')
 * @param {Function} [onClick] - Click event handler
 * @param {boolean} [disabled=false] - Disables button and prevents clicks
 * @returns {React.ReactNode} Styled button element
 *
 * @example
 * <Button
 *   label="Click Me"
 *   variant="primary"
 *   onClick={handleClick}
 *   disabled={isLoading}
 * />
 *
 * CSS Classes:
 * - button button--primary (default variant)
 * - button button--secondary (alternative variant)
 * - :disabled state for disabled styling
 *
 * Used by: PageLayout, ConceptPage, and throughout app
 */
const Button = ({ label, variant = 'primary', onClick, disabled = false }) => {
  return (
    <button
      className={`button button--${variant}`}
      onClick={onClick}
      disabled={disabled}
    >
      {label}
    </button>
  );
};

export default Button;


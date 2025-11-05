import React from 'react';
import './Button.css';

/**
 * Button - Reusable button component
 *
 * @param {string} label - Button text
 * @param {string} variant - Button style variant (e.g., "primary", "secondary")
 * @param {function} onClick - Optional click handler
 * @param {boolean} disabled - Whether button is disabled
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


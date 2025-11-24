import { defineConfig } from 'vitest/config';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  test: {
    // Use jsdom environment for DOM testing
    environment: 'jsdom',
    
    // Setup files to run before tests
    setupFiles: ['./src/__tests__/setup.js'],
    
    // Globals - no need to import describe, it, expect, etc.
    globals: true,
    
    // Reporter configuration
    reporters: ['verbose'],
    
    // Coverage configuration
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'src/__tests__/',
        'src/setupTests.js',
        'src/reportWebVitals.js',
        'src/index.js'
      ]
    },
    
    // Test include patterns
    include: ['src/__tests__/**/*.{test,spec}.{js,jsx}'],
    
    // Test exclude patterns
    exclude: ['node_modules', 'dist', '.idea', '.git', '.cache'],
  },
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
});

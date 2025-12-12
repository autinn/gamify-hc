# ==============================================================================
# PROCFILE - Process Types for Gamify-HC
# ==============================================================================
# Defines process types for platform deployment (Heroku, Railway, etc.)
# Implements 12-Factor App Factor VI: Processes
#
# Process Types:
#   web     - HTTP server (Gunicorn WSGI)
#   release - Pre-deployment tasks (database seeding)
#
# Scaling Examples:
#   heroku ps:scale web=2          # Scale to 2 web dynos
#   heroku ps:scale web=1:standard-1x  # Use specific dyno type
#
# ==============================================================================

# Web Process: Gunicorn WSGI server
# Handles HTTP requests with worker processes and graceful shutdown
web: gunicorn --config backend/gunicorn_config.py run:app

# Release Process: Pre-deployment tasks
# Runs once before new release is deployed
# Use for database migrations, seeding, etc.
release: python -m backend.cli seed

# Backend Dockerfile for Gamify-HC Flask API
# Uses Python 3.13-slim with Gunicorn WSGI server

FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for Python packages
# libpq-dev is required for psycopg2 (PostgreSQL driver)
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/
COPY run.py .

# Create non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5001/api/health || exit 1

# Run with Gunicorn (production)
CMD ["gunicorn", "--config", "backend/gunicorn_config.py", "run:app"]

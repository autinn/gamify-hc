#!/bin/bash
# Wrapper script to run docker-compose with environment validation
# Usage: ./start.sh [docker-compose arguments]
#
# Examples:
#   ./start.sh          # Start all services
#   ./start.sh -d       # Start in detached mode
#   ./start.sh --build  # Rebuild and start

set -e

# Change to project root directory
cd "$(dirname "$0")"

# Run environment check
./scripts/check-env.sh

# Run docker-compose with any passed arguments
docker compose "$@"

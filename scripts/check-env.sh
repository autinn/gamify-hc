#!/bin/bash
# Environment validation script for gamify-hc
# This script checks if .env file exists and warns about default/insecure values

set -e

# Colors for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo -e "${BLUE}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║           🎮 Gamify-HC Environment Check                      ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠️  No .env file found - creating from .env.example...${NC}"
    cp .env.example .env
    echo -e "${GREEN}✅ Created .env from .env.example${NC}"
    echo ""
    echo -e "${YELLOW}⚠️  IMPORTANT: Edit .env to set secure values before deploying to production!${NC}"
    echo -e "${YELLOW}   At minimum, change: JWT_SECRET_KEY and POSTGRES_PASSWORD${NC}"
else
    echo -e "${GREEN}✅ .env file found${NC}"
    echo ""
    
    # Check for insecure default values
    WARNINGS=0
    
    # Check JWT_SECRET_KEY
    if grep -q "JWT_SECRET_KEY=dev-secret-key-change-in-production" .env 2>/dev/null; then
        echo -e "${YELLOW}⚠️  WARNING: JWT_SECRET_KEY is using the default insecure value!${NC}"
        echo -e "   Please change this to a secure random string for production."
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Check POSTGRES_PASSWORD
    if grep -q "POSTGRES_PASSWORD=gamify_secret" .env 2>/dev/null; then
        echo -e "${YELLOW}⚠️  WARNING: POSTGRES_PASSWORD is using the default value!${NC}"
        echo -e "   Consider changing this to a more secure password."
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Check FLASK_DEBUG in production
    if grep -q "FLASK_ENV=production" .env 2>/dev/null && grep -q "FLASK_DEBUG=True" .env 2>/dev/null; then
        echo -e "${YELLOW}⚠️  WARNING: FLASK_DEBUG=True in production environment!${NC}"
        echo -e "   Set FLASK_DEBUG=False for production deployments."
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ Environment configuration looks good!${NC}"
    else
        echo ""
        echo -e "${YELLOW}   Found $WARNINGS warning(s) - please review your .env file${NC}"
    fi
fi

echo ""
echo -e "${BLUE}───────────────────────────────────────────────────────────────${NC}"
echo ""

"""
Tests for health check endpoint.

This module contains tests for the health check endpoint:
- GET /api/health: Check if API is running
"""

import json


class TestHealthEndpoint:
    """Tests for health check endpoint"""

    def test_health_check(self, test_client):
        """
        Test health check endpoint.

        Verifies:
        - Returns 200 status code
        - Response contains status and message fields
        - Status is 'ok'
        """
        response = test_client.get('/api/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'ok'
        assert 'message' in data


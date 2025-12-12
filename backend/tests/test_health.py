"""
Tests for health check endpoints.

This module contains tests for the health check endpoints:
- GET /api/health: Comprehensive health status
- GET /api/health/live: Liveness probe
- GET /api/health/ready: Readiness probe
"""

import json


class TestHealthEndpoints:
    """Tests for health check endpoints"""

    def test_health_check_comprehensive(self, test_client):
        """
        Test comprehensive health check endpoint.

        Verifies:
        - Returns 200 status code
        - Response contains all required fields
        - Status is 'ok'
        - Database status is included
        - Application info is present
        """
        response = test_client.get('/api/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        
        # Check top-level fields
        assert data['status'] == 'ok'
        assert 'timestamp' in data
        assert 'uptime_seconds' in data
        
        # Check application info
        assert 'application' in data
        assert data['application']['name'] == 'gamify-hc'
        assert 'version' in data['application']
        assert 'environment' in data['application']
        
        # Check database status
        assert 'database' in data
        assert data['database']['status'] == 'ok'
        assert data['database']['type'] == 'postgresql'
        assert 'response_time_ms' in data['database']

    def test_liveness_probe(self, test_client):
        """
        Test liveness probe endpoint.

        Verifies:
        - Returns 200 status code
        - Status is 'ok'
        - Probe type is 'liveness'
        - Does not include database check
        """
        response = test_client.get('/api/health/live')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'ok'
        assert data['probe'] == 'liveness'
        assert 'timestamp' in data
        
        # Liveness should NOT check database
        assert 'database' not in data

    def test_readiness_probe(self, test_client):
        """
        Test readiness probe endpoint.

        Verifies:
        - Returns 200 status code
        - Status is 'ready'
        - Probe type is 'readiness'
        - Includes database check
        """
        response = test_client.get('/api/health/ready')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'ready'
        assert data['probe'] == 'readiness'
        assert 'timestamp' in data
        
        # Readiness MUST check database
        assert 'database' in data
        assert data['database']['status'] == 'ok'

    def test_health_check_includes_uptime(self, test_client):
        """
        Test that health check includes uptime.

        Verifies:
        - uptime_seconds is a positive integer
        """
        response = test_client.get('/api/health')
        data = json.loads(response.data)
        
        assert 'uptime_seconds' in data
        assert isinstance(data['uptime_seconds'], int)
        assert data['uptime_seconds'] >= 0



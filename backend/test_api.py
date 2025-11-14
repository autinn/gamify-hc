#!/usr/bin/env python3
"""
Test script for refactored API endpoints
Run this after starting the API server with: python run.py
"""

import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:5001/api"

def test_endpoint(method: str, endpoint: str, data: Dict[str, Any] = None) -> None:
    """Test an API endpoint and print results"""
    url = f"{BASE_URL}{endpoint}"
    print(f"\n{'='*60}")
    print(f"Testing: {method} {endpoint}")
    print(f"{'='*60}")
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {json.dumps(result, indent=2)}")
            print("✅ PASS")
        else:
            print(f"Error: {response.text}")
            print("❌ FAIL")
            
    except requests.exceptions.ConnectionError:
        print("❌ FAIL - Cannot connect to API. Is the server running?")
    except Exception as e:
        print(f"❌ FAIL - {str(e)}")


def main():
    print("""
╔════════════════════════════════════════════════════════════╗
║         Testing Refactored Gamify-HC API                   ║
║         Aligned with Meeting Notes Standards               ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Health check
    test_endpoint("GET", "/health")
    
    # Course endpoints
    test_endpoint("GET", "/courses")
    test_endpoint("GET", "/courses/1")
    test_endpoint("GET", "/courses/1/units")
    
    # Unit endpoints
    test_endpoint("GET", "/units/1")
    test_endpoint("GET", "/units/1/hcs")  # Updated from /concepts
    
    # HC endpoints (updated from concepts)
    test_endpoint("GET", "/hcs/1")
    test_endpoint("GET", "/hcs/1/quizzes")  # Updated from /quiz-cards
    
    # Quiz endpoints
    test_endpoint("GET", "/quiz-cards/1")
    
    # User endpoints
    test_endpoint("GET", "/users/1")
    test_endpoint("GET", "/users/1/progress")
    
    # Quiz submission (POST)
    test_endpoint("POST", "/quiz-submit", {
        "user_id": 1,
        "quiz_card_id": 1,
        "answer_id": 1
    })
    
    print(f"\n{'='*60}")
    print("Testing Complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()

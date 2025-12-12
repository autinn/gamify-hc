#!/usr/bin/env python3
"""Start the Flask API server"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import create_app

# Create app at module level for Gunicorn
app = create_app()

if __name__ == '__main__':
    print("\n🚀 Starting API Server at http://localhost:5001")
    print("Press CTRL+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5001)

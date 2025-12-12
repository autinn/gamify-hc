#!/usr/bin/env python3
"""Start the Flask API server"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import create_app
from backend.config import Config

if __name__ == '__main__':
    flask_config = Config.get_flask_config()
    host = flask_config['host']
    port = flask_config['port']
    print(f"\n🚀 Starting API Server at http://{host}:{port}")
    print("Press CTRL+C to stop\n")

    app = create_app()
    app.run(**flask_config)

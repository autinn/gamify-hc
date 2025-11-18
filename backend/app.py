"""
Flask API for Gamify-HC
Modular REST API using Flask blueprints
"""

from flask import Flask, jsonify
from flask_cors import CORS
from backend.utils.database_manager import DatabaseManager
from backend.routes.auth import auth_bp
from backend.routes.courses import courses_bp
from backend.routes.units import units_bp
from backend.routes.concepts import concepts_bp
from backend.routes.quiz import quiz_bp
from backend.routes.users import users_bp


def create_app(database_url=None):
    """Create and configure Flask app with blueprints"""
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Setup database manager
    db_manager = DatabaseManager(database_url)
    
    # Make db session available to blueprints via app context
    app.db_session = db_manager.get_session
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(units_bp)
    app.register_blueprint(concepts_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(users_bp)
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        """Check if API is running"""
        return jsonify({
            'status': 'ok',
            'message': 'Gamify-HC API is running'
        })
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)

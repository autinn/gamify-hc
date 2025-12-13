"""
Flask API for Gamify-HC
Modular REST API using Flask blueprints with Swagger UI
"""

from pathlib import Path

from flask import Flask, Response, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from backend.config import Config
from backend.utils.database_manager import DatabaseManager
from backend.routes.auth import auth_bp
from backend.routes.courses import courses_bp
from backend.routes.units import units_bp
from backend.routes.concepts import concepts_bp
from backend.routes.quiz import quiz_bp
from backend.routes.users import users_bp

SWAGGER_URL = '/api/docs'
SWAGGER_SPEC_URL = '/api/swagger.json'
SWAGGER_SPEC_PATH = Path(__file__).resolve().parent.parent / 'docs' / 'swagger.json'


def create_app(database_url=None, auto_seed=True):
    """Create and configure Flask app with blueprints
    
    Args:
        database_url: Database connection string (required, or set DATABASE_URL env var)
        auto_seed: If True, seed database with initial data if empty. Default True.
                   Set to False for testing.
    """
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Setup database manager
    db_manager = DatabaseManager(database_url, auto_seed=auto_seed)
    
    # Make db session available to blueprints via app context
    app.db_session = db_manager.get_session
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(units_bp)
    app.register_blueprint(concepts_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(users_bp)
    
    # Swagger UI served from static bundle; spec is loaded from SWAGGER_SPEC_URL
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        SWAGGER_SPEC_URL,
        config={'app_name': 'Gamify-HC API'}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.route(SWAGGER_SPEC_URL, methods=['GET'])
    def swagger_spec():
        """Serve the Swagger/OpenAPI specification file for Swagger UI and clients."""
        if not SWAGGER_SPEC_PATH.exists():
            return jsonify({'error': 'Swagger spec not found'}), 404
        return Response(SWAGGER_SPEC_PATH.read_text(), mimetype='application/json')
    
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
    flask_config = Config.get_flask_config()
    app = create_app()
    app.run(**flask_config)

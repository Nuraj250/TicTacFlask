from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO
from backend.config import Config
from backend.utils.db import db
from backend.routes.auth import auth_bp
from backend.routes.matchmaking import matchmaking_bp
from backend.routes.game import game_bp
from backend.routes.leaderboard import leaderboard_bp
from backend.routes.ai import ai_bp
from backend.routes.chat import chat_bp

# Initialize Flask application
app = Flask(__name__)

# Load configuration settings from Config class
app.config.from_object(Config)

# Initialize database with Flask application
db.init_app(app)

# Initialize JWT authentication
jwt = JWTManager(app)

# Enable real-time communication with WebSockets (allows cross-origin access)
socketio = SocketIO(app, cors_allowed_origins="*")

# Enable Cross-Origin Resource Sharing (CORS) for API security
CORS(app)

# Register Blueprints (modular route handlers) with URL prefixes
app.register_blueprint(auth_bp, url_prefix="/api/auth")  # Authentication routes
app.register_blueprint(matchmaking_bp, url_prefix="/api/matchmaking")  # Matchmaking routes
app.register_blueprint(game_bp, url_prefix="/api/game")  # Game logic routes
app.register_blueprint(leaderboard_bp, url_prefix="/api")  # Leaderboard routes
app.register_blueprint(ai_bp, url_prefix="/api")  # AI-based move calculation
app.register_blueprint(chat_bp, url_prefix="/api/chat")  # Chat system routes

# Run the application with WebSocket support
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensures database tables are created before starting the server

    # Start the server with WebSocket support, enable debugging
    socketio.run(app, debug=True)

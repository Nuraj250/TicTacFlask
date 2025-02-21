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

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(matchmaking_bp, url_prefix="/api/matchmaking")
app.register_blueprint(game_bp, url_prefix="/api/game")
app.register_blueprint(leaderboard_bp, url_prefix="/api")
app.register_blueprint(ai_bp, url_prefix="/api")
app.register_blueprint(chat_bp, url_prefix="/api/chat")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensures database tables are created
    socketio.run(app, debug=True)

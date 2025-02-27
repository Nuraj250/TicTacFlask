import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """
    Configuration settings for the Tic-Tac-Toe application.

    - Loads environment variables from a .env file.
    - Provides default values if environment variables are not set.
    """

    # Security key for Flask application (used for session management)
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

    # Database connection URI (defaults to a local PostgreSQL database)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost/tic_tac_toe"
    )

    # Disables SQLAlchemy event system to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for JWT authentication (used for secure token signing)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret")

    # Message queue for real-time WebSocket communication (defaults to Redis)
    SOCKETIO_MESSAGE_QUEUE = os.getenv("SOCKETIO_MESSAGE_QUEUE", "redis://")

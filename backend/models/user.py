from backend.utils.db import db
from datetime import datetime

class User(db.Model):
    """
    Represents a user in the Tic-Tac-Toe application.

    - Stores authentication details, ranking, and match statistics.
    - Uses a hashed password for secure authentication.
    """

    # Unique user identifier (Primary Key)
    id = db.Column(db.Integer, primary_key=True)

    # Unique username (Required)
    username = db.Column(db.String(50), unique=True, nullable=False)

    # Unique email address (Required)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Hashed password (Required for authentication security)
    password_hash = db.Column(db.String(255), nullable=False)

    # Player's ranking score (Default: 1200 for Elo-based ranking system)
    ranking_score = db.Column(db.Integer, default=1200)

    # Total number of games played
    total_games = db.Column(db.Integer, default=0)

    # Number of games won
    wins = db.Column(db.Integer, default=0)

    # Number of games lost
    losses = db.Column(db.Integer, default=0)

    # Timestamp when the user account was created (Defaults to current UTC time)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        """
        Saves the user instance to the database.

        - Adds the user object to the database session.
        - Commits the transaction to save changes.
        """
        db.session.add(self)
        db.session.commit()

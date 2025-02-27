from backend.utils.db import db
from datetime import datetime

class Match(db.Model):
    """
    Represents a match record in the database.

    - Stores player IDs, winner, game data, and match timestamp.
    - Keeps a history of played matches for leaderboard and analytics.
    """

    # Unique match identifier (Primary Key)
    id = db.Column(db.Integer, primary_key=True)

    # Foreign key linking to Player 1 (Required)
    player1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Foreign key linking to Player 2 (Required)
    player2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Foreign key linking to the winner (Nullable since the game might be ongoing or a draw)
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    # Stores the game board state as JSON (Required)
    game_data = db.Column(db.JSON, nullable=False)

    # Timestamp when the match was played (Defaults to current UTC time)
    played_at = db.Column(db.DateTime, default=datetime.utcnow)

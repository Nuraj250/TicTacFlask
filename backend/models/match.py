from backend.utils.db import db
from datetime import datetime

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    player2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    game_data = db.Column(db.JSON, nullable=False)  # Stores board state
    played_at = db.Column(db.DateTime, default=datetime.utcnow)

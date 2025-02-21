from backend.utils.db import db

class Leaderboard(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    ranking_score = db.Column(db.Integer, default=1200)
    win_streak = db.Column(db.Integer, default=0)

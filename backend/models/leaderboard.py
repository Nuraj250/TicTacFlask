from backend.utils.db import db

class Leaderboard(db.Model):
    """
    Represents the leaderboard table in the database.

    - Tracks user rankings and win streaks.
    - Uses `user_id` as a foreign key referencing the `User` table.
    - Includes ranking score and win streak for each user.
    """

    # Foreign key linking to the User table (Primary Key)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    # Player's ranking score (default: 1200 for Elo-based ranking)
    ranking_score = db.Column(db.Integer, default=1200)

    # Player's current win streak count (default: 0)
    win_streak = db.Column(db.Integer, default=0)

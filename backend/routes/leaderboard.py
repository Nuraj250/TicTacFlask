from flask import Blueprint, jsonify
from backend.models.user import User

# Create a Blueprint for leaderboard-related routes
leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """
    Retrieves the top 10 players based on ranking score.

    - Fetches users ordered by `ranking_score` in descending order.
    - Limits the results to the top 10 players.
    - Returns a JSON response with player usernames and scores.

    Response Format (JSON):
    [
        {"username": "player1", "ranking_score": 1500},
        {"username": "player2", "ranking_score": 1450},
        ...
    ]

    Returns:
    - 200 OK: If the leaderboard data is successfully retrieved.
    """
    # Query the top 10 players sorted by ranking score (highest first)
    top_players = User.query.order_by(User.ranking_score.desc()).limit(10).all()

    # Format and return leaderboard data as JSON
    return jsonify([
        {"username": player.username, "ranking_score": player.ranking_score}
        for player in top_players
    ]), 200

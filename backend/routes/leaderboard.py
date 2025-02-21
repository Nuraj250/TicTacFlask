from flask import Blueprint, jsonify
from backend.models.user import User

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    top_players = User.query.order_by(User.ranking_score.desc()).limit(10).all()
    return jsonify([{"username": player.username, "ranking_score": player.ranking_score} for player in top_players]), 200

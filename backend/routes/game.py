from flask import Blueprint, request, jsonify
from backend.models.match import Match
from backend.utils.db import db

game_bp = Blueprint('game', __name__)

@game_bp.route('/play_move', methods=['POST'])
def play_move():
    data = request.get_json()
    match = Match.query.get(data['match_id'])

    if match:
        match.game_data = data['game_data']
        db.session.commit()
        return jsonify({"message": "Move updated!"}), 200
    
    return jsonify({"message": "Match not found!"}), 404

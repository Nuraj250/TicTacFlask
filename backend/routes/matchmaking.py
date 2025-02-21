from flask import Blueprint, jsonify
from flask_socketio import emit, join_room
from backend.utils.db import db
from backend.models.match import Match

matchmaking_bp = Blueprint('matchmaking', __name__)
waiting_players = []

@matchmaking_bp.route('/find_match', methods=['POST'])
def find_match():
    global waiting_players

    if len(waiting_players) > 0:
        opponent = waiting_players.pop(0)
        new_match = Match(player1_id=opponent, player2_id=request.json['player_id'], game_data={})
        db.session.add(new_match)
        db.session.commit()

        return jsonify({"match_id": new_match.id, "opponent_id": opponent}), 200
    else:
        waiting_players.append(request.json['player_id'])
        return jsonify({"message": "Waiting for an opponent..."}), 202

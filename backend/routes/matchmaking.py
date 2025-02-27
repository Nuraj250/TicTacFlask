from flask import Blueprint, jsonify, request
from flask_socketio import emit, join_room
from backend.utils.db import db
from backend.models.match import Match

# Create a Blueprint for matchmaking-related routes
matchmaking_bp = Blueprint('matchmaking', __name__)

# List to track players waiting for a match
waiting_players = []

@matchmaking_bp.route('/find_match', methods=['POST'])
def find_match():
    """
    Handles player matchmaking.

    - If a player is waiting in the queue, pairs them with the new player and starts a match.
    - If no players are waiting, adds the player to the queue.
    - Returns match details if a match is found or a waiting message if not.

    Expected Request Format (JSON):
    {
        "player_id": 42
    }

    Response Format (JSON):
    - If a match is found:
    {
        "match_id": 1,
        "opponent_id": 24
    }

    - If waiting for an opponent:
    {
        "message": "Waiting for an opponent..."
    }

    Returns:
    - 200 OK: If a match is successfully created.
    - 202 Accepted: If the player is waiting for an opponent.
    """
    global waiting_players

    # Check if another player is waiting for a match
    if len(waiting_players) > 0:
        opponent = waiting_players.pop(0)  # Get the first waiting player

        # Create a new match with the two players
        new_match = Match(player1_id=opponent, player2_id=request.json['player_id'], game_data={})
        db.session.add(new_match)
        db.session.commit()

        return jsonify({"match_id": new_match.id, "opponent_id": opponent}), 200
    else:
        # No players available, add current player to the waiting queue
        waiting_players.append(request.json['player_id'])
        return jsonify({"message": "Waiting for an opponent..."}), 202

from flask import Blueprint, request, jsonify
from backend.models.match import Match
from backend.utils.db import db

# Create a Blueprint for game-related routes
game_bp = Blueprint('game', __name__)

@game_bp.route('/play_move', methods=['POST'])
def play_move():
    """
    Handles updating the game board when a player makes a move.

    - Receives a match ID and updated game board state from the client.
    - Updates the match record in the database.
    - Returns a success message if the move is successfully recorded.

    Expected Request Format (JSON):
    {
        "match_id": 1,
        "game_data": [["X", "", "O"], ["", "X", ""], ["", "", "O"]]
    }

    Response Format (JSON):
    {
        "message": "Move updated!"
    }

    Returns:
    - 200 OK: If the move was successfully saved.
    - 404 Not Found: If the match does not exist.
    """
    data = request.get_json()

    # Find the match by ID
    match = Match.query.get(data['match_id'])

    if match:
        # Update the game board state in the database
        match.game_data = data['game_data']
        db.session.commit()
        return jsonify({"message": "Move updated!"}), 200

    # Return an error if the match is not found
    return jsonify({"message": "Match not found!"}), 404

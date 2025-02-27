from flask import Blueprint, request, jsonify
from backend.services.ai_logic import get_ai_move

# Create a Blueprint for AI-related routes
ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai-move', methods=['POST'])
def ai_move():
    """
    Handles AI move requests.

    - Receives the current board state from the client.
    - Calls the AI logic to determine the best move.
    - Returns the AI's chosen move as a JSON response.

    Expected Request Format (JSON):
    {
        "board": [["X", "", "O"], ["", "X", ""], ["", "", "O"]]
    }

    Response Format (JSON):
    {
        "ai_move": 4  # Example: AI chooses the center cell (0-based index)
    }

    Returns:
    - JSON response with the AI's move and a 200 status code.
    """
    data = request.get_json()  # Parse incoming JSON request
    board = data["board"]  # Extract the board state

    # Get the best AI move based on the current board state
    ai_move = get_ai_move(board)

    # Return the AI's move as a JSON response
    return jsonify({"ai_move": ai_move}), 200

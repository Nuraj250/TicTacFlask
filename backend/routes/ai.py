from flask import Blueprint, request, jsonify
from backend.services.ai_logic import get_ai_move

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai-move', methods=['POST'])
def ai_move():
    data = request.get_json()
    board = data["board"]
    ai_move = get_ai_move(board)
    return jsonify({"ai_move": ai_move}), 200

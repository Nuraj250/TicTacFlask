from flask import Blueprint, request, jsonify
from flask_socketio import emit
from backend.utils.db import db
from backend.models.match import Match

# Create a Blueprint for chat-related routes
chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/send-message', methods=['POST'])
def send_message():
    """
    Handles sending chat messages during a match.

    - Receives a match ID, sender ID, and message from the client.
    - Broadcasts the message to all connected players using WebSockets.
    - Returns a confirmation response.

    Expected Request Format (JSON):
    {
        "match_id": 1,
        "sender_id": 42,
        "message": "Good luck!"
    }

    Response Format (JSON):
    {
        "message": "Message sent!"
    }

    WebSocket Event Broadcast:
    - Event Name: "new_message"
    - Data Format:
    {
        "match_id": 1,
        "sender_id": 42,
        "message": "Good luck!"
    }

    Returns:
    - 200 OK: If the message is successfully broadcasted.
    """
    data = request.get_json()

    # Prepare message payload
    message = {
        "match_id": data['match_id'],
        "sender_id": data['sender_id'],
        "message": data['message']
    }

    # Broadcast the message to all connected clients in real-time
    emit('new_message', message, broadcast=True)

    return jsonify({"message": "Message sent!"}), 200

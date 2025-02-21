from flask import Blueprint, request, jsonify
from flask_socketio import emit
from backend.utils.db import db
from backend.models.match import Match

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = {
        "match_id": data['match_id'],
        "sender_id": data['sender_id'],
        "message": data['message']
    }
    emit('new_message', message, broadcast=True)
    return jsonify({"message": "Message sent!"}), 200

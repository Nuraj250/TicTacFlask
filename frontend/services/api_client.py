import requests
from frontend.settings import API_BASE_URL

def get_leaderboard():
    response = requests.get(f"{API_BASE_URL}/leaderboard")
    if response.status_code == 200:
        return response.json()
    return []

def play_move(match_id, board_state):
    payload = {"match_id": match_id, "game_data": board_state}
    response = requests.post(f"{API_BASE_URL}/game/play_move", json=payload)
    return response.status_code == 200

def get_ai_move(board_state):
    response = requests.post(f"{API_BASE_URL}/ai-move", json={"board": board_state})
    return response.json().get("ai_move")

def get_match_history():
    response = requests.get(f"{API_BASE_URL}/match-history")
    if response.status_code == 200:
        return response.json()
    return []
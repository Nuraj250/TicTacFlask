import requests
from frontend.settings import API_BASE_URL

def get_leaderboard():
    """
    Fetches the leaderboard from the API.

    - Sends a GET request to retrieve player rankings.
    - If the request is successful, returns the JSON response.
    - If the request fails, returns an empty list.

    Returns:
    - list: A list of leaderboard data (if available).
    """
    response = requests.get(f"{API_BASE_URL}/leaderboard")
    if response.status_code == 200:
        return response.json()  # Return leaderboard data
    return []  # Return empty list if request fails

def play_move(match_id, board_state):
    """
    Sends a player's move to the API.

    - Constructs a payload containing match ID and the current board state.
    - Sends a POST request to update the game state.
    - Returns True if the move was successfully processed, False otherwise.

    Parameters:
    - match_id (str): The ID of the ongoing match.
    - board_state (list): The current state of the game board.

    Returns:
    - bool: True if the move was accepted, False otherwise.
    """
    payload = {"match_id": match_id, "game_data": board_state}
    response = requests.post(f"{API_BASE_URL}/game/play_move", json=payload)
    return response.status_code == 200  # Return True if move was successful

def get_ai_move(board_state):
    """
    Requests an AI-generated move based on the current board state.

    - Sends a POST request to the AI move API.
    - Extracts and returns the AI's suggested move.

    Parameters:
    - board_state (list): The current state of the game board.

    Returns:
    - dict or None: The AI's move (if available), None otherwise.
    """
    response = requests.post(f"{API_BASE_URL}/ai-move", json={"board": board_state})
    return response.json().get("ai_move")  # Extract and return AI move

def get_match_history():
    """
    Retrieves past match history from the API.

    - Sends a GET request to fetch previous match records.
    - If the request is successful, returns the JSON response.
    - If the request fails, returns an empty list.

    Returns:
    - list: A list of past match records (if available).
    """
    response = requests.get(f"{API_BASE_URL}/match-history")
    if response.status_code == 200:
        return response.json()  # Return match history
    return []  # Return empty list if request fails

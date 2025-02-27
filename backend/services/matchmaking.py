from backend.models.match import Match
from backend.utils.db import db

# List to track players waiting for a match
waiting_players = []

def find_match(player_id):
    """
    Finds a match for the given player.

    - If another player is already waiting, pairs them and creates a match.
    - If no players are waiting, adds the player to the queue.
    - Returns match details if a match is found, otherwise None.

    Parameters:
    - player_id (int): The ID of the player looking for a match.

    Returns:
    - tuple: (match_id, opponent_id) if matched, (None, None) if waiting.
    """

    global waiting_players

    if waiting_players:
        # Get the first waiting player
        opponent = waiting_players.pop(0)

        # Create a new match with the two players
        new_match = Match(player1_id=opponent, player2_id=player_id, game_data={})
        db.session.add(new_match)
        db.session.commit()

        return new_match.id, opponent  # Return match ID and opponent
    else:
        # No players available, add the current player to the queue
        waiting_players.append(player_id)
        return None, None  # Indicate player is still waiting

from backend.models.match import Match
from backend.utils.db import db

waiting_players = []

def find_match(player_id):
    global waiting_players

    if waiting_players:
        opponent = waiting_players.pop(0)
        new_match = Match(player1_id=opponent, player2_id=player_id, game_data={})
        db.session.add(new_match)
        db.session.commit()
        return new_match.id, opponent
    else:
        waiting_players.append(player_id)
        return None, None

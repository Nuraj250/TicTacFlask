def calculate_elo(winner_elo, loser_elo):
    K = 32
    expected_win = 1 / (1 + 10 ** ((loser_elo - winner_elo) / 400))
    new_winner_elo = winner_elo + K * (1 - expected_win)
    new_loser_elo = loser_elo + K * (0 - expected_win)
    return int(new_winner_elo), int(new_loser_elo)

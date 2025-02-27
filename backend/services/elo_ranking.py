def calculate_elo(winner_elo, loser_elo):
    """
    Calculates the updated Elo ratings for the winner and loser after a match.

    - Uses the Elo rating system to adjust player rankings.
    - Factors in the difference in skill levels between players.

    Parameters:
    - winner_elo (int): The Elo rating of the winning player.
    - loser_elo (int): The Elo rating of the losing player.

    Returns:
    - tuple: (new_winner_elo, new_loser_elo) representing updated ratings.

    Elo Rating Formula:
    - Expected win probability: `1 / (1 + 10 ^ ((loser_elo - winner_elo) / 400))`
    - New Elo Calculation:
      - Winner: `winner_elo + K * (1 - expected_win)`
      - Loser: `loser_elo + K * (0 - expected_win)`

    Example Usage:
    ```
    new_winner, new_loser = calculate_elo(1500, 1400)
    print(new_winner, new_loser)  # Updated ratings
    ```
    """
    K = 32  # The K-factor determines rating adjustment sensitivity

    # Calculate the expected probability of the winner winning
    expected_win = 1 / (1 + 10 ** ((loser_elo - winner_elo) / 400))

    # Update Elo ratings based on match outcome
    new_winner_elo = winner_elo + K * (1 - expected_win)
    new_loser_elo = loser_elo + K * (0 - expected_win)

    # Return updated ratings as integers
    return int(new_winner_elo), int(new_loser_elo)

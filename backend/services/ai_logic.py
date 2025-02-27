def get_ai_move(board):
    """
    Determines the AI's move in a Tic-Tac-Toe game.

    - The AI selects the first available empty spot.
    - The board is a 1D list representing a 3x3 grid.

    Parameters:
    - board (list): A 1D list of 9 elements representing the Tic-Tac-Toe board.

    Returns:
    - int: The index of the selected move (0-8).
    - None: If no move is possible (board is full).

    Example Usage:
    ```
    board = ["X", "", "O", "", "X", "", "O", "", ""]
    ai_move = get_ai_move(board)
    print(ai_move)  # AI chooses the first available empty space
    ```
    """
    for i in range(9):
        if board[i] == "":
            return i  # AI picks the first empty spot
    
    return None  # No available move

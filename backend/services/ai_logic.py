def get_ai_move(board):
    for i in range(9):
        if board[i] == "":
            return i  # AI picks the first empty spot
    return None

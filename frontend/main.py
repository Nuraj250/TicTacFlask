import pygame
import sys
from frontend.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from frontend.components.board import Board
from frontend.components.player import Player
from frontend.components.chat import Chat
from frontend.components.history_screen import HistoryScreen
from frontend.services.api_client import play_move, get_ai_move
from frontend.services.websocket_client import connect_to_server

# Initialize pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

def restart_game():
    """
    Resets the game state to start a new match.

    - Creates a new board.
    - Resets the current player to "X".
    - Clears the winner status.
    """
    global board, current_player, winner
    board = Board(restart_game)  # Create a new board instance
    current_player = "X"  # Reset to player X's turn
    winner = None  # Clear the winner

# Initialize game components
board = Board(restart_game)
player_x = Player("Player 1", "X")
player_o = Player("Player 2", "O")
chat = Chat()
history_screen = HistoryScreen()

# Set initial game state
current_player = "X"  # Player X starts first
winner = None  # No winner at the beginning

# Connect to the game server for real-time updates
connect_to_server()

# Main game loop
running = True
while running:
    # Clear the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw game elements
    board.draw(screen)
    player_x.draw(screen, (10, 10))
    player_o.draw(screen, (10, 50))
    chat.draw(screen)

    # If there's a winner, animate the win effect
    if winner:
        board.animate_winner(screen)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait before restarting

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handle window close
            running = False

        # Pass event to board (for button handling)
        board.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # Show match history when 'H' key is pressed
                history_screen.draw(screen)
                pygame.display.flip()
                pygame.time.wait(3000)  # Pause to display history

        # Handle player move (if it's Player X's turn and no winner yet)
        if event.type == pygame.MOUSEBUTTONDOWN and current_player == "X" and not winner:
            x, y = pygame.mouse.get_pos()  # Get mouse click position
            row, col = y // 200, x // 200  # Convert position to grid coordinates

            if board.grid[row][col] == "":  # Check if the cell is empty
                board.animate_move(screen, row, col, "X")  # Animate the move
                play_move(1, board.grid)  # Send the move to the server
                winner = board.check_winner()  # Check if this move wins the game

                if not winner:
                    current_player = "O"  # Switch turn to AI

    # Handle AI move (if it's AI's turn and no winner yet)
    if current_player == "O" and not winner:
        ai_move = get_ai_move(board.grid)  # Request AI move from server
        if ai_move is not None:
            row, col = divmod(ai_move, 3)  # Convert AI move to grid coordinates
            board.animate_move(screen, row, col, "O")  # Animate AI move
            play_move(1, board.grid)  # Send AI move to the server
            winner = board.check_winner()  # Check if AI won

            if not winner:
                current_player = "X"  # Switch turn back to Player X

    pygame.display.flip()  # Refresh the screen

# Quit the game when the loop exits
pygame.quit()
sys.exit()

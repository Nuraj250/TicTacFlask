import pygame
import sys
from frontend.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from frontend.components.board import Board
from frontend.components.player import Player
from frontend.components.chat import Chat
from frontend.components.history_screen import HistoryScreen
from frontend.services.api_client import play_move, get_ai_move
from frontend.services.websocket_client import connect_to_server

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

def restart_game():
    global board, current_player, winner
    board = Board(restart_game)
    current_player = "X"
    winner = None

board = Board(restart_game)
player_x = Player("Player 1", "X")
player_o = Player("Player 2", "O")
chat = Chat()
history_screen = HistoryScreen()

current_player = "X"
winner = None

connect_to_server()

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    board.draw(screen)
    player_x.draw(screen, (10, 10))
    player_o.draw(screen, (10, 50))
    chat.draw(screen)

    if winner:
        board.animate_winner(screen)
        pygame.display.flip()
        pygame.time.wait(2000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        board.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                history_screen.draw(screen)
                pygame.display.flip()
                pygame.time.wait(3000)

        if event.type == pygame.MOUSEBUTTONDOWN and current_player == "X" and not winner:
            x, y = pygame.mouse.get_pos()
            row, col = y // 200, x // 200
            if board.grid[row][col] == "":
                board.animate_move(screen, row, col, "X")
                play_move(1, board.grid)
                winner = board.check_winner()
                if not winner:
                    current_player = "O"

    if current_player == "O" and not winner:
        ai_move = get_ai_move(board.grid)
        if ai_move is not None:
            row, col = divmod(ai_move, 3)
            board.animate_move(screen, row, col, "O")
            play_move(1, board.grid)
            winner = board.check_winner()
            if not winner:
                current_player = "X"

    pygame.display.flip()

pygame.quit()
sys.exit()

import socketio

# Create a Socket.IO client instance
sio = socketio.Client()

def connect_to_server():
    """
    Connects the client to the game server using Socket.IO.

    - Establishes a WebSocket connection with the server at the specified address.
    - This allows real-time communication for chat messages and game updates.
    """
    sio.connect("http://127.0.0.1:5000")  # Connect to the server

@sio.on("new_message")
def handle_new_message(data):
    """
    Handles incoming chat messages from the server.

    - Listens for the "new_message" event.
    - Extracts and prints the received chat message.

    Parameters:
    - data (dict): The data received from the server, containing the message.

    Example of expected data:
    {
        "message": "Player1: Hello!"
    }
    """
    print(f"Chat: {data['message']}")  # Print the received message

@sio.on("update_game")
def handle_game_update(data):
    """
    Handles game state updates from the server.

    - Listens for the "update_game" event.
    - Prints the updated game data received.

    Parameters:
    - data (dict): The game state update sent by the server.

    Example of expected data:
    {
        "board": [["X", "", "O"], ["", "X", ""], ["", "", "O"]],
        "turn": "player2"
    }
    """
    print("Game Updated:", data)  # Print the updated game state

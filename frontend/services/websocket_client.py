import socketio

sio = socketio.Client()

def connect_to_server():
    sio.connect("http://127.0.0.1:5000")

@sio.on("new_message")
def handle_new_message(data):
    print(f"Chat: {data['message']}")

@sio.on("update_game")
def handle_game_update(data):
    print("Game Updated:", data)

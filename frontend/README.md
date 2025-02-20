

# 🎮 Tic-Tac-Toe Frontend (Pygame UI)

This is the **Pygame-based frontend** for the **Web-Powered Tic-Tac-Toe Game**.  
It provides an interactive game board, real-time updates, chat functionality, and animations.

---

## **🚀 Features**
✅ **Interactive UI with Animations & Sound Effects**  
✅ **Multiplayer Mode with Real-Time Updates**  
✅ **Single-Player Mode (AI Opponent)**  
✅ **In-Game Chat System**  
✅ **Flashing Win Animation & Restart Button**  
✅ **Match History Screen to View Past Games**  

---

## **📂 Project Structure**
```
frontend/
├── assets/                    # Game Assets (Images, Sounds)
│   ├── board.png               # Game board background
│   ├── x_piece.png             # X piece image
│   ├── o_piece.png             # O piece image
│   ├── restart_button.png      # Restart button image
│   ├── move_sound.wav          # Move placement sound
│   ├── click_sound.wav         # Click sound
│   ├── win_sound.wav           # Winning sound effect
│   ├── font.ttf                # Game font
├── components/                 # UI Components
│   ├── board.py                # Renders Tic-Tac-Toe board
│   ├── player.py               # Player profiles & status
│   ├── chat.py                 # In-game chat system
│   ├── button.py               # UI button handling
│   ├── history_screen.py       # Displays past matches
├── services/                   # API & WebSocket Services
│   ├── api_client.py           # Fetches match history, leaderboard, and gameplay
│   ├── websocket_client.py     # Manages real-time updates
├── main.py                     # Main Pygame Application
├── settings.py                 # Game Configuration
├── README.md                   # Documentation
```

---

## **📦 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/tic-tac-toe-web.git
cd tic-tac-toe-web/frontend
```

### **2️⃣ Install Dependencies**
```bash
pip install pygame requests socketio-client
```

### **3️⃣ Configure Game Settings**
Modify `settings.py` if needed:
```python
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
API_BASE_URL = "http://127.0.0.1:5000/api"
```

---

## **🚀 Running the Game**
### **Start the Backend (if not running)**
```bash
bash ../backend/scripts/start_server.sh
```

### **Run the Pygame Frontend**
```bash
bash scripts/start_game.sh
```
or manually:
```bash
python main.py
```

---

## **🎮 Gameplay Instructions**
### **Game Controls**
- **Click on a cell** to place your move.
- **Wait for your turn** (if multiplayer).
- **Press "H"** to view match history.
- **Click "Restart"** after a win to start a new game.

### **Multiplayer Mode**
1. The game **automatically pairs** two players.
2. **Wait in the lobby** until an opponent joins.
3. Moves are **synced in real-time** via WebSockets.

### **Single-Player Mode (vs AI)**
1. Click on a cell to place **"X"**.
2. AI will **automatically respond** as "O".
3. Try to **win against the AI!**

---

## **💼 API Endpoints Used**
### **🎮 Game Logic**
| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| `POST` | `/api/game/play_move` | Submit a move            |
| `GET`  | `/api/match/{id}`    | Get match history        |

### **🤖 AI Opponent**
| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| `POST` | `/api/ai-move`       | Get AI move suggestion   |

### **🏆 Leaderboard**
| Method | Endpoint              | Description              |
|--------|----------------------|--------------------------|
| `GET`  | `/api/leaderboard`    | Get top players         |

### **💬 Chat System**
| Method | Endpoint              | Description              |
|--------|----------------------|--------------------------|
| `POST` | `/api/chat/send-message` | Send chat message     |

---

## **🔊 Sound & Animations**
### **Animations**
- Moves are **animated with a fade effect**.
- Winning row **flashes yellow** before showing the restart button.

### **Sound Effects**
| Action | Sound File | Description |
|--------|-----------|-------------|
| **Move Placement** | `move_sound.wav` | Plays when a move is made |
| **Click Sound** | `click_sound.wav` | Plays when clicking UI elements |
| **Win Sound** | `win_sound.wav` | Plays when a player wins |

---

## **📌 Deployment**
### **1️⃣ Package the Game**
Use **PyInstaller** to create an executable:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```
This will create an executable file under `dist/`.

### **2️⃣ Deploy on a Web Platform**
Convert Pygame to a **Web App** using **Pyodide or PyScript** for browser support.

---

## **💡 Troubleshooting**
### **Game Won't Start?**
- Ensure **Flask backend is running**:
```bash
bash ../backend/scripts/start_server.sh
```
- Check `API_BASE_URL` in `settings.py`.

### **No Sound?**
- Verify sound files are in **frontend/assets/**.
- Ensure **pygame.mixer** is initialized:
```python
pygame.mixer.init()
```

---

## **🐝 License**
This project is licensed under the **MIT License**.


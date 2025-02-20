### **📂 `README.md`** (Full Project Documentation)

```md
# 🎮 Web-Powered Tic-Tac-Toe Game

This is a **fully-featured Tic-Tac-Toe game** built with **Flask, Pygame, PostgreSQL/Firebase, and WebSockets**.  
It supports **multiplayer matchmaking, AI opponents, chat system, leaderboards, animations, and sound effects**.

---

## **🚀 Features**
✅ **Classic Tic-Tac-Toe Gameplay** (Pygame-based UI)  
✅ **Multiplayer Mode** (Real-time matchmaking via Flask-SocketIO)  
✅ **Single-Player Mode (AI Opponent)** (Minimax Algorithm)  
✅ **ELO-Based Ranking System**  
✅ **In-Game Chat System**  
✅ **Flashing Win Animation & Sound Effects**  
✅ **Match History & Leaderboard**  

---

## **📂 Project Structure**
```
tic-tac-toe-web/
├── backend/                     # Flask Backend
│   ├── models/                   # Database Models
│   ├── routes/                   # API Endpoints
│   ├── services/                 # Business Logic
│   ├── utils/                    # Utilities
│   ├── database/                 # Database Setup
│   ├── scripts/                  # Deployment & Server Management
│   ├── tests/                    # Unit & Integration Tests
│   ├── config.py                  # Configuration
│   ├── app.py                     # Main Flask Application
│   ├── requirements.txt            # Dependencies
│   ├── .env                        # Environment Variables
│   ├── README.md                    # Backend Documentation
├── frontend/                     # Pygame Frontend
│   ├── assets/                    # Game Assets (Images, Sounds)
│   ├── components/                 # UI Components
│   ├── services/                   # API & WebSocket Services
│   ├── main.py                     # Main Pygame Application
│   ├── settings.py                  # Game Configuration
│   ├── README.md                    # Frontend Documentation
├── README.md                      # Full Project Documentation
```

---

## **📦 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/tic-tac-toe-web.git
cd tic-tac-toe-web
```

### **2️⃣ Backend Setup**
#### **Create Virtual Environment & Install Dependencies**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### **Configure Environment Variables**
Create a `.env` file in `backend/`:
```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=postgresql://user:password@localhost/tic_tac_toe
SOCKETIO_MESSAGE_QUEUE=redis://
```

#### **Initialize Database**
```bash
python database/init_db.py
```

#### **Start the Flask API**
```bash
bash scripts/start_server.sh
```
or manually:
```bash
python app.py
```

---

### **3️⃣ Frontend Setup**
#### **Install Dependencies**
```bash
cd frontend
pip install pygame requests socketio-client
```

#### **Run the Pygame Frontend**
```bash
bash ../backend/scripts/start_game.sh
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

## **📡 API Endpoints**
### **🔐 Authentication**
| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| `POST` | `/api/auth/register` | Register a new user      |
| `POST` | `/api/auth/login`    | Login & get JWT token    |

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

## **📜 Deployment**
### **1️⃣ Deploy on Heroku**
```bash
heroku login
heroku create tic-tac-toe-web
git push heroku main
```

### **2️⃣ Deploy on AWS (EC2)**
```bash
scp -i your-key.pem backend/* ec2-user@your-instance:/home/ec2-user/
ssh -i your-key.pem ec2-user@your-instance
```

### **3️⃣ Deploy on DigitalOcean**
Use **Docker**:
```bash
docker build -t tic-tac-toe-backend .
docker run -p 5000:5000 tic-tac-toe-backend
```

---

## **💡 Troubleshooting**
### **Game Won't Start?**
- Ensure **Flask backend is running**:
```bash
bash backend/scripts/start_server.sh
```
- Check `API_BASE_URL` in `frontend/settings.py`.

### **Database Connection Issues**
- Ensure PostgreSQL is running:
```bash
sudo service postgresql start
```
- Verify database URL in `.env`.

### **Flask-SocketIO Not Working?**
- Install Redis:
```bash
sudo apt install redis-server
```
- Start Redis:
```bash
redis-server
```

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **🔗 Connect**
💻 [Your GitHub](https://github.com/Nuraj250)  
🚀 Happy Coding! 🎮🔥
``

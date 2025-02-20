# 🎮 Tic-Tac-Toe Backend (Flask API)

This is the **Flask-based backend** for the **Web-Powered Tic-Tac-Toe Game**.  
It manages authentication, matchmaking, game logic, AI opponent, leaderboards, and real-time interactions.

---

## **🚀 Features**
- ✅ **User Authentication** (Email/Password with JWT)  
- ✅ **Real-Time Multiplayer** (Flask-SocketIO for matchmaking & gameplay)  
- ✅ **AI Opponent** (Minimax Algorithm for single-player mode)  
- ✅ **Leaderboard System** (ELO ranking for competitive players)  
- ✅ **Chat System** (In-game messaging)  
- ✅ **Match History API** (Track past games)  

---

## **📂 Project Structure**
```
backend/
├── models/                     # Database Models (SQLAlchemy)
│   ├── user.py                 # User Model
│   ├── match.py                # Match Model
│   ├── leaderboard.py          # Leaderboard Model
├── routes/                     # API Endpoints
│   ├── auth.py                 # Authentication API
│   ├── game.py                 # Game logic API
│   ├── matchmaking.py          # Matchmaking API
│   ├── leaderboard.py          # Leaderboard API
│   ├── ai.py                   # AI Opponent API
│   ├── chat.py                 # Chat API
├── services/                   # Business Logic Services
│   ├── elo_ranking.py          # ELO Ranking Calculation
│   ├── matchmaking.py          # Matchmaking Logic
│   ├── ai_logic.py             # AI Minimax Algorithm
├── utils/                      # Utilities
│   ├── db.py                   # Database Connection
│   ├── auth.py                 # JWT Authentication Helper
├── database/                   # Database Setup
│   ├── migrations/             # PostgreSQL Migrations
│   ├── init_db.py              # Database Initialization
├── scripts/                    # Deployment & Server Management
│   ├── deploy.sh               # Deployment Script
│   ├── start_server.sh         # Start Flask API
│   ├── start_game.sh           # Start Pygame Client
├── tests/                      # Unit & Integration Tests
│   ├── test_auth.py            # Authentication Tests
│   ├── test_game.py            # Game Logic Tests
│   ├── test_matchmaking.py     # Matchmaking Tests
│   ├── test_ai.py              # AI Tests
│   ├── test_chat.py            # Chat Tests
├── config.py                    # Configuration Settings
├── app.py                        # Main Flask Application
├── requirements.txt              # Dependencies
├── .env                          # Environment Variables
├── README.md                     # Backend Documentation
```

---

## **📦 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/tic-tac-toe-web.git
cd tic-tac-toe-web/backend
```

### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Environment Variables**
Create a `.env` file in `backend/` and add:
```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=postgresql://user:password@localhost/tic_tac_toe
SOCKETIO_MESSAGE_QUEUE=redis://
```

### **5️⃣ Initialize Database**
```bash
python database/init_db.py
```

---

## **🚀 Running the Backend**
### **Start Flask API**
```bash
bash scripts/start_server.sh
```
or manually:
```bash
python app.py
```

### **Run Tests**
```bash
python -m unittest discover tests
```

---

## **💼 API Endpoints**
### **🔒 Authentication**
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

## **🗂 Deployment**
### **1️⃣ Deploy on Heroku**
```bash
heroku login
heroku create tic-tac-toe-backend
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

## **🐟 License**
This project is licensed under the **MIT License**.


# 🎮 Tic-Tac-Toe Web App (Flask)

A simple, interactive, and visually appealing **Tic-Tac-Toe game** built using **Python (Flask)** for the backend and **HTML, CSS, JavaScript** for the frontend.
Features include **real-time updates**, **win/draw detection**, and a glowing **dark-mode UI**.

---

## 📌 Live Demo (Optional)

If you deploy it on Render/Heroku/etc., add the link here.

---

## 🧩 Features

* ✔️ Classic Tic-Tac-Toe gameplay
* ✔️ Flask-powered backend with JSON APIs
* ✔️ Real-time move updates without page reload
* ✔️ Win, lose, and draw detection
* ✔️ Reset game with one click
* ✔️ Stylish **dark-mode neon UI**
* ✔️ Fully responsive grid layout

---

## 📂 Project Structure

```
Tic-Tac-Toe-Web-App/
│
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   └── style.css          # Styling
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/RasikhAli/Tic-Tac-Toe-Web-App.git
cd Tic-Tac-Toe-Web-App
```

### 2. Create & activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the game

Visit in your browser:

```
http://127.0.0.1:5000/
```

---

## 🕹️ How It Works

### Backend (Flask)

* Manages the game board, current player, win/draw logic
* `/play` route handles moves and returns JSON updates
* `/reset` resets the board

### Frontend

* **index.html** renders the board and status text
* JavaScript handles:

  * Sending player moves
  * Updating board cells live
  * Showing win/draw messages
  * Resetting the game

### Styling

* **Dark neon cyber-style UI**
* Glowing hover effects
* Responsive centered layout

---

## 📸 Preview (Optional)

Add screenshots or GIFs of gameplay here once available.

---

## 🛠️ API Routes

| Route    | Method | Description                            |
| -------- | ------ | -------------------------------------- |
| `/`      | GET    | Loads the game UI                      |
| `/play`  | POST   | Submit a move (JSON: `{ index: int }`) |
| `/reset` | POST   | Resets the game                        |

---

## 🔮 Future Improvements

* Add AI opponent (Minimax / Easy / Hard modes)
* Add multiplayer online support
* Add score tracking
* Animate winning line

---

## 📄 License

This project is open-source. Feel free to modify and improve it!
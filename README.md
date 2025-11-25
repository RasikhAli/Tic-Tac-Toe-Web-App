# Tic-Tac-Toe Web App 🎮

A simple and modern **Tic Tac Toe game** built using **Flask (Python)** for the backend and **HTML/CSS/JavaScript** for the frontend. The UI features a futuristic **dark mode neon theme**.

---

## 🔗 GitHub Repository

**[https://github.com/RasikhAli/Tic-Tac-Toe-Web-App.git](https://github.com/RasikhAli/Tic-Tac-Toe-Web-App.git)**

---

## ✨ Features

✔️ Play Tic Tac Toe in the browser
✔️ Neon dark-mode UI
✔️ Real-time game updates without page reloads
✔️ Win detection, draw detection, and turn switching
✔️ “Reset Game” button
✔️ Lightweight Flask backend API
✔️ Simple folder structure and easy to extend

---

## 📁 Project Structure

```
Tic-Tac-Toe-Web-App/
│
├── app.py               # Flask backend and game logic
├── templates/
│   └── index.html       # Frontend layout
├── static/
│   └── style.css        # Styling (dark mode neon theme)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/RasikhAli/Tic-Tac-Toe-Web-App.git
cd Tic-Tac-Toe-Web-App
```

### 2. Create a Virtual Environment (Optional but recommended)

```sh
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```sh
pip install flask
```

### 4. Run the App

```sh
python app.py
```

### 5. Open in Browser

Visit:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

### Backend (Flask)

* Stores game board, current player, and game status
* Exposes endpoints:

  * **POST /play** → Handles user moves & checks win/draw conditions
  * **POST /reset** → Resets the game state
* Runs basic game logic such as:

  * Win checking
  * Draw detection
  * Turn switching

### Frontend

* HTML grid representing the board
* JavaScript fetches `/play` API to update the state dynamically
* CSS provides dark neon styling and hover animations

---

## 📸 UI Preview (Optional — you can add a screenshot here)

If you want, I can generate a mock-up image or help you place real screenshots.

---

## 🛠 Future Improvements (Ideas)

* Add AI opponent (Minimax algorithm)
* Add score tracking
* Add animations for wins
* Allow multiplayer over network or WebSockets
* Mobile-responsive design

---

## 📄 License

This project is open-source and available for modification.
(If you want a formal license like MIT, I can add it!)
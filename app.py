# pip install flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [str(i) for i in range(1, 10)]
current_player = "X"
game_over = False
winner = None

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

@app.route("/")
def index():
    return render_template("index.html", board=board)

@app.route("/play", methods=["POST"])
def play():
    global current_player, game_over, winner

    data = request.json
    index = int(data["index"])

    if game_over or board[index] in ['X', 'O']:
        return jsonify({"status": "invalid", "board": board, "winner": winner})

    board[index] = current_player

    if check_winner(board, current_player):
        winner = f"Player {current_player}"
        game_over = True
    elif is_draw(board):
        winner = "Draw"
        game_over = True
    else:
        current_player = "O" if current_player == "X" else "X"

    return jsonify({
        "status": "ok",
        "board": board,
        "winner": winner,
        "current_player": current_player
    })

@app.route("/reset", methods=["POST"])
def reset():
    global board, current_player, game_over, winner
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    game_over = False
    winner = None
    return jsonify({"status": "reset", "board": board, "winner": None})

if __name__ == "__main__":
    app.run(debug=True)

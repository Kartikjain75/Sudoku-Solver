from flask import Flask, render_template, request
from solver import solve_sudoku

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solved = False

    if request.method == "POST":
        for i in range(9):
            for j in range(9):
                val = request.form.get(f"cell-{i}-{j}")
                board[i][j] = int(val) if val and val.isdigit() else 0

        if solve_sudoku(board):
            solved = True

    return render_template("index.html", board=board, solved=solved)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

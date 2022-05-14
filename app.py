from flask import Flask, jsonify, render_template, request
import requests
app = Flask(__name__)

api_url = "http://localhost:8000"
request_url = "/board"

def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}{}".format(api_url, request_url)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board

@app.route("/")
def hello_world():
    board = read_board()
    return render_template("tictactoe.html", board=board)

if __name__ == "__main__":
    debug=True
    app.run(host="0.0.0.0",debug=debug)
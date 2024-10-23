from flask import render_template, request
from app import app
from app.game import play_game


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""

    if request.method == 'POST':
        letter = request.form['letter'].lower()
        message = play_game(letter)

    return render_template('index.html', message=message)
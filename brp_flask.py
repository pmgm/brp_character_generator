# model
from dice_roller import *
from game_system import *
from genre import *
from genre_brp_fantasy import *
# visualisation
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/")
def choose_game():
    games_available = [cls() for cls in GameSystem.__subclasses__()]
    game_name_class = {}
    for game in games_available:
        game_name_class[game.name] = type(game).__name__
    return render_template(
        'choose_game.html',
        title="Choose game system",
        systems=games_available,
        game_class=game_name_class
    )

@app.route("/genre", methods = ['POST', 'GET'])
def choose_genre():
    if request.method == 'POST':
        gamessystem = request.form['gamesystem']
        # instatiate a game_system
        bob = globals()[gamessystem]
    return render_template(
        'choose_genre.html',
        title="Choose genre",
        system= gamessystem
    )
    
if __name__ == "__main__":
    app.run()
    

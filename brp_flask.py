# model
from dice_roller import *
from game_system import *
from genre import *
from genre_brp_fantasy import *
# visualisation
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def choose_game():
    games_available = [cls() for cls in GameSystem.__subclasses__()]
    return render_template(
    'choose_game.html',
    title="Choose game system",
    systems=games_available
    )

if __name__ == "__main__":
    app.run()
    

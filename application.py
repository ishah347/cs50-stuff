__author__ = 'Imran Shah'


from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
import world
from player import Player

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

world.load_tiles()
player = Player()


@app.route("/", methods=["GET", "POST"])
def index():
    """Page for game"""
    # Establish the parameters of the room player is in and what effect it has on him
    room = world.tile_exists(player.location_x, player.location_y)
    if player.is_alive() and not player.victory:
        available_actions = room.available_actions()
        action_input = request.form.get("btn_submit")
        available_hotkeys = []
        # If a button was pushed, match it to the key word for one of the actions and do it
        for action in available_actions:
            available_hotkeys.append(action.hotkey)
            if action_input == action.hotkey:
                player.do_action(action, **action.kwargs)
                # Establish the parameters of the possibly new room player is in and what effect it has on him
                room = world.tile_exists(player.location_x, player.location_y)
                availableactions = room.available_actions()
                # Return relevant data so it can be printed in the HTML
                if player.is_alive() and not player.victory:
                    if action_input == "inventory":
                        return render_template("index.html", firsttext=room.intro_text(), nexttext=room.modify_player(player), items=player.act, thentext="", availableactions=availableactions, picture=room.getName())
                    else:
                        return render_template("index.html", firsttext=room.intro_text(), nexttext=room.modify_player(player), items="", thentext=player.act, availableactions=availableactions, picture=room.getName())
                break
        if action_input not in available_hotkeys and action_input is not None:
            return render_template("index.html", firsttext=room.intro_text(), nexttext="Please select a valid option", items="", thentext="", picture=room.getName())
    if player.victory or not player.is_alive():
        return render_template("index.html", firsttext=room.intro_text(), nexttext="You must restart", items="", thentext="", picture=room.getName())
    return render_template("index.html", firsttext=room.intro_text(), nexttext=room.modify_player(player), items="", thentext="", picture=room.getName())

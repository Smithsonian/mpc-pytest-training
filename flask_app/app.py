from flask import Flask, send_from_directory, render_template
from mpc_training import team
import random

app = Flask(__name__)


@app.route("/")
def mpc():
    team_output = {}
    input_int = random.randint(0, 9)
    for name, function in team.__dict__.items():
        if name.startswith("mpc") and callable(function):
            team_output[name.replace("mpc_", "")] = function(input_int)
    return render_template('base.html', team_output=team_output, input_int=input_int)


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

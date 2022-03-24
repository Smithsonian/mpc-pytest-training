from flask import Flask, send_from_directory, render_template
from mpc_training import team

app = Flask(__name__)


@app.route("/")
def mpc():
    d = {"chris": team.chris()}
    return render_template('base.html', d=d)


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

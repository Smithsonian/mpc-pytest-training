from flask import Flask, jsonify, send_from_directory
from mpc import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {"hello": "world"}


@app.route("/mpc")
def mpc():
    return {"chris": chris()}


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

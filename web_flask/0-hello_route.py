#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """return a given string'"""
    return render_template("10-hbnb_filters.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

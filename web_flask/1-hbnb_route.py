#!/usr/bin/python3
"""
This is to run a minimal app using flask
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''flask app'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    '''flask app'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
Flask is awesome
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''flask app'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Second route'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_cool(text):
    '''c is cool'''
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    '''python is cool'''
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even(n):
    if n % 2 == 0:
        odds = "even"
    else:
        odds = "odd"
    return render_template("6-number_odd_or_even.html", n=n, odds=odds)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""WebFlask module"""
from flask import Flask, render_template
from os import environ
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Diplay Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Diplay HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Diplay text"""
    real_text = text.replace('_', ' ')
    return 'C {}'.format(real_text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Diplay text"""
    real_text = text.replace('_', ' ')
    return 'Python {}'.format(real_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Diplay number if integer"""
    return '{}'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Diplay number if integer from template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)

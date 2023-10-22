#!/usr/bin/python3
"""WebFlask application module"""
from flask import Flask, render_template
from os import environ
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(session):
    """Remove the current session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """Listings cities by state"""
    from models.state import State
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

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


@app.route('/states_list', strict_slashes=False)
def listing_states():
    """Listings states"""
    from models.state import State
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)

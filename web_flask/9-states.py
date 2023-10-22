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


@app.route('/states', strict_slashes=False, defaults={'id': ''})
@app.route('/states/<id>', strict_slashes=False)
def show_state(id):
    """Shows state by id"""
    from models.state import State
    states = storage.all(State).values()
    if id:
        for state in states:
            if state.id == id:
                return render_template("9-states.html", state=state)
        return render_template("9-states.html", state=None)
    return render_template("9-states.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""WebFlask application module"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def show_filters():
    """Shows filters"""
    from models.state import State
    from models.amenity import Amenity
    from models.place import Place
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

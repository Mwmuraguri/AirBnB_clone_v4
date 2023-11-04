#!/usr/bin/python3
"""
Flask framework interacting withwith AirBnB static HTML Template
"""
import uuid
from flask import Flask, render_template, url_for
from models import storage

# flask framework
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    close() is called on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/3-hbnb/')
def hbnb_filters(the_id=None):
    """
    request is handled to custom template with states, cities & amentities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amenis = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('3-hbnb.html',
                           states=states,
                           amenis=amenis,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    """
     the MAIN Flask App"""
    app.run(host=host, port=port)

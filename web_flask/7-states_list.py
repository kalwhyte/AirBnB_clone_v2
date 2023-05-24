#!/usr/bin/python3
"""

    Runs a Flask web application on 0.0.0.0:5000

"""
<<<<<<< HEAD
from models import storage
=======
from models.storage import storage
>>>>>>> 7e84b8d77bfaf2ea8b7630ba7ac3e39e93694429
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ Returns an HTML page of all States sorted by name """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Removes the current SQLAlchemy session. """
    storage.close()


if __name__ == "__main__":
    """ Run on 0.0.0.0 """
    app.run(host='0.0.0.0')

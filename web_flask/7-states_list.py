#!/usr/bin/python3
"""getting and rendering data from storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def render_state_obj():
    """render html list"""
    # if os.getenv("HBNB_TYPE_STORAGE") == "db":
    list_of_states = storage.all(State)
    print(list_of_states)

    return render_template('7-states_list.html', obj=obj)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
"""web Flask app"""
from flask import Flask
from flask import abort, render_template
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def get_hbnb_filters():
    ''' Gets states and amenities form DB
    then renders the template
    '''
    states = [v for k, v in storage.all("State").items()]
    states = sorted(states, key=lambda s: s.name)
    amenity = [v for k, v in storage.all("Amenity").items()]
    amenity = sorted(amenity, key=lambda a: a.name)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenity
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')

#!/usr/bin/python3
"""a web flask app"""
from flask import Flask
from flask import abort, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def get_state(id=None):
    '''Gets a state is id is provided then renders a template'''
    states_db = storage.all('State')
    states = {'size': 0, 'states': list()}
    if id:
        key = 'State.{}'.format(id)
        if key in states_db:
            states['states'].append(states_db.get(key))
            states['size'] = 1
        else:
            states = None
    else:
        for key, state in states_db.items():
            states['size'] += 1
            states['states'].append({
                'id': state.id,
                'name': state.name,
            })
            states['states'] = sorted(
                states['states'], key=lambda s: s['name'])
    return render_template("9-states.html", item=states)


@app.teardown_appcontext
def teardown_storage(self):
    '''Closes or Teardown storage'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')

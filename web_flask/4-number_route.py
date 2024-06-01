#!/usr/bin/python3
"""a Flask web application."""
# python script to add route '/hbnb' that returns HBNB
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''return a string'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    ''' return string for route /hbnb
    '''
    return 'HBNB'


@app.route('/c/<text>')
def c_said(text):
    '''retuns a string with "C <text>"'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    '''retuns a string with "python <text>"'''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_int_number(n):
    '''checks if n is a int number'''
    try:
        string = "{} is a number".format(int(n))
        return string
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

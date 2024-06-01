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
    '''retuns a string with "C <text>"
    '''
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

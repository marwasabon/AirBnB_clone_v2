#!/usr/bin/python3
"""a Flask web application."""
# python script to add route '/hbnb' that returns HBNB
from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_is_number(n):
    '''checks if n is a int number'''
    try:
        num = int(n)
        return render_template('5-number.html', n=num)
    except Exception:
        abort(404)


@app.route('/number_odd_or_even/<int:n>')
def render_number_odd_even(n):
    '''checks if n is a int number
    then render a template that check if the number is odd or even
    '''
    try:
        num = {
            'n': int(n),
            'parity': '{}'.format('even' if int(n) % 2 == 0 else 'odd')
        }
        return render_template('6-number_odd_or_even.html', n=num)
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

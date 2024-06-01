#!/usr/bin/python3
"""a Flask web application"""
# Python script run a flask server with a route to return hello
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' return string'''
    return "Hello HBNB!"


if __name__ == "__main__":
    ''' return app'''
    app.run(host='0.0.0.0')
# app.run(host='0.0.0.0', port=5000)

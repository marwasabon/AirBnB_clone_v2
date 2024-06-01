#!/usr/bin/python3
# Python script run a flask server with a route to return hello
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    ''' return string'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    #app.run()


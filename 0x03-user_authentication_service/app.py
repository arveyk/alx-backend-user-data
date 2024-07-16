#!/usr/bin/env python3
"""
App module
"""
from flask import Flask

app = Flask(__name__)

@app(route='/')
def methods=['GET']:
    return flask.jasonify()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
"""
App module
"""
import requests
from auth import Auth
from flask import Flask, jsonify

AUTH = AUTH()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    msg = {"message": "Bienvenue"}
    return jsonify(msg)

@app.route('/users', methods['POST'])
def users(requests):
    """Registers users
    """
    # search for user
    data = {"email" email, "password": password}
    if user does not exist
    return jsonify({"message": "email already registered"}), 400



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
"""
App module
"""
import requests
from auth import Auth
from flask import Flask, jsonify, request, redirect

AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users/', methods=['POST'], strict_slashes=False)
def users():
    """Registers users
    Args: none
    Returns: 200 if ok 400 if user is not existent
    """
    # search for user
    # if user does not exist
    try:
        user = AUTH.register_user(request.form.get("email"),
                                  request.form.get("password"))
        email = user.email
        return jsonify({"email": email, "message": "user created"})
    except ValueError as VE:
        print(VE)
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions/', methods=["POST"], strict_slashes=False)
def login():
    """Function to login
    Args: None
    Returns:
    """
    email = request.form.get("email")
    is_user = AUTH.valid_login(email, request.form.get("password"))
    if is_user is False:
        flask.abort(401)
    cookie = AUTH.create_session(email)
    response.set_cookie("session_id", cookie)
    return jsonify({"email": email, "message": "logged in"})


@app.route('/sessions/', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout funtion
    Args: No args
    Returns: respose
    """
    session_id = request.form.get("session_id")
    user = Auth.get_user_from_session_id(session_id)
    if user is None:
        return 403
    Auth.destroy_session(user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

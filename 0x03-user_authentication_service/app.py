#!/usr/bin/env python3
"""
App module
"""
import requests
from auth import Auth
from flask import Flask, jsonify, request, redirect, abort

AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users/', methods=['POST'], strict_slashes=False)
def users() -> str:
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
def login() -> str:
    """Function to login
    Args: None
    Returns:
    """
    email = request.form.get("email")
    is_user = AUTH.valid_login(email, request.form.get("password"))
    if is_user is False:
        abort(401)
    try:
        session_id = AUTH.create_session(email)
        response.set_cookie("session_id", session_id)
        return jsonify({"email": email, "message": "logged in"})
    except ValueError:
        abort(401)


@app.route('/sessions/', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logout funtion
    Args: No args
    Returns: respose
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        return 403
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile/', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """Get user profile
    Args:
        request
    Returns: user profile
    """
    cookie = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(cookie)
    if user is None:
        return 403
    return 200, jsonify({"email": user.email})


@app.route('/reset_password/', methods=['POST'], strict_slashes=False )
def get_reset_password_token() -> str:
    """Get a reset password token
    Args:
        requests
    Returns: response
    """
    email = request.form.get("email")
    user_cred = {"email": email}
    try:
        user = AUTH._db.find_user_by(**user_cred)
        token = AUTH.get_reset_password_token(email)        
        return jsonify({"email": email, "reset_token": token})
    except NoResultFound:
        return 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

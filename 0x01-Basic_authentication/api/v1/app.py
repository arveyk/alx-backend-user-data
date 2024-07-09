#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

# auth = os.environ.get('AUTH_TYPE')
auth = getenv('AUTH_TYPE')
if auth:
    if auth == 'basic_auth':
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()
    else:
        from api.v1.auth.auth import Auth
        auth = Auth()

    @app.before_request
    def handle():
        """Auth list check
        Args:
            request
        Return: None or req
        """
        auth_list = [
                '/api/v1/status/',
                '/api/v1/unauthorized/',
                '/api/v1/forbidden/'
                ]
        result = auth.require_auth(request.path, auth_list)
        if result:
            result = auth.authorization_header(request)
            if result is None:
                abort(401)
            result = auth.current_user(request)
            if result is None:
                abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    Args:
        error: error msg
    Returns: error msg jsonified
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized access handler
    Args:
        error: error msg
    Returns: 401 error msg
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden access handler
    Args:
        error: error msg
    Returns: 403 error msg
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

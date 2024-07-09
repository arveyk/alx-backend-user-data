#!/usr/bin/env python3
"""Authentication module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar, List


class BasicAuth(Auth):
    """Basic Auth class
    """
    pass

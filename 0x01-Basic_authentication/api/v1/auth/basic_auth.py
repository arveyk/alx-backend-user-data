#!/usr/bin/env python3
"""Authentication module
"""
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    """Basic Auth class
    """
    pass

#!/usr/bin/env python3
"""Authentication module
"""
from flask import request
from typing import TypeVar, List
Auth = __import__('auth').Auth


class BasicAuth(Auth):
    """Basic Auth class
    """
    pass

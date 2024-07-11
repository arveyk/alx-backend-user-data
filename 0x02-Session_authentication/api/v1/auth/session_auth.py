#!/usr/bin/env python3
"""Session Authentication
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authentication class
    """
    def __init__(self):
        """Initialize class
        """
        super().__init__()

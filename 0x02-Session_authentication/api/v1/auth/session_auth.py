#!/usr/bin/env python3
"""Session Authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Authentication class
    """
    user_id_by_session_id = {}

    def __init__(self):
        """Initialize class
        Args: None
        Returns: No return value
        """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """Creates  a session ID for user_id
        Args:
            user_id: id to use to create session
        Returns: None if user_id is None, otherwise session id
        """
        if user_id is None:
            return None
        if isinstance(user_id, str) is False:
            return None
        sess_id = str(uuid.uuid4())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id

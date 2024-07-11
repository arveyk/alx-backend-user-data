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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a user Id based on session id
        Args:
            session_id: key to use to search for session id
        Returns: user_id
        """
        if session_id is None:
            return None
        if isinstance(session_id, str) is False:
            return None
        return self.user_id_by_session_id.get(session_id)

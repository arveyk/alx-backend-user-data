#!/usr/bin/env python3
"""Session Authentication
"""
from api.v1.auth.auth import Auth
import os
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

    def session_cookie(self, request=None):
        """Returns a cookie value for a request
        Args:
            requests: Http request
        Returns: cookie value"""
        if request is None:
            return None
        ssn_name = os.getenv('SESSION_NAME')
        return request._my_session_id

    def current_user(self, request=None):
        """Return a user based on cookie value
        Args:
            request: resource to be retrived
        Returns: None
        """
        self.session_cookie(request)

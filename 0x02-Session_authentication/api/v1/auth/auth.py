#!/usr/bin/env python3
"""Authentication module
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """Class for authentication of user details
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a user requires authentication
        Args:
            path: the path to resource(?)
            excluded_path: path to special files
        Returns: True if authentication is required to access
        """
        last_char = '/'
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path not in excluded_paths:
            if path[-1] == '*':
                for elem in excluded_paths:
                    if elem.startswith(path):
                        return False
            if path[-1] != last_char:
                path += last_char
                if path in excluded_paths:
                    return False
            return True

        status = "/api/v1/status"
        status2 = status + '/'
        if status in excluded_paths or status in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        """ Return authentication header
        Args:
            request: a http request
        Return: None
        """
        if request is None:
            return None
        # if request.get("Authentication"):
        #    return None
        # return request.get("Authentication")
        return request.headers

    def current_user(self, request=None) -> TypeVar('User'):
        """Check the current user
        Args:
            request: the requested resources
        Returns: the current user's name
        """
        return None

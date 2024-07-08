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
        return False

    def authorization_header(self, request=None) -> str:
        """ Return authentication header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Check the current user
        Args:
            request: the requested resources
        Returns: the current user's name
        """
        return None

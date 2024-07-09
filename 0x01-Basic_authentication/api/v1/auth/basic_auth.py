#!/usr/bin/env python3
"""Authentication module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import TypeVar, List


class BasicAuth(Auth):
    """Basic Auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:

        """extraction of auth or something
        Args:
            authrization_header: header to use
        Returns: authorozation header or None"""
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        if len(authorization_header) >= 7:
            Basic = authorization_header[:6]

            if Basic == 'Basic ':
                return authorization_header[6:]
            return None
        return None

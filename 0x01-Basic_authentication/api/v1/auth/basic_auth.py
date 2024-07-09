#!/usr/bin/env python3
"""Authentication module
"""
from api.v1.auth.auth import Auth
import base64
from flask import request
from typing import TypeVar, List


class BasicAuth(Auth):
    """Basic Auth class
    """

    def __init__(self):
        """Initialize"""
        super().__init__()

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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decode using base64
        Args:
            base64-authorization_header: as the name suggests
        Returns: decode msg
        """
        result = None
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            result = bytes(base64_authorization_header, 'ascii')
            result = base64.b64decode(result)
            return result.decode('utf-8')
        except Exception as e:
            return None

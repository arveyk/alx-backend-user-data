#!/usr/bin/env python3
"""Authentication module
"""
from api.v1.auth.auth import Auth
import base64
from flask import request
from models.user import User
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

    def extract_user_credentials(self,
                                 decode_base64_authorization_header: str)\
            -> (str, str):
        """ Extracts users info
        Args:
            decode_base64_authorization
        Returns: email and user password"""
        if decode_base64_authorization_header is None:
            return (None, None)
        if isinstance(decode_base64_authorization_header, str) is False:
            return (None, None)
        if ':' not in decode_base64_authorization_header:
            return (None, None)

        user_cred = decode_base64_authorization_header.split(':')
        cred_len = len(user_cred)
        if cred_len > 1:
            if cred_len > 2:
                with_colon = ''

                for i in range(1, cred_len):
                    with_colon += user_cred[i]
                    if i < cred_len - 1:
                        with_colon += ':'
                return (user_cred[0], with_colon)
            return (user_cred[0], user_cred[1])

    def user_object_from_credentials(self, user_email: str, user_pwd: str)\
            -> TypeVar('User'):
        """Creates a user object from credentials obtained
            Args:
                user_email: email address
                user_pwd: user password
            Returns: User instance
        """
        if user_email is None or user_pwd is None:
            return None
        if isinstance(user_email, str) is False or\
                isinstance(user_pwd, str) is False:
            return None
        user = User()
        if user.count() == 0:
            new_user = User(user_email, user_pwd)
            return None

        user_s = User.search({'email': user_email})
        if len(user_s) == 0:
            return None
        user_obj = user_s[0]
        if user_obj.is_valid_password(user_pwd) is False:
            return None
        return user_obj

        # if user_s.is_valid_password(user_pwd):
        #    if user_s.password != user_pwd:
        #        return None
        #    return user_s

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve current user
        Args:
            request: request object or somethin
        Returns: Current User
        """
        header = self.authorization_header(request)
        base_hdr = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(base_hdr)
        user_cred = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(user_cred[0], user_cred[1])

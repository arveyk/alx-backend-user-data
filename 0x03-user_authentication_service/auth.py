#!/usr/bin/env python3
"""Auth Module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar


def _hash_password(password: str) -> bytes:
    """function to Hash a password
    Args:
        password: users password string to be hashed
    Returns: hashed password
    """
    hpasswd = bytes(password.encode('utf-8'))
    hpasswd = bcrypt.hashpw(hpasswd, bcrypt.gensalt())
    return hpasswd


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        """Initialize instances of Auth
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """Registers a user into the database
        Args:
            email: users email
            password: users password
        Returns: User object
        """
        # if user already exists
        # raise ValueError("User email already exists")
        # else:
        #    hpwd = _hash_password(password)
        try:
            kwarg = {"email": email}
            user = self._db.find_user_by(**kwarg)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hpwd = _hash_password(password)
            user = self._db.add_user(email, hpwd)
            return user

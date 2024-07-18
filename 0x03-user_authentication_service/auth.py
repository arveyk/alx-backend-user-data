#!/usr/bin/env python3
"""Auth Module
"""
import bcrypt
import uuid
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar, ByteString, Union
from user import User


def _hash_password(password: str) -> ByteString:
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

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a login
        Args:
            email: user email
            password: login password
        Returns: True if valid, False if invalid login
        """
        # user = self._db._session.query(User).filter(
        #                                        User.email == email).first()
        try:
            user_cred = {"email": email}
            user = self._db.find_user_by(**user_cred)
            passwd_byt = bytes(password.encode('utf-8'))
            is_valid_pwd = bcrypt.checkpw(passwd_byt, user.hashed_password)

            if is_valid_pwd:
                return True
            return False

        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """ Generates a uuid
        Args: No arguments
        Returns: uuid
        """
        return str(uuid.uuid4())

    def create_session(self, email: str) -> Union[str, None]:
        """ Creates a session id
        Args:
            email: user email
        Returns: session id
        """
        try:
            user_cred = {"email": email}
            user = self._db.find_user_by(**user_cred)
            session_id = self._generate_uuid()
            user.session_id = session_id
            self._db._session.commit()
            self._db._session.close()
            return session_id
        except NoResultFound:
            return None

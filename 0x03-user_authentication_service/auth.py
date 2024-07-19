#!/usr/bin/env python3
"""Auth Module
"""
import bcrypt
import uuid
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User


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

    def register_user(self, email: str, password: str) -> User:
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
        try:
            user_cred = {"email": email}
            user = self._db.find_user_by(**user_cred)
            passwd_byt = bytes(password.encode('utf-8'))
            is_valid_pwd = bcrypt.checkpw(passwd_byt, user.hashed_password)

            if is_valid_pwd is True:
                return True
            return False

        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """ Generates a uuid
        Args: No arguments
        Returns: uuid
        """
        return str(uuid.uuid1())

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

            sess_cred = {"session_id": session_id}
            self._db.update_user(user.id, **sess_cred)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Gets a user by the session id given
        Args:
            session_id: user's session id
        Returns: the user object
        """
        if session_id is None:
            return None
        user_cred = {"session_id": session_id}
        try:
            user = self._db.find_user_by(**user_cred)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a session
        """
        if user_id is None:
            return None
        user_cred = {"id": user_id}
        user = self._db.find_user_by(**user_cred)
        sess_cred = {"session_id": None}

        self.update_user(user_id, **sess_cred)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Gets a reset password token
        Args:
            email: user email
        Returns: reset token
        """
        user_cred = {"email": email}
        try:
            user = self._db.find_user_by(**user_cred)
            token = self._generate_uuid()
            token_cred = {"reset_token": token_cred}
            self._db.update_user(user.id, **token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates user password
        Args:
            reset_token: string to check if reset should be done
            password: old password
        Returns: None
        """
        try:

            token_cred = {"reset_token": reset_token}
            user = self._db.find_user_by(**token_cred)
            hpass = _hash_password(password)

            token_res = {"reset_token": None}
            pass_cred = {"hashed_password": hpass}
            self._db.update_user(user.id, **pass_cred)
            self._db.update_user(user.id, **token_res)
            return None
        except NoResultFound:
            raise ValueError

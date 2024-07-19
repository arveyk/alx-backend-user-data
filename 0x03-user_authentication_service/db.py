#!/usr/bin/env python3
"""DB Module
"""
from typing import TypeVar, Any, Dict
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """ Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a user to database
        Args:
            email: user email
            hashed_password: users hashed password
        Returns: User object"""
        person = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(person)
        session.commit()
        return person

    def find_user_by(self, **kwarg: Dict[str, Any]) -> TypeVar('User'):
        """Find user in database
        Args:
            kwargs: keyword arguments
        Returns: first row found in users"""
        try:
            result = ""
            key = list(kwarg.keys())
            value = list(kwarg.values())
            rows = self._session.query(User).all()

            param_list = ["id", "email", "hashed_password", "session_id"
                          "reset_token"
                          ]
            if key[0] not in param_list:
                raise(InvalidRequestError)
            if key[0] == param_list[0]:
                row = self._session.query(User).filter_by(
                        id=value[0]).one()
                return row
            elif key[0] == param_list[1]:
                row = self._session.query(User).filter_by(
                         email=value[0]).one()
                return row
            elif key[0] == param_list[2]:
                row = self._session.query(User).filter(
                        hashed_password=value[0]).one()
                return row
            elif key[0] == param_list[3]:
                row = self._session.query(User).filter(
                        session_id=value[0]).one()
                return row
            elif key[0] == param_list[4]:
                row = self._session.query(User).filter(
                        reset_token=value[0]).one()
                return row

        except NoResultFound as err:
            raise(err)
        except InvalidRequestError as invalid:
            raise(invalid)

    def update_user(self, user_id: int, **kwargs: Dict[str, Any]) -> None:
        """Updates user
        Args:
        Returns:
        """
        # rows = self._session.query(User).filter(User.id = user_id).one()

        arg_find = {"id": user_id}
        user = self.find_user_by(**arg_find)
        update_val = list(kwargs.values())
        update_key = list(kwargs.keys())
        param_list = ["id", "email", "hashed_password", "session_id"
                      "reset_token"
                      ]
        if update_key[0] not in param_list:
            raise ValueError
        setattr(user, update_key[0], update_val[0])

        self._session.commit()
        self._session.close()

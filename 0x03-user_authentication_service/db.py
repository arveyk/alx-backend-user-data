#!/usr/bin/env python3
"""DB Module
"""
from typing import TypeVar
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

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
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

    def find_user_by(self, **kwarg):
        """Find user in database
        Args:
            kwargs: keyword arguments
        Returns: first row found in users"""
        try:
            result = ""
            key1 = list(kwarg.values())
            result = self.__session.query(User).filter(
                    User.email == key1[0]).one()
            return result
        except NoResultFound as err:
            raise(err)
        except InvalidRequestError as invalid:
            raise(invalid)
        # query and filter by input argument
        # NoResultFound
        # InvalidRequestError

    def update_user(user_id: int, **kwargs) -> None:
        """Updates user
        Args:
        Returns:
        """
        try:
            user = self.find_user_by(user_id)
            self.session
        except Exception as e:
            raise(e)
        # update user
        # commit changes
        # if value not found in user:
        #    raise ValueError
        pass

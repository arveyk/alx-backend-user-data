#!/usr/bin/env python3
"""User Module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User class for declaring a database table
    Rows:
        id: primary key of table
        email: user string email
        hashed_password: user hashed password
        session_id: string to be used every time the user is logged-in
        reset_token: token to reset password
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

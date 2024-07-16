#!/usr/bin/env python3
""" Main file 5
"""
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfullt created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfullt created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

#!/usr/bin/env python3
"""Auth Module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """function to Hash a password
    Args:
        password: users password string to be hashed
    Returns: hashed password
    """
    hpasswd = bytes(password.encode('utf-8'))
    hpasswd = bcrypt.hashpw(hpasswd, bcrypt.gensalt())
    return hpasswd

#!/usr/bin/env python3
"""Encrypt password
"""
import bcrypt


def hash_password(password: str):
    """
    create a hash for a paswd
    Args:
        password: the password to hash
    Returns: hashed btyes of the password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a password is valid
    Args:
        hashed_password: hashed version of the password to compare
        password: password to check
    Returns: True if password is valid, False if not
    """
    if bcrypt.checkpw(password.encode('utf-8'),
                      hashed_password.decode('utf-8').encode()):
        return True
    return False

#!/usr/bin/env python3
""" 3-main
"""
from api.v1.auth.auth import Auth


a = Auth()

print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.authorization_header())
print(a.current_user())

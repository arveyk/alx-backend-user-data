#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.auth import Auth

    a = Auth()
    """path = "/api/v1/users"
    paths_excluded = ["/api/v1/us*"]
    res = a.require_auth(path, paths_excluded)
    if res:
        print("require_auth must return True: {} - {}".format(path, paths_excluded))
        exit(1)
    print("OK", end="")
    """

    path = "/api/v1/uas"
    paths_excluded = ["/api/v1/us*"]
    res = a.require_auth(path, paths_excluded)
    if not res:
        print("require_auth must return False: {} - {}".format(path, paths_excluded))
        exit(1)
    print("OK", end="")


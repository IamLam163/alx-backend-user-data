#!/usr/bin/env python3
"""
BasicAuth that inherits from Auth
"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class inherits from auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns Base64 part of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

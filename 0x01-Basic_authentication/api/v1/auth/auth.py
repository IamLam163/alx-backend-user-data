#!/usr/bin/env python3
"""create Auth class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        # return False
        if path is None or excluded_paths is None:
            return True
        """
        for exc_path in excluded_paths:
            if path.startswith(exc_path):
                if exc_path.endswith('/'):
                    return False
                elif path[len(exc_path)] == '/':
                    return False"""
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None

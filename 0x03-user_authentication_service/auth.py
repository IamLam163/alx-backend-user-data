#!/usr/bin/env python3
"""
Hashing passwords with bcrypt
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashing passwords with bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

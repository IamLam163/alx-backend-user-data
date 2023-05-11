#!/usr/bin/env python3
"""
Hashing passwords with bcrypt
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB, User
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Hashing passwords with bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """function generates a uuid"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method registers user"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """checks is password matches the hashed password"""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                validate_pw = bcrypt.checkpw(password.encode("utf-8"),
                                             user.hashed_password)
                return validate_pw
        except NoResultFound:
            return False    # if hashed password dies not match
        return False

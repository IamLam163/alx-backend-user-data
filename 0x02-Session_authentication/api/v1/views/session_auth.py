#!/usr/bin/env python3
"""
New route to handle session authentication
"""
from os import abort, getenv
from typing import Tuple
from flask import jsonify, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """retrieves user instance"""
    email = request.form.get('email')
    if email is None or len(email) == 0:
        return jsonify({'error': 'email missing'}), 400
    password = request.form.get('password')
    if password is None or len(password) == 0:
        return jsonify({'error': 'password missing'}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404
    if len(users) == 0:
        return jsonify({'error': 'no user found for this email'}), 404
    if users[0].is_valid_password(password):
        from api.v1.app import auth
        session_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(getenv("SESSION_NAME"), session_id)
        return res
    return jsonify({'error': 'wrong password'}), 401


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> Tuple[str, int]:
    """destroy a session on logout"""
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return jsonify({})

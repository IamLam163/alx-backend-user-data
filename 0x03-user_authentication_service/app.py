#!/usr/bin/env python3
"""
Basic Flask APP
"""
from flask import Flask, abort, jsonify, request
from auth import Auth

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """returns a string with a message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def create_user() -> str:
    """users function that implements the POST /users route."""
    email, password = (request.form.get(key) for key in ["email", "password"])
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """login function enables a user to login"""
    email, password = (request.form.get(key) for key in ["email", "password"])
    if not AUTH.valid_login(email, password):
        abort(401)
    gen_session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", gen_session_id)
    return res  # res -> response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

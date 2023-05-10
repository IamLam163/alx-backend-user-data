#!/usr/bin/env python3
"""
Basic Flask APP
"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

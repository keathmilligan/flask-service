"""
Flask Service Template
"""

import os.path
from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    """
    Create Flask app
    """
    app = Flask(__name__)
    public_key = open(
        os.path.join(app.root_path, "..", "app.key.pub"), "r", encoding="utf-8"
    ).read()
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_ALGORITHM"] = "RS256"
    app.config["JWT_DECODE_ALGORITHMS"] = ["RS256"]
    app.config["JWT_PUBLIC_KEY"] = public_key

    # setup authentication
    JWTManager(app)

    # register blueprints
    # pylint: disable=import-outside-toplevel
    from . import todo

    app.register_blueprint(todo.blueprint)

    return app

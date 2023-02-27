from flask import Flask
from os import environ


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("SECRET_KEY", "sqlite:///project.db")


def get_environ(var_name: str, default_value=None):
    var_value = environ.get("JWT_KEY", default_value)
    if var_value is None:
        raise Exception(f"{var_name} environment variable not configured")
    return var_value


class Config:

    JWT_KEY = get_environ("JWT_KEY")
    ACCESS_TOKEN_MINUTES_DURATION = 5  # TODO: Change
    REFRESH_TOKEN_MINUTES_DURATION = 10  # TODO: Change

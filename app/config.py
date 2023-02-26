from flask import Flask


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

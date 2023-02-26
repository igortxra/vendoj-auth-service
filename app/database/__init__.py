from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def init_app(app: Flask):

    db.init_app(app)

    # Import models that have to be in migrations
    from app.repositories import UserDTO

    migrate.init_app(app, db)

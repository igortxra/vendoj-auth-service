from flask import Flask
from . import config
from .controllers import auth
from . import database


def create_app() -> Flask:

    app = Flask(__name__)

    # Load configurations
    config.init_app(app)

    # Blueprints
    auth.init_app(app)

    # Database
    database.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

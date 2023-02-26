from flask import Blueprint, Flask
from flask import request

import logging

from app.models import InvalidUserOrPasswordException
from app.usecases import Usecases


bp_auth = Blueprint("auth", __name__)


@bp_auth.route('/login', methods=["POST"])
def login():
    request_body = request.get_json()

    email = request_body.get("email")
    password = request_body.get("password")

    try:
        usecase_login = Usecases.login()
        access_token, refresh_token = usecase_login.run(email, password)
        return {"access_token": access_token, "refresh_token": refresh_token}

    except InvalidUserOrPasswordException as ex:
        return {"message": ex.get_message()}, 401

    except Exception as ex:
        logging.error(ex)
        return {}, 500


def init_app(app: Flask):
    app.register_blueprint(bp_auth)

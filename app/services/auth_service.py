import datetime

import jwt
from app.config import Config

from app.interfaces import IAuthService
from app.models.user import User


class AuthService(IAuthService):

    def generate_access_token(self, user: User):
        claims = {
            "sub": user.id,
            "refresh": False,
            "exp": self._generate_expiration_claim(Config.REFRESH_TOKEN_MINUTES_DURATION)}

        return jwt.encode(claims, Config.JWT_KEY, algorithm="HS256")

    def generate_refresh_token(self, user: User):
        claims = {
            "sub": user.id,
            "refresh": True,
            "exp": self._generate_expiration_claim(Config.REFRESH_TOKEN_MINUTES_DURATION)}

        return jwt.encode(claims, Config.JWT_KEY, algorithm="HS256")

    def _generate_expiration_claim(self, minutes_to_expire: int) -> int:

        now = datetime.datetime.utcnow()
        timedelta_token = datetime.timedelta(minutes_to_expire)

        return int((now + timedelta_token).timestamp())

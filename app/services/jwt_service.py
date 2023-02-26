from typing import Dict

import jwt

from app.interfaces import IJWTService


class JWTService(IJWTService):

    def generate_token(self, claims: Dict):
        return jwt.encode(claims, "SECRET_KEY", algorithm="HS256")  # ENV VAR

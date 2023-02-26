from app.repositories import UserRepository
from app.services import JWTService, CryptService

from .login import UCLogin


class Usecases:

    @staticmethod
    def login() -> UCLogin:
        return UCLogin(
            user_repository=UserRepository(),
            crypt_service=CryptService(),
            jwt_service=JWTService()
        )

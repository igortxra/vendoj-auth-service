from typing import Tuple

from app.interfaces import ICryptService, IUserRepository, IJWTService
from app.models.errors import InvalidUserOrPasswordException


class UCLogin:

    def __init__(
        self,
        user_repository: IUserRepository,
        crypt_service: ICryptService,
        jwt_service: IJWTService
    ) -> None:
        self.user_repository = user_repository
        self.crypt_service = crypt_service
        self.jwt_service = jwt_service

    def run(self, email: str, password: str) -> Tuple[str, str]:
        user = self.user_repository.get_user_by_email(email)
        if (
            user is None
            or self.crypt_service.check_password(password, user.password) is False
        ):
            raise InvalidUserOrPasswordException

        claims_access_token = {
            "sub": user.id,
            # "exp": value
        }

        claims_refresh_token = {
            "sub": user.id,
            # "exp": value,
            "refresh": True
        }

        access_token = self.jwt_service.generate_token(claims_access_token)
        refresh_token = self.jwt_service.generate_token(claims_refresh_token)

        return (access_token, refresh_token)

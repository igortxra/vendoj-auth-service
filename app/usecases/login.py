from typing import Tuple
from app.interfaces import ICryptService, IUserRepository, IAuthService
from app.models.errors import InvalidUserOrPasswordException


class UCLogin:

    def __init__(
        self,
        user_repository: IUserRepository,
        crypt_service: ICryptService,
        auth_service: IAuthService
    ) -> None:
        self.user_repository = user_repository
        self.crypt_service = crypt_service
        self.auth_service = auth_service

    def run(self, email: str, password: str) -> Tuple[str, str]:
        user = self.user_repository.get_user_by_email(email)
        if user is None or not self.crypt_service.check_password(password, user.password):
            raise InvalidUserOrPasswordException

        access_token = self.auth_service.generate_access_token(user)
        refresh_token = self.auth_service.generate_refresh_token(user)

        return access_token, refresh_token

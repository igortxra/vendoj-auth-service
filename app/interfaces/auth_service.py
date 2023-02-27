from abc import abstractmethod

from app.models.user import User


class IAuthService:

    @abstractmethod
    def generate_access_token(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def generate_refresh_token(self, user: User):
        raise NotImplementedError

from abc import abstractmethod
from app.models import User


class IUserRepository:

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        raise NotImplementedError

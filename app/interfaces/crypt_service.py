from abc import abstractmethod


class ICryptService:

    @abstractmethod
    def check_password(self, plain_password: str, hashed_password: str) -> bool:
        raise NotImplementedError

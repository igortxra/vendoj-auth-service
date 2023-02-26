from abc import abstractmethod
from typing import Dict


class IJWTService:

    @abstractmethod
    def generate_token(self, claims: Dict):
        raise NotImplementedError

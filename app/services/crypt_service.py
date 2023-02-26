from app.interfaces.crypt_service import ICryptService
import bcrypt


class CryptService(ICryptService):

    def check_password(self, plain_password: str, hashed_password: str):
        return bcrypt.checkpw(
            plain_password.encode(),
            hashed_password.encode())

from app.interfaces.user_repository import IUserRepository
from app.models import User
from app.database import db


class UserDTO(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def to_user(self) -> User:
        return User(
            id=self.id,
            email=self.email,
            password=self.password)


class UserRepository(IUserRepository):

    def get_user_by_email(self, email: str) -> User | None:
        user_dto = UserDTO.query.filter_by(email=email).one_or_none()
        if user_dto:
            return user_dto.to_user()

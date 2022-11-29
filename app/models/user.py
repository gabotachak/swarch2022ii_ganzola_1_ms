from sqlalchemy import Column, Integer, VARCHAR

from app.repositories.orm import Base


class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    first_name = Column(VARCHAR(45), nullable=True)
    last_name = Column(VARCHAR(45), nullable=True)
    username = Column(VARCHAR(45), nullable=False, unique=True)

    def __init__(
            self,
            id_user: int = None,
            first_name: str = None,
            last_name: str = None,
            username: str = None
    ):
        self.id_user = id_user
        self.first_name = first_name.title() if first_name else None
        self.last_name = last_name.title() if last_name else None
        self.username = username.lower() if username else None

    def to_dict(self):
        return {
            "id_user": self.id_user,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username
        }

    def __eq__(self, other):
        if not isinstance(other, User):
            return False

        return self.id_user == other.id_user

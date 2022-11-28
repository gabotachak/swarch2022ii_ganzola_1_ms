from sqlalchemy.orm import session

from app import models
from app.exceptions import UserNotFoundException


class UserController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def search_user(self, params: dict) -> models.User:
        user = self.db_session.query(models.User).filter_by(**params).first()
        if not user:
            raise UserNotFoundException(params)
        return user

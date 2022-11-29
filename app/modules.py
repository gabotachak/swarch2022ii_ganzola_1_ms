from app.controllers import UserController, TransactionController
from app.repositories.orm import db_session

user_controller = UserController(db_session)
transaction_controller = TransactionController(db_session)

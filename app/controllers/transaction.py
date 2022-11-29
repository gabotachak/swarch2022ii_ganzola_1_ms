from sqlalchemy.orm import session

from app import models
from app.exceptions import TransactionNotFoundException, UserNotFoundException


class TransactionController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def search_transactions(self, params: dict) -> list:
        if params.get("sender"):
            sender = {}
            if params["sender"].isnumeric():
                sender["id_user"] = params["sender"]
            else:
                sender["username"] = params["sender"]

            sender = self.db_session.query(models.User).filter_by(**sender).first()
            if not sender:
                raise UserNotFoundException(params["sender"])

            params["sender"] = sender.id_user

        if params.get("receiver"):
            receiver = {}
            if params["receiver"].isnumeric():
                receiver["id_user"] = params["receiver"]
            else:
                receiver["username"] = params["receiver"]

            receiver = self.db_session.query(models.User).filter_by(**receiver).first()
            if not receiver:
                raise UserNotFoundException(params["receiver"])

            params["receiver"] = receiver.id_user

        transactions = self.db_session.query(models.Transaction).filter_by(**params).all()
        if not transactions:
            raise TransactionNotFoundException(params)

        transactions_dict = []
        for transaction in transactions:
            transaction_dict = transaction.to_dict()

            sender = self.db_session.query(models.User).filter_by(id_user=transaction_dict["sender"]).first()
            transaction_dict["sender"] = sender.to_dict() if sender else None

            receiver = self.db_session.query(models.User).filter_by(id_user=transaction_dict["receiver"]).first()
            transaction_dict["receiver"] = receiver.to_dict() if receiver else None

            transactions_dict.append(transaction_dict)

        return transactions_dict

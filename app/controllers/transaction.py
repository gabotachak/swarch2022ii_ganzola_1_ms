from sqlalchemy import func
from sqlalchemy.orm import session

from app import models
from app.exceptions import TransactionNotFoundException, UserNotFoundException, InsufficientFundsException


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

        transactions_list = []
        for transaction in transactions:
            transaction_dict = transaction.to_dict()

            sender = self.db_session.query(models.User).filter_by(id_user=transaction_dict["sender"]).first()
            transaction_dict["sender"] = sender.to_dict() if sender else None

            receiver = self.db_session.query(models.User).filter_by(id_user=transaction_dict["receiver"]).first()
            transaction_dict["receiver"] = receiver.to_dict() if receiver else None

            transactions_list.append(transaction_dict)

        return sorted(transactions_list, key=lambda d: d['id_transaction'], reverse=True)

    def search_transactions_by_user(self, params: dict) -> dict:
        user = self.db_session.query(models.User).filter_by(**params).first()
        if not user:
            raise UserNotFoundException(params)

        tr_sender = self.db_session.query(models.Transaction).filter_by(sender=user.id_user).all()
        tr_receiver = self.db_session.query(models.Transaction).filter_by(receiver=user.id_user).all()

        transactions_list = []
        for transaction in tr_sender + tr_receiver:
            transaction_dict = transaction.to_dict()

            sender = self.db_session.query(models.User).filter_by(id_user=transaction_dict["sender"]).first()
            transaction_dict["sender"] = sender.to_dict() if sender else None

            receiver = self.db_session.query(models.User).filter_by(id_user=transaction_dict["receiver"]).first()
            transaction_dict["receiver"] = receiver.to_dict() if receiver else None

            transactions_list.append(transaction_dict)

        transactions_dict = {
            "transactions": sorted(transactions_list, key=lambda d: d['id_transaction'], reverse=True),
            "balance": float(sum([t.amount for t in tr_receiver] + [-t.amount for t in tr_sender]))
        }

        return transactions_dict

    def create_transaction(self, transaction: models.Transaction) -> dict:
        sender = {}
        if transaction.sender.isnumeric():
            sender["id_user"] = transaction.sender
        else:
            sender["username"] = transaction.sender
        sender = self.db_session.query(models.User).filter_by(**sender).first()
        if not sender:
            raise UserNotFoundException(transaction.sender)
        transaction.sender = sender.id_user

        receiver = {}
        if transaction.receiver.isnumeric():
            receiver["id_user"] = transaction.receiver
        else:
            receiver["username"] = transaction.receiver
        receiver = self.db_session.query(models.User).filter_by(**receiver).first()
        if not receiver:
            raise UserNotFoundException(transaction.receiver)
        transaction.receiver = receiver.id_user

        income = self.db_session.query(func.sum(models.Transaction.amount)).filter_by(receiver=sender.id_user).scalar()
        income = income if income else 0

        outcome = self.db_session.query(func.sum(models.Transaction.amount)).filter_by(sender=sender.id_user).scalar()
        outcome = outcome if outcome else 0

        balance = float(income - outcome)
        if balance < transaction.amount:
            raise InsufficientFundsException(sender.username)

        self.db_session.add(transaction)
        self.db_session.commit()

        return transaction.to_dict()

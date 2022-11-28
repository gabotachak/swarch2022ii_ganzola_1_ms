from datetime import datetime

from app.models.user import User


class Transaction:
    id_transaction: int
    sender: User
    receiver: User
    transaction_time: datetime

    def __init__(
            self,
            id_transaction: int = None,
            sender: User = None,
            receiver: User = None,
            transaction_time: datetime = None
    ):
        self.id_transaction = id_transaction
        self.sender = sender
        self.receiver = receiver
        self.transaction_time = transaction_time

    def to_dict(self):
        return {
            "id_transaction": self.id_transaction,
            "sender": self.sender.to_dict(),
            "receiver": self.receiver.to_dict(),
            "transaction_time": self.transaction_time
        }

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False

        return self.id_transaction == other.id_transaction

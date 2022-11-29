from datetime import datetime


class Transaction:
    id_transaction: int
    sender: str
    receiver: str
    amount: float
    transaction_time: datetime

    def __init__(
            self,
            id_transaction: int = None,
            sender: str = None,
            receiver: str = None,
            amount: float = None,
            transaction_time: datetime = None
    ):
        self.id_transaction = id_transaction
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transaction_time = transaction_time

    def to_dict(self):
        return {
            "id_transaction": self.id_transaction,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": float(self.amount) if self.amount else None,
            "transaction_time": self.transaction_time
        }

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False

        return self.id_transaction == other.id_transaction

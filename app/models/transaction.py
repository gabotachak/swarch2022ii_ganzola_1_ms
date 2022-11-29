from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime
from sqlalchemy.sql.functions import now

from app.repositories.orm import Base


class Transaction(Base):
    __tablename__ = 'transaction'

    id_transaction = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    sender = Column(ForeignKey("user.id_user"), nullable=True)
    receiver = Column(ForeignKey("user.id_user"), nullable=True)
    amount = Column(DECIMAL(10, 2), nullable=True)
    transaction_time = Column(DateTime(timezone=True), server_default=now())

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

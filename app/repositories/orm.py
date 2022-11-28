from sqlalchemy import MetaData, Table, VARCHAR, Column, ForeignKey, DateTime, INTEGER
from sqlalchemy.orm import mapper
from sqlalchemy.sql.functions import now

from app.models.transaction import Transaction
from app.models.user import User
from app.utils.log import logger

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id_user", INTEGER, primary_key=True, nullable=False, unique=True, autoincrement=True),
    Column("first_name", VARCHAR(45), nullable=True),
    Column("last_name", VARCHAR(45), nullable=True),
    Column("username", VARCHAR(20), nullable=False, unique=True),
)

transaction = Table(
    "transaction",
    metadata,
    Column("id_transaction", INTEGER, primary_key=True, nullable=False, unique=True, autoincrement=True),
    Column("sender", ForeignKey("user.id_user"), nullable=True),
    Column("receiver", ForeignKey("user.id_user"), nullable=True),
    Column("transaction_time", DateTime(timezone=True), server_default=now()),
)


def start_mappers():
    logger.info("================> Starting mappers")
    mapper(User, user)
    mapper(Transaction, transaction)

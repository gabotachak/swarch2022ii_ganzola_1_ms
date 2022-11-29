import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

db_host = os.getenv("DB_HOST", "")
db_port = os.getenv("DB_PORT", "")
db_schema = os.getenv("DB_SCHEMA", "")
db_user = os.getenv("DB_USER", "")
db_password = os.getenv("DB_PASSWORD", "")

uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_schema}"

engine = create_engine(uri, echo=True)

Session = sessionmaker(bind=engine)
db_session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)

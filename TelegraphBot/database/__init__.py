from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "postgres://nmjrboas:4UpeJ89pSZMw8dkK5T8XoFIZR50HxTw6@kashin.db.elephantsql.com/nmjrboas"

def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

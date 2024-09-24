# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclapativeBase
# from sqlalchemy import Column, Integer, String
#
# engine = create_engine("sqlite:///taskmanager.db", echo=True)  # создаём движок
#
# SessionLocal = sessionmaker(bind=engine)  # создаём сессию связи с нашей db
#
#
# class Base(DeclapativeBase):  # создаём класс будующей db
#     pass




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///taskmanager.db'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)

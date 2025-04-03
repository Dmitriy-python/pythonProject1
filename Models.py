import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from environs import Env

env=Env()
env.read_env()
db_path=env.str('database_path')
engine = create_engine(db_path)
SessionLocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)



base=declarative_base()




def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()





from sqlalchemy import Column, Integer, String

from Models import base


class Category(base):
    __tablename__="category"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False)

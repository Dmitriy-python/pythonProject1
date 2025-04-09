
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, false
from sqlalchemy.dialects.mysql import NUMERIC
from sqlalchemy.orm import relationship

from Models import base


class Category(base):
    __tablename__="category"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False)


    products_list = relationship('Product', back_populates='categories', uselist=True)



class Product(base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(50), nullable=False)
    price=Column(Integer, nullable=False, default=0)
    stock=Column(Integer, nullable=False, default=0)
    description = Column(String(255), nullable=False)
    img_url = Column(String(255), nullable=False)
    age_restriction=Column(Integer, default=0)
    category_id=Column(Integer, ForeignKey('category.id'))



    categories = relationship('Category', back_populates='products_list', uselist=False)



class Role(base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    users_list=relationship('User', back_populates='roles', uselist=True)



class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age=Column(Integer, nullable=False)
    tg_id = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    id_role=Column(Integer, ForeignKey('roles.id'), default=1)
    isdelete=Column(BOOLEAN, default=False)

    roles=relationship('Role', back_populates='users_list', uselist=False)

    # carts = relationship('Cart', backref='user', cascade='all, delete')
    # bonus_cards = relationship('Bonus', backref='user', cascade='all, delete')


class Cart(base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey('users.id'))
    isdelete = Column(BOOLEAN, default=False)



class Bonus(base):
    __tablename__ = "bonus_card"
    id = Column(Integer, primary_key=True, index=True)
    balance=Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    isdelete = Column(BOOLEAN, default=False)


class Size(base):
    __tablename__ = "sizes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    mult=Column(NUMERIC, nullable=False,default=1)





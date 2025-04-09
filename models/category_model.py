
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

    cart = relationship('Cart', back_populates='users', uselist=False)

    bonus_card = relationship('Bonus', back_populates='users', uselist=False)


class Cart(base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey('users.id'))
    isdelete = Column(BOOLEAN, default=False)


    users = relationship('User', back_populates='cart', uselist=False)



class Bonus(base):
    __tablename__ = "bonus_card"
    id = Column(Integer, primary_key=True, index=True)
    balance=Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    isdelete = Column(BOOLEAN, default=False)



    users=relationship('User', back_populates='bonus_card', uselist=False)




class Size(base):
    __tablename__ = "sizes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    mult=Column(NUMERIC, nullable=False,default=1)



class CartProduct(base):
    __tablename__ = "cart_products"
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('cart.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    size_id = Column(Integer, ForeignKey('sizes.id'))
    quantity = Column(Integer, default=1)

    cart = relationship('Cart', back_populates='cart_products')
    product = relationship('Product', back_populates='cart_products')
    size = relationship('Size', back_populates='cart_products')





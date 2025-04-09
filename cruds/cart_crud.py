import sqlalchemy
from environs import Env
from fastapi import Body
from unicodedata import category

from Models import SessionLocal
from models.category_model import Category, Product, User, Role, Cart, Bonus, CartProduct, Size, Cart_products_view
from schemas.product_schemas import ProductModel
from schemas.user_schemas import UserModel

def tuple_to_float(list: list[tuple]) -> list[float]:
    list_str = []
    for i in list:
        list_str.append(float(i[0]))
    return list_str



def all_p_in_one_cart(db:SessionLocal, user_id:int):
    user_cart=db.query(Cart).filter_by(user_id=user_id).first()

    rezult=(db.query(Product.name, Product.price, Size.name, CartProduct.quantity).join(CartProduct, CartProduct.product_id==Product.id)
            .filter_by(cart_id=user_cart.id).join(Size, CartProduct.size_id==Size.id).all())
    return rezult


def total_price(db:SessionLocal, user_id:int):
    user_cart = db.query(Cart).filter_by(user_id=user_id).first()
    total_sum=db.query(Cart_products_view.total_price).filter_by(cart_id=user_cart.id).all()
    converted=tuple_to_float(total_sum)
    return sum(converted)





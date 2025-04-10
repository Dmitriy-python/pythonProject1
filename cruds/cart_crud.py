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


def total_price(db:SessionLocal, user_id:int):
    user_cart = db.query(Cart).filter_by(user_id=user_id).first()
    total_sum=db.query(Cart_products_view.total_price).filter_by(cart_id=user_cart.id).all()
    converted=tuple_to_float(total_sum)
    return sum(converted)



def all_p_in_one_cart(db:SessionLocal, user_id:int):
    user_cart=db.query(Cart).filter_by(user_id=user_id).first()

    rezult=(db.query(Product.name, Product.price, Size.name, Cart_products_view.quantity, Cart_products_view.total_price).
            join(Cart_products_view, Cart_products_view.product_id==Product.id)
            .filter_by(cart_id=user_cart.id).
            join(Size, Cart_products_view.size_id==Size.id).all())
    items=[]
    for item in rezult:
        items.append({"product_name":item[0], "product_price":item[1], "size_name":item[2]
                      ,"quantity":item[3], "total_sum":int(item[4])})
    total_sum=total_price(db,user_id)
    items.append({"total_price":total_sum})
    return items










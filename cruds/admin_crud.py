from environs import Env
from fastapi import Body
from unicodedata import category

from Models import SessionLocal
from models.category_model import Category, Product, User, Role, Cart, Bonus
from schemas.product_schemas import ProductModel
from schemas.user_schemas import UserModel

env = Env()
env.read_env()
admin_id = env.str('ADMIN_ID')



def update_user_role(db:SessionLocal, phone_number, new_role_id):
    existing_user=db.query(User).filter_by(phone_number=phone_number).first()
    if existing_user is not None:
        existing_user.id_role=new_role_id
        db.commit()
        db.refresh(existing_user)
        return True
    else:
        return False



def create_new_role(db:SessionLocal, name):
    new_role=Role(name=name)
    db.add(new_role)
    db.commit()
    return True




def delete_existing_role(db:SessionLocal, name):
    role=db.query(Role).filter_by(name=name).first()
    db.delete(role)
    db.commit()
    return True


def get_all_roles(db:SessionLocal):
    roles=db.query(Role).all()
    return roles

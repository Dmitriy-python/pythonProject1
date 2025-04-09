from aiofiles.ospath import exists
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

def get_users(db:SessionLocal):
    return db.query(User).filter_by(isdelete=False).all()


def get_user_by_tg_id(db:SessionLocal, tg_id:str):
    user = db.query(User).filter_by(tg_id=tg_id).first()
    return user





def get_one_role_users(db:SessionLocal, role_id:int):
    role=db.query(Role).filter_by(id=role_id).first()
    db.commit()
    if role is None:
        return False
    else:
       return role.users_list



def get_admin_role_as_object(db:SessionLocal):
    return db.query(Role).filter_by(name='admin').first()



def give_user_bonus_card_and_cart(db:SessionLocal, user):
    new_cart=Cart(user_id=user.id)
    new_bonus_card=Bonus(user_id=user.id)
    db.add(new_cart)
    db.add(new_bonus_card)
    db.commit()



def add_user_to_db(db:SessionLocal, user=UserModel):
    if user.tg_id==admin_id:
        a=get_admin_role_as_object(db)
        new_user_admin=User(name=user.name, age=user.age, tg_id=user.tg_id,
                             phone_number=user.phone_number, id_role=a.id)
        a.users_list.append(new_user_admin)
        db.commit()
        give_user_bonus_card_and_cart(db,new_user_admin)
        db.commit()
    else:
        new_user = User(name=user.name, age=user.age, tg_id=user.tg_id,
                              phone_number=user.phone_number)
        db.add(new_user)
        db.commit()
        give_user_bonus_card_and_cart(db,new_user)
        db.commit()




def update_user_role(db:SessionLocal, phone_number, new_role_id):
    existing_user=db.query(User).filter_by(phone_number=phone_number).first()


    if existing_user is not None:
        existing_user.id_role=new_role_id
        db.commit()
        db.refresh(existing_user)
        return True
    else:
        return False





def make_on_delete(db:SessionLocal, user):
    cart=db.query(Cart).filter_by(user_id=user.id).first()
    bonus_card=db.query(Bonus).filter_by(user_id=user.id).first()
    cart.isdelete=True
    db.commit()
    db.refresh(cart)
    bonus_card.isdelete=True
    db.commit()
    db.refresh(bonus_card)



def delete_user(db:SessionLocal, user_phone:str):
    user_to_del=db.query(User).filter_by(phone_number=user_phone).first()
    if user_to_del is None:
        return False
    else:
        user_to_del.isdelete=True
        db.commit()
        db.refresh(user_to_del)
        make_on_delete(db, user_to_del)
        return True


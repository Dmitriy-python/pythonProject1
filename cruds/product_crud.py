from fastapi import Body
from unicodedata import category

from Models import SessionLocal
from models.category_model import Category,Product



def get_products(db:SessionLocal):
    return db.query(Product).all()



def get_one_category_products(db:SessionLocal, category_name:str):
    cat=db.query(Category).filter_by(name=category_name).first()
    db.commit()
    if cat is None:
        return False
    else:
       return cat.products_list



def add_product(db:SessionLocal, cat_name:str, data=Body()):
    cat1=db.query(Category).filter_by(name=cat_name).first()
    db.commit()
    new_product=Product(name=data['name'], price=data['price'], stock=data['stock'],
                        description=data['description'],img_url=data['img_url'],
                        age_restriction=data['age_restriction'])
    cat1.products_list.append(new_product)
    db.commit()
    db.close()




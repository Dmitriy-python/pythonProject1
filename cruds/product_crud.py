from fastapi import Body
from unicodedata import category

from Models import SessionLocal
from models.category_model import Category,Product
from schemas.product_schemas import ProductModel


def get_products(db:SessionLocal):
    return db.query(Product).all()



def get_one_category_products(db:SessionLocal, category_name:str):
    cat=db.query(Category).filter_by(name=category_name).first()
    db.commit()
    if cat is None:
        return False
    else:
       return cat.products_list



def add_product(db:SessionLocal, data:ProductModel):
    cat1=db.query(Category).filter_by(id=data.category_id).first()
    db.commit()
    new_product=Product(name=data.name, price=data.price, stock=data.stock,
                        description=data.description,img_url=data.img_url,
                        age_restriction=data.age_restriction, category_id=data.category_id)
    cat1.products_list.append(new_product)
    db.commit()


def get_product_by_name(db: SessionLocal, name: str):
    return db.query(Product).filter(Product.name==name).first()




def update_product1(db: SessionLocal, name:str, data:ProductModel):
    prod=get_product_by_name(db, name)
    if prod is None:
        return False
    else:
        prod.price=data.price
        prod.stock=data.stock
        db.commit()
        db.refresh(prod)
        return prod


def delete_product(db:SessionLocal, name:str):
    prod_to_del=db.query(Product).filter_by(name=name).first()
    if prod_to_del is None:
        return False
    else:
        db.delete(prod_to_del)
        db.commit()
        return True



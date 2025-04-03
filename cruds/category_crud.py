from fastapi import Body
from unicodedata import category

from Models import SessionLocal
from models.category_model import Category



def get_categories(db:SessionLocal):
    return db.query(Category).all()









def create_category2(db:SessionLocal, category_name:str):
    new_category=Category(name=category_name)
    db.add(new_category)
    db.commit()








def del_category(db:SessionLocal, category_name:str):
      cat =  db.query(Category).filter(Category.name==category_name).first()
      if cat is None:
          return False
      else:
          db.delete(cat)
          db.commit()
          return True



def update_category(db:SessionLocal, category_name:str, new_name):
      cat =  db.query(Category).filter(Category.name==category_name).first()
      if cat is None:
          return False
      else:
          cat.name=new_name
          db.commit()
          db.refresh(cat)
          return True





def get_cat_by_name(db:SessionLocal, name:str):
    category=db.query(Category).filter_by(name=name).first()
    if category is None:
        return False
    return category
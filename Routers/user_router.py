from importlib.metadata import requires
from typing import Optional

from environs import Env
from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends,  Path
from sqlalchemy.dialects.oracle.dictionary import all_users
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from fastapi import FastAPI, Body
from Models import SessionLocal, get_db
from cruds.category_crud import get_categories, create_category2, update_category, del_category
from cruds.product_crud import get_products, get_one_category_products, add_product, update_product1, delete_product, get_product_by_name
from cruds.user_crud import get_users, get_user_by_tg_id, get_one_role_users, add_user_to_db,  delete_user
from schemas.product_schemas import ProductModel
from schemas.user_schemas import UserModel




router=APIRouter(prefix='/api/users', tags=["users"])







@router.get("/")
def root(tg_id:Optional[str]=Query(None), db:SessionLocal=Depends(get_db)):
    if tg_id:
         user=get_user_by_tg_id(db, tg_id)
         if user is None:
             return JSONResponse(content={"message": "User not found"}, status_code=status.HTTP_404_NOT_FOUND)
         else:
             serialized_user = jsonable_encoder(user)
             return JSONResponse(content=serialized_user, status_code=status.HTTP_200_OK)
    return get_users(db)




@router.get("/{role_id}")
def one_role_users(role_id:int,db:SessionLocal=Depends(get_db)):
    selected_users=get_one_role_users(db, role_id)
    if selected_users is False:
        return JSONResponse(content={"message": "Users with entered role not found"}, status_code=status.HTTP_404_NOT_FOUND)
    else:
        serialized_users = jsonable_encoder(selected_users)
        return JSONResponse(content=serialized_users, status_code=status.HTTP_200_OK)



@router.post("/")
def add_user(user:UserModel, db:SessionLocal=Depends(get_db)):
        add_user_to_db(db,user)
        return JSONResponse(content={"message": "User added"}, status_code=status.HTTP_201_CREATED)





@router.delete("/{phone_number}")
def del_user(phone_number:str, db:SessionLocal=Depends(get_db)):
   if delete_user(db, phone_number):
       return  JSONResponse(content={"message": "User deleted"}, status_code=status.HTTP_200_OK)
   else:
       return JSONResponse(content={"message": "No user found"}, status_code=status.HTTP_404_NOT_FOUND)









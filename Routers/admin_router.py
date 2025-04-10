from importlib.metadata import requires
from typing import Optional
from environs import Env
from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends,  Path
from sqlalchemy.dialects.oracle.dictionary import all_users
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from fastapi import FastAPI, Body
from Models import SessionLocal, get_db
from cruds.admin_crud import update_user_role, create_new_role, delete_existing_role, get_all_roles
from cruds.category_crud import get_categories, create_category2, update_category, del_category
from cruds.product_crud import get_products, get_one_category_products, add_product, update_product1, delete_product, \
    get_product_by_name
from cruds.user_crud import get_users, get_user_by_tg_id, get_one_role_users, add_user_to_db
from schemas.product_schemas import ProductModel
from schemas.user_schemas import UserModel




router=APIRouter(prefix='/api/admin', tags=["admin_commands"])

@router.get('/roles')
def get_roles( db:SessionLocal=Depends(get_db)):
    all_roles=get_all_roles(db)
    if all_roles is None:
        return JSONResponse(content={"message": "No roles found"}, status_code=status.HTTP_404_NOT_FOUND)
    else:
        all_roles=jsonable_encoder(all_roles)
        return JSONResponse(content=all_roles, status_code=status.HTTP_404_NOT_FOUND)




@router.patch("/roles/update")
def change_role(phone_number:str=Body(embed=True), new_role_id:int=Body(embed=True), db:SessionLocal=Depends(get_db)):
    if update_user_role(db, phone_number, new_role_id):
        return JSONResponse(content={"message": "Role updated"}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "No user found"}, status_code=status.HTTP_404_NOT_FOUND)



@router.post('/roles/create')
def create_r(db:SessionLocal=Depends(get_db), name:str=Body(embed=True)):
    if create_new_role(db, name):
        return JSONResponse(content={"message": "New role created"}, status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"message": "error while creating"}, status_code=HTTP_400_BAD_REQUEST)



@router.delete('/roles/delete')
def delete_r(db:SessionLocal=Depends(get_db), name:str=Body(embed=True)):
    if delete_existing_role(db, name):
        return JSONResponse(content={"message": "New role deleted"}, status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"message": "error while deleting"}, status_code=HTTP_400_BAD_REQUEST)




















@router.post('/categories')
def create_category(db:SessionLocal=Depends(get_db), name:str=Body(embed=True)):
    create_category2(db, name)
    return JSONResponse(content={'message': "succes"}, status_code=status.HTTP_201_CREATED)



@router.delete('/categories/{name}')
def delete_category(name:str, db:SessionLocal=Depends(get_db)):
    if del_category(db, name):
        return JSONResponse(content={"message": "Category deleted successfully"}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "Category not found"}, status_code=HTTP_404_NOT_FOUND)


@router.put('/categories/{name}')
def update_categories(name, new_name:str=Body(embed=True), db:SessionLocal=Depends(get_db)):
    if update_category(db, name, new_name):
        return JSONResponse(content={"message": "Category name updated successfully"}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "Category not found"}, status_code=HTTP_404_NOT_FOUND)

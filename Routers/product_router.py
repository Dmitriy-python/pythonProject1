from importlib.metadata import requires
from typing import Optional

from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends,  Path
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from fastapi import FastAPI, Body
from Models import SessionLocal, get_db
from cruds.category_crud import get_categories, create_category2, update_category, del_category
from cruds.product_crud import get_products, get_one_category_products, add_product, update_product1, delete_product, \
    get_product_by_name
from schemas.product_schemas import ProductModel


router=APIRouter(prefix='/api/products', tags=["products"])







@router.get("/")
def root(name:Optional[str]=Query(None), db:SessionLocal=Depends(get_db)):
    if name:
        return get_product_by_name(db, name)
    return get_products(db)



@router.get('/{category_name}')
def get_products_by_category_name(category_name:str, db:SessionLocal=Depends(get_db)):
        return get_one_category_products(db, category_name)





#
# @router.get("/{prod_name}")
# def get_one_prod(name:str, db:SessionLocal=Depends(get_db)):
#     prod=get_product_by_name(db, name)
#     prod=jsonable_encoder(prod)
#     return JSONResponse(content=prod, status_code=status.HTTP_200_OK)





@router.post('/')
def create_new_product(data: ProductModel, db:SessionLocal=Depends(get_db)):
    add_product(db,data)
    return {"message": "uspeshno"}





@router.patch("/{name}")
def update_product (name:str, data:ProductModel,db:SessionLocal=Depends(get_db)):
    prod=update_product1(db, name, data)
    if prod is None:
        return JSONResponse(content={"message": "Prod not found"}, status_code=status.HTTP_404_NOT_FOUND)
    else:
        serialized_prod=jsonable_encoder(prod)
        return JSONResponse(content=serialized_prod, status_code=status.HTTP_200_OK)




@router.delete("/{name}")
def del_prod(name:str, db:SessionLocal=Depends(get_db)):
   if delete_product(db,name):
       return JSONResponse(content={"message": "deleted successfully"}, status_code=status.HTTP_200_OK)
   else:
       return JSONResponse(content={"message": "Prod not found"}, status_code=status.HTTP_404_NOT_FOUND)



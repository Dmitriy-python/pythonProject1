from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from fastapi import FastAPI, Body
from Models import SessionLocal, get_db
from cruds.product_crud import get_products, get_one_category_products, add_product

router=APIRouter(prefix='/api/products', tags=["products"])




@router.get("/")
def root(db:SessionLocal=Depends(get_db)):
    return get_products(db)



@router.get('/{category_name}')
def get_products_by_category_name(category_name:str, db:SessionLocal=Depends(get_db)):
    return get_one_category_products(db, category_name)


@router.post('/{category_name}')
def create_new_product(category_name:str, data=Body(), db:SessionLocal=Depends(get_db)):
    add_product(db,category_name, data)
    return {"message": "uspeshno"}



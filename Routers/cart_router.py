from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from fastapi import FastAPI, Body
from Models import SessionLocal, get_db
from cruds.cart_crud import all_p_in_one_cart, total_price
from cruds.category_crud import get_categories, create_category2, del_category, update_category

router=APIRouter(prefix='/api/cart', tags=["cart"])


@router.get("/all_products/{user_id}")
def display_all_products(user_id:int,db:SessionLocal=Depends(get_db)):
    a = all_p_in_one_cart(
        db, user_id
    )


    total_sum = total_price(
        db, user_id
    )
    return JSONResponse(content=a, status_code=status.HTTP_200_OK)







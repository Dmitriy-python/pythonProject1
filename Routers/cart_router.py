from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from fastapi import FastAPI, Body
from Models import SessionLocal, get_db
from cruds.category_crud import get_categories, create_category2, del_category, update_category

router=APIRouter(prefix='/api/cart', tags=["cart"])



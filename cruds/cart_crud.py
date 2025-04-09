from environs import Env
from fastapi import Body
from unicodedata import category

from Models import SessionLocal
from models.category_model import Category, Product, User, Role, Cart, Bonus
from schemas.product_schemas import ProductModel
from schemas.user_schemas import UserModel





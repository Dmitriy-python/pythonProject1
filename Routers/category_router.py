from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from fastapi import FastAPI, Body
from Models import SessionLocal, get_db
from cruds.category_crud import get_categories, create_category2, del_category, update_category

router=APIRouter(prefix='/api/categories', tags=["categories"])


@router.get("/")
def root(db:SessionLocal=Depends(get_db)):
    return get_categories(db)

@router.post('/')
def create_category(db:SessionLocal=Depends(get_db), name:str=Body(embed=True)):
    create_category2(db, name)
    return JSONResponse(content={'message': "succes"}, status_code=status.HTTP_201_CREATED)



@router.delete('/{name}')
def delete_category(name:str, db:SessionLocal=Depends(get_db)):
    if del_category(db, name):
        return JSONResponse(content={"message": "Category deleted successfully"}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "Category not found"}, status_code=HTTP_404_NOT_FOUND)


@router.put('/{name}')
def update_categories(name, new_name:str=Body(embed=True), db:SessionLocal=Depends(get_db)):
    if update_category(db, name, new_name):
        return JSONResponse(content={"message": "Category name updated successfully"}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "Category not found"}, status_code=HTTP_404_NOT_FOUND)

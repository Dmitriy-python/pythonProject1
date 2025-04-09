from pydantic import BaseModel, Field



class ProductModel(BaseModel):
    name: str = Field(max_length=50)
    price: int|None=Field(default=0)
    stock: int|None=Field(default=0)
    description:str =Field(max_length=255)
    img_url:str  = Field(max_length=255)
    age_restriction:int
    category_id : int =Field()



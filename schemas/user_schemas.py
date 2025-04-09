from pydantic import BaseModel, Field




class UserModel(BaseModel):
    name: str = Field(max_length=50)
    age: int = Field(ge=14, le=100)
    tg_id: str=Field(max_length=255)
    phone_number:str=Field(max_length=20)
    id_role:int|None = Field(default=1)




class BonusCardModel(BaseModel):
    balance: int
    user_id:int


class CartModel(BaseModel):
    user_id:int


class Role(BaseModel):
    name:str=Field(max_length=50)

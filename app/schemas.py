from pydantic import BaseModel,EmailStr,conint
from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    email:str
    id:int
    created_at:datetime

    class Config:
        orm_mode=True

class BasePost(BaseModel):
    title:str
    content:str
    published:bool=True



class Post(BaseModel):
    title:str
    content:str

class UserCreate(BaseModel):
    email:EmailStr            #EmailStr will automatically validate the email
    password:str
    


class ResponseBody(BasePost):
    owner_id:int
    id:int
    created_at:datetime
    owner:UserOut
    votes:int
    class Config:             #it helps to converting sqlalchemy model to python dictionary
        orm_mode=True

class ResponseBodyTwo(BaseModel):
    title:str
    content:str
    owner_id:int
    id:int
    published:bool=True
    created_at:datetime
    owner:UserOut
    votes:int
    class Config:             #it helps to converting sqlalchemy model to python dictionary
        orm_mode=True






class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:int


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)

# class PostOut(BasePost):
#     Post:ResponseBody
#     class Config:             #it helps to converting sqlalchemy model to python dictionary
#         orm_mode=True

class Vot(BaseModel):
    post_id:int
    user_id:int

class PostOut(BaseModel):
    owner_id:int
    id:int
    created_at:datetime
    title:str
    content:str
    published:bool=True
    # owner:UserOut
    # votes:Vot
    # votes:int=0
    class Config:             #it helps to converting sqlalchemy model to python dictionary
        orm_mode=True
    # class Config:             #it helps to converting sqlalchemy model to python dictionary
    #     orm_mode=True
        
class Examp(BaseModel):
    post:PostOut
    # votes:int=0
    # votes:int=0
    # class Config:             #it helps to converting sqlalchemy model to python dictionary
    #     orm_mode=True


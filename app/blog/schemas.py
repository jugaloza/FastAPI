from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    
    title: str
    body: str


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    #blogs: List

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    
    class Config():
        orm_mode = True
    pass 

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
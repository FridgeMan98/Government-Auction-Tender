from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class UserSigin(BaseModel):
    Email_id: EmailStr
    Username: str
    Password: str
    Role: str
    DateOfBirth: date

class UserLogin(BaseModel):
    Email_id: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email_id: EmailStr
    username: str
    role: str
    
    class Config:
        from_attributes = True

class Post_new_item(BaseModel):
    title:str
    description: str
    posted_by: EmailStr
    id: int
    time_duration:int
    base_price: int

class Items(BaseModel):
    posted_at : date
    Base_price: int
    description: str
    posted_by: str
    time_left: str
    id: int

class Bids(BaseModel):
    name: str
    posted_at: date
    bidder_id: int
    posted_by: str
    amount: int

class Bids_info(BaseModel):
    name: str
    Posted_at: date
    Base_price: int
    description: str
    time_duration: int
    status: str
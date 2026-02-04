from app import models, schemas
from app import utils
from fastapi import Depends, APIRouter, status, HTTPException, Response
from sqlalchemy.orm import Session
from app.db import get_db


router = APIRouter()


@router.post("/signin", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserSigin, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login')
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    check_user = db.query(models.User).filter(models.User.email_id == user.Email_id).first()
    
    if not check_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.verify_password(user.password, check_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    return {"message": "Login successful"}
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status
from .. import models, schemas
from ..database import get_db
from . import oauth2
from ..utils import hash


router = APIRouter()



@router.get("/users")
def get_users(db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    new_user = db.query(models.Users).all()
    return new_user


@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):

    hased_password = hash(user.password)
    user.password = hased_password
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{id}", response_model = schemas.UserCreate)
def get_users(id:int,db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    new_user = db.query(models.Users).filter(models.Users.id == id).first()
    if not new_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    return new_user




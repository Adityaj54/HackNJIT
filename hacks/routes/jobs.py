from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status
from .. import models, schemas
from ..database import get_db
from typing import List
from . import oauth2
router = APIRouter()


@router.get("/jobs",response_model=List[schemas.Jobs])
def get_jobs(db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    jobs = db.query(models.Jobs).all()
    if not jobs:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Location with Loc: {jobs} not found")
    return jobs


@router.get("/jobs/{name}", response_model=schemas.Jobs)
def get_by_location(name: str, db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    jobs = db.query(models.Jobs).filter(models.Jobs.name == name).all()
    if not jobs:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Company with Loc: {name} not found")
    print(jobs)
    return jobs


@router.get("/test", response_model=List[schemas.Jobs])
def test_posts(db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    jobs = db.query(models.Jobs).all()
    return jobs

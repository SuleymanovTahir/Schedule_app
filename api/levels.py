from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.level import LevelCreate, Level
from crud.level import create_level, get_level
from database import get_db

router = APIRouter()

@router.post("/levels/", response_model=Level)
def create_level_endpoint(level: LevelCreate, db: Session = Depends(get_db)):
    return create_level(db, level)

@router.get("/levels/{level_id}", response_model=Level)
def read_level(level_id: int, db: Session = Depends(get_db)):
    db_level = get_level(db, level_id)
    if db_level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return db_level
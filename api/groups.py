from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.group import GroupCreate, Group
from crud.group import create_group, get_group
from database import get_db

router = APIRouter()

@router.post("/groups/", response_model=Group)
def create_group_endpoint(group: GroupCreate, db: Session = Depends(get_db)):
    return create_group(db, group)  # Создаем группу

@router.get("/groups/{group_id}", response_model=Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = get_group(db, group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Группа не найдена")
    return db_group
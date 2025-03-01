from sqlalchemy.orm import Session
from models.level import Level
from schemas.level import LevelCreate

def create_level(db: Session, level: LevelCreate):
    db_level = Level(**level.dict())
    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level

def get_level(db: Session, level_id: int):
    return db.query(Level).filter(Level.id == level_id).first()
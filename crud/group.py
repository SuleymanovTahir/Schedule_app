from sqlalchemy.orm import Session
from models.group import Group
from schemas.group import GroupCreate

def create_group(db: Session, group: GroupCreate):
    db_group = Group(**group.dict())  # Создаем объект группы
    db.add(db_group)  # Добавляем в сессию
    db.commit()  # Сохраняем изменения
    db.refresh(db_group)  # Обновляем объект
    return db_group  # Возвращаем созданную группу

def get_group(db: Session, group_id: int):
    return db.query(Group).filter(Group.id == group_id).first()  # Получаем группу по ID
# create_director.py
from database import SessionLocal
from models.director import Director

def create_director():
    db = SessionLocal()
    try:
        existing_director = db.query(Director).first()
        if not existing_director:
            new_director = Director(
                username='a',
                email='add'
            )
            new_director.set_password('a')  # Используем set_password()
            db.add(new_director)
            db.commit()
            db.refresh(new_director)
            print(f"✅ Директор {new_director.username} успешно зарегистрирован!")
        else:
            print(f'Директор {existing_director.username} уже существует')
    finally:
        db.close()


def see_directors():
    db = SessionLocal()
    directors = db.query(Director).all()
    for d in directors:
        print(f"Имя: {d.username}, Пароль: {d.password}")


from models.base import *
# from werkzeug.security import generate_password_hash, check_password_hash
import logging

USE_HASHING = False  # ❗ Измени на True, если нужно хеширование

class Director(Base):
    __tablename__ = "directors"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str | None] = mapped_column(String, unique=True, index=True, nullable=True)
    password: Mapped[str] = mapped_column(String)  # Пароль хранится в зашифрованном виде
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    notes: Mapped[str | None] = mapped_column(String, nullable=True)

    can_manage_admins: Mapped[bool] = mapped_column(Boolean, default=True)
    # admins: Mapped[list["Model_Admin"]] = relationship("Model_Admin", back_populates="director")

    def set_password(self, password: str):
        if USE_HASHING:
            self.password = generate_password_hash(password)
        else:
            self.password = password  # Без хеширования

    def verify_password(self, password: str):
        if USE_HASHING:
            return check_password_hash(self.password, password)
        return self.password == password  # Обычное сравнение
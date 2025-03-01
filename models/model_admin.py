# from models.base import *


# class Model_Admin(Base):
#     __tablename__ = "admins"
    
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     name: Mapped[str] = mapped_column(String, unique=True, index=True)
#     email: Mapped[str] = mapped_column(String, unique=True, index=True)
#     password: Mapped[str] = mapped_column(String)  # Храните пароль в зашифрованном виде
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True)
#     can_manage_users: Mapped[bool] = mapped_column(Boolean, default=False)
#     can_edit_schedule: Mapped[bool] = mapped_column(Boolean, default=False)
#     can_view_reports: Mapped[bool] = mapped_column(Boolean, default=False)

#     # Связь с директором
#     director_id: Mapped[int] = mapped_column(ForeignKey("directors.id"))
#     director: Mapped["Director"] = relationship("Director", back_populates="model_admins")
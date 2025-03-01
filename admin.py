#admin.py
from sqladmin import Admin as SQLAdmin, ModelView
from database import engine, SessionLocal
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from models.director import Director
# from models.model_admin import Model_Admin
from models.teacher import Teacher
from models.student import Student
from models.level import Level
from models.group import Group
from wtforms import TextAreaField, FileField, SelectField
from models.teacher import Teacher, WorkMode, Teacher_Level
from wtforms.validators import DataRequired



import logging

# admin.py

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        try:
            form = await request.form()
            username = form.get("username")  # Изменено с name на username
            password = form.get("password")

            # Логируем данные формы
            logging.info(f"Данные формы: username={username}, password={password}")

            if not username or not password:
                logging.warning("❌ Логин или пароль не были предоставлены")
                return False

            logging.info(f"Попытка входа: {username}")

            session = SessionLocal()
            director = session.query(Director).filter(Director.username == username).first()

            if not director:
                logging.warning(f"❌ Директор с именем '{username}' не найден")
                return False

            logging.info(f"Найден директор: {director.username}")

            if not director.verify_password(password):
                logging.warning(f"❌ Неверный пароль для директора '{director.usenrame}'")
                return False

            if not director.is_active:
                logging.warning(f"❌ У пользователя '{director.username}' нет прав администратора")
                return False

            # Если все проверки пройдены
            request.session.update({"token": director.username})
            logging.info(f"✅ Успешный вход! Директор: {director.username}")
            return True

        except Exception as e:
            logging.error(f"❌ Ошибка при аутентификации: {e}")
            return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        logging.info("✅ Пользователь вышел из системы")
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if token:
            logging.info(f"✅ Пользователь '{token}' аутентифицирован")
            return True
        else:
            logging.warning("❌ Пользователь не аутентифицирован")
            return False

class DirectorAdmin(ModelView, model=Director):
    column_list = [
        'id', 'username', 'email', 'is_active', 'can_manage_admins'
    ]
    column_searchable_list = ['username', 'email']
    column_sortable_list = ['id', 'username', 'email']
    form_columns = [
        'username', 'email', 'password', 'is_active', 'notes', 'can_manage_admins'
    ]
    column_labels = {
        'id': 'ID',
        'username': 'Имя пользователя',
        'email': 'Электронная почта',
        'is_active': 'Активен',
        'can_manage_admins': 'Может управлять администраторами',
        'password': 'Пароль',
        'notes': 'Примечания'
    }

    def on_model_change(self, form, model, is_created):
        logging.info(f"Директор {model.username} был {'создан' if is_created else 'обновлен'}")


from models.teacher import  ScheduleType  # Импортируем ScheduleType
class TeacherAdmin(ModelView, model=Teacher):
    column_list = [
        'id', 'name', 'surname', 'patronymic', 'date_of_birth', 'english_level', 'can_teach_ielts', 'ielts_score',
        'work_mode', 'is_active', 'hourly_rate', 'fixed_salary', 'formatted_schedule'  # Используем formatted_schedule
    ]
    column_searchable_list = ['name', 'surname']
    column_sortable_list = ['id', 'name', 'surname', 'is_active']
    form_columns = [
        'name', 'surname', 'patronymic', 'date_of_birth', 'resume', 'english_level', 'can_teach_ielts', 'ielts_score',
        'work_mode', 'is_active', 'notes', 'hourly_rate', 'fixed_salary', 'group_payment_rules', 'individual_payment_rules',
        'working_schedule'  # Поле для выбора типа расписания
    ]
    column_labels = {
        'id': 'ID',
        'name': 'Имя',
        'surname': 'Фамилия',
        'patronymic': 'Отчество',
        'date_of_birth': 'Дата рождения',
        'resume': 'Резюме',
        'english_level': 'Уровень английского',
        'can_teach_ielts': 'Может преподавать IELTS',
        'ielts_score': 'Результат по IELTS',
        'work_mode': 'Режим работы',
        'is_active': 'Активен',
        'notes': 'Примечания',
        'hourly_rate': 'Почасовая ставка',
        'fixed_salary': 'Фиксированная зарплата',
        'group_payment_rules': 'Правила оплаты для групп',
        'individual_payment_rules': 'Правила оплаты для индивидуальных занятий',
        'working_schedule': 'Тип расписания',
        'formatted_schedule': 'Расписание'  # Лейбл для отформатированного расписания
    }

    # Используем SelectField для выбора типа расписания
    form_overrides = {
        'working_schedule': SelectField
    }

    # Настройка выпадающего списка для working_schedule
    form_args = {
        'working_schedule': {
            'choices': [(type.value, type.value) for type in ScheduleType],  # Варианты для выбора
            'validators': [DataRequired()]
        }
    }

    # Метод для отображения расписания в читаемом формате
    def formatted_schedule(self, model: Teacher) -> str:
        schedule = get_schedule(model.working_schedule)  # Получаем расписание по типу
        if not schedule:
            return "Расписание не указано"
        
        result = []
        for day, times in schedule.items():
            if times:
                start_time = times.get("start_time", "Не указано")
                end_time = times.get("end_time", "Не указано")
                lunch_start = times.get("lunch_start", "Нет")
                lunch_end = times.get("lunch_end", "Нет")
                result.append(f"{day}: {start_time}–{end_time} (Обед: {lunch_start}–{lunch_end})")
            else:
                result.append(f"{day}: Выходной")
        return "\n".join(result)

    # Логирование изменений
    def on_model_change(self, form, model, is_created):
        logging.info(f"Учитель {model.name} {model.surname} был {'создан' if is_created else 'обновлен'}")

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)       
# Класс для администрирования модели Student
class StudentAdmin(ModelView, model=Student):
    column_list = [
        'id', 'full_name', 'group_id', 'parent_name', 'parent_contact', 'email', 'age',
        'school_shift', 'lesson_times', 'lesson_days', 'lesson_format', 'teacher_type',
        'course_type', 'age_group', 'english_level', 'start_date', 'end_date','payment_date', 'discount',
        'cost', 'payment_type', 'payment_status', 'lesson_type', 'notes'
    ]
    column_searchable_list = ['full_name', 'email', 'parent_name','parent_contact']
    column_sortable_list = ['full_name', 'group_id', 'parent_name', 'parent_contact', 'email', 'age',
        'school_shift', 'lesson_times', 'lesson_days', 'lesson_format', 'teacher_type',
        'course_type', 'age_group', 'english_level', 'start_date', 'end_date', 'payment_date', 'discount',
        'cost', 'payment_type', 'payment_status', 'lesson_type', 'notes']
    form_columns = [
        'full_name', 'group_id', 'parent_name', 'parent_contact', 'email', 'age',
        'school_shift', 'lesson_times', 'lesson_days', 'lesson_format', 'teacher_type',
        'course_type', 'age_group', 'english_level', 'start_date', 'end_date', 'payment_date', 'discount',
        'cost', 'payment_type', 'payment_status', 'lesson_type', 'notes'
    ]
    column_labels = {
        'id': 'ID',
        'full_name': 'ФИО ученика',
        'group_id': 'Группа',
        'parent_name': 'Имя родителя',
        'parent_contact': 'Контакт родителя',
        'email': 'Электронная почта',
        'age': 'Возраст',
        'school_shift': 'Смена занятий',
        'lesson_times': 'Время занятий',
        'lesson_days': 'Дни занятий',
        'lesson_format': 'Формат занятий',
        'teacher_type': 'Тип преподавателя',
        'course_type': 'Тип курса',
        'age_group': 'Возрастная группа',
        'english_level': 'Уровень английского',
        'start_date': 'Дата начала обучения',
        'end_date': 'Дата окончания обучения',
        'discount': 'Скидка',
        'cost': 'Стоимость обучения',
        'payment_type': 'Тип оплаты',
        'payment_status': 'Статус оплаты',
        'lesson_type': 'Тип обучения',
        'payment_date': 'Дата оплаты',
        'notes': 'Примечания'
    }

    def on_model_change(self, form, model, is_created):
        logger.info(f"Студент {model.full_name} был {'создан' if is_created else 'обновлен'}")

from models.level import  LevelType

class LevelAdmin(ModelView, model=Level):
    # Список полей для отображения в таблице
    column_list = [
        'id', 'name', 'lessons', 'groups'  # Добавляем lessons и groups
    ]
    
    # Поля, по которым можно искать
    column_searchable_list = ['name']
    
    # Поля, по которым можно сортировать
    column_sortable_list = ['id', 'name']
    
    # Поля, которые отображаются в форме редактирования/создания
    form_columns = [
        'name', 'lessons', 'groups'  # Добавляем lessons и groups
    ]
    
    # Лейблы для полей
    column_labels = {
        'id': 'ID',
        'name': 'Уровень',
        'lessons': 'Уроки',
        'groups': 'Группы'
    }

    # Используем SelectField для выбора уровня
    form_overrides = {
        'name': SelectField
    }

    # Настройка выпадающего списка для уровня
    form_args = {
        'name': {
            'choices': [(type.value, type.value) for type in LevelType],  # Варианты для выбора
            'validators': [DataRequired()]
        }
    }

# Класс для администрирования модели Group
class GroupAdmin(ModelView, model=Group):
    column_list = [
        'id', 'name', 'level_id', 'teacher_id', 'group_type', 'lesson_format',
        'days', 'materials', 'notes', 'cost', 'created_at', 'updated_at'
    ]
    column_searchable_list = ['name']  # Поиск по названию группы
    column_sortable_list = ['id', 'name', 'created_at']  # Сортировка по ID, названию и дате создания
    form_columns = [
        'name', 'level_id', 'teacher_id', 'group_type', 'lesson_format',
        'days', 'materials', 'notes', 'cost'
    ]
    column_labels = {
        'id': 'ID',
        'name': 'Название группы',
        'level_id': 'Уровень группы',
        'teacher_id': 'Преподаватель',
        'group_type': 'Тип группы',
        'lesson_format': 'Формат занятий',
        'days': 'Дни занятий',
        'materials': 'Учебные материалы',
        'notes': 'Примечания',
        'cost': 'Стоимость группы',
        'created_at': 'Дата создания',
        'updated_at': 'Дата обновления'
    }

    def on_model_change(self, form, model, is_created):
        logger.info(f"Группа {model.name} была {'создана' if is_created else 'обновлена'}.")

        
def create_admin(app):
    authentication_backend = AdminAuth(secret_key="supersecretkey")
    admin = SQLAdmin(app, engine, authentication_backend=authentication_backend)

    admin.add_view(DirectorAdmin)
    # admin.add_view(AdminAdmin)
    admin.add_view(TeacherAdmin)
    admin.add_view(StudentAdmin)
    admin.add_view(LevelAdmin)
    admin.add_view(GroupAdmin)

    logging.info("Админ панель успешно создана")
    return admin
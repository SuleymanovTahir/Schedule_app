#main.py
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from api import lessons, levels, teachers, groups, students
from fastapi.templating import Jinja2Templates
from admin import create_admin
from scripts.add_director import *

# from seed import add_data




app = FastAPI()
admin = create_admin(app)

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Подключаем роутеры
app.include_router(lessons.router)
app.include_router(levels.router)
app.include_router(teachers.router)
app.include_router(groups.router)
app.include_router(students.router)

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в приложение для управления расписанием!"}



@app.get("/schedule")
async def schedule(request: Request):
    return templates.TemplateResponse("schedule.html", {"request": request})

# # add_data()
# create_director()
# see_directors()
# from analysis.analysis_schedule import save_students_to_db,load_schedule_data,file_path
# save_students_to_db(load_schedule_data(file_path))
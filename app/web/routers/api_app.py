# -*- coding: utf-8 -*-

"""Тут будут только роуты, предназначенные для API (взаимодействия с android)"""

from app.web.dependencies import *


session_keyless_api = APIRouter(prefix="/api")  # Для роутов, не использующих session_key

# =======! Роуты, не использующие session_key !=======


@session_keyless_api.get("/")
def test1():
    return {"answer-------------- : False"}


@session_keyless_api.get("/log_in/{login}/{password}")
@db_session
def log_in(login: str, password: str):
    """Авторизация"""
    if User.exists(name=login):
        user = User.get(name=login)
        if user.password == password:
            session_key = random.random()
            user.session_key_for_app = str(session_key)
            User.select().show()
            return {
                'answer : True' + ', group_name : ' + 'user.groups' + ', name : ' + user.name + ', session_key : ' + str(
                    session_key)}
        return {"answer : False"}
    return {"answer : False"}


@session_keyless_api.get("/sign_in/{login}/{password}/{_id}")
@db_session
def sign_in(login: str, password: str, _id: int):
    """Регистрация пользователя"""
    if User.exists(id=_id):
        return {"false"}
    else:
        User(id=_id, name=login, password=password)
    return {"true"}


# =======! Дальше роуты, использующие session_key1 !=======

api_app = APIRouter(  # Для роутов, которые используют session_key
    prefix="/api/{session_key1}",
    dependencies=[Depends(checking_session_key)],
)


@api_app.get("/news/{group_name}")
@db_session
def news(group_name: str):
    """Новости"""
    return {
        "first : Это новости, ты просто не видишь их,  second : Да-да, это именно так, не удивляйся, third : Именно так и должно быть"}


@api_app.get("/homework/{group_name}/all")
@db_session
def all_homework(group_name: str):
    """Домашние задания (все)"""
    return {"Тут домашка"
            "<дд.мм.гггг> : { <Предмет1> : {домашка1, домашка2, ..., домашка}, <Предмет2> : {домашка1, домашка2, ..., домашка}, ... <Предмет> : {домашка1, домашка2, ..., домашка}"}


@api_app.get("/homework/{group_name}/subject/{subject}")
@db_session
def subject_homework(group_name: str, subject: str):
    """Домашние задания (по предмету)"""
    if subject == "rus":
        return {
            "rus : <дд.мм.гггг> : {домашка1, домашка2, ..., домашка}, <дд.мм.гггг> : {домашка1, домашка2, ..., домашка},... <дд.мм.гггг> : {домашка1, домашка2, ..., домашка},"}
    elif subject == "sit":
        return {
            "sit : <дд.мм.гггг> : {домашка1, домашка2, ..., домашка}, <дд.мм.гггг> : {домашка1, домашка2, ..., домашка},... <дд.мм.гггг> : {домашка1, домашка2, ..., домашка},"}
    return {"У нас нет такого предмета"}


@api_app.get("/homework/{group_name}/day/{data}")
@db_session
def data_homework(group_name: str, data: str):
    """Домашние задания (по дате)"""
    return {"Предмет1": ["домашка1", "домашка2", "домашка"],
            "Предмет2": ["домашка1", "домашка2", "домашка"],
            "Предмет3": ["домашка1", "домашка2", "домашка"], }


@api_app.get("/teachers/{group_name}/")
@db_session
def teachers(group_name: str):
    """Информация о преподавателях"""
    return {
        "ФИО1": ["инфа1", "инфа2", 'инфа'],
        "ФИО2": ["инфа1", "инфа2", 'инфа'],
        "ФИО3": ["инфа1", "инфа2", 'инфа']
    }


@api_app.get("/{group_name}/schedule/{change}")
@db_session
def schedule(group_name: str, change: str):
    """Расписание"""

    return {"Тут будет расписание на 2 недели"}


@api_app.get("/educational_materials/{group_name}")
@db_session
def educational_materials(group_name: str):
    """Получает образовательные материалы"""
    return {
        "Файлы с учебниками: <предмет> : {инфа1, инфа2, ..., инфа}, <предмет> : {инфа1, инфа2, ..., инфа}, ... , <предмет> : {инфа1, инфа2, ..., инфа},"}


@api_app.get("/log_out")
@db_session
def log_out():
    """Выход из пользователя"""
    k = 1
    if k == 1:
        return {"True"}
    return {"False"}


@api_app.get("/reg_group/{group_name}")
@db_session
def reg_group(group_name: str):
    """Регистрация группы"""
    k = 1
    if k == 1:
        return {"True"}
    return {"Falseg"}


@api_app.get("/settings_user/get")
@db_session
def settings_user_get():
    """Получить настройки пользователя"""
    return {"<какой-то параметр> : <какое-то значение>"}


# Установка настроек - не знаю, как сделать


@api_app.get("/settings_admin/get")
@db_session
def settings_user_admin():
    """Получить настройки для администратора"""
    return {"<какой-то параметр> : <какое-то значение>"}


@api_app.get("/settings_bot/get")
@db_session
def settings_user_bot():
    """Получить настройки для бота (для личного пользования)"""
    return {"<какой-то параметр> : <какое-то значение>"}


@api_app.get("/settings_group_senior/get")
@db_session
def settings_group_senior():
    """Получить настройки старосты"""
    return {"<какой-то параметр> : <какое-то значение>"}

class TestClass2(BaseModel):
    number1: int
    name1: str

class TestClass(BaseModel):
    # senior_in_the_group: PdOptional[Union[PdSeniorInTheGroup, str, List, Dict, PdSet]]
    # users: PdOptional[PdSet[Union[PdUser, str, List, Dict, PdSet]]]
    # dustbining_chats: PdOptional[PdSet[Union[PdDustbiningChat, str, List, Dict, PdSet]]]
    # important_chats: PdOptional[PdSet[Union[PdImportantChat, str, List, Dict, PdSet]]]
    # subjects: PdOptional[PdSet[Union[PdSubject, str, List, Dict, PdSet]]]
    name: Union[str, int, Dict]
    name1: Union[int, List[int]] = [7, 9]
    name2: PdOptional[Union[List[int]]]
    events: PdOptional[List[Union[int, str, TestClass2, Dict, List]]] = None  # Union[PdEvent, str, List, Dict, PdSet]  , List, Dict, TestClass2
    timesheet_update: datetime = lambda: datetime.now
    # news: PdOptional[PdSet[Union[PdNews, str, List, Dict, PdSet]]]
    # queues: PdOptional[PdSet[Union[PdQueue, str, List, Dict, PdSet]]]

"""  
"events": {
    "number1": 0,
    "name1": "string"
  }
"""

@api_app.post("/test")
@db_session
def testing_pd_model(my_group: TestClass):
    print(my_group)
    return {'dfv': 'gooood'}



if __name__ == "__main__":
    # is_DB_created()
    show_all()

    # uvicorn.run("api_app:app", host="127.0.0.1", port=8000, reload=True)

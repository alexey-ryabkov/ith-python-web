from ..db.manager import DatabaseManager
from ..models.user import create_user, get_user_data
from ..password import hash_password, verify_password
from ..session import start_user_session, end_user_session
from ..validate import validate_user_data


def process_signup(request):
    data = request.form
    with DatabaseManager() as cursor:
        validate_user_data(cursor, data)
        create_user(
            cursor,
            data["login"],
            data["email"],
            hash_password(data["password"]),
        )
    with DatabaseManager() as cursor:
        user_data = get_user_data(cursor, data["login"])
        start_user_session(user_data["id"])


def process_signin(request):
    login = request.form["login"].strip()
    password = request.form["password"].strip()
    if not login or not password:
        raise ValueError("Все поля обязательны для заполнения")
    with DatabaseManager() as cursor:
        user_data = get_user_data(cursor, login)
        if user_data is None:
            raise ValueError(
                f"Пользователь с логином {login} не зарегистрирован в системе"
            )
        if not verify_password(user_data["password"], password):
            raise ValueError("Неверный пароль!")
        start_user_session(user_data["id"])


def process_logout(_):
    end_user_session()

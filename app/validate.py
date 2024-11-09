import re
from .models.user import is_unique_login_email

MIN_LOGIN_LEN = 3
MAX_LOGIN_LEN = 16
MIN_PSSWD_LEN = 6
MAX_PSSWD_LEN = 20


def validate_user_data_input(user_data):
    if not all(value.strip() for value in user_data.values()):
        raise ValueError("Все поля обязательны для заполнения")
    if not re.match(
        rf"^(?=.*[a-zA-Z])[a-zA-Z0-9_]{{{MIN_LOGIN_LEN-1},{MAX_LOGIN_LEN-1}}}$",
        user_data["login"].strip(),
    ):
        raise ValueError(
            f"""Неверный формат логина (от {MIN_LOGIN_LEN} до {MAX_LOGIN_LEN} символов,
            нужно использовать латинские буквы, можно использовать цифры и символ подчеркивания"""
        )
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", user_data["email"].strip()):
        raise ValueError("Неверный формат e-mail")
    if not re.match(
        rf"^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9_]{{{MIN_PSSWD_LEN-1},{MAX_PSSWD_LEN-1}}}$",
        user_data["password"].strip(),
    ):
        raise ValueError(
            f"""Неверный формат пароля (от {MIN_PSSWD_LEN} до {MAX_PSSWD_LEN} символов,
            нужно использовать латинские буквы и цифры, можно использовать символ подчеркивания)"""
        )


def validate_user_data(cursor, user_data):
    validate_user_data_input(user_data)
    login = user_data["login"]
    email = user_data["email"]
    if not is_unique_login_email(cursor, login, email):
        raise ValueError("Логин и e-mail должны быть уникальны!")

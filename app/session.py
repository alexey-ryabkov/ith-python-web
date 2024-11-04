from flask import session


def start_user_session(user_id):
    session["user_id"] = user_id


def end_user_session():
    session.pop("user_id", None)


def get_user():
    return session.get("user_id")


def is_user_authorized():
    return bool(get_user())

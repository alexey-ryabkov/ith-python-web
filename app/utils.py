from .db.manager import DatabaseManager
from .session import get_user
from .models.user import get_user_data


def get_cur_user_data():
    with DatabaseManager() as cursor:
        return get_user_data(cursor, get_user())

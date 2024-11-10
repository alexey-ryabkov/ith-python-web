from .db.manager import DatabaseManager
from .config import APP_CONFIG
from .session import get_user
from .models.user import get_user_data


def get_cur_user_data():
    with DatabaseManager() as cursor:
        return get_user_data(cursor, get_user())


def get_page(request):
    page = None
    for _, page_config in APP_CONFIG["pages"].items():
        if request.path == page_config["url"]:
            page = page_config
            break
    return page

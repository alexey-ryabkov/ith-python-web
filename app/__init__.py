import os
from flask import Flask
from .config import APP_CONFIG
from .session import is_user_authorized
from .utils import get_cur_user_data
from .db.manager import DatabaseManager


app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
)
app.secret_key = os.urandom(24)
just_started = True


@app.before_request
def init_db_data_on_start():
    global just_started
    if just_started:
        DatabaseManager().init_data()
        just_started = False


@app.context_processor
def define_context():
    return dict(
        is_user_authorized=is_user_authorized(),
        user_data=get_cur_user_data(),
        pages=APP_CONFIG["pages"],
    )

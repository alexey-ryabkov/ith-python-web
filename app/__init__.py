import os
from flask import Flask
from .config import APP_CONFIG
from .session import is_user_authorized
from .utils import get_cur_user_data


app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
)
app.secret_key = os.urandom(24)


@app.context_processor
def inject_utils():
    return dict(
        is_user_authorized=is_user_authorized(),
        user_data=get_cur_user_data(),
        pages=APP_CONFIG["pages"],
    )

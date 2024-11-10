import os
from flask import Flask
from .session import is_user_authorized
from .pages import get_pages
from .utils import get_cur_user_data


app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
)
app.secret_key = os.urandom(24)


@app.context_processor
def inject_utils():
    return dict(
        is_user_authorized=is_user_authorized,
        user_data=get_cur_user_data(),
        pages={k: v for k, v in get_pages().items() if v},
    )

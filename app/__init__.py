import os
from flask import Flask
from .session import is_user_authorized


app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
)
app.secret_key = os.urandom(24)


@app.context_processor
def inject_is_user_authorized():
    return dict(is_user_authorized=is_user_authorized)

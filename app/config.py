import os
from typing import TypedDict, Dict, Optional
from dotenv import load_dotenv


class PageConfig(TypedDict):
    title: str
    url: str
    menu_title: Optional[str]
    tmpl: Optional[str]
    in_menu: Optional[bool]
    auth_only: Optional[bool]
    anonym_only: Optional[bool]


class DBConfig(TypedDict):
    host: str
    user: str
    password: str
    database: str
    port: int


class AppConfig(TypedDict):
    flask_port: int
    db: DBConfig
    pages: Dict[str, PageConfig]


load_dotenv()

APP_CONFIG = AppConfig(
    flask_port=int(os.getenv("FLASK_PORT", "5000")),
    db=DBConfig(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_DATABASE", "match_result"),
        port=int(os.getenv("DB_PORT", "3306")),
    ),
    pages={
        "events": PageConfig(
            title="Последние события",
            url="/events",
            menu_title="События",
            tmpl="events.html",
        ),
        "favorites": PageConfig(
            title="Избранные события",
            url="/favorites",
            menu_title="Избранное",
            tmpl="events.html",
            auth_only=True,
        ),
        "section1": PageConfig(title="И еще пара", url="#"),
        "section2": PageConfig(title="Разделов", url="#"),
        "signup": PageConfig(
            title="Регистрация",
            url="/signup",
            tmpl="signup.html",
            cls="md:hidden",
            anonym_only=True,
        ),
        "signin": PageConfig(
            title="Авторизация",
            url="/signin",
            menu_title="Вход",
            tmpl="signin.html",
            cls="md:hidden",
            anonym_only=True,
        ),
        "profile": PageConfig(
            title="Профиль",
            url="/profile",
            tmpl="profile.html",
            in_menu=False,
            auth_only=True,
        ),
    },
)

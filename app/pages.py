from .session import is_user_authorized


def get_pages():
    return {
        "events": {
            "title": "Последние события",
            "menu_title": "События",
            "url": "/events",
            "tmpl": "events.html",
        },
        "favorites": (
            {
                "title": "Избранные события",
                "menu_title": "Избранное",
                "url": "/favorites",
                "tmpl": "events.html",
            }
            if is_user_authorized()
            else None
        ),
        "section1": {"title": "И еще пара", "url": "#"},
        "section2": {"title": "Разделов", "url": "#"},
        "signup": (
            {
                "title": "Регистрация",
                "url": "/signup",
                "tmpl": "signup.html",
                "cls": "md:hidden",
            }
            if not is_user_authorized()
            else None
        ),
        "signin": (
            {
                "title": "Авторизация",
                "menu_title": "Вход",
                "url": "/signin",
                "tmpl": "signin.html",
                "cls": "md:hidden",
            }
            if not is_user_authorized()
            else None
        ),
    }

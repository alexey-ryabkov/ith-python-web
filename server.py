from functools import wraps
from flask import render_template, redirect, url_for, request, flash
from mysql.connector import Error
from app import app
from app.config import APP_CONFIG
from app.session import is_user_authorized
from app.controllers.event import (
    process_events,
    process_add_event_2fav,
    process_del_event_from_fav,
)
from app.controllers.auth import (
    process_signup,
    process_signin,
    process_logout,
)
from app.controllers.user import process_profile
from app.utils import get_page


pages = APP_CONFIG["pages"]
favorites_url = pages["favorites"]["url"]


def check_user(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        page = get_page(request)
        if page is None:
            return func(*args, **kwargs)
        if page.get("auth_only", False) and not is_user_authorized():
            flash(
                f"Пожалуйста, войдите в систему для доступа к странице {request.path}.",
                "error",
            )
            return redirect(url_for("signin"))
        if page.get("anonym_only", False) and is_user_authorized():
            flash(
                f"Нет доступа к {request.path}, т.к. вы уже зарегистированы и авторизованы в системе.",
                "error",
            )
            return redirect(url_for("profile"))
        return func(*args, **kwargs)

    return wrapped_func


@app.route("/")
def main():
    return redirect(url_for("events"))


@app.route(pages["events"]["url"])
def events():
    show_fav = is_user_authorized()
    events_data = process_events(request)
    return render_template(
        pages["events"]["tmpl"],
        events=events_data,
        show_fav=show_fav,
        title=pages["events"]["title"],
    )


@app.route(pages["favorites"]["url"])
@check_user
def favorites():
    events_data = process_events(request, True)
    return render_template(
        pages["favorites"]["tmpl"],
        events=events_data,
        show_fav=True,
        title=pages["favorites"]["title"],
    )


@app.route(f"{favorites_url}/<int:event_id>", methods=["POST", "DELETE"])
@check_user
def change_fav_list(event_id):
    try:
        if request.method != "DELETE" and request.form.get("_method") != "DELETE":
            if process_add_event_2fav(request, event_id):
                flash("Событие добавлено в избранное", "success")
            else:
                flash("Событие уже добавлено в избранное", "info")
        else:
            if process_del_event_from_fav(request, event_id):
                flash("Событие удалено из избранного", "success")
            else:
                flash("События уже нет в избранном", "info")
    except Error as e:
        flash(f"При изменении списка избранных событий возникла ошибка: {e}", "error")
    return redirect(request.args.get("next", url_for("events")))


@app.route(pages["signup"]["url"], methods=["GET", "POST"])
@check_user
def signup():
    if request.method == "POST":
        try:
            process_signup(request)
            flash("Вы успешно зарегистрированы!", "success")
            return redirect(url_for("profile"))
        except ValueError as e:
            flash(str(e), "error")
        except Error as e:
            flash(f"При регистрации возникла ошибка: {e}", "error")
    return render_template(pages["signup"]["tmpl"])


@app.route(pages["signin"]["url"], methods=["GET", "POST"])
@check_user
def signin():
    if request.method == "POST":
        try:
            process_signin(request)
            flash("Вы успешно авторизованы!", "success")
            return redirect(url_for("profile"))
        except ValueError as e:
            flash(str(e), "error")
        except Error as e:
            flash(f"При авторизации возникла ошибка: {e}", "error")
    return render_template(pages["signin"]["tmpl"])


@app.route(pages["profile"]["url"], methods=["GET", "POST"])
@check_user
def profile():
    if request.method == "POST":
        try:
            process_profile(request)
            flash("Ваш профиль обновлен!", "success")
        except ValueError as e:
            flash(str(e), "error")
        except Error as e:
            flash(f"При обновлении профиля возникла ошибка: {e}", "error")
    return render_template(pages["profile"]["tmpl"])


@app.route("/logout")
@check_user
def logout():
    process_logout(request)
    flash("Вы успешно вышли из системы!", "success")
    return redirect(url_for("signin"))


if __name__ == "__main__":
    app.run(debug=True, port=APP_CONFIG["flask_port"])

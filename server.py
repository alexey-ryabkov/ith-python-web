from flask import render_template, redirect, url_for, request
from app import app


@app.route("/")
def main():
    return redirect(url_for("events"))


@app.route("/events")
def events():
    events = [
        {
            "date": "2024-11-01",
            "tournament": "Лига Чемпионов",
            "teams": "Команда А - Команда Б",
            "score": "2:1",
        },
        {
            "date": "2024-11-02",
            "tournament": "Лига Европы",
            "teams": "Команда В - Команда Г",
            "score": "1:1",
        },
    ]
    return render_template("events.html", events=events)


@app.route("/favorites")
def favorites():
    # TODO
    return render_template("events.html", events=[])


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # TODO
        pass
    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # TODO
        pass
    return render_template("signin.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        # TODO
        pass
    return render_template("profile.html")


@app.route("/logout")
def logout():
    # TODO
    pass
    return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(debug=True)

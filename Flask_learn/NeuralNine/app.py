from flask import (
    Flask,
    flash,
    make_response,
    render_template,
    session,
    request,
)

app = Flask(__name__)
app.secret_key = "SOME KEY"


@app.route("/")  # pyright: ignore
def index():
    return render_template("index.html")


@app.route("/setSession")  # pyright: ignore
def setSession():
    session["name"] = "Grish Rana"
    session["username"] = "grishrana"
    return render_template("index.html", message="Session Data Set")


@app.route("/getData")  # pyright: ignore
def getData():
    if "name" in session.keys() and "username" in session.keys():
        return render_template(
            "index.html",
            message=f"Name: {session['name']} username: {session['username']}",
        )
    else:
        return render_template("index.html", message="No session Running")


@app.route("/destroySession")  # pyright: ignore
def destroySession():
    session.clear()
    # you can also destroy only certain parts of session eg: session['name'] = ""
    return render_template("index.html", message="Session destroyed Successfully.")


@app.route("/setCookie")  # pyright: ignore
def setCookie():
    response = make_response(render_template("index.html", message="Cookie set"))
    response.set_cookie("Mode", "dark")
    response.set_cookie("Lang", "en")
    return response


@app.route("/getCookie")  # pyright: ignore
def getCookie():
    mode = request.cookies["Mode"]
    lang = request.cookies["Lang"]
    return render_template("index.html", message=f"Mode: {mode} Language: {lang}")


@app.route("/destroyCookie")  # pyright: ignore
def destroyCookie():
    if "Mode" in request.cookies.keys() and "Lang" in request.cookies.keys():
        response = make_response(
            render_template("index.html", message="Cookie destroyed")
        )
        response.set_cookie("Mode", expires=0)
        response.set_cookie("Lang", expires=0)
    else:
        return render_template("index.html", message="No Cookies to destroy")
    return response


@app.route("/login", methods=["GET", "POST"])  # pyright: ignore
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin":
            flash("Logged in Successfully!!")
            return render_template("index.html", message=f"Weclome {username}!!")
        else:
            flash("Invalid Credentials")
            return render_template("login.html")


@app.route("/helloworld")  # pyright: ignore
def helloworld():
    return "helloworld"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)

import os
import uuid
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    Response,
    send_from_directory,
)
import pandas as pd

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])  # pyright: ignore
def index():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form["password"]
        if username == "grishrana" and password == "password":
            return "Sucess"
        else:
            return "Failure"

    else:
        return 0


@app.route("/file_upload", methods=["POST"])  # pyright: ignore
def file_upload():
    file = request.files["file"]
    if file.content_type == "text/plain":
        return file.read()
    else:
        df = pd.read_excel(file)
        return df.to_html()


@app.route("/convert_csv", methods=["POST"])  # pyright: ignore
def convert_csv():
    file = request.files["file"]
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=result.csv"},
    )
    return response


@app.route("/convert_csv_two", methods=["POST"])  # pyright: ignore
def convert_csv_two():
    file = request.files["file"]
    df = pd.read_excel(file)

    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")

    filename = f"{uuid.uuid4()}.csv"
    df.to_csv(os.path.join("Downloads", filename))

    return render_template("downloadpage.html", filename=filename)


@app.route("/download/<filename>")  # pyright: ignore
def download(filename):
    return send_from_directory("Downloads", filename, download_name="result.csv")


@app.route("/handle_post", methods=["POST"])  # pyright: ignore
def handle_post():
    data = request.get_json()
    greeting = data.get("greeting")
    name = data.get("name")

    with open("file.txt", "w") as f:
        f.write(f"{greeting}, {name}")

    return jsonify({"message": "Successfully written!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)

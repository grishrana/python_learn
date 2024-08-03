import os
import uuid
import pandas as pd
from flask import Flask, render_template, request, send_from_directory, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])  # pyright: ignore
def upload():
    try:
        file = request.files["file"]
        df = pd.read_excel(file)

        if not os.path.exists("downloads"):
            os.mkdir("downloads")

        filename = f"{uuid.uuid4()}.csv"
        df.to_csv(os.path.join("downloads", filename), index=False)
        return (
            jsonify(
                {
                    "message": "Successfully Uploaded and converted the file",
                    "filename": str(filename),
                }
            ),
            200,
        )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory("downloads", filename, download_name="converted.csv")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556, debug=True)

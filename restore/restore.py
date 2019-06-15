import os
import pathlib

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(
    __name__,
    static_folder = "./dist/static",
    template_folder = "./dist",
)
app.config["UPLOAD_FOLDER"] = "./temp"


@app.route("/")
def serve_vue_app():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_backup():
    file = request.files.get("file")
    if not file:
        return "No file attached...", 400
    elif file.filename == "":
        return "No file attached...", 400
    elif not file.filename.endswith("tar.gz"):
        return "Not a gzipped tarball...", 400
    else:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        pathlib.Path(app.config["UPLOAD_FOLDER"]).mkdir(parents=True, exist_ok=True)
        file.save(filepath)
        restore_backup(filepath)
        return "Success!"


def restore_backup(filepath):
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0")

import os
import pathlib
import tarfile

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(
    __name__,
    static_folder = "./dist/static",
    template_folder = "./dist",
)

app.config["UPLOAD_FOLDER"] = "/tmp"
app.config["MINECRAFT_FOLDER"] = "/minecraft"


@app.route("/")
def serve_vue_app():
    """Serve the Vue application."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_backup():
    """Extract backup gzipped tarball to the Minecraft server directory."""
    file = request.files.get("file")
    if not file:
        return "No file attached...", 400
    elif file.filename == "":
        return "No file attached...", 400
    elif not file.filename.endswith("tar.gz"):
        return "Not a gzipped tarball...", 400
    else:
        # Save backup to disk.
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        pathlib.Path(app.config["UPLOAD_FOLDER"]).mkdir(parents=True, exist_ok=True)
        file.save(filepath)
        # Extract the backup to server directory.
        tarball = tarfile.open(filepath, "r:gz")
        tarball.extractall(app.config["MINECRAFT_FOLDER"])
        return "Success!"


if __name__ == "__main__":
    if not os.path.isdir(app.config["MINECRAFT_FOLDER"]):
        print("Minecraft server files not found. Starting restoration server.")
        app.run(host="0.0.0.0")
    else:
        print("Minecraft server files found! Exiting init container.")

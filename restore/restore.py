from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder = "./dist/static",
    template_folder = "./dist",
)

@app.route("/")
def serve_vue_app():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

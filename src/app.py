import os
from flask import Flask, send_from_directory

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "..", "static")

app = Flask(
    __name__,
    static_folder=STATIC_DIR,
    static_url_path=""
)

port = int(os.getenv("PORT", 3030))

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    print(f"Server started on port {port}")
    app.run(host="0.0.0.0", port=port)


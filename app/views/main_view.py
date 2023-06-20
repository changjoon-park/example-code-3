from flask import render_template, Blueprint, url_for

bp = Blueprint("main", __name__, url_prefix="/")

@bp.route("/")
def index():
    data = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"}
    ]
    return render_template("index.html", data=data)
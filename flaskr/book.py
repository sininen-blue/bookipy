from flask import Blueprint, flash, g, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("book", __name__)


@bp.route("/")
def index():
    db = get_db()
    chapters = db.execute(
        "SELECT id, title, body FROM chapter ORDER BY id DESC"
    ).fetchall()

    return render_template("blog/index.html", chapters=chapters)

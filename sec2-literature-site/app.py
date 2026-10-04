"""Sec 2 English Literature Cheat Sheet — a small Flask website (same setup as the other subject sites).

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5004
"""
import json
from pathlib import Path

from flask import Flask, abort, render_template, request
from markupsafe import Markup

BASE = Path(__file__).parent
DATA_FILE = BASE / "data" / "topics.json"


def load_data():
    """(Re)load data/topics.json. Called at start-up and again whenever the file changes,
    so edits show up on the next page load without restarting the server."""
    global DATA, STRANDS, TOPICS, DATA_MTIME
    DATA_MTIME = DATA_FILE.stat().st_mtime_ns
    DATA = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    STRANDS = {s["slug"]: s for s in DATA["strands"]}
    TOPICS = DATA["topics"]
    for t in TOPICS:
        t["html"] = Markup(t["html"])  # trusted content from our own data file
        t["css"] = STRANDS[t["strand"]]["css"]
        t["text"] = Markup(t["html"]).striptags().lower() + " " + t["title"].lower()


load_data()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True      # template edits show without a restart
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0     # browsers always fetch the latest CSS
app.jinja_env.auto_reload = True


@app.before_request
def refresh_data():
    """Pick up changes to data/topics.json on the next request."""
    if DATA_FILE.stat().st_mtime_ns != DATA_MTIME:
        load_data()


def grouped(topics):
    out = []
    for s in DATA["strands"]:
        items = [t for t in topics if t["strand"] == s["slug"]]
        if items:
            out.append((s, items))
    return out


@app.context_processor
def nav_data():
    return {"strands": DATA["strands"]}


def page(topics, **kw):
    kw.setdefault("q", "")
    kw.setdefault("active", None)
    kw.setdefault("heading", None)
    return render_template("index.html", groups=grouped(topics), count=len(topics), **kw)


@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    topics = TOPICS
    if q:
        words = q.lower().split()
        topics = [t for t in TOPICS if all(w in t["text"] for w in words)]
    return page(topics, q=q)


@app.route("/theme/<slug>")
def theme(slug):
    if slug not in STRANDS:
        abort(404)
    return page([t for t in TOPICS if t["strand"] == slug], active=slug)


@app.route("/topic/<slug>")
def topic(slug):
    t = next((t for t in TOPICS if t["slug"] == slug), None)
    if t is None:
        abort(404)
    return render_template("topic.html", t=t, strand=STRANDS[t["strand"]], active=t["strand"], q="")


@app.errorhandler(404)
def not_found(_):
    return page([], missing=True), 404


if __name__ == "__main__":
    app.run(debug=True, port=5004)

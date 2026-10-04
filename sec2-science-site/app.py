"""Lower Secondary Science Cheat Sheet — a small Flask website (same setup as the math and geography sites).

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5001
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
        t["eoy"] = STRANDS[t["strand"]].get("eoy", False)
        t["text"] = Markup(t["html"]).striptags().lower() + " " + t["title"].lower()


load_data()

BOOKS = {
    "1a": {"code": "1A", "name": "Book 1A", "theme": "Scientific Endeavour · Diversity", "level": "sec1"},
    "1b": {"code": "1B", "name": "Book 1B", "theme": "Models", "level": "sec1"},
    "2a": {"code": "2A", "name": "Book 2A", "theme": "Interactions", "level": "sec2"},
    "2b": {"code": "2B", "name": "Book 2B", "theme": "Systems", "level": "sec2"},
}
LEVELS = {
    "sec1": {"name": "Secondary 1", "short": "Sec 1", "chapters": "Chapters 1–8"},
    "sec2": {"name": "Secondary 2", "short": "Sec 2", "chapters": "Chapters 9–16"},
}

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
    """Return [(level, [(book, [(strand, [topics])])])] in textbook order, skipping empty parts.

    level and book are dicts with a "name"; topics outside the books go in an "Other" level.
    """
    out = []
    parts = [(lv, [b for b in BOOKS.values() if b["level"] == key]) for key, lv in LEVELS.items()]
    parts.append(({"name": "Other topics", "short": "Other", "chapters": ""}, [{"code": "other", "name": "", "theme": ""}]))
    for level, books in parts:
        level_books = []
        for b in books:
            chapters = []
            for s in DATA["strands"]:
                if s.get("book") != b["code"]:
                    continue
                items = [t for t in topics if t["strand"] == s["slug"]]
                if items:
                    chapters.append((s, items))
            if chapters:
                level_books.append((b, chapters))
        if level_books:
            out.append((level, level_books))
    return out


@app.context_processor
def nav_data():
    return {"strands": DATA["strands"], "strand_map": STRANDS, "books": BOOKS, "levels": LEVELS}


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


@app.route("/eoy")
def eoy():
    topics = [t for t in TOPICS if t["eoy"]]
    return page(topics, active="eoy", heading="EOY exam scope (Chapters 2–4 and 7–8)")


@app.route("/sec/<slug>")
def level(slug):
    key = f"sec{slug}"
    if key not in LEVELS:
        abort(404)
    topics = [t for t in TOPICS if STRANDS[t["strand"]].get("level") == key]
    return page(topics, active=key)


@app.route("/book/<slug>")
def book(slug):
    if slug not in BOOKS:
        abort(404)
    code = BOOKS[slug]["code"]
    topics = [t for t in TOPICS if STRANDS[t["strand"]].get("book") == code]
    return page(topics, active=slug)


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
    app.run(debug=True, port=5001)

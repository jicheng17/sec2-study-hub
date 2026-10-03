"""Sec 2 Math Cheat Sheet — a small Flask website.

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5002
"""
import json
from pathlib import Path

from flask import Flask, abort, render_template, request
from markupsafe import Markup

BASE = Path(__file__).parent
DATA = json.loads((BASE / "data" / "topics.json").read_text(encoding="utf-8"))

STRANDS = {s["slug"]: s for s in DATA["strands"]}
TOPICS = DATA["topics"]
for t in TOPICS:
    t["html"] = Markup(t["html"])  # trusted content from our own data file
    t["css"] = STRANDS[t["strand"]]["css"]

app = Flask(__name__)


def grouped(topics):
    """Return [(strand, [topics...]), ...] in syllabus order, skipping empty strands."""
    out = []
    for s in DATA["strands"]:
        items = [t for t in topics if t["strand"] == s["slug"]]
        if items:
            out.append((s, items))
    return out


@app.context_processor
def nav_data():
    return {"strands": DATA["strands"]}


@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    topics = TOPICS
    if q:
        words = q.lower().split()
        topics = [t for t in TOPICS if all(w in t["text"].lower() or w in t["title"].lower() for w in words)]
    return render_template("index.html", groups=grouped(topics), q=q, active=None, count=len(topics))


@app.route("/strand/<slug>")
def strand(slug):
    if slug not in STRANDS:
        abort(404)
    topics = [t for t in TOPICS if t["strand"] == slug]
    return render_template("index.html", groups=grouped(topics), q="", active=slug, count=len(topics))


@app.route("/topic/<slug>")
def topic(slug):
    t = next((t for t in TOPICS if t["slug"] == slug), None)
    if t is None:
        abort(404)
    return render_template("topic.html", t=t, strand=STRANDS[t["strand"]], active=t["strand"])


@app.errorhandler(404)
def not_found(_):
    return render_template("index.html", groups=[], q="", active=None, count=0, missing=True), 404


if __name__ == "__main__":
    app.run(debug=True, port=5002)

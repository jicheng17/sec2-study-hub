"""Sec 2 Study Hub — home page that brings the math and science sites together.

Run (from this folder):
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:8000

    /            home page
    /math/       Sec 2 Math Cheat Sheet
    /science/    Sec 2 Science Cheat Sheet
    /geography/  Sec 2 Geography Cheat Sheet
    /plan        EOY revision plan
    /files/...   the parents' briefing and exam scope PDFs
"""
import importlib.util
import sys
from datetime import date
from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory
from werkzeug.middleware.dispatcher import DispatcherMiddleware

HERE = Path(__file__).parent
ROOT = HERE.parent  # the O-LEVEL folder

BRIEFING_FILE = "Sec 2 Parents e-Engagement Session 2026 _ For circ_260522_140922.pdf"
SCOPE_FILE = "2026 S2 EOY Exam Scope  Format_20260928_161016.pdf"
SHARED_FILES = {BRIEFING_FILE, SCOPE_FILE}

import plan  # noqa: E402  (revision plan data, edit plan.py to change it)


def load_site(folder, name):
    """Import <folder>/app.py as its own module and return its Flask app."""
    spec = importlib.util.spec_from_file_location(name, ROOT / folder / "app.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module  # Flask needs this to find the site's templates
    spec.loader.exec_module(module)
    module.app.config["HOME_URL"] = "/"
    return module.app


math_app = load_site("sec2-math-site", "sec2_math_site")
science_app = load_site("sec2-science-site", "sec2_science_site")
geography_app = load_site("sec2-geography-site", "sec2_geography_site")

app = Flask(__name__)

# Key dates taken from the Sec 2 Parents' e-Engagement Session slides (19 May 2026)
KEY_DATES = [
    {"start": date(2026, 9, 30), "end": date(2026, 10, 8), "what": "End-of-year exam", "note": "Worth 60% of the year's result"},
    {"start": date(2026, 10, 22), "end": date(2026, 10, 26), "what": "Sec 3 subject combination option exercise", "note": "Choose 2027 subject combination"},
    {"start": date(2026, 11, 3), "end": None, "what": "Subject combination results", "note": "Sent to each student's email"},
]


def fmt(d):
    return d.strftime("%-d %b")


@app.route("/")
def home():
    today = date.today()
    dates = []
    for k in KEY_DATES:
        last = k["end"] or k["start"]
        if last < today:
            status, label = "past", "Done"
        elif k["start"] <= today:
            status, label = "now", "Happening now"
        else:
            days = (k["start"] - today).days
            status, label = "soon", f"in {days} day{'s' if days != 1 else ''}"
        when = fmt(k["start"]) + (f" – {fmt(k['end'])}" if k["end"] else "")
        dates.append({**k, "when": when, "status": status, "label": label})
    return render_template(
        "home.html", dates=dates,
        briefing_file=BRIEFING_FILE, briefing_ok=(ROOT / BRIEFING_FILE).exists(),
        scope_file=SCOPE_FILE, scope_ok=(ROOT / SCOPE_FILE).exists(),
    )


@app.route("/plan")
def revision_plan():
    today = date.today().isoformat()
    in_exams = plan.EXAM_START <= today <= plan.EXAM_END
    return render_template(
        "plan.html", plan=plan, today=today, in_exams=in_exams,
        scope_file=SCOPE_FILE, scope_ok=(ROOT / SCOPE_FILE).exists(),
    )


@app.route("/files/<path:filename>")
def files(filename):
    if filename not in SHARED_FILES:
        abort(404)
    return send_from_directory(ROOT, filename)


app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/math": math_app, "/science": science_app, "/geography": geography_app})

if __name__ == "__main__":
    # Local development: the server restarts when any content, template, CSS or Python file
    # changes, and open pages reload themselves (see livereload.py). Render uses gunicorn instead.
    from livereload import LiveReload, watched_files

    app.wsgi_app = LiveReload(app.wsgi_app, ROOT)
    app.run(debug=True, port=8000, extra_files=[str(p) for p in watched_files(ROOT)])

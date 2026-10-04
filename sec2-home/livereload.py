"""Live reload for local development.

When you run `python app.py`, every page polls /__livereload about once a second.
If any watched file (content JSON, templates, CSS, Python) changes, the server restarts
(Flask's reloader, via `extra_files`) and the browser reloads the page by itself.

Not used on Render: gunicorn imports `app` directly, so this middleware is never switched on.
"""
import json
from pathlib import Path

WATCH_DIRS = ["sec2-home", "sec2-math-site", "sec2-science-site", "sec2-geography-site"]
WATCH_SUFFIXES = {".json", ".html", ".css", ".py", ".js"}
SKIP_PARTS = {".venv", "venv", "__pycache__", ".git"}

SNIPPET = b"""<script>
(function () {
  var last = null;
  function check() {
    fetch('/__livereload', {cache: 'no-store'})
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (last === null) { last = d.v; }
        else if (d.v !== last) { location.reload(); return; }
        setTimeout(check, 1000);
      })
      .catch(function () { setTimeout(check, 1000); });  // server restarting: try again
  }
  check();
})();
</script>
"""


def watched_files(root):
    """All files that should trigger a reload."""
    files = []
    for d in WATCH_DIRS:
        for p in (Path(root) / d).rglob("*"):
            if p.is_file() and p.suffix in WATCH_SUFFIXES and not (SKIP_PARTS & set(p.parts)):
                files.append(p)
    return files


def version(root):
    """A value that changes whenever any watched file is edited, added or removed."""
    files = watched_files(root)
    return f"{len(files)}-{max((p.stat().st_mtime_ns for p in files), default=0)}"


class LiveReload:
    """WSGI middleware: serves /__livereload and adds the polling script to every HTML page."""

    def __init__(self, wsgi_app, root):
        self.wsgi_app = wsgi_app
        self.root = root

    def __call__(self, environ, start_response):
        if environ.get("PATH_INFO") == "/__livereload":
            body = json.dumps({"v": version(self.root)}).encode()
            start_response("200 OK", [("Content-Type", "application/json"),
                                      ("Cache-Control", "no-store"),
                                      ("Content-Length", str(len(body)))])
            return [body]

        captured = {}

        def capture(status, headers, exc_info=None):
            captured["status"], captured["headers"] = status, headers
            return lambda data: None  # not used by Flask

        chunks = self.wsgi_app(environ, capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()

        headers = captured["headers"]
        ctype = next((v for k, v in headers if k.lower() == "content-type"), "")
        if ctype.startswith("text/html") and b"</body>" in body:
            body = body.replace(b"</body>", SNIPPET + b"</body>", 1)
            headers = [(k, v) for k, v in headers if k.lower() != "content-length"]
            headers.append(("Content-Length", str(len(body))))
        start_response(captured["status"], headers)
        return [body]

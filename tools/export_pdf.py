"""Export a cheat sheet site to an A4 PDF.

Usage (from the O-LEVEL folder):
    pip install flask playwright
    playwright install chromium
    python tools/export_pdf.py geography        # or: math, science, literature

Writes "Sec 2 <Subject> Cheat Sheet.pdf" into the O-LEVEL folder.
"""
import importlib.util
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent

SITES = {
    # layout "grid": two columns, cards kept whole (short cards, e.g. maths formulas)
    # layout "column": one column, long cards may continue on the next page
    "math": {"folder": "sec2-math-site", "title": "Sec 2 Math Cheat Sheet", "layout": "grid"},
    "science": {"folder": "sec2-science-site", "title": "Lower Sec Science Cheat Sheet", "layout": "column"},
    "geography": {"folder": "sec2-geography-site", "title": "Sec 2 Geography Cheat Sheet", "layout": "column"},
    "literature": {"folder": "sec2-literature-site", "title": "Sec 2 Literature Cheat Sheet", "layout": "column"},
}

BASE_CSS = """
body{background:#fff !important;background-image:none !important;line-height:1.45}
nav.jump,nav.subnav,.back,form.search,footer,.qa-intro{display:none !important}
.level + .level{break-before:page}
.level-head{font-size:24px}
.book-head{font-size:16px;break-after:avoid}
.strand-head h4{font-size:16px}
.wrap{max-width:none;padding:0}
header.top{gap:4px;margin-bottom:8px}
h1{font-size:26px}
.lede{font-size:12px;max-width:none}
.card{border-color:#cfd6cf;padding:9px 12px;gap:5px}
.card h3{font-size:14.5px;break-after:avoid}
.card h3 a{color:inherit}
table.t{font-size:11px} table.t th,table.t td{padding:2px 6px}
.ex,.warn{font-size:11px}
.f{font-size:15px;padding:5px 10px}
.diag svg{max-height:110px;width:auto}
ul.k,ol.k{gap:1px}
section.strand{margin-bottom:10px}
.strand-head{margin-bottom:6px;break-after:avoid}
.strand-head h2{font-size:18px}
details.qa summary::after{display:none}
details.qa{break-inside:avoid}
.qa-body{font-size:11px;padding:6px 9px}
.qa-tip{font-size:10.5px}
"""

LAYOUT_CSS = {
    "grid": """
body{font-size:12px}
.grid{columns:auto !important;display:grid;grid-template-columns:1fr 1fr;gap:10px;align-items:start}
.card{margin:0;break-inside:avoid}
""",
    "column": """
body{font-size:11.5px}
.grid{columns:auto !important;display:block}
.card{margin:0 0 9px;break-inside:auto;display:grid}
.card>*{break-inside:avoid}
.card>.tw{break-inside:auto} tr{break-inside:avoid}
section.strand + section.strand{break-before:page}
""",
}


def load_app(folder):
    spec = importlib.util.spec_from_file_location(f"{folder}_app", ROOT / folder / "app.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.app


def main(subject):
    if subject not in SITES:
        sys.exit(f"Unknown subject '{subject}'. Choose from: {', '.join(SITES)}")
    site = SITES[subject]
    folder = ROOT / site["folder"]
    html = load_app(site["folder"]).test_client().get("/").data.decode()
    html = html.replace("/static/style.css", (folder / "static" / "style.css").as_uri())

    out = ROOT / f"{site['title']}.pdf"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        page_file = Path(f.name)

    footer = (f'<div style="font-size:8px;width:100%;text-align:center;color:#777">{site["title"]} · '
              'page <span class="pageNumber"></span> of <span class="totalPages"></span></div>')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.emulate_media(media="print", color_scheme="light")
        page.goto(page_file.as_uri())
        page.add_style_tag(content=BASE_CSS + LAYOUT_CSS[site["layout"]])
        page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
        page.wait_for_timeout(1500)  # let web fonts load
        page.pdf(path=str(out), format="A4", print_background=True,
                 margin={"top": "10mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
                 display_header_footer=True, header_template="<span></span>", footer_template=footer)
        browser.close()
    page_file.unlink(missing_ok=True)
    print(f"Saved {out.name}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")

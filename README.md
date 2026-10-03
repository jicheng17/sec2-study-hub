# Sec 2 Study Hub

Revision cheat sheets for a Singapore Secondary 2 (G3 / Express) student, built with Flask.

| Site | What it covers |
|---|---|
| `sec2-home/` | Study Hub home page, EOY revision plan, and mounts all subject sites |
| `sec2-math-site/` | Sec 2 Mathematics cheat sheet |
| `sec2-science-site/` | Lower Secondary Science, Sec 1 and Sec 2 (Books 1A–2B, Chapters 1–16) |
| `sec2-geography-site/` | Sec 2 Geography Chapters 7–11, answering techniques, practice questions |
| `tools/export_pdf.py` | Export any cheat sheet to an A4 PDF |

## Run

```bash
cd sec2-home
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:8000

See [GUIDELINES.md](GUIDELINES.md) for project structure, content rules and how to add a subject.

School documents (the parents' briefing and the EOY scope sheet) are not included in this repository. Put them in the project folder to enable the links on the home page.

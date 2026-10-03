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

## Deploy on Render

The repo includes a `render.yaml` Blueprint, so Render reads the settings automatically.

1. Push this repo to GitHub.
2. Sign in at [render.com](https://render.com) with your GitHub account.
3. Click **New → Blueprint**, choose this repository, and click **Apply**.
   For a public repo you can instead open `https://render.com/deploy?repo=https://github.com/YOUR-USERNAME/sec2-study-hub`.
4. When the build finishes, Render gives you a link like `https://sec2-study-hub.onrender.com`.

Every `git push` to `main` redeploys automatically. On the free plan the site sleeps after about 15 minutes without visitors, so the first visit after that takes up to a minute to load.

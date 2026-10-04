# Sec 2 Geography Cheat Sheet (Flask)

Covers the 2026 Sec 2 EOY geography scope: Chapters 7–11 (Chapter 11 up to page 139), the geographical investigation skills, and how to answer each question type including the Chapter 9 housing evaluation essay.

The easiest way to use it is through the Study Hub (`sec2-home`), where it appears at `/geography`. To run it on its own:

```bash
cd sec2-geography-site
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5003

## Pages

- `/`: all 27 cards, including 20 practice questions
- `/theme/cities-housing`, `/theme/transport`, `/theme/skills`, `/theme/answering`, `/theme/practice`: one section
- `/topic/<name>`, e.g. `/topic/evaluation-essay`: a single topic
- `/?q=ERP`: search

## Editing content

Topics live in `data/topics.json` (`slug`, `strand`, `badge`, `title`, `html`). Save the file and open pages update by themselves, no restart needed.

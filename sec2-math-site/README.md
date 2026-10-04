# Sec 2 Math Cheat Sheet (Flask)

A small Python website for the Singapore Sec 2 (G3 / Express) math cheat sheet.

## Run it

```bash
cd sec2-math-site
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5002 (not 5000, which macOS AirPlay Receiver uses)

## Pages

- `/`: all 17 topics
- `/strand/algebra`, `/strand/geometry`, `/strand/stats`: one strand
- `/topic/<name>`, e.g. `/topic/pythagoras-theorem`: a single topic card
- `/?q=gradient`: search across every topic

## Editing content

All topics live in `data/topics.json`. Each entry has a `slug`, `strand`, `title` and an `html` body. Edit or add entries there and save: open pages update by themselves, no restart needed. Styling is in `static/style.css` (light and dark mode follow your system setting).

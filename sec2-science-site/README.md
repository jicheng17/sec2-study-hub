# Lower Sec Science Cheat Sheet (Flask)

Covers Secondary 1 (Books 1A and 1B, Chapters 1–8) and Secondary 2 (Books 2A and 2B, Chapters 9–16), one card per sub-chapter, grouped by level, then book, then chapter. Chapters in the EOY exam scope (Book 1A Ch 2–4, Book 1B Ch 7–8) are marked EOY.

The easiest way to use it is through the Study Hub (`sec2-home`), where it appears at `/science`. To run it on its own:

```bash
cd sec2-science-site
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5001

## Pages

- `/`: all 68 cards
- `/eoy`: the 20 cards in the EOY scope
- `/sec/1`, `/sec/2`: one level (Sec 1 or Sec 2)
- `/book/1a`, `/book/1b`, `/book/2a`, `/book/2b`: one book
- `/theme/ch1` … `/theme/ch16`, `/theme/other`: one chapter
- `/topic/<name>`, e.g. `/topic/2-3-density`: a single card
- `/?q=density`: search

## Editing content

Cards live in `data/topics.json` (`slug`, `strand`, `badge`, `title`, `html`). Strands also have `book`, `level` (`sec1` / `sec2` / `other`) and `eoy`. Edit and restart.

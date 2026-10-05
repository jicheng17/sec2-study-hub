# Sec 2 History Cheat Sheet (Flask)

Covers the 2026 Sec 2 EOY History scope: Chapter 8 (How did Singapore become an independent nation?) and Chapter 9 (How did Singapore safeguard its independence after 1965?), the three source skills (inferring purpose, comparing sources, assessing reliability) and the "explain two reasons" essay.

The easiest way to use it is through the Study Hub (`sec2-home`), where it appears at `/history`. To run it on its own:

```bash
cd sec2-history-site
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5005

## Pages

- `/`: all 19 cards
- `/theme/ch8`, `/theme/ch9`, `/theme/skills`, `/theme/essay`, `/theme/practice`: one section
- `/topic/<name>`, e.g. `/topic/why-separation`: a single topic
- `/?q=Coldstore`: search

## Editing content

Topics live in `data/topics.json` (`slug`, `strand`, `badge`, `title`, `html`). Save the file and refresh the page, no restart needed.

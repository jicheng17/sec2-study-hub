# Sec 2 English Literature Cheat Sheet (Flask)

Built around the school's 2026 Sec 2 Literature EOY Briefing and class notes (kept in `resources/s2.literature/`, not in git). Covers Section A, *Emily of Emerald Hill* by Stella Kon (essay or passage-based question, 25 marks), and Section B, unseen poetry (both parts, 25 marks).

The easiest way to use it is through the Study Hub (`sec2-home`), where it appears at `/literature`. To run it on its own:

```bash
cd sec2-literature-site
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5004

## Pages

- `/`: all 27 cards
- `/theme/drama`, `/theme/characters`, `/theme/themes`, `/theme/emily-answers`, `/theme/poetry`, `/theme/poetry-practice`: one section
- `/topic/<name>`, e.g. `/topic/themes`: a single topic
- `/?q=Richard`: search

## Editing content

Topics live in `data/topics.json` (`slug`, `strand`, `badge`, `title`, `html`). Save the file and refresh the page, no restart needed. Poems use `<div class="poem">…<cite>Title, Poet (year)</cite></div>`, which keeps line breaks. Only use public-domain poems for practice.

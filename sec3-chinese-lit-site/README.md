# SEC / O-Level Literature in Chinese (华文文学) Cheat Sheet (Flask)

For Sec 3–4 (CLEP-Sec at Nan Chiau High requires Literature in Chinese). Covers both versions in SEAB's 2027 SEC syllabus: full subject K332 (Paper 1 novel 《放逐与追逐》 + Paper 2) and elective K338 (Paper 2 only). Written in Chinese.

The easiest way to use it is through the Study Hub (`sec2-home`) at `/chinese-lit`. To run it on its own:

```bash
cd sec3-chinese-lit-site
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5006

## Pages

- `/`: all 22 cards
- `/theme/exam`, `/theme/novel`, `/theme/classical`, `/theme/modern-poetry`, `/theme/stories`, `/theme/practice`
- `/topic/<name>`, e.g. `/topic/kongyiji`
- `/?q=孔乙己`: search

## Editing content

Topics live in `data/topics.json`. Save and refresh, no restart needed. Only public-domain poems (classical poems, 徐志摩《偶然》) are reproduced in full; other modern texts are summarised. Check set texts against the year's syllabus (texts can change).

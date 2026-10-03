# Sec 2 Study Hub — Project Guidelines

How this project is organised, how to run it, and the rules for adding or changing content. Read this before starting a new subject or editing an existing one.

## 1. Purpose

Revision material for a Singapore Secondary 2 (G3 / Express) student, built around the school's end-of-year (EOY) exam.

- **Reader:** a Sec 2 student revising alone, often the night before a paper. Content must be quick to scan and accurate.
- **Goal:** one place for cheat sheets, practice questions, the revision plan and school documents.
- **Source of truth:** the school's *2026 S2 EOY Exam Scope & Format* sheet decides what is in scope. The MOE syllabus and textbook come second.

## 2. Folder structure

```
O-LEVEL/
├── GUIDELINES.md                 ← this file
├── tools/
│   └── export_pdf.py             ← exports a cheat sheet site to PDF
├── sec2-home/                    ← Study Hub: home page, revision plan, mounts all subject sites
│   ├── app.py
│   ├── plan.py                   ← revision plan data (tasks, routines, subject checklists)
│   ├── templates/  home.html, plan.html
│   └── static/style.css
├── sec2-math-site/               ← one folder per subject, all with the same layout
├── sec2-science-site/
├── sec2-geography-site/
│   ├── app.py
│   ├── data/topics.json          ← all content lives here
│   ├── templates/  base.html, index.html, topic.html, _card.html
│   ├── static/style.css
│   ├── requirements.txt
│   └── README.md
├── Sec 2 <Subject> Cheat Sheet.pdf          ← exported PDFs
├── 2026 S2 EOY Exam Scope  Format_….pdf     ← school documents (keep file names unchanged;
└── Sec 2 Parents e-Engagement Session ….pdf    the hub links to them by name)
```

## 3. Tech stack

| Part | Choice | Notes |
|---|---|---|
| Web framework | **Flask** (Python 3) | Same stack as the PSLE project. Keep it. |
| Templates | Jinja2 | `base.html` shell, `_card.html` per topic |
| Content | JSON (`data/topics.json`) | HTML snippets inside JSON, loaded once at start-up |
| Styling | One plain CSS file per site | No CSS framework, no JavaScript framework |
| Fonts | Google Fonts | Bricolage Grotesque (headings), Atkinson Hyperlegible (body), STIX Two Text (maths) |
| PDF export | Playwright + Chromium | `tools/export_pdf.py` |
| Combining sites | Werkzeug `DispatcherMiddleware` | The hub mounts each subject at `/math`, `/science`, `/geography` |

No database and no login. Ticks on the revision plan are saved in the browser (`localStorage`) only.

## 4. Running it

```bash
cd ~/Documents/O-LEVEL/sec2-home
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:8000**. Restart (Ctrl+C, then `python app.py`) after editing any `.json` or `.py` file.

| Site | Port when run on its own | Path inside the hub |
|---|---|---|
| Study Hub | 8000 | `/` |
| Science | 5001 | `/science/` |
| Maths | 5002 | `/math/` |
| Geography | 5003 | `/geography/` |

**Never use port 5000.** macOS AirPlay Receiver uses it and the browser shows "Access to localhost was denied".

## 5. Content model

Each subject's `data/topics.json` has two lists.

**`strands`**: the sections of the page, in display order.

```json
{"slug": "transport", "name": "Transport", "css": "tr", "blurb": "Chapters 10–11"}
```

- `css` is a short code. Its colour is defined as `--<code>` in `style.css` (light and dark), with a matching `.<code> h3` rule.
- Don't reuse a code that is already a CSS class (for example `ex` clashes with the example box).

**`topics`**: one card each.

```json
{"slug": "sustainable-transport", "strand": "transport", "badge": "Ch 11",
 "title": "Managing transport sustainably", "html": "<p>…</p>"}
```

- `slug`: lowercase with hyphens. It becomes the URL `/topic/<slug>`, so don't change it once shared.
- `badge`: short tag shown on the card (sub-chapter number such as "9.3", chapter "Ch 7", "Exam", "GI").
- Science strands also carry `book` ("1A", "1B", "2A", "2B"), `level` ("sec1", "sec2", "other") and `eoy` (true for chapters in the EOY scope). Pages are grouped Level → Book → Chapter, and the site filters by `/sec/<1|2>`, `/book/<1a|1b|2a|2b>` and `/eoy`.
- `html`: the card body, using the building blocks in section 6.

## 6. Card building blocks

Use these classes inside `html`. Don't add inline styles.

| Block | Markup | Use for |
|---|---|---|
| Formula | `<span class="f">…</span>` | Key formula or rule, shown large |
| Table | `<div class="tw"><table class="t">…</table></div>` | Comparisons, definitions, strategy + limitation |
| List | `<ul class="k">` or `<ol class="k">` | Key facts. Use `ol` only for real sequences |
| Flow | `<p class="flow">A → B → C</p>` | Pathways and chains |
| Example | `<div class="ex"><b>Example</b>…</div>` | Worked example or model answer. The first `<b>` is the label |
| Watch out | `<div class="warn"><b>Watch out:</b> …</div>` | The most common mistake. **Every topic card ends with one** |
| Practice question | `<details class="qa"><summary><span class="qm">4m</span>Question</summary><div class="qa-body">Answer<p class="qa-tip"><b>Marking tip:</b> …</p></div></details>` | Hidden answer on the web, always shown in the PDF |

**Standard topic card:** key facts → table(s) → example → Watch out.

## 7. Writing rules

**Accuracy**

- Check every topic against the school's scope sheet first. Mark anything out of scope (e.g. "Probability is not tested").
- Use Singapore examples that are well known and stable (HDB, ERP, COE, MRT, Tengah, Punggol, LTMP 2040).
- If a figure is approximate, say so ("about", "close to 8 in 10"). If the exam gives the data, show the answer *structure* rather than inventing numbers.
- When writing from general knowledge rather than the textbook, add a note to check against class notes.

**Language**

- Write for a 14-year-old: short sentences, plain words, active voice.
- British/Singapore spelling: urbanisation, colour, programme, organise.
- Use the exam's own terms: identify, describe, explain, evaluate, sustainable, accessibility.
- Bold the key term the first time it appears in a card.
- Chinese content (Higher Chinese) is written in Chinese.

**Exam answers**

- Match points to marks: about 1 mark per point, 2 marks per developed "explain" point.
- Describe data with **TEA**: Trend, Evidence (data with units), Anomaly.
- Explain with **PEE**: Point, Explain, Example.
- Essays (level-descriptor questions): both sides with examples and a limitation each, then a judgement with a reason ("because it benefits the most people").
- Practice questions give a model answer *and* a one-line marking tip.

## 8. Design rules

- All colours are CSS variables on `:root`, with a dark-mode set under `prefers-color-scheme: dark` and `[data-theme="dark"]`. Never hard-code a colour inside a card.
- Background is a faint graph-paper grid. Cards are white with a thin border. No shadows except focus states.
- Layout must work at phone width (about 400 px) with a 16 px side margin and no sideways scrolling. Wide tables sit inside `.tw` so they scroll on their own.
- Each subject keeps the same header, navigation (All topics, strand filters, search) and footer, so the sites feel like one product.
- Subject colours on the hub: Maths blue, Science green, Geography teal.

## 9. Adding a new subject

1. Copy an existing site folder (geography is the most complete) and rename it, e.g. `sec2-history-site`.
2. In `app.py`, update the docstring and pick an unused port (5004 and up).
3. In `templates/base.html`, update the eyebrow, title, intro and search placeholder.
4. In `static/style.css`, replace the strand colour variables and `.<code> h3` rules.
5. Write `data/topics.json` following sections 5–7.
6. Add the site to the hub. In `sec2-home/app.py`: `history_app = load_site("sec2-history-site", "sec2_history_site")`, then add `"/history": history_app` to the `DispatcherMiddleware` map.
7. Add a tile in `sec2-home/templates/home.html`, and set the subject's `link` in `sec2-home/plan.py`.
8. Add the subject to `SITES` in `tools/export_pdf.py`.
9. Run the checks in section 11.

## 10. Exporting PDFs

```bash
cd ~/Documents/O-LEVEL
pip install playwright && playwright install chromium   # first time only
python tools/export_pdf.py geography                     # or math, science
```

- Output: A4, light theme, page numbers, all practice answers shown, saved as `Sec 2 <Subject> Cheat Sheet.pdf`.
- **grid** layout (maths, science): two columns, cards never split. Best for short cards.
- **column** layout (geography): one column, each section starts on a new page, long cards may continue on the next page but tables and tip boxes never split. Best for text-heavy subjects.
- Look through the PDF before printing: no empty card outlines at page bottoms, no headings alone at the bottom of a page.

## 11. Checks before you finish

- [ ] Every page loads: `/`, each strand filter, a topic page, a search, and a bad URL (should show the not-found message).
- [ ] Content matches the school scope sheet. Nothing out of scope is presented as tested.
- [ ] Every topic card ends with a Watch out.
- [ ] The page reads correctly in dark mode and at phone width.
- [ ] The PDF is re-exported if content changed.
- [ ] The hub tile text and revision plan still describe the subject correctly.

## 12. Key dates (from school documents)

| Date | Event |
|---|---|
| 30 Sep – 8 Oct 2026 | EOY exam (60% of the year's result) |
| 22 – 26 Oct 2026 | Sec 3 subject combination option exercise |
| 3 Nov 2026 | Subject combination results (sent to student's email) |

Promotion to Sec 3: pass English, and 50% or more on the average of all subjects. Triple Science guide: at least A2 in Science and A2 in Maths.

## 13. Known gaps

- **Maths:** the cheat sheet still includes probability (not tested) and is missing the quadratic formula, graphical solution of quadratics, congruence proofs, angles of elevation and depression, and Sec 1 topics such as standard form.
- **Science:** the site covers Sec 1 (Books 1A, 1B, Chapters 1–8) and Sec 2 (Books 2A, 2B, Chapters 9–16), one card per sub-chapter. The EOY scope (Chapters 2–4 and 7–8) matches Book 1A Ch 2–4 and Book 1B Ch 7–8; those cards carry an EOY badge and the `/science/eoy` filter. Cards are written from the contents pages and the MOE syllabus, not the textbook text.
- **Geography:** written from the scope sheet's chapter titles and public school papers, not the school textbook. Check examples against class notes.
- **Not yet built:** English, Higher Chinese, History, English Literature cheat sheets.
- **Revision plan:** exam-week days follow a routine because the paper-by-paper timetable wasn't available.

## 14. Useful sources

- MOE Lower Secondary Geography syllabus: <https://www.moe.gov.sg/-/media/files/secondary/syllabuses/humanities/2021-lower-secondary-geography-syllabus.pdf>
- MOE Lower Secondary Science syllabus (G2/G3): <https://www.moe.gov.sg/-/media/files/secondary/fsbb/syllabus/2021-g2g3-lower-secondary-science-syllabus-updated-apr-2024.pdf>
- Holy Grail (free past papers, Sec 1–2): <https://grail.moe/notes/sec-1-2/geography>

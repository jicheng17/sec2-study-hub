"""Sec 2 EOY revision plan data (from the 2026 S2 EOY Exam Scope & Format sheet).

Edit the lists below to change the plan; the page picks up changes on restart.
Task ids must stay unique — they are used to remember ticked boxes in the browser.
"""

EXAM_START = "2026-09-30"
EXAM_END = "2026-10-08"

# ---- Before the exams: two full days --------------------------------------
PREP_DAYS = [
    {
        "id": "d1",
        "date": "2026-09-28",
        "label": "Mon 28 Sep",
        "focus": "Close the maths gaps and start the science scope",
        "hours": "about 2½ hours",
        "tasks": [
            ("d1-1", 45, "Maths", "Learn the extra topics not on the cheat sheet: quadratic formula, solving a quadratic by drawing a straight line on its graph, congruence proofs, angles of elevation and depression (see the Maths card below)."),
            ("d1-2", 30, "Maths", "Sec 1 recap: standard form, gradient formula, percentages, ratio and speed."),
            ("d1-3", 45, "Science", "Read the EOY scope cards on the science cheat sheet: Book 1A Ch 2–4 and Book 1B Ch 7–8."),
            ("d1-4", 20, "All", "Write one weak-topic list per subject. Pack files, calculator and stationery."),
        ],
    },
    {
        "id": "d2",
        "date": "2026-09-29",
        "label": "Tue 29 Sep",
        "focus": "Practise under time, then touch every other subject once",
        "hours": "about 3 hours",
        "tasks": [
            ("d2-1", 50, "Science", "20 MCQs plus 2 free-response questions from chapters 2–4 and 7–8. Mark them and add errors to the weak-topic list."),
            ("d2-2", 40, "Maths", "Timed: 8 short-answer questions in 30 minutes, then one real-world problem (the last Section B question type)."),
            ("d2-3", 30, "Higher Chinese", "词语 from 课文 and 《生活空间》. Revise the formats for 私人电邮 and 反映建议类公务电邮."),
            ("d2-4", 30, "English", "One grammar MCQ set, then plan two essays in 10 minutes each."),
            ("d2-5", 20, "Humanities", "Geography key terms for chapters 7–11. History chapters 8–9 main events in order."),
            ("d2-6", 0, "All", "Lights out by 10.30 pm. Aim for at least 8 hours of sleep."),
        ],
    },
]

# ---- During the exam window ----------------------------------------------
EXAM_DAY_ROUTINE = [
    ("After school", "Eat, rest 30–45 minutes. No revision straight after a paper."),
    ("90 minutes", "Tomorrow's paper: work through that subject's checklist below."),
    ("30 minutes", "Light preview of the paper after that: key terms or formulas only."),
    ("By 9.30 pm", "Stop new material. Pack for tomorrow, check the calculator."),
    ("After each paper", "Spend 5 minutes noting what felt hard, then move on."),
]

WEEKEND = {
    "label": "Sat 3 – Sun 4 Oct",
    "tasks": [
        ("w-1", "Two 90-minute blocks each day on the heaviest papers still to come (usually Maths, Science or Higher Chinese)."),
        ("w-2", "One full timed section from a past paper for the next big subject."),
        ("w-3", "Sunday evening: redo every question on the weak-topic lists. Early night."),
    ],
}

# ---- Night-before checklists, one per subject -----------------------------
SUBJECTS = [
    {
        "slug": "maths", "name": "Mathematics", "color": "na",
        "paper": "2 h 15 min · 90 marks · Section A 45 (13–15 short questions) · Section B 45 (6–7 long questions, last one a real-world problem) · calculator allowed",
        "scope": "All Sec 2 topics except probability, plus the quadratic formula, graphical solution of quadratics, congruence proofs, angles of elevation and depression, and all Sec 1 topics.",
        "link": "/math/",
        "tasks": [
            ("m-1", "Quadratic formula: x = (−b ± √(b² − 4ac)) ÷ 2a. Practise 3 questions, giving answers to 2 decimal places."),
            ("m-2", "Graphical method: draw y = ax² + bx + c, add the straight line, read the x-values where they cross."),
            ("m-3", "Congruence proofs: state each pair of equal sides or angles with a reason, then the test (SSS, SAS, AAS, RHS), keeping vertex order."),
            ("m-4", "Elevation and depression: the angle of depression from A equals the angle of elevation from B (alternate angles). Use tan most often."),
            ("m-5", "Sec 1: standard form (A × 10ⁿ, 1 ≤ A < 10), gradient formula, percentages, speed."),
            ("m-6", "Do one misleading-graph question. There is one in Section A."),
            ("m-7", "Skip probability. It is not tested."),
        ],
    },
    {
        "slug": "science", "name": "Science", "color": "sci",
        "paper": "Section A MCQ 30 marks · Section B structured 40 marks · Section C free-response 30 marks",
        "scope": "Book 1A Ch 2–4 (physical properties, chemical composition, separation techniques) and Book 1B Ch 7–8 (particulate nature of matter, atoms and molecules).",
        "link": "/science/eoy",
        "tasks": [
            ("s-1", "Density: learn ρ = m ÷ V, the displacement method, and float or sink. Practise 2 calculations with units (g/cm³)."),
            ("s-2", "Elements, compounds and mixtures: the comparison table, particle diagrams, and purity (fixed melting and boiling points)."),
            ("s-3", "Separation: match each mixture to its technique (filtration, evaporation, crystallisation, distillation, chromatography), plus Singapore's Four National Taps and NEWater steps."),
            ("s-4", "Particles: solid, liquid and gas table, changes of state, diffusion and gas pressure, explained using particle movement and spacing."),
            ("s-5", "Atoms: protons, neutrons and electrons, proton and nucleon numbers, electron arrangement (2, 8, 8), and counting atoms in formulas like 3H₂O."),
        ],
    },
    {
        "slug": "english", "name": "English", "color": "en",
        "paper": "Paper 1 1 h 20 min (grammar MCQ 30 questions, 1 essay) · Paper 2 1 h 15 min (comprehension)",
        "scope": "Units 1–6.",
        "link": None,
        "tasks": [
            ("e-1", "One grammar MCQ set: tenses, subject–verb agreement, prepositions, connectors."),
            ("e-2", "Plan two essays in 10 minutes each: clear introduction, 3 body paragraphs, conclusion."),
            ("e-3", "Comprehension: practise one \"in your own words\" question and one inference question."),
            ("e-4", "Skim the vocabulary and notes from Units 1–6."),
        ],
    },
    {
        "slug": "hcl", "name": "Higher Chinese", "color": "hcl",
        "paper": "试卷一 60分（实用文 20分，作文 60分）· 试卷二 70分（综合填空、看拼音填词语、词语替换、阅读理解一和二、片段缩写）",
        "scope": "中一中二课文、校本篇章、校本作业、《生活空间》词语；人物描写、修辞手法、写作手法、说明方法、说明顺序、议论文三要素、论证方法、新闻结构。",
        "link": None,
        "tasks": [
            ("h-1", "词语：听写课文和《生活空间》的词语，看拼音写词语。"),
            ("h-2", "实用文：背熟私人电邮和反映建议类公务电邮的格式。"),
            ("h-3", "作文：为议论文列一个提纲（论点、论据、论证）。"),
            ("h-4", "复习修辞手法、说明方法、论证方法的名称和作用。"),
            ("h-5", "做一篇片段缩写练习，控制字数。"),
        ],
    },
    {
        "slug": "geography", "name": "Geography", "color": "geo",
        "paper": "Structured questions (identify, describe and compare, explain) · 1 evaluation essay on Chapter 9 housing",
        "scope": "Chapters 7–11 (Chapter 11 up to page 139). Investigation skills: sampling, data representation, reliability testing, scatter graphs.",
        "link": "/geography/",
        "tasks": [
            ("g-1", "Key terms and one Singapore example for each of chapters 7–11."),
            ("g-2", "Describe and compare: quote figures from the data, and use \"whereas\" or \"higher than\"."),
            ("g-3", "Plan one Chapter 9 housing evaluation essay: both sides, then a clear judgement."),
            ("g-4", "Investigation skills: sampling methods, how to improve reliability, reading a scatter graph."),
        ],
    },
    {
        "slug": "history", "name": "History", "color": "his",
        "paper": "Section A source-based case study 17 marks (purpose, comparison, reliability) · Section B essay 8 marks (explain two reasons)",
        "scope": "Chapters 8 and 9.",
        "link": None,
        "tasks": [
            ("hi-1", "Chapters 8–9: list the main events in order, with causes."),
            ("hi-2", "Practise one purpose question: who wrote it, to whom, why, and what they wanted the audience to do."),
            ("hi-3", "Reliability: check the source against provenance and other sources, then give a clear answer."),
            ("hi-4", "Essay: write two paragraphs, one reason each, with evidence and a link back to the question."),
        ],
    },
    {
        "slug": "literature", "name": "English Literature", "color": "lit",
        "paper": "Section A Emily of Emerald Hill 25 marks (essay or passage-based) · Section B unseen poetry 25 marks (both parts)",
        "scope": "Emily of Emerald Hill and unseen poetry.",
        "link": "/literature/",
        "tasks": [
            ("l-1", "Emily of Emerald Hill: 3–4 short quotes each for the main themes and for Emily's character."),
            ("l-2", "Plan one essay answer and one passage-based answer."),
            ("l-3", "Unseen poem: practise one, covering what it's about, the tone, and 2 techniques with their effect."),
            ("l-4", "Each paragraph: point, quote, explain the word choice, link to the question."),
        ],
    },
    {
        "slug": "msp", "name": "Malay Special Programme", "color": "msp", "optional": True,
        "paper": "Paper 1 20 marks (Instapos, picture essay) · Paper 2 40 marks · Paper 3 30 marks (listening, oral)",
        "scope": "Sec 1 Unit 7 and Sec 2 Units 1–5. Skip this if not taking MSP.",
        "link": None,
        "tasks": [
            ("ms-1", "Revise vocabulary from Sec 1 Unit 7 and Sec 2 Units 1–5."),
            ("ms-2", "Practise one Instapos and plan one picture essay."),
            ("ms-3", "Read one passage aloud for the oral."),
        ],
    },
]

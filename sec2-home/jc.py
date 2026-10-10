"""Junior college admission data for the /jc page. Edit here to update the page."""

SOURCE = "2026 JAE (2025 O-Level cohort) L1R5 cut-off points, from a Singapore Hokkien Huay Kuan / Nan Chiau High School slide"

# (JC, Science cut-off, Arts cut-off). None = stream not offered through the JAE.
CUTOFFS_2026 = [
    ("Anderson Serangoon", 9, 10),
    ("Anglo-Chinese", 7, 9),
    ("ACS (Independent)", 5, None),
    ("Catholic", 11, 12),
    ("Dunman High", 6, 8),
    ("Eunoia", 5, 6),
    ("Hwa Chong Institution", 3, 5),
    ("Jurong Pioneer", 14, 14),
    ("Nanyang", 5, 7),
    ("National", 6, 8),
    ("Raffles", 3, 5),
    ("River Valley High", 8, 9),
    ("St. Andrew's", 8, 10),
    ("St. Joseph's Institution", 6, None),
    ("Tampines Meridian", 12, 12),
    ("Temasek", 7, 7),
    ("Victoria", 6, 8),
    ("Yishun Innova", 19, 18),
]


def band(score):
    if score <= 4:
        return "Most competitive"
    if score <= 6:
        return "Very competitive"
    if score <= 9:
        return "Competitive"
    return "Moderate"


GRADES = [("A1", 1), ("A2", 2), ("B3", 3), ("B4", 4), ("C5", 5), ("C6", 6), ("D7", 7), ("E8", 8), ("F9", 9)]

BONUS_NOW = [
    ("CCA: Excellent", "2"),
    ("CCA: Good", "1"),
    ("English and Higher Mother Tongue, grade A1 to C6", "2"),
    ("Chinese or Malay Special Programme, grade A1 to C6", "2"),
    ("Choosing an affiliated JC as 1st choice", "2"),
    ("Maximum (any combination of the above)", "4"),
    ("CLEP-JC: applying through the JAE to a JC that offers the Chinese Language Elective Programme, for admission to that JC", "+2 on top of the cap"),
]

# Your child's path (Sec 1 in 2025)
TIMELINE = [
    ("2026", "Sec 2", "EOY exam; Sec 3 subject option exercise 22–26 Oct"),
    ("2027", "Sec 3", "Start of the 2-year SEC subjects"),
    ("2028", "Sec 4", "Sits the SEC exam (replaces O-Levels)"),
    ("2029", "Post-sec", "Applies to JC using L1R4"),
]

CHANGES = [
    ("Score", "L1R5: 6 subjects", "L1R4: 5 subjects"),
    ("Subjects", "L1 + R1 humanities, R2 maths/science, R3 humanities or maths/science, R4 and R5 any", "L1 + R1 humanities, R2 maths/science, R3 humanities or maths/science, R4 one more listed subject"),
    ("Best possible score", "6", "5"),
    ("JC qualifying score", "20 or better", "16 or better"),
    ("Bonus point cap", "4", "3 (Language Elective Programme still adds 2 extra)"),
    ("Exam", "O-Level", "SEC (Singapore-Cambridge Secondary Education Certificate)"),
]

SOURCES = [
    ("MOE: JAE admission criteria and bonus points", "https://beta.moe.gov.sg/post-secondary/admissions/jae/admission-criteria/"),
    ("L1R4 JC admission from 2028: parent guide (Ancourage Academy)", "https://ancourage.academy/articles/l1r4-jc-admission-2028-parent-guide-singapore"),
    ("How L1R5 works and how to read cut-off points (EDU FIRST)", "https://www.edufirst.com.sg/blog/jc-cut-off-points-how-l1r5-works-and-how-to-read-the-numbers/"),
]


# ---- Our plan: CLEP (Chinese Language Elective Programme) ----
CLEP_JCS = ["Dunman High", "Hwa Chong Institution", "Nanyang", "Temasek", "Jurong Pioneer"]

# From the Nan Chiau High School (NCHS) "MOE Special Programmes @ NCHS" slide
CLEP_NCHS = [
    "Offered at NCHS since 2020 (华文语文特选课程)",
    "Students must read <b>Literature in Chinese</b> as an anchor subject, either full or elective",
    "Outstanding students are awarded <b>MOE CLEP-Sec scholarships</b>",
    "Students who apply for CLEP-JC through the JAE get <b>2 CLEP bonus points</b> for admission to that JC",
]

# (when, step, done-by)
CLEP_STEPS = [
    ("Now: Sec 2 EOY (Oct 2026)", "Aim for <b>A2 or better in Chinese</b>, or <b>B3 or better in Higher Chinese</b>. CLEP-Sec selection uses Sec 2 results"),
    ("Oct 2026", "Ask the NCHS Chinese department how and when Sec 2 students are invited or apply for CLEP-Sec. Do this before or during the Sec 3 option exercise (22–26 Oct)"),
    ("2027–2028: Sec 3–4", "Take <b>Literature in Chinese</b> (full or elective) and keep Higher Chinese strong. Look out for the MOE CLEP-Sec scholarship"),
    ("SEC results (2028)", "To qualify for CLEP-JC: B3 in Higher Chinese; or B4 in Higher Chinese and B3 in Literature in Chinese; or A2 in Chinese"),
    ("JAE (Jan 2029)", "On the JAE form, <b>indicate interest in CLEP</b> and put a CLEP JC as <b>first choice</b>. If selected: +2 bonus points for that JC"),
]

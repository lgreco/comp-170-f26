# COMP 170 (Fall 2026) — Coursework Repo

This repo holds weekly assignments (`week01/`, `week02/`, `week03/`, …) and
reusable reference material (`tutorials/`) for an intro programming course
taught in Python. The audience is first-time programmers — write and edit
everything with that in mind.

## Read this first, every session

Before writing or editing anything in this repo, read the classroom
recording transcripts and summaries at
**`../classroom-recordings/comp170f26/`** (sibling directory to this repo,
note the hyphen — not `classroom_recordings`). Each class date has a
`YYYY-MM-DD-summary.md` (read this first, it's short) and a matching
`YYYY-MM-DD-transcript.txt` (fuller detail when the summary isn't enough).
At minimum, read the **most recent** summary before touching an assignment
file — read further back when you need to confirm what's already been
taught, what hasn't, or the exact wording/analogy Leo used for a concept.

This matters because:

- **Sequencing is strict.** Assignments must only use concepts already
  covered in class. As of the latest recording (2026-09-11), the class has
  covered: variables/types/arithmetic, the interactive shell vs. script
  files, `input()`/`int()`/`float()` conversion, ASCII/`ord()`, constants,
  a first hand-written function (`check()` in `our_first_function.py`),
  Boolean values, and a first `for` loop. `try`/`except`, comprehensions,
  classes, and other not-yet-taught features should not appear in
  assignments or examples until the transcripts show they were introduced.
- **Due dates and logistics get corrected live in class.** E.g., a wrong
  Sakai due date was announced and fixed in the 2026-09-11 session. Don't
  trust a stale assignment file's due date over what the most recent
  transcript/summary says.
- **Wording and analogies are part of the pedagogy.** Assignments echo the
  specific phrasing and analogies used in lecture (e.g., "the anyone from
  Bloomington?" example for short-circuit validation, "taking attendance"
  for loops). Reusing them, rather than inventing new ones, keeps the
  written material consistent with what students heard.

## Repo layout

- `week0N/` — one folder per week. Each holds that week's assignment
  `.md` file(s), instructor-provided starting-point `.py` program(s) (e.g.
  `age.py`, `our_first_function.py`), and — once Leo provides them —
  solution file(s) for that week's assignment.
- `tutorials/` — standalone reference docs (`intro-linux.md`,
  `intro-vim.md`, `intro-nano.md`, `intro-python.md`) that get copied or
  linked into early weeks rather than rewritten each time.
- `README.md` — minimal, not a syllabus.

## Assignment `.md` file conventions

Follow the shape already established in `week03/temperature_conversion.md`:

1. `# Assignment: <Topic>` title, then a `Due <Weekday, Month Day>.` line.
   Assignments run Friday to Friday.
2. A short framing paragraph connecting the new work to what was just
   covered in class, naming the file that serves as the model to follow.
3. Numbered, concrete steps per part, using `## Part N — <name> (given)` or
   `(yours to work out)` to distinguish handed-to-you formulas/logic from
   ones students must derive themselves.
4. State the hard rules explicitly where they apply, don't assume they're
   remembered: no naked numeric/string literals in a computation except
   `0`, `1`, `-1`; every other literal gets a well-named `ALL_CAPS`
   constant declared at the top of the file. This rule is enforced
   seriously — it's called out as a failing-grade issue in the follow-on
   course (COMP 271).
5. Optional `## A question to think about (no need to write code for it)`
   — a reflection question that previews the next class session, meant to
   be answered verbally, not in code.
6. `## Reading`, split into:
   - `### New this week` — this week's official docs / textbook links.
   - `### Previously assigned (cumulative)` — a nested list, one bullet
     per earlier week, carrying forward that week's reading links. Add a
     new week's bullet to this list rather than replacing it; it's meant
     to keep growing. This cumulative list isn't limited to textbook/docs
     readings — fold in earlier **tutorials** (e.g. `tutorials/intro-vim.md`,
     `week01/intro-linux.md`) and earlier **exercises** (e.g.
     `week02/variables_arithmetic_finger_practice.md`,
     `week02/interactive_shell_reading.md`) whenever the current
     assignment builds on skills those covered, so a student can jump
     straight back to the relevant one instead of hunting for it.
7. `## Turning it in` — explicit submission mechanism (Sakai) and a
   concrete self-check ("run it twice, confirm these numbers come back").
8. Once Leo has provided a solution file for a given assignment, add a
   `## Solution` section (placed after `Turning it in`) linking to it —
   see **Solutions**, below. Leave this section out entirely until a
   solution actually exists; don't add a placeholder or stub link.

Link every in-repo file reference as a relative markdown link
(`[`age.py`](age.py)`, `[interactive_shell_reading.md`](../week02/interactive_shell_reading.md)`)
so it's clickable on GitHub. Link external readings straight to the source
(O'Reilly for Lubanovic's *Introducing Python*, Green Tea Press for *Think
Python*, docs.python.org for official docs) — don't paraphrase a citation
without a link.

## Tutorial `.md` file conventions

`tutorials/*.md` (and their week01/week02 copies) share one header
skeleton — reuse it rather than inventing a new structure for a new tool:

`What Is X?` → `The One Thing You Must Understand First: …` → `Opening a
File` / `Your First … Session, Step by Step` → `Essential Commands` →
`Recovering from Common Problems` → `A Minimal Workflow for This Course` →
`What X Looks Like in Practice` → `Cheat Sheet (One Page)` → `Going
Further (Optional)`.

## Python file conventions

Match `week03/age.py` and `week03/our_first_function.py`:

- Comments do most of the teaching. They explain *why*, in first-person,
  plain-English narration tied to how the class arrived at the code (e.g.
  "we invented this ourselves," "the same way taking attendance works") —
  not just restating what the line does.
- Constants: `ALL_CAPS`, declared at the top of the file, one per literal
  that isn't `0`, `1`, or `-1`.
- Straight-line, simple procedural style at this stage of the course —
  no `try`/`except`, no defensive coding beyond what's been taught.
  Input validation is done by hand-rolled checks (loops + `ord()`-based
  comparisons), because exceptions haven't been introduced yet.
- A little dry humor in student-facing `print()` messages and comments is
  in character for this repo — don't sand it down to something generic.

## Solutions

Leo will provide reference solution `.py` files for past assignments over
time — they don't all exist yet. Convention for handling them:

- A solution for `week0N/some_assignment.md` lives alongside it in the
  same `week0N/` folder (e.g. `week03/celsius_to_fahrenheit_solution.py`
  next to `week03/temperature_conversion.md`), unless Leo says otherwise.
  If a week ends up with several solution files, it's fine to collect
  them in a `week0N/solutions/` subfolder instead — match whichever
  pattern already exists in the repo at the time, and ask if neither
  pattern is established yet.
- When a solution file is added for an assignment that doesn't yet link
  to it, add the `## Solution` section described above (relative markdown
  link, brief description) rather than leaving it undiscoverable.
- Never fabricate, stub, or pre-write a solution yourself and pass it off
  as Leo's — this section is specifically for linking solutions *he*
  supplies. Writing original worked solutions on request is a separate,
  explicit task, not something to do proactively while editing assignment
  files.
- Solutions should stay out of `## Reading`'s cumulative list — that list
  is for tutorials, past exercises, and outside readings a student
  consults *before* solving a problem; a solution is what they check
  *after*.

## Working in this repo

- Don't introduce a concept, function, or shortcut ahead of when the
  transcripts show it was taught, even if it's the "better" way to write
  something — the point is matching the course's current level, not
  writing idiomatic Python.
- When a due date, submission mechanism, or other logistic is unclear or
  possibly stale, check the most recent transcript/summary before
  guessing.

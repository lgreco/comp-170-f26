# Week 7 Assignment, Part 1 — Midterm Reflection and Self-Assessment

Due Monday, October 12.

This assignment has two parts, published together on Friday, October 9, with two different due dates. This part — the midterm reflection called for in the course's ungrading policy — is due Monday, October 12. Part 2, the week's technical work, is due Friday, October 16, the usual Friday-to-Friday cadence.

Grades in this course are not accumulated from scores on individual assignments; they are proposed by you, based on your own honest account of your engagement with the course, and then reviewed by me. This essay is that account at the midpoint of the term.

Write your reflection as a single essay — not a checklist — of roughly 400–600 words. Address each of the five areas below with specific detail: not just a number, but what that number reflects about how you've engaged with the course so far. Submit it through Sakai by Monday, October 12.

## What to cover

**Attendance.** How many class meetings have you missed this term, and how does that compare against the course's attendance policy? If you've missed meetings, say why in as much or as little detail as you're comfortable sharing, and how you recovered what you missed (notes from a classmate, catching up on your own, etc.).

**Homework submission.** How many assignments have you submitted, and how many — if any — have you missed? If you missed one, what happened, and did you make any attempt to catch up even without credit for doing so?

**Adherence to feedback.** This is the heart of how ungrading works in this course: progress is measured by whether the issues identified in feedback on one assignment show up again in the next one. Look back over the feedback you've received so far. Did you make the same mistake — technical or otherwise (e.g., multiple returns in a method, a missed constant, a late submission, a submission mechanics error) — more than once? Be specific about which issue, and whether you changed how you worked in response to it.

**Time spent outside class.** Roughly how many hours per week, outside of class meetings, have you been spending on this course — reading, practicing, working through assignments? Is that consistent week to week, or does it vary? If you're not sure, say so rather than guessing a number that sounds better.

**Class participation and engagement.** Do you offer to answer questions in class, especially when you're not sure you have the exact right answer? Do you stay engaged during class — not distracted by your phone, laptop, or other non-class activities? If your participation and engagement haven't been what you hoped, what's your plan to improve them for the rest of the term — and, being honest with yourself, do you actually want to improve them in the first place?

## Proposing your midterm grade

Based on your answers above, close the essay by proposing a midterm grade. For this reflection, there are three possible grades — A, C, or D:

- **A** — You have missed fewer than 6 class meetings. You have not missed any homework assignment. Where feedback identified a mistake, you did not repeat it. You have consistently spent 6 or more hours per week studying or reading for the course outside of class time.
- **C** — You have missed 6–10 class meetings and/or 1 assignment. You repeated a mistake that had already been identified in feedback, at least once. You are unsure how much time you've spent studying or reading for the course outside of class.
- **D** — You have missed 11 or more class meetings and/or more than 1 assignment.

A is an acknowledgment of good work; C is a pass; D is a fail. If your term so far is a mix of these descriptions — doing well in some areas and not others — say so plainly and propose the band that best reflects the overall picture, with your reasoning. As with every reflection in this course, your proposal is a starting point for my own determination, not a final grade.

---

## Part 2 — Technical work (due Friday, October 16)

Due Friday, October 16.

In class this week we took [`sears_tower.py`](../week06/sears_tower.py) — correct, but doing everything in one or two functions — and split it into separate files, one per concern, tied together with Python's `import *`. Four of those files are already in this folder:

- [`sears_facts.py`](sears_facts.py) — the facts concern. Nothing but constants: the real tower's height, width, and aspect ratio, and the proportionality constants every tier's height and width are derived from. No program logic lives here.
- [`input_concern.py`](input_concern.py) — the input concern. `get_input()` is complete; it asks for a height and won't return until it has a usable one.
- [`compute_dimensions.py`](compute_dimensions.py) — the logic concern, split in two. `compute_widths(height)` is complete and is your model for the function you're about to write.
- [`output_concern.py`](output_concern.py) — the output concern. `draw_tower(widths, heights, building_block)` is a stub — yours to complete.

You will also create a fifth file, `tower.py`, for the manager (a stub is already here as a starting point).

### What to do

**1. Complete `compute_heights(height)` in `compute_dimensions.py`.** Using `BOTTOM_TIER_HEIGHT_SCALE`, `MIDDLE_TIER_HEIGHT_SCALE`, and `TOP_TIER_HEIGHT_SCALE` from `sears_facts`, split `height` into the three tier heights and return them as a list, bottom/middle/top — the same shape `compute_widths` already returns, and the same `import *` access to `sears_facts`'s constants that `compute_widths` already uses.

**2. Write `draw_tower(widths, heights, building_block)` in `output_concern.py`.** It takes the widths list, the heights list, and a character, and prints the tower — no computing, only printing. The stub's docstring has the detail. Note: building this one may get easier after the Monday, October 12 and Wednesday, October 14 class meetings cover techniques it needs — attempt it now with what you already know (indexing into a list with a loop variable, a nested loop for the rows within a tier), and come back to it after those two meetings if it isn't working yet.

**3. Write the manager in `tower.py`.** Import what you need from the other four files (see the stub already in `tower.py` for the `import` lines), then write a function that calls `get_input()`, `compute_widths()`, `compute_heights()`, and `draw_tower()` in order, passing data between them. This function should do no computing and no printing itself — only call the other four, the same "conductor" idea from class.

## Rules that apply

- **Every function follows the single-return rule, with no exceptions for guard conditions** — a guard condition gets expressed as a pessimistic default that's conditionally overwritten, never an early `return`. `get_input` in `input_concern.py` is the pattern to copy.
- **No naked numbers or strings** except `0`, `1`, `-1` — same rule as Week 6, still enforced.
- **Function names stay verb-like**; nothing is named `print`.

## A question to think about (no need to write code for it)

Neither `compute_widths` nor `compute_heights` ever has to check whether `height` is legit. Why not — and what would break if someone called either one directly, skipping `get_input()` first?

## Reading

### New this week (Week 7)

- `sears_facts.py`, `input_concern.py`, `compute_dimensions.py`, `output_concern.py` — this week's starter code.
- [Lubanovic, *Introducing Python*, 3rd edition, Ch. 8, "Lists"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html) — list creation and indexing, for the two functions that return lists.

### Previously assigned (cumulative)

Still fair game for questions in class or on assessments. Carried forward from each earlier week's assignment:

- Week 6 — from [the skyscrapers assignment](../week06/skyscraper_towers.md):
  - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) — comments, docstrings, and naming.
  - [`sears_tower.py`](../week06/sears_tower.py) and [`sears_tower.ipynb`](../week06/sears_tower.ipynb).
  - [Lubanovic, *Introducing Python*, 3rd edition, Ch. 6, "If and Match"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch06.html)
- Week 5 — from [the functions-that-draw-shapes assignment](../week05/README.md):
  - [Lubanovic, *Introducing Python*, 3rd edition, Ch. 10, "Functions"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html), specifically: "Define a Function with def," "Call a Function with Parentheses," "Arguments and Parameters," and "Docstrings."
  - [Python's own tutorial section on defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) and [its follow-up on default values, keyword arguments, and scope](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) — these two may read a bit more technical than you need at this point; the Lubanovic sections above cover everything required for this assignment, so don't let that stop you.
  - [Stanford's short walkthrough of function syntax](https://cs.stanford.edu/people/nick/py/python-function.html)
  - [OpenStax's own function-definition chapter section](https://openstax.org/books/introduction-python-programming/pages/6-1-defining-functions)
  - [Think Python, 3rd edition, Ch. 3, "Functions"](https://greenteapress.com/wp/think-python-3rd-edition/)
  - [`functions.py`](../week05/functions.py) and [`block.py`](../week05/block.py).

## Turning it in

Upload `compute_dimensions.py`, `output_concern.py`, and your new `tower.py` to Sakai.

Self-check before you upload. From this folder, run `tower.py` — confirm it draws a correctly centered tower, and that typing `0` or a negative number when asked for a height loops back and asks again instead of crashing or drawing nothing.

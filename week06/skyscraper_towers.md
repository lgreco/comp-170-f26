# Assignment: Skyscrapers, Centered

Due Friday, October 9.

Two parts, both in one file, `skyscrapers.py`. The model to follow is
[`sears_tower.py`](sears_tower.py) (also in
[`sears_tower.ipynb`](sears_tower.ipynb), where we built it in class on
9/30 and 10/2): `draw_tier(height, width, building_block)` draws one
tier, and `draw_sears_tower(height, aspect_ratio, building_block)` calls
it three times to draw the whole building. Copy `sears_tower.py` into
your own `skyscrapers.py` and start from there.

Right now the tower is mathematically correct but, as we put it in class,
looks like a toothpick: each tier prints flush against the left edge,
with no notion of a center. Both parts of this assignment are about
fixing that — first for the Sears Tower, then for a second building.

## Part 1 — Center the Sears Tower (yours to work out)

Modify `draw_sears_tower` so that every tier sits centered on the tier
below it, at any height. Work it out on paper the way we did on the
whiteboard: a tier of width *w* needs *(base width − w) / 2* blank
characters in front of it to sit centered on a base of that width — and
each tier is the "base" for the one above it. Two examples, just to show
roughly what centered output looks like (these are samples, not targets —
your own numbers will come out of your own arithmetic):

```
                       ***
                       ***
                       ***
                       ***
                       ***
  ***                *******
  ***                *******
  ***                *******
 *****               *******
 *****               *******
 *****               *******  
 *****             ***********
 *****             ***********
*******            ***********
*******            ***********
*******            ***********
*******            ***********
*******            ***********
*******            ***********
*******            ***********
*******            ***********
*******            ***********
height=17          height=22
```


Remember from class: a top tier needs to be at least 3 characters wide to
leave room for two spaced antennas, which pushes the middle tier's
minimum to 5 and the bottom tier's minimum to 7 — `sears_tower.py` already
enforces that 7-character floor with `MINIMUM_ACCEPTABLE_WIDTH`. Centering
has to keep working whether `draw_sears_tower` is called at that minimum
or at a much taller height.

There are two ways to do this, one easier than the other. Get the easier
one working first, confirm it's centered at several heights — including
the smallest height `MINIMUM_ACCEPTABLE_WIDTH` allows — and only then try
the harder one if you want to push further. A working easy version
submitted on time beats an unfinished hard one.

## Part 2 — `draw_hancock` (yours to work out)

Using `sears_tower.py` as your template, write `draw_hancock(height)` to
draw Chicago's other iconic black tower, the John Hancock Center (875 N.
Michigan Avenue) — the building with two huge antennas that Fazlur Khan
and Bruce Graham designed before the Sears Tower.

Start the same way we started the Sears Tower: look up the real building
yourself (Wikipedia, the Chicago Architecture Center, or an AI assistant
are all fair game) and come up with your own height, width, and aspect
ratio. Figuring out those numbers is part of the assignment, not a step
to skip.

Shape-wise, think about what makes the Hancock different from the Sears
Tower's three stacked tiers. As we described it in class: it's a triangle
with the top shaved off — a flat-topped pyramid, but with a much gentler
slope than an actual pyramid. That's a steady, continuous narrowing from
a wide base to a narrower (but not pointed) top, rather than three
distinct jumps in width. Decide for yourself how to turn "steady
narrowing" into rows and loops — that decision is the real content of
this part. And just like the Sears Tower, the top of the Hancock needs to
be wide enough for its two antennas, and every row needs to come out
centered on the base, at any height.

## Rules that apply to both parts

- **No naked numbers or strings** except `0`, `1`, `-1`. Every other
  literal — including `2` — gets a well-named `ALL_CAPS` constant,
  declared at the top of the file. `sears_tower.py` already does this for
  the tier scales; follow the same pattern for anything new you add.
- **Function names are verb-like**, parameter names are nouns, and nothing is
  named `print`.
- **Keep lines within 80 columns**, breaking a long `def` line across
  lines the way `draw_square` does in
  [`functions.py`](../week05/functions.py).
- **Check the height first.** One `if`/`else`, the same shape as
  `draw_square`'s: `if` the height makes no sense (zero or negative),
  print a message telling the client so; `else`, do the drawing. Put the
  whole rest of the function's work inside that `else`, the way
  `draw_square` does.

## Reading

### New this week (Week 6)

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  — just the sections on comments and docstrings, and on naming, which we
  walked through in class on 9/30.
- [`sears_tower.py`](sears_tower.py) and [`sears_tower.ipynb`](sears_tower.ipynb)
  — this week's class code; the notebook also has the full write-up of
  how we derived it.
- [Lubanovic, *Introducing Python*, 3rd edition, Ch. 6, "If and Match"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch06.html)
  — covers the `if`/`else` height check you're writing for both
  `draw_sears_tower` and `draw_hancock`.
- **Recommended, not required:** [Lubanovic, *Introducing Python*, 3rd edition, Ch. 14, "Type Hints and Documentation"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch14.html)
  — the docstrings and type annotations we used on 9/30 in
  `sears_tower.py`.

### Previously assigned (cumulative)

Still fair game for questions in class or on assessments. Carried forward
from each earlier week's assignment:

- Week 5 — from [the functions-that-draw-shapes assignment](../week05/README.md):
  - [Lubanovic, *Introducing Python*, 3rd edition, Ch. 10, "Functions"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html)
    — the first four sections: "Define a Function with `def`," "Call a
    Function with Parentheses," "Arguments and Parameters," and
    "Positional Arguments."
  - [Think Python, 3rd edition, Ch. 3, "Functions"](https://greenteapress.com/wp/think-python-3rd-edition/)
  - [Official Python tutorial, "Defining Functions"](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
    — up to the start of "More on Defining Functions."
  - [`print()`](https://docs.python.org/3/library/functions.html#print)
    — the `end` parameter.
  - [Common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
    — the `s * n` row, for string repetition.
  - [`functions.py`](../week05/functions.py) and
    [`block.py`](../week05/block.py) — Week 5's class code.
- Week 4 — from [`range_strings_practice.md`](../week04/range_strings_practice.md):
  - [Lubanovic, Ch. 4, "Strings"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch04.html) — in full.
  - [Lubanovic, Ch. 7, "For and While"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) — loops, in terms of iterables.
  - [`for_loops_primer.md`](../week04/for_loops_primer.md) — the `for`-loop primer.
  - [`compute_interest.py`](../week04/compute_interest.py) — the compound-interest `for` loop.
  - [`range`](https://docs.python.org/3/library/stdtypes.html#range)
  - [Text sequence type — `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
  - [`ord()`](https://docs.python.org/3/library/functions.html#ord)
  - [`len()`](https://docs.python.org/3/library/functions.html#len)
- Week 3 — from [`temperature_conversion.md`](../week03/temperature_conversion.md):
  - [`input()`](https://docs.python.org/3/library/functions.html#input)
  - [`int()`](https://docs.python.org/3/library/functions.html#int)
  - [`float()`](https://docs.python.org/3/library/functions.html#float)
  - [Lubanovic, type conversions](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html#c03_h_conversions)
  - [Official Python tutorial on input (and output)](https://docs.python.org/3/tutorial/inputoutput.html)
- Week 2 — from [`interactive_shell_reading.md`](../week02/interactive_shell_reading.md):
  - [Lubanovic, Ch. 1, "Introduction"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch01.html) — in full.
  - [Lubanovic, Ch. 2, "Types and Variables"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch02.html) — up to and including "Variables."
  - [Lubanovic, Ch. 3, "Numbers"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html) — integer and float sections only.
  - [Think Python, Ch. 2, "Variables, Expressions, and Statements"](https://greenteapress.com/wp/think-python-3rd-edition/) — complementary, same material from a different angle.

## Turning it in

Upload `skyscrapers.py` to Sakai, containing `draw_tier`, your centered
`draw_sears_tower`, and `draw_hancock`.

Self-check before you upload. From the folder that holds
`skyscrapers.py`, start interactive Python:

```python
from skyscrapers import *
draw_sears_tower(16, SEARS_TOWER_ASPECT_RATIO, '#')
draw_sears_tower(60, SEARS_TOWER_ASPECT_RATIO, '#')
draw_hancock(16)
draw_hancock(60)
```

For each call, check by eye that every tier (or row) is centered on the
one below it, at both a short height and a tall one, and that the top is
wide enough for two antennas. Then call `draw_sears_tower` and
`draw_hancock` with a height of `0` and confirm you get your message
instead of a drawing.

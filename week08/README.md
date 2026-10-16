# Assignment: Airplane Seating Chart

Due Friday, October 23.

Deliverable is a single file, [`airplane_seating.py`](./airplane_seating.py)
(model: the starter code in this folder, which gives you `PASSENGERS`,
`position_to_seat`, and stubs for the rest). Copy the starter into your
own `airplane_seating.py` and start from there.

In class on 10/12 we previewed the idea that a two-dimensional array is
really a one-dimensional array "snaking" through memory, and on 10/14 we
used the real-world example of airplane seat 25A to talk about why 2D
data needs two coordinates instead of one. This assignment makes that
idea concrete: a small airplane's passenger list is stored as one flat
array, `PASSENGERS`, in boarding order — row 1's four seats, then row
2's four seats, and so on, "2+2" style (two seats, the aisle, two more
seats: A, B, C, D). Nowhere does the code store a grid of rows. Instead,
every function in this assignment works out a passenger's row and seat
letter — or a seat's position in the array — using **`//`** (integer
division) and **`%`** (modulo), the two operators we met in class on
10/16.

That day's puzzle was printing a list of names a fixed number of columns
per line: a new line starts whenever `position % names_per_line == 0`.
Here the same remainder idea does double duty. `position // SEATS_PER_ROW`
counts the complete rows that came before a position, and
`position % SEATS_PER_ROW` says how far into the current row it sits.
`position_to_seat`, in the starter file, is given to you complete and
explained line by line — read it slowly before writing anything else,
since everything else in this assignment is that same idea, applied in
reverse or put to use.

## Part 1 — Decode: `position_to_seat(position)` (given)

Already written for you in the starter file. Make sure you understand
*why* it works before moving on:

- `position // SEATS_PER_ROW` (integer division) throws away the remainder
  and tells you how many complete rows of seats come before this position — add `1`
  because rows are numbered starting at 1, not 0.
- `position % SEATS_PER_ROW` keeps only the remainder — how far into the
  *current* row this position sits (0, 1, 2, or 3) — which becomes a
  seat letter by counting that many letters past `'A'`.

Try it in the interactive shell on a few positions by hand first — work
out on paper what row and letter position `6` should be, then check
`position_to_seat(6)` against your own answer — before trusting it on
the rest.

**A handy trick: unpacking a small list.** Say you have a small list and
you want each item under its own name. You could index it:

```python
pair = [2, 'C']
row = pair[0]
seat_letter = pair[1]
```

or do it in one step:

```python
row, seat_letter = [2, 'C']   # row is 2, seat_letter is 'C'
```

The list on the right is split up in order: the first item goes to the
first name, the second item to the second name. The number of names on
the left must match the number of items in the list. It works the same
with variables, e.g. `x, y = [a, b]` gives `x` the value of `a` and `y`
the value of `b`.

`position_to_seat` hands back a two-item list, `[row, seat_letter]`, so
the same trick applies to its result:

```python
row, seat_letter = position_to_seat(6)
```

## Part 2 — Encode: `seat_to_position(row, seat_letter)` (yours to work out)

The reverse direction: a passenger is told "you're in seat 2C," and you
need the position in `PASSENGERS` that corresponds to. Work it out the
same way we worked out centering on the whiteboard for the skyscrapers:
on paper, before code. How many seats come before row `row` even starts?
How many more past that does `seat_letter` add, within the row? Add
those two pieces together.

Once it's written, confirm it actually undoes Part 1: for every valid
seat, `position_to_seat(seat_to_position(row, letter))` should give you
back `[row, letter]`.

## Part 3 — Put them to work (yours to work out)

Using the two functions from Parts 1 and 2:

- **`print_seat_assignments(passengers)`** — print a seating chart in the form:
  
  ```text
  1A         1B        |  1C        1D
  Leo        Saruman   |  Petunia   Ron

  2A         2B        |  2C        2D
  Bellatrix  Hermione  |  Alberich  Tristan

  etc
  ```

  Loop by position (you need the position itself to decode a seat, not just the name), and call `position_to_seat` on each one.

- **`who_is_in_seat(passengers, row, seat_letter)`** — answer "who's in
 seat 1A?" by converting the row/letter to a position with `seat_to_position`, then looking that position up in `passengers`. If the position doesn't actually fall inside `passengers`, say so instead of allowing the program to crash.

**Hint:** study the sample print chart carefully. Replicate it by hand on squared paper, with one character per square.

## Rules that apply

- **No naked numbers or strings** except `0`, `1`, `-1`. `SEATS_PER_ROW`
  and `FIRST_SEAT_LETTER` are already declared as constants in the
  starter file for exactly this reason — use them instead of writing `4`
  or `'A'` again anywhere in your own code.
- **Every function follows the single-return rule**, with no exceptions
  for guard conditions — `who_is_in_seat`'s pessimistic-default `result`
  variable, already started in the stub, is the pattern to finish, the
  same shape as `get_input`.
- **Function names stay verb-like**; nothing is named `print`.
- **You may write new functions** if you so desire.



## Reading

### New this week (Week 8)

- [`airplane_seating.py`](./airplane_seating.py)
  — this week's starter code; `position_to_seat` is this week's main
  worked example of `//` and `%`. Also see the cleaned-up names-per-line
  code from the 10/16 class, which I'll send out separately.
- [Lubanovic, building a list from scratch](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html#c08_h_list_create_list)
  — how `PASSENGERS` itself is built, before any encoding/decoding
  touches it.
- [Python docs, the authoritative list reference](https://docs.python.org/3/builtins/stdtypes.html#lists)
  — the official definition of `list`, straight from the source rather
  than a textbook's retelling of it.
- [Official tutorial on lists and other data structures](https://docs.python.org/3/tutorial/datastructures.html)
  — a related walkthrough covering lists in more depth, plus the other
  data structures built from them.
- [Lubanovic, *Introducing Python*, 3rd edition, Ch. 3, "Numbers"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html)
  — in full this time; it's where `//` and `%` are defined alongside the
  other arithmetic operators.
- [Python docs, "Numeric Types — int, float, complex"](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
  — the operator table partway down the page covers `x // y` and `x % y`
  directly.
- [Wikipedia, modulo as a remainder operation](https://en.wikipedia.org/wiki/Modulo)
  — the remainder idea from the 10/16 class in general terms, plus how
  programming languages implement `%` (including negative numbers, which
  we haven't needed yet).

### Previously assigned (cumulative)

Still fair game for questions in class or on assessments. Carried
forward from each earlier week's assignment:

- Week 7 — from [the Sears Tower decomposition assignment](../week07/README.md):
  - [Lubanovic, *Introducing Python*, 3rd edition, Ch. 8, "Lists"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html)
    — list creation and indexing.
  - [`sears_facts.py`](../week07/sears_facts.py),
    [`input_concern.py`](../week07/input_concern.py),
    [`compute_dimensions.py`](../week07/compute_dimensions.py),
    [`output_concern.py`](../week07/output_concern.py)
    — Week 7's starter files.
- Week 6 — from [the skyscrapers assignment](../week06/skyscraper_towers.md):
  - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) — comments, docstrings, and naming.
  - [`sears_tower.py`](../week06/sears_tower.py) and
    [`sears_tower.ipynb`](../week06/sears_tower.ipynb).
  - [Lubanovic, *Introducing Python*, 3rd edition, Ch. 6, "If and Match"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch06.html)
- Week 5 — from [the functions-that-draw-shapes assignment](../week05/README.md):
  - [Lubanovic, *Introducing Python*, 3rd edition, Ch. 10, "Functions"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html),
    specifically: "Define a Function with `def`," "Call a Function with
    Parentheses," "Arguments and Parameters," and "Docstrings."
  - [Python's own tutorial section on defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
    and [its follow-up on default values, keyword arguments, and scope](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions).
  - [Stanford's short walkthrough of function syntax](https://cs.stanford.edu/people/nick/py/python-function.html)
  - [OpenStax's own function-definition chapter section](https://openstax.org/books/introduction-python-programming/pages/6-1-defining-functions)
  - [Think Python, 3rd edition, Ch. 3, "Functions"](https://greenteapress.com/wp/think-python-3rd-edition/)
  - [`functions.py`](../week05/functions.py) and
    [`block.py`](../week05/block.py).
- Week 4 — from [`range_strings_practice.md`](../week04/range_strings_practice.md):
  - [Lubanovic, Ch. 4, "Strings"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch04.html) — in full.
  - [Lubanovic, Ch. 7, "For and While"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) — loops, in terms of iterables.
  - [`for_loops_primer.md`](../week04/for_loops_primer.md)
  - [`compute_interest.py`](../week04/compute_interest.py)
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
  - [Think Python, Ch. 2, "Variables, Expressions, and Statements"](https://greenteapress.com/wp/think-python-3rd-edition/)

## Turning it in

Upload `airplane_seating.py` to Sakai, containing `PASSENGERS`,
`position_to_seat`, your completed `seat_to_position`,
`print_seat_assignments`, `who_is_in_seat`, and any helper functions you wrote.

Self-check before you upload. From the folder that holds
`airplane_seating.py`, start interactive Python:

```python
from airplane_seating import *
print_seat_assignments(PASSENGERS)
who_is_in_seat(PASSENGERS, 2, 'C')   # should come back 'Alberich'
who_is_in_seat(PASSENGERS, 1, 'A')   # should come back the name you see printed for seat 1A
who_is_in_seat(PASSENGERS, 99, 'A')  # should come back the "no one booked" message, not a crash
```

Confirm the two `who_is_in_seat` results that should succeed match what
`print_seat_assignments` printed for those exact seats, and that asking
about a seat that doesn't exist fails safely instead of crashing.

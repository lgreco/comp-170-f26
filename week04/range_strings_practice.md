# Assignment: Range, Strings, and Symbols

Due Friday, September 25.

Three small programs and one question, all built from what we did in class
this week: `range`, `for` loops, `if`/`elif`/`else`, and strings as
iterables of symbols. The model to follow is [`age.py`](../week03/age.py) for
its overall shape (named constants at the top, `input()`, a computation,
an informative message) and the `for` loop we wrote for compound interest
in [`compute_interest.py`](compute_interest.py).

Same rule as before: no naked numbers or strings in a computation except
`0`, `1`, `-1`. Every other literal gets a name, declared at the top of
the file: `ALL_CAPS` for a fixed value that never changes, an ordinary
lowercase variable for a value that is really just data. For example,
instead of

```python
# Area of circle with radius 5
circle_area = 3.14 * 5 * 5
```

you write

```python
PI = 3.14
radius = 5
circle_area = PI * radius * radius
```

One exception, in Part 1 only: the numbers inside `range(...)` may stay
bare, because `range`'s arguments are exactly what you're studying there.

## Part 1 — `range` predictions (given)

Write `range_practice.py`. For each of the five calls below, do this in
order:

1. Before touching the keyboard, write a comment stating what you think
   it produces.
2. Then add a `for` loop that prints each value, and run it.
3. If your prediction was wrong, leave the wrong prediction in the
   comment and add a second comment saying what actually happened and why.

The five calls:

```
range(5)
range(3, 8)
range(1, 21, 2)
range(0, 20, 2)
range(-50, 51, 10)
```

Then add one more of your own: a `range` that counts *down* from 10 to 1.
You are not given this one — work out which of the three arguments has to
change, and which sign.

## Part 2 — Symbol classifier (yours to work out)

Write `symbol_classifier.py`, following the same four steps as
[`age.py`](../week03/age.py): get input, convert, operate, report.

1. Ask the user for a line of text — anything at all. Letters, digits,
   spaces, punctuation.
2. Loop over it one symbol at a time, the same way we take attendance:
   `for symbol in string:`.
3. For each symbol, get its ASCII code with `ord()` and decide which
   group it belongs to, using `if`/`elif`/`else`:
   * a digit (`'0'` through `'9'`, codes 48 through 57)
   * an uppercase letter (`'A'` through `'Z'`, codes 65 through 90)
   * a lowercase letter (`'a'` through `'z'`, codes 97 through 122)
   * anything else (the catch-all `else`)
4. Keep four counts, one per group, and after the loop finishes print an
   informative message with all four — not just bare numbers.

The 48, 57, 65, 90, 97, and 122 above are not `0`, `1`, or `-1`, so each
one gets a name. The four counters start at `0`, which may stay bare.

Test it with `Hello World 2026!` — you should get 4 digits, 2 uppercase,
8 lowercase, and 3 other (two spaces and the exclamation point). Then try
a string you invent yourself and predict the four counts before you run it.

## Part 3 — Indexing and slicing (yours to work out)

Write `pick_apart.py`. Ask the user for a word or phrase and print, each
with an informative label:

1. The first symbol.
2. The last symbol. Don't hard-code the position; use `len()` so it works
   for any input.
3. The first three symbols, as a slice.
4. Every symbol except the first and the last, as a slice.

Then, at the bottom of the file, deliberately provoke an `IndexError`
by asking for the symbol one position *past* the end. Run it, read the
error message, and leave a comment above that line explaining in your own
words what the error says and why counting from 0 caused it.

Run it with a normal phrase, and then with a single-symbol input like `a`.
Some of your four outputs may surprise you on that second run; note in a
comment which ones and why.

## A question to think about (no need to write code for it)

Your classifier in Part 2 touches every symbol exactly once, and a `for`
loop was the right tool because you knew how many symbols there were before
you started. Suppose instead the program had to keep asking the user for
text *until they typed a line containing no digits*. Which kind of loop
would that call for, and what would have to be true before the first pass
through it? Be ready to talk about this in class Monday.

## Reading

Expect roughly two to three hours, including rereading the same pages after
you've worked through the examples.

### New this week (Week 4)

Textbook material — easier reading:

* [Lubanovic, Ch. 4, "Text Strings"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch04.html),
  in full — a little technical, but it's the most complete and
  authoritative source on Python strings. Strings have a lot of methods
  (behaviors); all useful, but you don't need to memorize every one of
  them. What matters is knowing where to look when you need a specific
  one for a task. The five worth having memorized are `index`, `join`,
  `lower`, `upper`, and `split`; for everything else, look it up first.
* [Lubanovic, Ch. 7](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) —
  loops, discussed in terms of the iterables we covered in class.
* [`for_loops_primer.md`](for_loops_primer.md) — the `for`-loop primer
  posted this week.

Official Python documentation — dry and formal, but ultimately *the*
source:

* [`range`](https://docs.python.org/3/library/stdtypes.html#range)
* [Text sequence type — `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
* [`ord()`](https://docs.python.org/3/library/functions.html#ord)
* [`len()`](https://docs.python.org/3/library/functions.html#len)

### Previously assigned (cumulative)

Still fair game for questions in class or on assessments. Carried
forward from each earlier week's assignment:

* Week 3 — from [`temperature_conversion.md`](../week03/temperature_conversion.md):
  * [`input()`](https://docs.python.org/3/library/functions.html#input)
  * [`int()`](https://docs.python.org/3/library/functions.html#int)
  * [`float()`](https://docs.python.org/3/library/functions.html#float)
  * [Lubanovic, type conversions](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html#c03_h_conversions)
  * [Official Python tutorial on input (and output)](https://docs.python.org/3/tutorial/inputoutput.html)
* Week 2 — from [`interactive_shell_reading.md`](../week02/interactive_shell_reading.md):
  * [Lubanovic, Ch. 1, "Introduction"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch01.html) — in full.
  * [Lubanovic, Ch. 2, "Types and Variables"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch02.html) — up to and including "Variables."
  * [Lubanovic, Ch. 3, "Numbers"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html) — integer and float sections only.
  * [Think Python, Ch. 2, "Variables, Expressions, and Statements"](https://greenteapress.com/wp/think-python-3rd-edition/) — complementary, same material from a different angle.

## Turning it in

Upload all three `.py` files (`range_practice.py`, `symbol_classifier.py`,
`pick_apart.py`) to Sakai. Self-check: run `symbol_classifier.py` on
`Hello World 2026!` and confirm 4 digits, 2 uppercase, 8 lowercase, and 3
other; run `pick_apart.py` on `Python` and confirm the first symbol is `P`,
the last is `n`, and the middle slice is `ytho`.

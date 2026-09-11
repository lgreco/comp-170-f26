# Assignment: Temperature Conversion

Due Friday, September 18.

This week we moved out of the interactive shell and into real program
files — [`age.py`](age.py) is your model. Both programs below should follow that
same shape:

1. Prompt the user and read their answer with `input()`.
2. Convert that string to a number (`float`, since temperatures aren't
   always whole numbers).
3. Compute the result using a formula.
4. Print an informative message — not just the bare number.

For the `float()` conversion, you don't need to worry about bad strings
this time. Assume whatever is typed on the keyboard is a correctly
formed number, like `77.5`, not something mistyped like `7y.5`. There's
no need to write any function like `check()` from
[`our_first_function.py`](our_first_function.py) to validate the input first — just wrap the
result of `input()` directly in `float()`.

These are straight-line programs, same style as [`age.py`](age.py). And same
rules as [`age.py`](age.py): no naked numbers or strings in the computation. Any
fixed number the formula needs gets a name, in ALL CAPS, declared at the
top of the file, the same way `CURRENT_YEAR` works in `age.py`.

## Part 1 — Celsius to Fahrenheit (given)

The formula to convert a Celsius temperature to Fahrenheit is:

```
F = C * 9/5 + 32
```

Write `celsius_to_fahrenheit.py`:

1. Ask the user for a temperature in Celsius.
2. Convert it to Fahrenheit using the formula above.
3. Print something like: `20.0 degrees Celsius is 68.0 degrees Fahrenheit`.

Two literals live in that formula — `9/5` and `32` — and neither one is
0, 1, or -1, so neither one gets to stay naked in the computation line.
Give each one a well-named constant, the way `CURRENT_YEAR` and
`ENTRY_PROMPT` are declared before they're used in [`age.py`](age.py).

## Part 2 — Fahrenheit to Celsius (yours to work out)

Now go the other direction. You're not given the formula this time —
derive it yourself by inverting the one from Part 1. Start from
`F = C * 9/5 + 32` and solve for `C`. Do the algebra on paper first;
don't guess and check in the shell until you believe you have it right,
then use the shell to confirm.

Write `fahrenheit_to_celsius.py`, structured exactly like Part 1:

1. Ask the user for a temperature in Fahrenheit.
2. Convert it to Celsius using the formula you derived.
3. Print an informative message in the same style as Part 1.

Same constant rule applies — whatever numbers your inverted formula
needs, name them, don't leave them naked in the computation.

## A question to think about (no need to write code for it)

[`age.py`](age.py) uses `check()` from [`our_first_function.py`](our_first_function.py) to reject input
that isn't all digits before converting it. Would `check()` work as-is
to validate a temperature like `-4` or `98.6`? Why or why not? You don't
need to fix or extend `check()` for this assignment — just be ready to
answer this in class Monday, since it's exactly where we're headed next
with loops and logic.

## Reading

### New this week (Week 3)

Official Python documentation — dry and formal, a bit technical, but
ultimately *the* source once you're done with this course:

* [`input()`](https://docs.python.org/3/library/functions.html#input)
* [`int()`](https://docs.python.org/3/library/functions.html#int)
* [`float()`](https://docs.python.org/3/library/functions.html#float)

Textbook material — easier reading:

* [Lubanovic, type conversions](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html#c03_h_conversions)
* [Official Python tutorial on input (and output)](https://docs.python.org/3/tutorial/inputoutput.html)

### Previously assigned (cumulative)

Still fair game for questions in class or on assessments. Carried
forward from each earlier week's assignment:

* Week 2 — from [`interactive_shell_reading.md`](../week02/interactive_shell_reading.md):
  * [Lubanovic, Ch. 1, "Introduction"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch01.html) — in full.
  * [Lubanovic, Ch. 2, "Types and Variables"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch02.html) — up to and including "Variables."
  * [Lubanovic, Ch. 3, "Numbers"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html) — integer and float sections only.
  * [Think Python, Ch. 2, "Variables, Expressions, and Statements"](https://greenteapress.com/wp/think-python-3rd-edition/) — complementary, same material from a different angle.

## Turning it in

Upload both `.py` files to Sakai. Run each one at least twice with different
inputs and make sure the numbers actually check out (e.g., when entering 0 in `celsius_to_fahrenheit.py`, you should get back 32. When entering 32 in `fahrenheit_to_celsius.py` you should get back 0.)
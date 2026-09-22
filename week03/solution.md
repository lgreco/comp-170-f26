# Solution: Temperature Conversion

Worked solutions for
[`temperature_conversion.md`](../../../comp-170-f26/week03/temperature_conversion.md),
in the same straight-line style as
[`age.py`](../../../comp-170-f26/week03/age.py) — no functions, no
`try`/`except`, every fixed number in the formula named as an
`ALL_CAPS` constant at the top of the file, comments explaining *why*
each step exists, not just what it does.

## Part 1 — Celsius to Fahrenheit (given)

```python
# celsius_to_fahrenheit.py
#
# The formula is handed to us this time: F = C * 9/5 + 32. Two numbers
# live inside it -- 9/5 and 32 -- and neither one is 0, 1, or -1, so
# neither gets to sit naked in the computation line. We name them the
# same way age.py names CURRENT_YEAR and ENTRY_PROMPT before using them.
SCALE_FACTOR = 9 / 5
FREEZING_OFFSET_F = 32
ENTRY_PROMPT = "Temperature in Celsius: "

# input() always hands back a string, no matter what the user types --
# even if they type "20", Python sees the two characters '2' and '0',
# not the number 20. We're told not to worry about bad input this week
# (no check() needed, unlike age.py), so we go straight to float(),
# trusting the string is a well-formed number. float(), not int(),
# because a temperature like 98.6 has a fractional part an int can't
# hold.
celsius = float(input(ENTRY_PROMPT))

# Now that celsius is an actual number (a float), the formula can run.
fahrenheit = celsius * SCALE_FACTOR + FREEZING_OFFSET_F

# An informative message, not just the bare number -- the assignment's
# own example is "20.0 degrees Celsius is 68.0 degrees Fahrenheit",
# so we echo both the input and the result back to the user.
print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit.")
```

Self-check: enter `0`, expect `32.0` back; enter `100`, expect `212.0`
back.

## Part 2 — Fahrenheit to Celsius (yours to work out)

The assignment asks us to invert `F = C * 9/5 + 32` ourselves, on paper,
before touching the shell. That algebra, one step at a time:

```
F = C * 9/5 + 32
F - 32 = C * 9/5              (subtract 32 from both sides)
(F - 32) * 5/9 = C            (multiply both sides by the reciprocal, 5/9)
```

So `C = (F - 32) * 5/9` — the same two numbers as Part 1, `9/5` and
`32`, just used differently: `32` is subtracted first this time instead
of added last, and we multiply by `5/9` (the reciprocal of `9/5`)
instead of `9/5` itself.

```python
# fahrenheit_to_celsius.py
#
# Same two numbers as Part 1's formula, reused here in their inverted
# roles -- see the algebra above for how C = (F - 32) * 5/9 falls out
# of F = C * 9/5 + 32. Naming them fresh (rather than importing Part
# 1's constants) keeps this file runnable on its own, the same way
# fahrenheit_to_celsius.py and celsius_to_fahrenheit.py are two
# separate, independent files to turn in.
INVERSE_SCALE_FACTOR = 5 / 9
FREEZING_OFFSET_F = 32
ENTRY_PROMPT = "Temperature in Fahrenheit: "

# Same reasoning as Part 1: input() hands back a string, and float()
# (not int()) converts it because Fahrenheit readings aren't always
# whole numbers either.
fahrenheit = float(input(ENTRY_PROMPT))

# The inverted formula: subtract the offset first, then scale.
celsius = (fahrenheit - FREEZING_OFFSET_F) * INVERSE_SCALE_FACTOR

# Same informative-message shape as Part 1, direction reversed.
print(fahrenheit, "degrees Fahrenheit is", celsius, "degrees Celsius.")
```

Self-check: enter `32`, expect `0.0` back; enter `212`, expect `100.0`
back — the exact round-trip the assignment's own "Turning it in"
section asks students to confirm.

## A note on the "question to think about"

The assignment asks whether `check()` from
[`our_first_function.py`](../../../comp-170-f26/week03/our_first_function.py)
would work as-is to validate a temperature like `-4` or `98.6`. It
wouldn't: `check()` walks the string one symbol at a time and rejects
anything whose ASCII code falls outside `48`–`57` (the digits `0`–`9`).
A `.` (decimal point) and a `-` (minus sign) both fall outside that
range, so `check("98.6")` and `check("-4")` both come back `False` even
though both are perfectly valid temperatures. That's exactly why this
assignment says not to bother with `check()` this week — it isn't built
to handle it yet, and extending it (to allow one optional leading `-`
and one optional `.`) is real work best saved for when the class gets to
loops and logic in more depth, per the assignment's own pointer to
"next with loops and logic."

## Turning it in

These are worked models to check a submission against, not a substitute
for running your own code — the assignment's own self-check (run each
file twice, confirm the numbers above) still applies to whatever you
actually submit.

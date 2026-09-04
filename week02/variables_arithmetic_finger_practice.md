# Finger Practice: Variables, Data Types, and Arithmetic

Work entirely at the interactive shell (`>>>`) — no file to create, no
Vim involved. Read the accompanying note,
`interactive_shell_reading.md`, before starting if you haven't
already.

These are short, low-stakes drills, not a program to design. Do each one,
look at what the shell echoes back, and make sure the result matches what
you expected *before* you typed it. If it doesn't match, that mismatch is
the point — figure out why before moving to the next one.

## Part 1 — Assigning and inspecting

1. Assign your own name to a variable called `student_name`, as a string.
   Then, on the next line, type just `student_name` and confirm the shell
   echoes it back.
2. Assign your age to a variable called `age`, as an `int`.
3. Assign your height in meters (a decimal, e.g. `1.75`) to a variable
   called `height_m`, as a `float`.
4. For each of the three variables above, call `type()` on it and confirm
   it reports what you expect (`str`, `int`, `float`).
5. Reassign `age` to `age + 1`. Then look at `age` again. Notice that the
   *name* didn't change, but the *value* it points to did.

## Part 2 — Arithmetic, predict then verify

For each expression below, **write down what you think the result will
be** before you type it. Then type it and compare.

1. `17 + 5`
2. `17 - 5`
3. `17 * 5`
4. `17 / 5`
5. `17 // 5`
6. `17 % 5`
7. `2 ** 10`
8. `(2 + 3) * 4` vs. `2 + 3 * 4` — predict both, then explain in one
   sentence why they differ.

Pay particular attention to #4 vs. #5 vs. #6 — three different operators
on the same two numbers, three different jobs: true division, floor
(whole-number) division, and remainder. If you can't yet say in your own
words what each one is doing, that's worth flagging in class.

## Part 3 — Strings are not numbers

1. Assign `first = "Ada"` and `last = "Lovelace"`. Combine them into a
   single string `full_name` using `+`, with a space in between. (You'll
   need a third piece — a literal `" "` — in the expression.)
2. Try `"Ada" + 7`. Read the error message carefully — don't just note
   that it failed, read *what Python says* about why.
3. Fix it: convert `7` to a string first with `str()`, then retry the
   concatenation.
4. Now go the other direction: assign `count = "7"` (a string that looks
   like a number) and try `count + 1`. It should fail the same way.
   Fix it with `int(count) + 1`.
5. In one sentence: why does Python insist you convert explicitly, instead
   of just guessing what you meant the way some other languages do? (This
   connects to the strong-vs-weak typing distinction from class.)

## Part 4 — Naming, for real this time

Class covered variable-naming rules and style (readable names, no
reserved words, conventions for multi-word names). Put that into practice:

1. Assign the price of an item and the sales-tax rate to two well-named
   variables — not `x` and `y`. Compute the total price (price plus tax)
   into a third well-named variable, and check the result.
2. Try naming a variable something that breaks the rules from class (a
   reserved word, or a name starting with a digit) and read the error.
   Then rename it correctly.

## Part 5 — Putting it together

No new tools here — just the same variables, types, and operators from
Parts 1–4, combined into slightly larger expressions.

1. Assign three test scores to `score1`, `score2`, and `score3` (as
   `int`s). Compute their average into a variable called `average` using
   `+` and `/`. Check its `type()` — is it still an `int`, or did it
   become a `float`? Explain why in one sentence.
2. Reuse `height_m` from Part 1. A meter is 100 centimeters. Without
   retyping the number, compute `height_cm` from `height_m` using
   arithmetic on the variable itself.
3. Assign `a = 1`, `b = -3`, `c = 2` — the coefficients of a quadratic,
   same roles as in the naive/documented/professional versions from
   class. Compute the discriminant, `b ** 2 - 4 * a * c`, into a variable
   called `discriminant`. Don't solve the equation yet (that's coming
   later in the term) — just get comfortable typing a multi-term
   arithmetic expression correctly in one line, including where
   parentheses are and aren't needed.
4. Assign `line = "-"` and use string repetition (`*`) to build a
   40-character divider line into a variable called `divider`, without
   typing 40 dashes by hand.
5. Pick any two variables from earlier in this worksheet that hold
   *different* types (e.g., `age` and `height_m`). Try combining them
   directly with `+`. If it fails, fix it with an explicit conversion, the
   same way you did in Part 3 — and say which of the two variables you
   converted, and why you chose that one instead of the other.

## Turning it in

No file to create by hand — for this one, keep a plain-text transcript of
your shell session (copy everything from your terminal, prompts and all)
and submit it the same way you'd submit anything else this early in the
term. Confirm the exact mechanism in class if you're unsure.

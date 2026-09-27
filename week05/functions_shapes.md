# Assignment: Functions That Draw Shapes

Due Friday, October 2.

Four functions, all in one file, `shapes.py`. Each takes its size and its
characters as input arguments and prints a shape. Their whole job is to
print. The model to follow is [`functions.py`](functions.py) from
Friday's class: `print_square` for a function that takes a size and a
fill character, and `draw_square` for one that takes several parameters
and works out the arithmetic of the borders. [`block.py`](block.py)
shows the nested loop and the `character * n` shortcut that can replace
the inner loop.

## How to work each part

> **Design on paper first.** Working code is the goal of everything we
> do in this course. In this assignment, though, what matters most is
> the design: working it out on paper *before* you write any code. Use a
> few examples of each shape to figure out its parameters: what changes
> from one size to the next, and what stays the same. Then write simple,
> plain-English instructions that would produce the shape. Those
> instructions become the comment lines in your code. **Code without its
> instructions written as comments is incomplete**, however well it runs.

For every shape:

1. **Draw it by hand first**, on grid paper: one character per square,
   the way you'd type it on a typewriter, one line at a time, left to
   right. Draw at least two sizes of each shape so you can see what
   changes and what stays the same.
2. **Make a table**: one row per printed line, with columns for the line
   number, how many background characters come first, and how many shape
   characters come after. The pattern you need is in that table.
3. **Write the instructions in plain English**, step by step, as if you
   were dictating them to someone at a typewriter who has never seen the
   shape. Keep each step simple: what gets repeated, how many times, and
   how many of which character go on each line. Write these before you
   write any code.
4. **Then write the function, with your instructions as its comments.**
   Put each instruction on a comment line directly above the code that
   carries it out, the way `draw_square` has `# print top half` above
   its first loop.

Rules that apply to every part:

- **Function names are verbs** (`draw_diamond`, not `diamond`) and
  parameter names are nouns. Don't name anything `print`.
- **Keep parameter lists within 80 columns.** When a `def` line gets
  long, break it across lines the way `draw_square` does.
- **Check the sizes first.** As in `draw_square`, if a size makes no
  sense (zero or negative), print a message telling the client so,
  instead of drawing anything. Be informative; there's no need to be
  nasty.
- **No naked numbers or strings** except `0`, `1`, `-1`. Every other
  literal gets a well-named `ALL_CAPS` constant at the top of the file.
  That includes `2`. You'll need it in every shape, for things like
  splitting something in half or counting both sides. Store it in a
  constant or a variable, and never write it bare in a computation.
  Think about what the `2` actually means each place you use it, and
  choose a meaningful name that says so. `TWO` is not a meaningful name;
  it tells a reader nothing the digit didn't already say.
- **Shapes are correct by character count**, not by how they look on
  screen. A character cell is taller than it is wide, so a correct shape
  will look a little stretched. That's expected; don't try to fix it.

## Part 1 — Diamond (given)

Write `draw_diamond(size, fill_char)`. `size` is the number of lines
from the top point down to (and including) the widest line. Here is
`draw_diamond(4, '*')`:

```
   *
  ***
 *****
*******
 *****
  ***
   *
```

The top half, line by line, for `size` 4:

| Line | Spaces | Stars |
|---:|---:|---:|
| 1 | 3 | 1 |
| 2 | 2 | 3 |
| 3 | 1 | 5 |
| 4 | 0 | 7 |

Work out on your own how the spaces and the stars each depend on the line
number and on `size`, and write that down in English before you write the
loop. Then work out the bottom half: how many lines it has, and in what
order it reuses the numbers from the top half.

## Part 2 — Diamond inside a square (yours to work out)

Write `draw_diamond_in_square(size, diamond_char, background_char)`. It
draws the same diamond as Part 1, but now the space around the diamond is
filled in with `background_char`, so the whole picture is a solid square.
Here is `draw_diamond_in_square(4, '*', '.')`:

```
...*...
..***..
.*****.
*******
.*****.
..***..
...*...
```

1. How wide and how tall is the square, in terms of `size`?
2. In Part 1, the spaces to the right of the diamond didn't need to be
   printed, because you can't see them. Now you can. What does each line
   need on its right, and how does that compare to what it needs on its
   left?
3. Extend your Part 1 table with a third count column for the right-hand
   side, then update your plain-English instructions to match.

Try it with at least two other sizes and two other pairs of characters.
`draw_diamond_in_square(1, '*', '.')` should print a single `*`.

## Part 3 — Christmas tree (yours to work out)

Write `draw_tree(tiers, leaf_char, trunk_char)`. The tree is a stack of
partially overlapping triangles, `tiers` of them, with a rectangular
trunk underneath. Here is `draw_tree(3, '*', '|')`:

```
    *
   ***
  *****
   ***
  *****
 *******
  *****
 *******
*********
   |||
   |||
```

Look at it closely before writing anything:

1. Every tier is a triangle three lines tall, like the top half of the
   Part 1 diamond. The line widths of the first tier are 1, 3, 5.
   Write down the line widths of the second tier and of the third. How
   does each tier relate to the one above it? This is where the overlap
   comes from.
2. The whole tree is centered on the widest line, which is the last line
   of the last tier. How wide is that line, in terms of `tiers`? Once you
   know it, how many spaces does any line of width *w* need in front of
   it to sit centered?
3. The trunk is 3 characters wide and 2 lines tall, whatever the number
   of tiers, and it's centered the same way the leaves are.

The 3 lines per tier, the trunk width of 3, and the trunk height of 2 are
fixed properties of the tree, not arguments, so each one becomes a named
constant at the top of the file. Once your function works, change one of
those constants, run it again, and check that the tree is still centered.
If it isn't, something in your function still depends on the old number.

`draw_tree(1, '*', '|')` should give:

```
  *
 ***
*****
 |||
 |||
```

## Part 4 — Staircase (yours to work out)

Write `draw_staircase(steps, step_width, step_height, fill_char)`. The
staircase climbs from left to right: the top step is on the right, and
the bottom step runs the full width. Here is
`draw_staircase(4, 2, 1, '#')`:

```
      ##
    ####
  ######
########
```

and here is `draw_staircase(3, 3, 2, '#')`:

```
      ###
      ###
   ######
   ######
#########
#########
```

Four parameters, like `draw_square`. Work out from the two examples above
(and at least one more you draw yourself on grid paper):

1. How many lines the staircase has in total.
2. For a given step, how many fill characters each of its lines has, and
   how many spaces come before them.
3. Why this shape needs a nested loop even if you use `character * n`
   for every line: what is the outer loop counting, and what is the inner
   loop counting?

## A question to think about (no need to write code for it)

Call `draw_diamond_in_square(4, '*', ' ')`, with a space as the
background. On screen, it looks exactly like `draw_diamond(4, '*')`. In
class we built `s2i` out of `s` and `i` rather than writing it from
scratch. Could `draw_diamond` be written in a single line that calls
`draw_diamond_in_square`? If it could, is there any reason left to keep
`draw_diamond` as a separate function at all? Think about it from the
point of view of the programmer-user, the one who imports your code and
calls it. Be ready to talk about this in class Monday.

## Reading

### New this week (Week 5)

- [Lubanovic, *Introducing Python*, 3rd edition, "Functions"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/)
  — only the first four sections: "Define a Function with `def`," "Call
  a Function with Parentheses," "Arguments and Parameters," and
  "Positional Arguments." The rest of the chapter is for later.
- [Think Python, 3rd edition, Ch. 3, "Functions"](https://greenteapress.com/wp/think-python-3rd-edition/)
  — defining a function, parameters, and calling one function from
  another.
- [Official Python tutorial, "Defining Functions"](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
  — read only up to the start of "More on Defining Functions"; the rest
  is for later.
- [`print()`](https://docs.python.org/3/library/functions.html#print) —
  the `end` parameter we used to keep characters on the same line.
- [Common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
  — find the row for `s * n` in the table; that's the string repetition
  we used to replace the inner loop.
- [`functions.py`](functions.py) and [`block.py`](block.py) — this
  week's class code.

### Previously assigned (cumulative)

Still fair game for questions in class or on assessments. Carried
forward from each earlier week's assignment:

- Week 4 — from [`range_strings_practice.md`](../week04/range_strings_practice.md):
  - [Lubanovic, Ch. 4, "Text Strings"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch04.html) — in full.
  - [Lubanovic, Ch. 7](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) — loops, in terms of iterables.
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

Upload `shapes.py` to Sakai, containing the four functions, each with
your plain-English instructions as comment lines in its body. A function
without them is incomplete, even if it draws the shape correctly. Your
grid-paper drawings stay with you; don't upload them.

Self-check before you upload. From the folder that holds `shapes.py`,
start interactive Python and import your functions the same way we did in
class:

```python
from shapes import *
draw_diamond(4, '*')
draw_diamond_in_square(4, '*', '.')
draw_tree(3, '*', '|')
draw_staircase(4, 2, 1, '#')
```

Compare each result, character by character, against the examples
above. Then call each function with a size of `0` and confirm you get
your message instead of a drawing.

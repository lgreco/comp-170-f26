# Solution: Functions That Draw Shapes

Worked solution for
[`week05_functions_shapes_v2.md`](../../../teaching/terms/f26/comp170/week05_functions_shapes_v2.md),
in the same style as [`functions.py`](functions.py)'s `draw_square`: a
size check up front (`if`/`else`, no early `return` — these functions
only print, so there's nothing to hand back), every fixed number named
as an `ALL_CAPS` constant, and the plain-English instructions written as
comments directly above the code that carries them out. All four
functions below belong in one file, `shapes.py`, the way the assignment
asks for.

```python
# shapes.py

# Every shape below grows by one fill character on each side per line --
# the point of a diamond adds one star, the next line down adds one more
# on the left and one more on the right, and so on. That's where the 2
# comes from in every "amount of fill" calculation in this file.
GROWTH_PER_LINE = 2

# Centering a line means splitting its leftover width evenly between a
# left side and a right side -- a different use of "2" than the growth
# above, so it gets its own name.
CENTER_SPLIT = 2

# The tree's own fixed shape, not arguments the caller can change:
# every tier is three lines tall, and the trunk is always 3 wide, 2 tall.
LINES_PER_TIER = 3
TRUNK_WIDTH = 3
TRUNK_HEIGHT = 2

SPACE_CHAR = " "
```

## Part 1 — Diamond (given)

For line `n` (counting from 1) of the top half, there are `size - n`
spaces before the fill and `GROWTH_PER_LINE * n - 1` fill characters —
one star on line 1, three on line 2, five on line 3, matching the
assignment's own table. The bottom half reuses those same two counts in
reverse, skipping the widest line since the top half already printed it
once.

```python
def draw_diamond(size, fill_char):
    # Reject a size that can't make a diamond, and say so, instead of
    # drawing anything.
    if size <= 0:
        print("Size must be greater than 0 to draw a diamond.")
    else:
        # Top half: from the single-character point down to (and
        # including) the widest line.
        for line in range(1, size + 1):
            spaces = size - line
            fill = GROWTH_PER_LINE * line - 1
            print(SPACE_CHAR * spaces + fill_char * fill)

        # Bottom half: the same spaces/fill pairs as the top half,
        # walked backwards, starting one line short of the widest
        # line (already printed above) and ending at the point.
        for line in range(size - 1, 0, -1):
            spaces = size - line
            fill = GROWTH_PER_LINE * line - 1
            print(SPACE_CHAR * spaces + fill_char * fill)
```

Self-check: `draw_diamond(4, '*')` should match the assignment's own
seven-line figure exactly, character for character.

## Part 2 — Diamond inside a square (yours to work out)

The square is `size` tall and `size` wide, same as the diamond's own
bounding box. Part 1's spaces become visible now, so both sides of
every line need `background_char` where Part 1 had nothing: the same
`spaces` count from Part 1, once on the left and once on the right of
the same `fill` count of `diamond_char`.

```python
def draw_diamond_in_square(size, diamond_char, background_char):
    if size <= 0:
        print("Size must be greater than 0 to draw a diamond in a square.")
    else:
        for line in range(1, size + 1):
            background = size - line
            diamond = GROWTH_PER_LINE * line - 1
            print(
                background_char * background
                + diamond_char * diamond
                + background_char * background
            )

        for line in range(size - 1, 0, -1):
            background = size - line
            diamond = GROWTH_PER_LINE * line - 1
            print(
                background_char * background
                + diamond_char * diamond
                + background_char * background
            )
```

Self-check: `draw_diamond_in_square(4, '*', '.')` against the
assignment's figure, and `draw_diamond_in_square(1, '*', '.')` should
print a single `*` — `size - line` is `0` on both sides when
`size == line == 1`, so the background count collapses to nothing and
only the one fill character prints.

## Part 3 — Christmas tree (yours to work out)

Each tier's three lines are the top half of a diamond, `LINES_PER_TIER`
lines tall, and each tier starts two leaves wider than the one above it
— the same `GROWTH_PER_LINE` idea as Parts 1 and 2, just counted across
tiers and lines together: `leaves = GROWTH_PER_LINE * (tier + line) + 1`
for tier `0` and line `0` at the very top.

The tree is centered on its own widest line — the last line of the
last tier, where `tier = tiers - 1` and `line = LINES_PER_TIER - 1`:

```
widest = GROWTH_PER_LINE * (tiers - 1 + LINES_PER_TIER - 1) + 1
       = GROWTH_PER_LINE * tiers + LINES_PER_TIER
```

(substituting `LINES_PER_TIER = 3` and `GROWTH_PER_LINE = 2` gives
`2 * tiers + 3` — the widest line is `5` wide for one tier, `9` wide for
three, matching the assignment's own two examples). Any narrower line
of width `w` needs `(widest - w) // CENTER_SPLIT` spaces in front of it
to sit centered under that widest line — the trunk included, using its
own fixed `TRUNK_WIDTH` in place of `w`.

```python
def draw_tree(tiers, leaf_char, trunk_char):
    if tiers <= 0:
        print("Tiers must be greater than 0 to draw a tree.")
    else:
        widest = GROWTH_PER_LINE * tiers + LINES_PER_TIER

        # Leaves: tier by tier, three lines per tier, each line two
        # characters wider than the one before it across the whole tree.
        for tier in range(tiers):
            for line in range(LINES_PER_TIER):
                leaves = GROWTH_PER_LINE * (tier + line) + 1
                spaces = (widest - leaves) // CENTER_SPLIT
                print(SPACE_CHAR * spaces + leaf_char * leaves)

        # Trunk: always TRUNK_WIDTH wide, TRUNK_HEIGHT tall, centered
        # under the same widest line as the leaves above it.
        trunk_spaces = (widest - TRUNK_WIDTH) // CENTER_SPLIT
        for line in range(TRUNK_HEIGHT):
            print(SPACE_CHAR * trunk_spaces + trunk_char * TRUNK_WIDTH)
```

Self-check: `draw_tree(3, '*', '|')` and `draw_tree(1, '*', '|')`
against the assignment's own figures. Then change `LINES_PER_TIER` or
`TRUNK_WIDTH`, run it again, and confirm the tree is still centered —
the assignment's own suggested check for whether every width still
traces back to a named constant instead of a leftover bare number.

## Part 4 — Staircase (yours to work out)

The staircase has `steps` steps, each `step_height` lines tall. Counting
steps from `1` (the narrowest, at the top) to `steps` (the widest, at
the bottom): step `s` needs `s * step_width` fill characters, and
whatever width is left over — `(steps - s) * step_width` — is spaces in
front of it. This needs a nested loop even with `character * n`
available, because the outer loop counts *steps* and the inner loop
counts the `step_height` identical lines each step repeats.

```python
def draw_staircase(steps, step_width, step_height, fill_char):
    if steps <= 0 or step_width <= 0 or step_height <= 0:
        print("Steps, step width, and step height must all be greater than 0.")
    else:
        for step in range(1, steps + 1):
            fill = step * step_width
            spaces = (steps - step) * step_width
            for line in range(step_height):
                print(SPACE_CHAR * spaces + fill_char * fill)
```

Self-check: `draw_staircase(4, 2, 1, '#')` and
`draw_staircase(3, 3, 2, '#')` against the assignment's own figures.

## A note on the "question to think about"

Yes: `draw_diamond(size, fill_char)` could be written as a single line,
`draw_diamond_in_square(size, fill_char, ' ')`, since a space background
is invisible — the two functions produce identical output whenever
`background_char` is a space. Whether `draw_diamond` is still worth
keeping as its own function is a question about the *programmer-user*,
not the screen: calling `draw_diamond(4, '*')` says directly "draw a
diamond," while `draw_diamond_in_square(4, '*', ' ')` makes a reader
stop and notice that the third argument is doing something invisible
and important. A name that says what you mean is worth keeping even
when the computation underneath could be borrowed from somewhere else.

## Turning it in

This is a worked model to check a submission against, not a substitute
for running your own code — the assignment's own self-check (import
`shapes`, call all four functions, compare character by character, then
confirm a size of `0` falls back to the message instead of a drawing)
still applies to whatever you actually submit.

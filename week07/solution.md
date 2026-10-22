# Solution: Sears Tower, One Concern per File

Worked solution for Part 2 of the [Week 7 assignment](README.md). Your own
submission doesn't have to match this line for line -- the comments below
explain *why* each piece is written the way it is, so you can compare
reasoning, not just output. Three things to check yours against: every
function has at most one `return` (and the two that only print have none),
no bare numbers other than `0`, `1`, and `-1`, and the order of every list
is **bottom, middle, top**.

Only the three files you were asked to write appear here. `sears_facts.py`,
`input_concern.py`, and `compute_widths` are unchanged from the starter.

## 1. `compute_heights` in `compute_dimensions.py`

Replace the TODO comment and the `pass` in the starter with the body
below. The docstring is the starter's, shortened here to the essentials;
keep the full one in your file.

```python
def compute_heights(height: int) -> list[int]:
    """The second logic concern: turn the same validated height into the
    three tier heights. Like compute_widths, this function does no
    validation -- that's already been done before this is ever called.

    Unlike widths, each tier's height is a fraction of the *total*
    height directly -- BOTTOM_TIER_HEIGHT_SCALE, MIDDLE_TIER_HEIGHT_SCALE,
    and TOP_TIER_HEIGHT_SCALE (all in sears_facts.py) -- not a fraction of
    the tier below it. Those three fractions add up to 1.0, so the three
    tier heights you compute should add up to (approximately) `height`
    itself, once each is truncated to a whole number of lines.

    Input:
    ------
    height: int
      The desired height for the Sears tower in lines.

    Returns:
    --------
    list[int]
      An array (list) with the bottom, middle, and top tier heights, in
      that order -- the same order compute_widths uses for its own list.
    """
    # Each tier's height is a fraction of the TOTAL height -- not a
    # fraction of the tier below it, the way the widths are. So all three
    # lines read straight from `height`, and none of them depends on
    # another. That's why the order we compute them in doesn't matter.
    #
    # `height * SCALE` is a float (e.g. 30 * 0.6 = 18.0, 30 * 0.25 = 7.5),
    # and a tier can only have a whole number of printed rows, so int()
    # truncates it: 7.5 -> 7. Truncation always rounds toward zero, which
    # is why the three heights can add up to a line or two LESS than
    # `height` (18 + 7 + 4 = 29 for a height of 30). The assignment's own
    # docstring warned us: "approximately".
    bottom_height: int = int(height * BOTTOM_TIER_HEIGHT_SCALE)
    middle_height: int = int(height * MIDDLE_TIER_HEIGHT_SCALE)
    top_height: int = int(height * TOP_TIER_HEIGHT_SCALE)

    # Package the three heights in the same bottom/middle/top order that
    # compute_widths uses. This ORDER is a contract: draw_tower reads
    # widths[i] and heights[i] as "the same tier," so if one list were
    # top-first and the other bottom-first, every tier would be drawn
    # with another tier's height.
    results: list[int] = [bottom_height, middle_height, top_height]

    # The function's one and only return, at the very bottom.
    return results
```

Check it: `compute_heights(60)` returns `[36, 15, 9]`, and
`compute_heights(30)` returns `[18, 7, 4]`. Notice that last one adds up
to 29, not 30. `int()` throws away the fraction of every tier, and three
thrown-away fractions can cost a line. The assignment's docstring warned
"approximately". If you want the heights to add up exactly, there is a
tidy fix: compute bottom and middle with `int()`, then let the top tier
take whatever is left (`height - bottom_height - middle_height`). Both
versions are fine for this assignment; just pick one on purpose.

## 2. `draw_tower` in `output_concern.py`

```python
# The output concern. Nothing in this file computes a tier's size -- the
# logic concern already did that. This file only decides WHERE each row
# goes on the screen and prints it.

# A tier narrower than the base has leftover width. That leftover is shared
# between the tier's left side and its right side, so we divide it by two
# sides. It's a named constant (not a bare 2) because "why 2?" deserves a
# name: it's the number of sides of a tower.
SIDES_OF_TOWER: int = 2

# What we print to push a tier in from the left edge of the screen.
PADDING_CHARACTER: str = " "


def draw_tower(widths: list[int], heights: list[int], building_block: str):
    """The output concern: print the tower, tier by tier, from
    already-computed widths and heights. This function does no
    computing of its own -- compute_widths and compute_heights have
    already done that -- it only prints.

    `widths` and `heights` are parallel lists: `widths[i]` and
    `heights[i]` describe the same tier (bottom, middle, top, in that
    order -- the order compute_widths and compute_heights both use).

    Parameters:
        widths: the bottom, middle, and top tier widths, in that order.
        heights: the bottom, middle, and top tier heights, in that order.
        building_block: the single character used to draw every tier.
    """
    # The bottom tier is the widest, and it sits at index 0. Every other
    # tier gets centered against it, so we remember its width once, here,
    # instead of re-reading widths[0] on every row.
    base_width: int = widths[0]

    # len() tells us how many tiers there are, so this function keeps
    # working if the logic concern ever produces four tiers instead of
    # three. No hard-coded 3 anywhere.
    number_of_tiers: int = len(widths)

    # The lists run bottom -> top (index 0 is the bottom), but a screen
    # prints top -> bottom. So we walk the indexes backwards:
    #   start at the last index (number_of_tiers - 1),
    #   stop just before -1 (so index 0 is included),
    #   step by -1 each time.
    # For three tiers that visits 2, 1, 0 -- top, middle, bottom.
    for tier in range(number_of_tiers - 1, -1, -1):
        # Centering = splitting the leftover width evenly between left
        # and right. Only the left half needs printed spaces; the right
        # half is just empty screen. `//` drops any odd leftover column,
        # so when the leftover is odd the tier sits one column left of
        # perfect center -- unavoidable with whole characters.
        leftover_width: int = base_width - widths[tier]
        indent: int = leftover_width // SIDES_OF_TOWER

        # The indent is the same for every row of this tier, so build it
        # once per tier rather than once per row.
        padding: str = PADDING_CHARACTER * indent

        # Every row of the tier looks identical: the padding, then
        # `widths[tier]` copies of the building block. `heights[tier]`
        # says how many such rows to print. The loop variable `row` isn't
        # used in the body -- it only counts repetitions.
        for row in range(heights[tier]):
            print(padding + building_block * widths[tier])

    # Nothing to return: this function's whole job is the printing it just
    # did. (A function that returns nothing needs no `return` at all.)
```

Check it: `draw_tower([9, 7, 4], [36, 15, 9], '#')` prints the 4-wide top
tier first, indented two spaces, then the 7-wide middle tier indented
one, then the 9-wide bottom tier flush left.

One honest caveat about centering. The tier widths come out of
`compute_widths` as whole numbers, and a 4-wide tier can't sit perfectly
in the middle of a 9-wide one: there are five leftover columns to split
between two sides. `//` gives the left side two and the right side three,
so the tier leans a hair left. That is not a bug in your code; it is what
centering costs when every width is a whole number of characters. A
centering formula that leaves the tier off by *at most one column* is
doing its job.

## 3. The manager in `tower.py`

```python
# The manager (conductor). It imports the four other concerns and calls
# them in order. Notice what is NOT in this file: no arithmetic, no
# print(), no loops. If you ever feel tempted to add one, it belongs in
# one of the other four files.

# `import *` brings in every name from sears_facts. The manager doesn't
# use any of them directly, but the starter file keeps this line so that
# all five files share the same facts.
from sears_facts import *

# These three lines each bring in exactly the functions we use, by name.
# That's the version of import to prefer when you can: a reader sees
# which concern supplies which function.
from input_concern import get_input
from compute_dimensions import compute_widths, compute_heights
from output_concern import draw_tower


def draw_sears_tower(building_block: str = '#'):
    """The manager (conductor) concern: calls the other four functions,
    in order, and passes data between them. This function does no
    computing and no printing itself -- it only tells the input, logic,
    and output concerns what to do and in what order, the same
    "conductor" idea from class, now written in code.

    Parameters:
        building_block: the single character used to draw the tower.
    """
    # Input concern: this loops until the user gives a usable height
    # (a positive integer, or 0 to quit), then hands it back to us.
    height: int = get_input()

    # Logic concerns: the same validated height goes into both. Neither
    # call depends on the other, so either order works. Each returns a
    # list in bottom/middle/top order.
    widths: list[int] = compute_widths(height)
    heights: list[int] = compute_heights(height)

    # Output concern: both lists, plus the character, go to the function
    # that prints. Data flowed input -> logic -> output, and this
    # function only carried it between them.
    draw_tower(widths, heights, building_block)


# This guard means "run draw_sears_tower only when this file is run
# directly (python3 tower.py)". If another file imports tower.py, the
# guard stops the whole program from starting just because of the import.
if __name__ == "__main__":  # ignore this line for now
    draw_sears_tower('#')
```

Check it: from the folder holding all five files, run `python3 tower.py`.
Type `abc` and the prompt appears again with an error message; type `60`
and the tower draws; type `0` and the program quits without drawing
anything (see the note below about that one).

## A question to think about

*Neither `compute_widths` nor `compute_heights` ever has to check whether
`height` is legit. Why not -- and what would break if someone called
either one directly, skipping `get_input()` first?*

They don't check because checking is the input concern's job, and it
happens exactly once, at the door. By the time a number reaches the logic
concern, `get_input()` has already refused everything else. Doing the
check again inside each function would mean three copies of the same rule
to keep in sync, and the logic functions would stop being "pure
arithmetic" that you can read at a glance.

What breaks when you skip the door? It depends on what you walk in with:

- **`"abc"` or `None`** crashes: `compute_heights("abc")` ends in a
  `TypeError`, because you can't multiply a string by `0.6`.
- **A negative number** doesn't crash, which is worse: `compute_heights(-30)`
  quietly returns `[-18, -7, -4]`, and `draw_tower` then prints nothing,
  because `range(-18)` has no rows. A silent wrong answer is harder to
  catch than a loud crash.
- **`0`** returns `[0, 0, 0]` for both lists, and nothing prints. That one
  is on purpose: it's the "quit" value.
- **A tiny positive number** like `3` or `5` gives `compute_widths` a
  result of `[0, 0, 0]`: the tower is "valid" but has no width to draw.
  `get_input()` accepts it, and `sears_facts.py` even defines
  `MINIMUM_ACCEPTABLE_WIDTH` for exactly this situation. Handling it would
  be a good extension, but it's more than this assignment asked for.

## A note on `0`

The self-check at the end of the assignment says that typing `0` should
loop back and ask again. As `get_input()` is written, `0` is the *quit*
value: the prompt itself says "0 to quit". The prompt is right and the
self-check sentence was wrong. Treat `0` as "quit" when you test.

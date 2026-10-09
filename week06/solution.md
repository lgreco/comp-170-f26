# Solution: Skyscrapers, Centered

Worked solution for
[`week06_skyscraper_towers_v2.md`](../../../teaching/terms/f26/comp170/week06_skyscraper_towers_v2.md),
starting from [`sears_tower.py`](sears_tower.py) the way the assignment
asks for: an `if`/`else` height check with no early `return` (the model's
own `draw_square` shape), every fixed number named as an `ALL_CAPS`
constant, lines kept within 80 columns.

```python
# skyscrapers.py

SEARS_TOWER_HEIGHT_FEET = 1_425
SEARS_TOWER_WIDTH_FEET = 225
SEARS_TOWER_ASPECT_RATIO = SEARS_TOWER_HEIGHT_FEET / SEARS_TOWER_WIDTH_FEET

BOTTOM_TIER_HEIGHT_SCALE = 0.6
MIDDLE_TIER_HEIGHT_SCALE = 0.25
TOP_TIER_HEIGHT_SCALE = 0.15
MIDDLE_TIER_WIDTH_SCALE = 0.8
TOP_TIER_WIDTH_SCALE = 0.8 * MIDDLE_TIER_WIDTH_SCALE
MINIMUM_ACCEPTABLE_WIDTH = 7

# Centering a tier means splitting the leftover width (base width minus
# the tier's own width) evenly between a left side and a right side.
CENTERING_SPLIT = 2

# The Hancock's own real-world facts -- looked up the same way the
# assignment asks: roughly 1,128 feet to the roof, a base footprint
# around 265 feet across. Its top is about 60% as wide as its base, a
# much gentler taper than the Sears Tower's three sharp jumps.
HANCOCK_HEIGHT_FEET = 1_128
HANCOCK_BASE_WIDTH_FEET = 265
HANCOCK_ASPECT_RATIO = HANCOCK_HEIGHT_FEET / HANCOCK_BASE_WIDTH_FEET
HANCOCK_TOP_WIDTH_SCALE = 0.6
# Same two-antennas-and-a-gap reasoning as the Sears Tower's top tier,
# but the Hancock doesn't need the full 7-character floor -- it's one
# continuously narrowing shape, not three stacked, independently-sized
# tiers, so only the top row's own 3-character minimum applies.
HANCOCK_MINIMUM_TOP_WIDTH = 3
HANCOCK_BUILDING_BLOCK = '#'
```

## Part 1 — Center the Sears Tower

The easier of the two ways to do this: instead of computing each tier's
own leading spaces from the tier directly below it, every tier centers
against the *same* number -- the bottom tier's width, since it's the
widest. A tier of width `w`, centered on a base of width `base_width`,
needs `(base_width - w) // CENTERING_SPLIT` spaces in front of it. That
works for every tier here because centering is transitive: if the
middle tier is centered on the bottom tier, and the top tier is centered
on the middle tier, the top tier ends up centered on the bottom tier too
-- so computing every tier's spaces directly against `bottom_tier_width`
gives the same result as nesting the centering tier by tier, with far
less bookkeeping.

That means `draw_tier` needs to know the base it's centering against, so
it grows one parameter:

```python
def draw_tier(height: int, width: int, base_width: int, building_block: str):
    """Draws one tier, height rows of width copies of building_block,
    centered on a base of base_width.

    Inputs:
    -------
    height: The number of rows in this tier.
    width: The number of building-block characters per row.
    base_width: The width of the tier this one is centered on.
    building_block: The character to use for the building block.
    """
    spaces = (base_width - width) // CENTERING_SPLIT
    for floor in range(height):
        print(" " * spaces + building_block * width)


def draw_sears_tower(height: int, aspect_ratio: float, building_block: str):
    """Draws a three-tier schematic of the Sears Tower, every tier
    centered on the one below it.

    Inputs:
    -------
    height: The total height of the tower, in printed lines.
    aspect_ratio: height / width for the building, used to work out the
        tower's width from its height.
    building_block: The character to use for the building block.
    """
    if height <= 0:
        print("Height must be greater than 0 to draw a tower.")
    else:
        if aspect_ratio <= 0:
            aspect_ratio = 1.0
        width = int(height / aspect_ratio)
        if width < MINIMUM_ACCEPTABLE_WIDTH:
            width = MINIMUM_ACCEPTABLE_WIDTH
        bottom_tier_height = int(height * BOTTOM_TIER_HEIGHT_SCALE)
        bottom_tier_width = width
        middle_tier_height = int(height * MIDDLE_TIER_HEIGHT_SCALE)
        middle_tier_width = int(width * MIDDLE_TIER_WIDTH_SCALE)
        top_tier_height = int(height * TOP_TIER_HEIGHT_SCALE)
        top_tier_width = int(width * TOP_TIER_WIDTH_SCALE)

        # Every tier centers on bottom_tier_width -- the widest tier,
        # and (per the note above) equivalent to each tier centering on
        # the one directly below it.
        draw_tier(top_tier_height, top_tier_width, bottom_tier_width, building_block)
        draw_tier(middle_tier_height, middle_tier_width, bottom_tier_width, building_block)
        draw_tier(bottom_tier_height, bottom_tier_width, bottom_tier_width, building_block)
```

Self-check: `draw_sears_tower(16, SEARS_TOWER_ASPECT_RATIO, '#')` and
`draw_sears_tower(60, SEARS_TOWER_ASPECT_RATIO, '#')` both come out
centered, by eye, at every tier -- verified here by checking the
left-padding and right-padding on every printed line are equal (within
rounding) at heights 16, 22, and 60, including the `MINIMUM_ACCEPTABLE_WIDTH`
floor that height 16 actually hits.

## Part 2 — `draw_hancock`

The Hancock narrows continuously, row by row, rather than jumping
between three fixed tiers -- so instead of three `draw_tier` calls with
three fixed widths, this calls `draw_tier` once per row, one row tall
each time, with that row's own width. Row `0` (the top) is `top_width`
wide; the last row (the bottom) is `base_width` wide; every row in
between is a straight-line (linear) interpolation between the two:

```python
def draw_hancock(height: int):
    """Draws the John Hancock Center as a continuously narrowing,
    flat-topped shape, centered on its own base, at any height.

    Inputs:
    -------
    height: The total height of the tower, in printed lines.
    """
    if height <= 0:
        print("Height must be greater than 0 to draw a tower.")
    else:
        base_width = int(height / HANCOCK_ASPECT_RATIO)
        if base_width < MINIMUM_ACCEPTABLE_WIDTH:
            base_width = MINIMUM_ACCEPTABLE_WIDTH
        top_width = int(base_width * HANCOCK_TOP_WIDTH_SCALE)
        if top_width < HANCOCK_MINIMUM_TOP_WIDTH:
            top_width = HANCOCK_MINIMUM_TOP_WIDTH

        # The last row index, floored at 1 so a one-line-tall tower
        # (row 0 is both the first and only row) never divides by zero.
        last_row = max(height - 1, 1)
        for row in range(height):
            # row 0 -> top_width; the last row -> base_width; every row
            # between is a straight line from one to the other.
            row_width = top_width + (base_width - top_width) * row // last_row
            draw_tier(1, row_width, base_width, HANCOCK_BUILDING_BLOCK)
```

Self-check: `draw_hancock(16)` and `draw_hancock(60)` both widen steadily
from a flat top to a wide base, centered at every row, with no sharp
jumps the way the Sears Tower has -- and the top row never goes below
`HANCOCK_MINIMUM_TOP_WIDTH`, confirmed down at `height=1` and up at
`height=60` here.

## Turning it in

This is a worked model to check a submission against, not a substitute
for running your own code -- the assignment's own self-check (call both
functions at a short height and a tall one, confirm every tier/row is
centered by eye, then confirm a height of `0` falls back to the message
instead of a drawing) still applies to whatever you actually submit.

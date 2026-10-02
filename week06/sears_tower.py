"""Draws a simplified, three-tier schematic of the Sears Tower (Willis
Tower) out of a single building-block character.

Given a height (in printed lines) and an aspect ratio, works out how wide
the building should be, then allocates that height and width across three
tiers -- bottom, middle, and top -- the way we worked it out in class on
9/30, from the sears_tower.ipynb notebook in this same folder.
"""

# Real-world facts about the Sears Tower, for testing draw_sears_tower
# against real numbers.
SEARS_TOWER_HEIGHT_FEET = 1_425
SEARS_TOWER_WIDTH_FEET = 225
SEARS_TOWER_ASPECT_RATIO = SEARS_TOWER_HEIGHT_FEET / SEARS_TOWER_WIDTH_FEET

# Height allocated to each tier, as a fraction of the building's total
# height.
BOTTOM_TIER_HEIGHT_SCALE = 0.6
MIDDLE_TIER_HEIGHT_SCALE = 0.25
TOP_TIER_HEIGHT_SCALE = 0.15

# Width allocated to each tier, as a fraction of the tier below it.
MIDDLE_TIER_WIDTH_SCALE = 0.8
TOP_TIER_WIDTH_SCALE = 0.8 * MIDDLE_TIER_WIDTH_SCALE

# A width below this leaves no room to center a top tier (at least 3
# characters wide, for two antennas with a gap between them) on a middle
# tier (at least 5) on a bottom tier (at least 7):
#   |
#   | |
#   ***
#   ***
#   #####
#   #####
#   #######
MINIMUM_ACCEPTABLE_WIDTH = 7


def draw_tier(height: int, width: int, building_block: str):
    """Draws one tier: `height` rows of `width` copies of `building_block`.

    Inputs:
    -------
    height: The number of rows in this tier.
    width: The number of building-block characters per row.
    building_block: The character to use for the building block.
    """
    for floor in range(height):
        print(building_block * width)


def draw_sears_tower(height: int, aspect_ratio: float, building_block: str):
    """Draws a three-tier schematic of the Sears Tower.

    Inputs:
    -------
    height: The total height of the tower, in printed lines.
    aspect_ratio: height / width for the building, used to work out the
        tower's width from its height.
    building_block: The character to use for the building block.
    """
    # Protect against a bad aspect ratio -- it must be a positive number.
    if aspect_ratio <= 0:
        aspect_ratio = 1.0
    width = int(height / aspect_ratio)
    # Protect against a width too small to hold three distinguishable
    # tiers with room for the antennas.
    if width < MINIMUM_ACCEPTABLE_WIDTH:
        width = MINIMUM_ACCEPTABLE_WIDTH
    bottom_tier_height = int(height * BOTTOM_TIER_HEIGHT_SCALE)
    bottom_tier_width = width
    middle_tier_height = int(height * MIDDLE_TIER_HEIGHT_SCALE)
    middle_tier_width = int(width * MIDDLE_TIER_WIDTH_SCALE)
    top_tier_height = int(height * TOP_TIER_HEIGHT_SCALE)
    top_tier_width = int(width * TOP_TIER_WIDTH_SCALE)
    draw_tier(top_tier_height, top_tier_width, building_block)
    draw_tier(middle_tier_height, middle_tier_width, building_block)
    draw_tier(bottom_tier_height, bottom_tier_width, building_block)


if __name__ == "__main__":  # ignore this line for now
    draw_sears_tower(30, SEARS_TOWER_ASPECT_RATIO, '#')

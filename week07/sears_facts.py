"""Real-world facts about the Sears Tower, and the proportionality
constants our drawing uses to turn one number (the desired height) into
a full set of tier dimensions.

This file contains no logic -- no loops, no conditionals, no functions.
It is nothing but data: the facts concern, kept separate from the input,
logic, and output concerns so that any of those three can `import *`
this file and use these names without needing to know where they came
from or how they were computed.
"""

# The tower's real height and width, in feet -- the only two numbers we
# actually look up. Everything else below is derived from these two, or
# is a design choice about how to divide up a tower once we know its
# height.
SEARS_TOWER_HEIGHT_FEET = 1_425
SEARS_TOWER_WIDTH_FEET = 225

# The real tower's height-to-width ratio. Whatever height the user asks
# for in printed lines, we use this same ratio to decide how wide the
# bottom tier should be, so our drawing keeps the real tower's proportions
# no matter what height is requested.
SEARS_TOWER_ASPECT_RATIO = SEARS_TOWER_HEIGHT_FEET / SEARS_TOWER_WIDTH_FEET

# Height allocated to each tier, as a fraction of the building's total
# height. These three fractions add up to 1.0 -- every line of height
# the user asked for goes to exactly one tier.
BOTTOM_TIER_HEIGHT_SCALE = 0.6
MIDDLE_TIER_HEIGHT_SCALE = 0.25
TOP_TIER_HEIGHT_SCALE = 0.15

# Width allocated to each tier, as a fraction of the tier *below* it --
# not a fraction of the total width. That's why TOP_TIER_WIDTH_SCALE is
# written as a fraction of MIDDLE_TIER_WIDTH_SCALE: the top tier is 0.8
# as wide as the middle tier, which is itself 0.8 as wide as the bottom
# tier, so the building narrows step by step as it goes up.
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

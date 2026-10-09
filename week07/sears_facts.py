
# Real-world facts about the Sears Tower, represented as constants in a file 
# of their own so that other programs can import them.

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

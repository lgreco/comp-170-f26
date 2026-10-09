from sears_facts import *

def compute_widths(height: int) -> list[int]:
    """The first of two logic concerns: turn one validated height into
    the three tier widths. This function does no validation of its own
    -- get_input() already guaranteed `height` is usable, so this
    function is free to just compute.

    The bottom tier's width comes from the tower's real aspect ratio
    (height-to-width), scaled down to the height we were actually given.
    The middle and top widths are each a fraction of the tier directly
    below them -- not of the bottom width directly -- which is why we
    compute them bottom-up: bottom first, then middle from bottom, then
    top from middle.

    Input:
    ------
    height: int
      The desired height for the Sears tower in lines.

    Returns:
    --------
    list[int]
      An array (list) with the bottom, middle, and top tier widths, in
      that order.
    """
    bottom_width: int = int(height / SEARS_TOWER_ASPECT_RATIO)
    middle_width: int = int(bottom_width * MIDDLE_TIER_WIDTH_SCALE)
    top_width: int = int(middle_width * TOP_TIER_WIDTH_SCALE)

    results: list[int]  = [ bottom_width, middle_width, top_width ]

    return results


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
    # TODO: using BOTTOM_TIER_HEIGHT_SCALE, MIDDLE_TIER_HEIGHT_SCALE, and
    # TOP_TIER_HEIGHT_SCALE from sears_facts, compute each tier's height
    # from `height` directly (the same way compute_widths computes
    # bottom_width from height and SEARS_TOWER_ASPECT_RATIO), package all
    # three into one list in bottom/middle/top order, and return it --
    # one return statement, same as compute_widths.
    pass

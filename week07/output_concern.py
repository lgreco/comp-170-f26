def draw_tower(widths: list[int], heights: list[int], building_block: str):
    """The output concern: print the tower, tier by tier, from
    already-computed widths and heights. This function does no
    computing of its own -- compute_widths and compute_heights have
    already done that -- it only prints.

    `widths` and `heights` are parallel lists: `widths[i]` and
    `heights[i]` describe the same tier (bottom, middle, top, in that
    order -- the order compute_widths and compute_heights both use).
    Use `len()` on either list to find out how many tiers there are,
    rather than hard-coding 3 -- that's what makes this function work no
    matter how many tiers the logic concern decided to produce.

    For each tier, print that many rows of that many copies of
    `building_block`, the same single-tier printing you already wrote in
    Week 6's draw_tier.

    Note: this may get easier to write after the Monday 10/12 and
    Wednesday 10/14 class meetings, which cover techniques this method
    needs. Attempt it now with what you already know (indexing into a
    list with a loop variable, a nested loop for the rows within a
    tier); revisit it after those two meetings if it isn't working yet.

    Parameters:
        widths: the bottom, middle, and top tier widths, in that order.
        heights: the bottom, middle, and top tier heights, in that order.
        building_block: the single character used to draw every tier.
    """
    # TODO: find the number of tiers from widths or heights with len().
    # For each tier index, print heights[tier] rows, each row being
    # building_block repeated widths[tier] times (the same
    # height-rows-of-width-copies idea as Week 6's draw_tier). This
    # function has nothing to return -- it only prints.
    pass

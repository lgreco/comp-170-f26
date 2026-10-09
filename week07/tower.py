from sears_facts import *
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
    # TODO: get a validated height from the input concern, compute the
    # tier widths and tier heights from it (two separate logic-concern
    # calls), then hand both lists to the output concern to draw the
    # tower. One function call per concern, in that order -- this
    # function itself should have nothing left to compute or print.
    pass


if __name__ == "__main__":  # ignore this line for now
    draw_sears_tower('#')

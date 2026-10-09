def get_input() -> int:
    """The input concern: ask for the tower's desired height, and don't
    hand back control until we have something usable.

    The loop below assumes the user typed something wrong -- that's
    `correct = False` to start -- and only stops once a value has proven
    itself valid. This is the same "optimistic result, pessimistic
    default" shape used everywhere else in this course: rather than
    `return`ing the moment something looks right, we fall through the
    loop and return once, at the bottom, after the loop itself has
    decided we're done.

    A non-numeric answer (e.g. "twenty-one") raises a ValueError when we
    try to convert it with int(); we catch that, print an error, and let
    the loop ask again instead of letting the program crash. A negative
    number is numeric but still not a usable height, so it's rejected
    the same way a bad string is: by leaving `correct` False and looping
    again.

    Returns:
    -------
    height: The valid height entered by the user, as an integer -- a
        positive number of printed lines, or 0 if the user wants to quit.
    """
    INPUT_MESSAGE: str = "Desired height? (must be a positive integer, or 0 to quit): "
    ERROR_MESSAGE: str = "Height must be a positive integer, or 0 to quit."
    correct: bool = False
    while not correct:
        try:
            height: int = int(input(INPUT_MESSAGE))
            correct = height >= 0
        except ValueError:
            print(ERROR_MESSAGE)
    return height

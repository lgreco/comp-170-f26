"""Week 9 starter: the list toolkit we built in class (10/19, 10/21), cleaned
up, plus a stub for the one function you write: compare.

The functions below work on a list of integers or a list of strings.
Two of them, index_of_min and index_of_max, are the greedy searches from 10/23.
Python already has min() and max(); we write our own to see how they work.

Two of the functions below are built on others -- that is deliberate:

    contains  asks index_of     "is it here?"  is  "does it have a position?"
    count     asks indices_of   "how many?"    is  "how long is the list of positions?"

Read all six before you write anything. Do not change them.
"""

friends: list[str] = [
    "Hamza",
    "Allie",
    "Sia",
    "Anthony",
    "Sia",
    "Isabella",
    "Tommy",
    "Sia",
    "Yasmin",
    "Adem",
    "Aldin",
    "MaryGrace",
    "Drew",
    "Sia",
    "Veloashan",
]

lottery: list[int] = [7, 3, 19, 3, 42, 8, 3, 15]


def index_of(values: list, target) -> int:
    """Return the position of the first element of values equal to target,
    or -1 if target is not in values."""
    idx = -1  # pessimistic: assume not found
    i = 0
    while i < len(values) and idx == -1:  # stop as soon as we find it
        if values[i] == target:
            idx = i
        i = i + 1
    return idx


def contains(values: list, target) -> bool:
    """Return True if target appears in values, False otherwise."""
    found = index_of(values, target) != -1
    return found


def indices_of(values: list, target) -> list[int]:
    """Return every position at which target appears in values, in order.
    The result is an empty list if target does not appear."""
    paper = []  # the "piece of paper"
    for i in range(len(values)):  # cannot stop early: we want all
        if values[i] == target:
            paper.append(i)
    return paper


def count(values: list, target) -> int:
    """Return the number of times target appears in values (0 if never)."""
    total = len(indices_of(values, target))
    return total


def index_of_min(values: list) -> int:
    """Return the position of the smallest element of values, or -1 if values
    is empty. Greedy: assume position 0 is the smallest until an element
    challenges that assumption. Ties keep the earliest position."""
    idx = -1  # pessimistic: empty list
    if len(values) > 0:
        idx = 0  # assume the first is the smallest
        for i in range(1, len(values)):
            if values[i] < values[idx]:  # challenged: move the pointer
                idx = i
    return idx


def index_of_max(values: list) -> int:
    """Return the position of the largest element of values, or -1 if values
    is empty. Same greedy search as index_of_min with the comparison
    flipped. Ties keep the earliest position."""
    idx = -1
    if len(values) > 0:
        idx = 0
        for i in range(1, len(values)):
            if values[i] > values[idx]:
                idx = i
    return idx


##############################################################################
##############################################################################
##                                                                          ##
##             >>>>>>>>>>   YOUR CODE STARTS HERE   <<<<<<<<<<              ##
##                                                                          ##
##          Everything ABOVE this banner is given. Do not edit it.          ##
##        Edit ONLY compare(), just below. The tests come after it.         ##
##                                                                          ##
##############################################################################
##############################################################################


def compare(first: list, second: list) -> int:
    """TODO: decide which of the two lists is greater and return a negative
    integer if first is less than second, zero if they are equal by your
    rule, or a positive integer if first is greater than second.

    Both lists hold integers, or both hold strings -- never one of each.

    Replace this docstring with a description of YOUR rule: what do you
    mean by "greater", and why did you choose it?
    """
    result = 0
    # TODO
    return result


# ---------------------------------------------------------------- given tests
# DO NOT CHANGE ANYTHING BELOW THIS LINE.
# The tests are here to help you
# check your work.
#
# These tests do not know your rule. They check what any sensible rule must
# satisfy. If your compare passes all of them, it meets the specification.
#
# A note on what you will see below. Some of the commands in these tests go
# beyond what we covered in class. You do not need to write them or master
# them; you only need to know roughly what they do and why they are here.
#
#   assert condition, "message"
#       Checks that condition is True. If it is, nothing happens and the
#       program moves on. If it is False, Python stops right there and raises
#       an AssertionError carrying the message. It is the standard way to
#       say "this must be true here", and it is how a test announces that
#       something is wrong without any if/else/print scaffolding.
#
#   isinstance(thing, int)
#       Asks whether thing is of the given type: True if it is an int,
#       False otherwise. We use it to check that compare returns an integer
#       and not, say, a string or None, and to tell a list of strings from
#       a list of numbers.
#
#   try: ... except AssertionError as err: ...
#       Runs the code under try. If an assert inside it fails, the program
#       does not crash; control jumps to the except block, where err holds
#       the failure message. This lets run_tests report every failing test
#       instead of stopping at the first one. We will meet this properly
#       when we validate input.
#
#   f"... {value} ..."
#       An f-string: text with Python expressions in curly braces filled in.
#       The tests use it to put the offending lists into the failure message.
#       The {value!r} form shows the value the way you would type it in code,
#       so that "3" (a string) is distinguishable from 3 (a number).
#
#   test.__name__ and the list of functions in run_tests
#       Functions are values in Python. run_tests keeps the test functions in
#       a list and calls each one in a loop; __name__ is the name the
#       function was defined with, used for printing.
#
#   Parentheses around a long assert
#       When an assert is too long for one line, the condition goes inside
#       parentheses and the message follows on the next line. Only layout.

SAMPLE_LISTS: list[list] = [
    [],
    [5],
    [3, 3, 3],
    [7, 3, 19, 42],
    [1, 2, 3, 4, 5, 6],
    [40, 2],
    ["Sia"],
    ["Hamza", "Allie", "Sia"],
    ["Drew", "Adem", "Aldin", "Veloashan"],
    ["Yasmin", "Zoe"],
]


def sign(number: int) -> int:
    """Return -1, 0 or 1 according to the sign of number."""
    result = 0
    if number < 0:
        result = -1
    elif number > 0:
        result = 1
    return result


def same_kind(first: list, second: list) -> bool:
    """True unless one list holds numbers and the other holds strings."""
    ok = True
    if len(first) > 0 and len(second) > 0:
        ok = isinstance(first[0], str) == isinstance(second[0], str)
    return ok


def test_returns_an_integer() -> None:
    for first in SAMPLE_LISTS:
        for second in SAMPLE_LISTS:
            if same_kind(first, second):
                answer = compare(first, second)
                assert isinstance(
                    answer, int
                ), f"compare({first}, {second}) returned {answer!r}, not an int"


def test_a_list_equals_itself() -> None:
    for values in SAMPLE_LISTS:
        assert compare(values, values) == 0, f"compare({values}, {values}) should be 0"


def test_swapping_reverses_the_answer() -> None:
    for first in SAMPLE_LISTS:
        for second in SAMPLE_LISTS:
            if same_kind(first, second):
                forward = sign(compare(first, second))
                backward = sign(compare(second, first))
                assert (
                    forward == -backward
                ), f"compare({first}, {second}) and the swapped call disagree"


def test_the_rule_is_consistent() -> None:
    # If A beats B and B beats C, then A must beat C.
    for a in SAMPLE_LISTS:
        for b in SAMPLE_LISTS:
            for c in SAMPLE_LISTS:
                if same_kind(a, b) and same_kind(b, c) and same_kind(a, c):
                    if compare(a, b) > 0 and compare(b, c) > 0:
                        assert (
                            compare(a, c) > 0
                        ), f"{a} > {b} and {b} > {c}, but not {a} > {c}"


def test_compare_tells_some_lists_apart() -> None:
    different = 0
    for first in SAMPLE_LISTS:
        for second in SAMPLE_LISTS:
            if same_kind(first, second) and compare(first, second) != 0:
                different = different + 1
    assert different > 0, "compare says every pair of lists is equal"


def run_tests() -> None:
    """Run each test above and report ok or FAIL, with the reason."""
    tests = [
        test_returns_an_integer,
        test_a_list_equals_itself,
        test_swapping_reverses_the_answer,
        test_the_rule_is_consistent,
        test_compare_tells_some_lists_apart,
    ]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"ok    {test.__name__}")
            passed = passed + 1
        except AssertionError as err:
            print(f"FAIL  {test.__name__}: {err}")
    print(f"\n{passed} of {len(tests)} checks passed")


if __name__ == "__main__":
    run_tests()

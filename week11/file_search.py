"""Week 11 starter: searching a text file.

You write three functions that answer questions about the words in a file:

    search    asks index_of   "is the word in the file?" is
                              "does the word have a position?"
    count     (stands alone)  "how many times does the word appear?"
    index_of  (the workhorse) "where does the word first appear?"

A "word" here is exactly what str.split() gives you for a line (the 11/6
class calls these tokens). Matching is exact: "The" is not "the", and
"Hello," (with its comma) is not "Hello". That is deliberate, and one of the
questions in the README asks you to think about it.

Positions are counted from 0, as everywhere else in this course: the first
line of the file is line 0, and the first word of a line is word 0.

Read the whole file before you write anything. Everything above the line
"YOUR CODE STARTS HERE" is given; the three stubs are yours.
"""

# The mode we pass to open() when we only want to read. Naming it, instead of
# typing 'r' each time, is the magic-value cleanup from the 11/6 class.
READ_MODE = "r"

# The mode we pass to open() when we want to create a file, or replace its
# contents. The tests below use it to build a small file with known contents.
WRITE_MODE = "w"

# The name of the small file the tests create and then search.
SAMPLE_FILE = "sample_text.txt"

# The six lines of the sample file, in order. Line 2 is blank on purpose: a
# blank line still counts as a line, so your line counter must not skip it.
SAMPLE_LINES = [
    "the quick brown fox",
    "jumps over the lazy dog",
    "",
    "The end of the story",
    "the fox returns the favor",
    "Hello, world!",
]


# =====================================================================
# YOUR CODE STARTS HERE
# =====================================================================
# =====================================================================
# Below are the three functions you write. Each has a docstring that
# says what it promises and a hint about how to get there. Keep the
# docstrings (you may add to them). Every function has exactly one
# return, so set a pessimistic default first and overwrite it only
# when you find what you are looking for.
# =====================================================================


def index_of(file_name: str, word: str) -> list[int]:
    """Return [line, position] for the FIRST appearance of word in the file.

    line is the 0-based number of the line the word is on. position is the
    0-based place of the word among the words of that line, as split() sees
    them. If the word is nowhere in the file, return [-1, -1].

    Hint: read the file one line at a time. Keep a counter for the line
    number (it goes up for EVERY line, blank ones too). For each line, split
    it into a list of words and look for the word in that list; you wrote a
    function for exactly that on 10/19. Once you have found the word, stop
    updating your answer, because only the first appearance counts.
    """
    result = [-1, -1]  # pessimistic: assume the word is not in the file
    # TODO: replace the next line with your code.
    result = [-1, -1]
    return result


def search(file_name: str, word: str) -> bool:
    """Return True if word appears anywhere in the file, False otherwise.

    Hint: this is a one-line function, in the same way contains was a
    one-line function in Week 9. Ask index_of, and compare its answer with
    [-1, -1].
    """
    found = False  # pessimistic: assume the word is not in the file
    # TODO: replace the next line with your code.
    found = False
    return found


def count(file_name: str, word: str) -> int:
    """Return how many times word appears in the file, counting every line.

    Unlike index_of, this function cannot stop early: it has to read the
    whole file. A word that appears twice on the same line counts twice.

    Hint: an accumulator, as in the 11/6 average. Start it at 0; for each
    line, split it into words; for each word that equals the target, add 1.
    """
    total = 0  # nothing counted yet
    # TODO: replace the next line with your code.
    total = 0
    return total


# =====================================================================
# GIVEN TESTS -- DO NOT CHANGE ANYTHING BELOW THIS LINE
# =====================================================================
# A few commands in this section have not been covered in class. You do not
# need to master them; they are explained here so nothing is a mystery.
#
#   assert condition, "message"
#       Does nothing if the condition is True. If it is False, Python stops
#       with an AssertionError and shows the message.
#
#   def test_xyz():
#       Each test is a function with no inputs. The test runner at the bottom
#       calls them one at a time.
#
#   try: ... except AssertionError as problem: ...
#       "Try to run this code. If an assert fails, do not crash: catch the
#       error, call it 'problem', and run the except block instead." The
#       runner uses this so one failing test does not hide the others.
#
#   f"{name}"
#       A formatted string: whatever is inside the braces is replaced by its
#       value. You used these in class.
#
#   if __name__ == "__main__":
#       The code under this line runs when you run the file directly (python
#       file.py) but not when another program imports it.
# =====================================================================


def make_sample_file() -> None:
    """Create SAMPLE_FILE with the six lines in SAMPLE_LINES.

    Write mode replaces the contents of a file that already exists. That is
    exactly what we want here: every run of the tests starts from the same
    file. It is also why you should never use sample_text.txt for your own
    notes.
    """
    # Open the sample file for writing; 'with' closes it for us afterwards.
    with open(SAMPLE_FILE, WRITE_MODE) as sample:
        # Go through the lines one at a time.
        for line in SAMPLE_LINES:
            # write() does not add a newline for us, so we add "\n" ourselves.
            sample.write(line + "\n")


def test_index_of_returns_two_integers() -> None:
    """Why: the other tests compare whole lists, so the shape must be right."""
    answer = index_of(SAMPLE_FILE, "fox")
    # The answer must be a list, with exactly two entries ...
    assert isinstance(answer, list) and len(answer) == 2, (
        f"index_of must return a list of two integers, got {answer!r}"
    )
    # ... and both entries must be integers.
    assert isinstance(answer[0], int) and isinstance(answer[1], int), (
        f"both entries must be integers, got {answer!r}"
    )


def test_index_of_finds_first_appearance() -> None:
    """Why: 'the' appears many times; only the first one counts."""
    answer = index_of(SAMPLE_FILE, "the")
    assert answer == [0, 0], f"'the' first appears at line 0, word 0; got {answer}"
    answer = index_of(SAMPLE_FILE, "fox")
    assert answer == [0, 3], f"'fox' first appears at line 0, word 3; got {answer}"


def test_index_of_on_a_later_line() -> None:
    """Why: the line number must go up from line to line."""
    answer = index_of(SAMPLE_FILE, "lazy")
    assert answer == [1, 3], f"'lazy' is at line 1, word 3; got {answer}"
    answer = index_of(SAMPLE_FILE, "returns")
    assert answer == [4, 2], f"'returns' is at line 4, word 2; got {answer}"


def test_blank_lines_still_count() -> None:
    """Why: line 2 is blank. A counter that skips it puts 'story' on line 2."""
    answer = index_of(SAMPLE_FILE, "story")
    assert answer == [3, 4], f"'story' is at line 3, word 4; got {answer}"


def test_index_of_missing_word() -> None:
    """Why: the file's way of saying 'not here' is [-1, -1]."""
    answer = index_of(SAMPLE_FILE, "cat")
    assert answer == [-1, -1], f"'cat' is not in the file; got {answer}"


def test_matching_is_exact() -> None:
    """Why: a word is whatever split() gives, so capitals and punctuation count."""
    # 'The' (capital T) is a different word from 'the'.
    answer = index_of(SAMPLE_FILE, "The")
    assert answer == [3, 0], f"'The' is at line 3, word 0; got {answer}"
    # 'Hello,' keeps its comma, so 'Hello' alone is not in the file.
    assert index_of(SAMPLE_FILE, "Hello,") == [5, 0], "'Hello,' is at line 5, word 0"
    assert index_of(SAMPLE_FILE, "Hello") == [-1, -1], "'Hello' (no comma) is not a word here"


def test_search() -> None:
    """Why: search says only whether the word is there."""
    assert search(SAMPLE_FILE, "dog") is True, "'dog' is in the file"
    assert search(SAMPLE_FILE, "cat") is False, "'cat' is not in the file"
    assert search(SAMPLE_FILE, "world") is False, "'world' is not a word; 'world!' is"
    assert search(SAMPLE_FILE, "world!") is True, "'world!' is in the file"


def test_search_agrees_with_index_of() -> None:
    """Why: the two functions must never disagree about the same word."""
    for word in ["the", "The", "fox", "cat", "Hello,", "Hello", "story", ""]:
        expected = index_of(SAMPLE_FILE, word) != [-1, -1]
        assert search(SAMPLE_FILE, word) is expected, (
            f"search and index_of disagree about {word!r}"
        )


def test_count() -> None:
    """Why: count reads the whole file, and every appearance counts."""
    assert count(SAMPLE_FILE, "the") == 5, f"'the' appears 5 times; got {count(SAMPLE_FILE, 'the')}"
    assert count(SAMPLE_FILE, "fox") == 2, f"'fox' appears 2 times; got {count(SAMPLE_FILE, 'fox')}"
    assert count(SAMPLE_FILE, "The") == 1, f"'The' appears once; got {count(SAMPLE_FILE, 'The')}"
    assert count(SAMPLE_FILE, "cat") == 0, f"'cat' appears 0 times; got {count(SAMPLE_FILE, 'cat')}"


def test_count_on_the_same_line() -> None:
    """Why: 'the' appears twice on line 4, and both appearances are counted."""
    # A count that adds 1 per LINE containing the word, instead of 1 per
    # appearance, would get 'the' wrong here: line 4 is
    # 'the fox returns the favor'.
    assert count(SAMPLE_FILE, "favor") == 1, "'favor' appears exactly once"
    assert count(SAMPLE_FILE, "the") == 5, "line 4 contributes two of the five"


def run_tests() -> None:
    """Build the sample file, then run every given test and report the result."""
    make_sample_file()
    # Every test function, in the order they are defined above.
    tests = [
        test_index_of_returns_two_integers,
        test_index_of_finds_first_appearance,
        test_index_of_on_a_later_line,
        test_blank_lines_still_count,
        test_index_of_missing_word,
        test_matching_is_exact,
        test_search,
        test_search_agrees_with_index_of,
        test_count,
        test_count_on_the_same_line,
    ]
    passed = 0  # how many tests passed so far
    for test in tests:
        try:
            test()
            print(f"  ok    {test.__name__}")
            passed += 1
        except AssertionError as problem:
            print(f"  FAIL  {test.__name__}: {problem}")
    print(f"\n{passed} of {len(tests)} tests passed.")


if __name__ == "__main__":
    run_tests()
    # Your own experiments go below this line, for example:
    # print(index_of("taleoftwocities.txt", "Defarge"))  # the book is in this folder

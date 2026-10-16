"""Facts: nothing but the passenger manifest and the seat-map
constants. No program logic lives here -- same idea as sears_facts.py.

The manifest is stored as one flat (one-dimensional) array, exactly the
way we've been storing everything else this term. The seat chart itself
is two-dimensional -- rows and seat letters -- but we are deliberately
*not* storing it as a 2D array of rows this time. Instead we store it
flat and compute each passenger's row and seat letter from their
position with // and %, the same "a 2D array is really a 1D array
snaking through memory" idea previewed in class on 10/12, and the same
airplane-seat-25A example used in class on 10/14 for real-world 2D
indexing.
"""

SEATS_PER_ROW: int = 4  # 2 seats, the aisle, 2 seats -- "2+2"
FIRST_SEAT_LETTER: str = 'A'

# One name per seat, in position order: seat 0 is row 1 seat A, seat 1 is
# row 1 seat B, and so on -- four names per row, then the next row starts.
PASSENGERS: list[str] = [
    'Leo',   'Saruman', 'Petunia', 'Ron',
    'Bellatrix', 'Hermione', 'Alberich', 'Tristan',
    'Kenji', 'Talia', 'Omar',  'Vera',
    'Diego', 'Hana',  'Felix', 'Zara',
    'Milo',  'Ingrid','Sam',   'Yuki',
]


def position_to_seat(position: int) -> list:
    """Decode: given a position in the flat PASSENGERS array, work out
    which row and seat letter that position corresponds to on the
    airplane. This is given to you, complete, as the worked example of the
    // and % operators from the 10/16 class -- read it carefully before
    you write seat_to_position, which does the same job in reverse.

    The idea: every SEATS_PER_ROW positions is one full row. // (integer
    division) throws away the remainder and tells you how many *complete*
    rows have gone by -- that's the row number, once we add 1 because
    rows are numbered starting at 1, not 0. % (modulo) keeps only the
    remainder -- how far into the *current* row this position sits --
    which we turn into a letter by counting that many letters past 'A'.

    Input:
    ------
    position: int
      A valid index into PASSENGERS (0, 1, 2, ...).

    Returns:
    --------
    list
      [row, seat_letter] -- row is an int (1, 2, 3, ...), seat_letter is
      a single character ('A', 'B', 'C', or 'D' for a 2+2 layout).
    """
    row: int = position // SEATS_PER_ROW + 1
    seat_index: int = position % SEATS_PER_ROW
    seat_letter: str = chr(ord(FIRST_SEAT_LETTER) + seat_index)

    result: list = [row, seat_letter]

    return result


def seat_to_position(row: int, seat_letter: str) -> int:
    """Encode: the reverse of position_to_seat. Given a row and a seat
    letter -- the way a passenger actually hears their own seat assignment,
    e.g. "2C" -- work out which position that is in the flat PASSENGERS
    array.

    TODO: using SEATS_PER_ROW and FIRST_SEAT_LETTER, write the one-line
    formula that undoes position_to_seat. Think about it in two pieces:
    how many full rows come before this row (and therefore how many
    seats that is), plus how far seat_letter sits past FIRST_SEAT_LETTER
    within this row. Add those two pieces together.

    Input:
    ------
    row: int
      The row number (1, 2, 3, ...).
    seat_letter: str
      A single character ('A', 'B', 'C', or 'D' for a 2+2 layout).

    Returns:
    --------
    int
      The matching position in PASSENGERS -- should satisfy
      position_to_seat(seat_to_position(row, seat_letter)) == [row, seat_letter]
      for every valid seat.
    """
    position: int = 0  # TODO: replace with the real formula

    return position


def print_seat_assignments(passengers: list[str]) -> None:
    """Print the seating chart, one block per row, with a "|" marking
    the aisle between seats B and C. Each block is a line of seat labels
    over a line of passenger names, columns aligned, a blank line
    between rows:

        1A         1B        |  1C        1D
        Leo        Saruman   |  Petunia   Ron

        2A         2B        |  2C        2D
        Bellatrix  Hermione  |  Alberich  Tristan

    TODO: study the sample above carefully (squared paper, one character
    per square, helps). Loop by position -- you need the position itself
    to decode a seat -- and call position_to_seat on each one. You will
    need the length of the longest name to pad columns, and you may
    write helper functions of your own.

    Input:
    ------
    passengers: list[str]
      The flat passenger manifest (pass in PASSENGERS).

    Returns:
    --------
    None
      This function only prints; it has nothing to hand back.
    """
    pass  # TODO


def who_is_in_seat(passengers: list[str], row: int, seat_letter: str) -> str:
    """Answer "who's sitting in seat 1A?" -- using seat_to_position to
    turn the row/letter the question is asked in into a position, then
    looking that position up in passengers.

    If the row/seat_letter given doesn't correspond to an occupied seat
    (out of range for this manifest), say so instead of crashing --
    pessimistic default first, the same pattern get_input used.

    Input:
    ------
    passengers: list[str]
      The flat passenger manifest (pass in PASSENGERS).
    row: int
      The row number being asked about.
    seat_letter: str
      The seat letter being asked about.

    Returns:
    --------
    str
      The passenger's name, or a message that the seat is empty/invalid.
    """
    result: str = 'No one is booked in that seat.'  # pessimistic default

    # TODO: compute the position with seat_to_position, then -- only if
    # that position actually falls inside passengers -- overwrite result
    # with passengers[position].

    return result

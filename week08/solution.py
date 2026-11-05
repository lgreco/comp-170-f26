# SOLUTION -- Week 8 (airplane seating chart). Posted after the deadline.
# Your own approach may differ; what must match is the output the assignment shows.
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
LAST_LEFT_COLUMN: int = SEATS_PER_ROW // 2 - 1  # column index of seat B
GAP: str = '  '    # between neighbouring seats
AISLE: str = '  |  '  # between the two halves of a row
EMPTY: str = ''
NO_ONE: str = 'No one is booked in that seat.'

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
    letter, work out which position that is in the flat PASSENGERS array.

    Two pieces, added together:
      - (row - 1) * SEATS_PER_ROW: the seats in all the complete rows
        before this one (rows are numbered from 1, so row 1 has zero
        rows before it);
      - ord(seat_letter) - ord(FIRST_SEAT_LETTER): how far into this row
        the letter sits ('A' is 0, 'B' is 1, ...).

    Input:
    ------
    row: int
      The row number (1, 2, 3, ...).
    seat_letter: str
      A single character ('A', 'B', 'C', or 'D' for a 2+2 layout).

    Returns:
    --------
    int
      The matching position in PASSENGERS.
    """
    seats_before_row: int = (row - 1) * SEATS_PER_ROW
    seat_index: int = ord(seat_letter) - ord(FIRST_SEAT_LETTER)
    position: int = seats_before_row + seat_index

    return position


def column_widths(passengers: list[str]) -> list[int]:
    """Helper: for each seat column (A, B, C, D), the width of the
    widest entry in that column -- either a passenger's name or a seat
    label such as '10A'. Columns are padded to their own widest entry,
    which is what makes the sample chart line up.

    Input:
    ------
    passengers: list[str]
      The flat passenger manifest.

    Returns:
    --------
    list[int]
      One width per seat column, SEATS_PER_ROW of them.
    """
    widths: list[int] = [0] * SEATS_PER_ROW
    for position in range(len(passengers)):
        row, seat_letter = position_to_seat(position)
        column: int = position % SEATS_PER_ROW
        label: str = f'{row}{seat_letter}'
        widest: int = max(len(label), len(passengers[position]))
        if widest > widths[column]:
            widths[column] = widest

    return widths


def build_line(cells: list[str], widths: list[int]) -> str:
    """Helper: join the cells of one printed line (either the seat
    labels or the names of one row). Each cell is padded to its column
    width; the gap after a column is GAP, except right after the
    last seat on the left side of the aisle, where it is AISLE. The
    final cell is not padded, so lines carry no trailing spaces.

    Input:
    ------
    cells: list[str]
      The texts for one row, in seat order (usually SEATS_PER_ROW of
      them; fewer on a partly filled last row).
    widths: list[int]
      Column widths from column_widths.

    Returns:
    --------
    str
      The assembled line.
    """
    line: str = EMPTY
    for column in range(len(cells)):
        is_last: bool = column == len(cells) - 1
        if is_last:
            line = line + cells[column]
        else:
            line = line + cells[column].ljust(widths[column])
            if column == LAST_LEFT_COLUMN:
                line = line + AISLE
            else:
                line = line + GAP

    return line


def print_seat_assignments(passengers: list[str]) -> None:
    """Print the seating chart, one block per row: a line of seat labels
    over a line of passenger names, columns aligned, the aisle marked
    with "|", a blank line between rows.

    Loops by position, decodes each position with position_to_seat, and
    flushes a block whenever the row is complete (or the manifest ends).

    Input:
    ------
    passengers: list[str]
      The flat passenger manifest (pass in PASSENGERS).

    Returns:
    --------
    None
      This function only prints.
    """
    widths: list[int] = column_widths(passengers)
    labels: list[str] = []
    names: list[str] = []

    for position in range(len(passengers)):
        row, seat_letter = position_to_seat(position)
        labels.append(f'{row}{seat_letter}')
        names.append(passengers[position])

        row_is_complete: bool = position % SEATS_PER_ROW == SEATS_PER_ROW - 1
        manifest_is_over: bool = position == len(passengers) - 1
        if row_is_complete or manifest_is_over:
            if row != 1:
                print()  # blank line *between* rows, not before the first
            print(build_line(labels, widths))
            print(build_line(names, widths))
            labels = []
            names = []


def who_is_in_seat(passengers: list[str], row: int, seat_letter: str) -> str:
    """Answer "who's sitting in seat 1A?" -- using seat_to_position to
    turn the row/letter into a position, then looking that position up
    in passengers.

    Pessimistic default first; the result is overwritten only if the
    seat really exists: a letter within the row, a row of at least 1,
    and a position inside passengers. (Checking the letter matters:
    1E would otherwise silently land on seat 2A.)

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
      The passenger's name, or a message that no one is booked there.
    """
    result: str = NO_ONE

    position: int = seat_to_position(row, seat_letter)
    seat_index: int = ord(seat_letter) - ord(FIRST_SEAT_LETTER)
    letter_ok: bool = 0 <= seat_index < SEATS_PER_ROW
    position_ok: bool = 0 <= position < len(passengers)
    if row >= 1 and letter_ok and position_ok:
        result = passengers[position]

    return result


if __name__ == '__main__':
    print_seat_assignments(PASSENGERS)
    print(who_is_in_seat(PASSENGERS, 2, 'C'))
    print(who_is_in_seat(PASSENGERS, 1, 'A'))
    print(who_is_in_seat(PASSENGERS, 99, 'A'))

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
    # Complete rows before this position, plus 1 because rows start at 1.
    row: int = position // SEATS_PER_ROW + 1
    # How far into the current row we are: 0 for A, 1 for B, and so on.
    seat_index: int = position % SEATS_PER_ROW
    # ord() turns 'A' into its character code, we add the offset, and chr()
    # turns the new code back into a letter: 'A' + 2 gives 'C'.
    seat_letter: str = chr(ord(FIRST_SEAT_LETTER) + seat_index)

    # Package both answers in a list so the function can return them together.
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
    # Every complete row before this one contributes SEATS_PER_ROW positions.
    seats_before_row: int = (row - 1) * SEATS_PER_ROW
    # Subtracting character codes gives the letter's offset: 'C' - 'A' is 2.
    seat_index: int = ord(seat_letter) - ord(FIRST_SEAT_LETTER)
    # Skip the earlier rows, then move across this row to the seat.
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
    # One running maximum per column, all starting at 0 so any entry beats it.
    widths: list[int] = [0] * SEATS_PER_ROW
    # Visit every seat in the manifest, one position at a time.
    for position in range(len(passengers)):
        # Decode the position; unpacking splits the [row, letter] list in two.
        row, seat_letter = position_to_seat(position)
        # The column is the seat's offset within its row, again via %.
        column: int = position % SEATS_PER_ROW
        # The seat label printed above the name, e.g. '10A'.
        label: str = f'{row}{seat_letter}'
        # The wider of the label and the name decides how much room this seat needs.
        widest: int = max(len(label), len(passengers[position]))
        # Keep the largest width seen so far for this column.
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
    # Start with an empty line and append to it, cell by cell.
    line: str = EMPTY
    for column in range(len(cells)):
        # The last cell on the line gets no padding and no gap after it.
        is_last: bool = column == len(cells) - 1
        if is_last:
            line = line + cells[column]
        else:
            # ljust pads the cell with spaces on the right up to the column's width.
            line = line + cells[column].ljust(widths[column])
            # After the last seat left of the aisle, draw the aisle;
            # after any other seat, just a small gap.
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
    # Measure the columns once, up front, so every row is aligned the same way.
    widths: list[int] = column_widths(passengers)
    # The two lines of the row being collected: seat labels and names.
    labels: list[str] = []
    names: list[str] = []

    for position in range(len(passengers)):
        # Decode this position into its row and letter.
        row, seat_letter = position_to_seat(position)
        # Add this seat's label and passenger to the row being collected.
        labels.append(f'{row}{seat_letter}')
        names.append(passengers[position])

        # The last seat of a row has offset SEATS_PER_ROW - 1 (here, D).
        row_is_complete: bool = position % SEATS_PER_ROW == SEATS_PER_ROW - 1
        # A partly filled last row must still be printed.
        manifest_is_over: bool = position == len(passengers) - 1
        if row_is_complete or manifest_is_over:
            if row != 1:
                print()  # blank line *between* rows, not before the first
            # Print the labels line, then the names line, of this row.
            print(build_line(labels, widths))
            print(build_line(names, widths))
            # Start fresh lists for the next row.
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
    # Pessimistic default: assume nobody is there.
    result: str = NO_ONE

    # Translate the seat into an index of the flat array.
    position: int = seat_to_position(row, seat_letter)
    # Where the letter falls within a row; must be 0..3 for a 2+2 plane.
    seat_index: int = ord(seat_letter) - ord(FIRST_SEAT_LETTER)
    # A chained comparison: True only if seat_index is between 0 and 3.
    letter_ok: bool = 0 <= seat_index < SEATS_PER_ROW
    # The position must also fall inside the manifest, or indexing would crash.
    position_ok: bool = 0 <= position < len(passengers)
    # Only when every check passes do we replace the default with the name.
    if row >= 1 and letter_ok and position_ok:
        result = passengers[position]

    return result


# Runs only when this file is executed directly, not when it is imported.
if __name__ == '__main__':
    # The whole chart.
    print_seat_assignments(PASSENGERS)
    # A seat in the middle of the plane.
    print(who_is_in_seat(PASSENGERS, 2, 'C'))
    # The very first seat (position 0).
    print(who_is_in_seat(PASSENGERS, 1, 'A'))
    # A row far beyond the manifest: expect the "No one" message.
    print(who_is_in_seat(PASSENGERS, 99, 'A'))

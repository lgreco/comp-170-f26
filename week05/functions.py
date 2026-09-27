# The border around the hollow square has two sides: one band of
# lines above it, one below. This constant is that count, used to
# split the border lines evenly between top and bottom.
BORDER_SIDES = 2


def print_square(size: int, fill_char: str):
    # A solid square is just "size" identical lines, and each line is
    # the same character repeated "size" times, so one loop is enough:
    # go around it "size" times, printing one full-width line each time.
    for i in range(size):
        print(fill_char * size)


def draw_square(outside_size: int,
                inside_size: int,
                fill_char: str,
                hollow_char: str):

    # check if sizes are ok: the hollow part has to fit inside the
    # square with at least a one-character border all around it, so
    # outside_size has to be bigger than inside_size by at least 2.
    # (outside_size > inside_size + 1 is the same thing written the
    # other way around.)
    if outside_size > inside_size + 1:
        # Picture the square as three horizontal bands, top to bottom:
        # a solid top border, a middle band where each line has a
        # border character, then hollow characters, then a border
        # character again, and a solid bottom border that mirrors the
        # top. Work out, in plain English, how many lines each band
        # needs before writing any loop.

        # The middle band has exactly one line per row of the hollow
        # square, so it's inside_size lines tall.
        hollow_lines = inside_size
        # Whatever lines aren't part of the middle band are split
        # evenly between the top and bottom borders.
        non_hollow_lines = outside_size - inside_size
        # Split those border lines evenly between the two sides, top
        # and bottom. Integer division (//) is what makes this a
        # whole number of lines.
        outside_border_size = non_hollow_lines // BORDER_SIDES

        # print top half: outside_border_size solid lines, each the
        # full outside_size wide, using only fill_char.
        for line in range(outside_border_size):
            print(fill_char * outside_size)

        # print the middle part: for each of the hollow_lines rows,
        # print a border on the left, the hollow characters in the
        # middle, then the same border on the right. Using end=""
        # for the first two pieces keeps them on the same line as the
        # third, which prints the newline as usual.
        for line in range(hollow_lines):
            print(fill_char * outside_border_size, end = "")
            print(hollow_char * inside_size, end ="")
            print(fill_char * outside_border_size)

        # print the bottom part: the mirror image of the top half,
        # same number of lines, same character, same width.
        for line in range(outside_border_size):
            print(fill_char * outside_size)

    else:
        # Bad input gets a message, not a drawing. This particular
        # message is a joke for class discussion; when you write your
        # own size check for the assignment, make yours informative
        # instead — say what was wrong and what a valid size looks like.
        print("Tell something nasty to the client")


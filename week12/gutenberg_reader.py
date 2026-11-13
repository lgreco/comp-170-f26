"""Week 12: counting words in a book straight from the Project Gutenberg server.

This is the cleaned-up version of the code from the 11/11 and 11/13 classes.
One function, count_words, does everything: it downloads the book line by
line, keeps ONLY the lines of the book itself (everything after the first
line that starts with "*** " and before the next one), and counts how many
times each word appears.

Every Project Gutenberg text file wraps the actual book between two marker
lines (we called them sentinels in class):

    *** START OF THE PROJECT GUTENBERG EBOOK A TALE OF TWO CITIES ***
    ... the book Dickens actually wrote ...
    *** END OF THE PROJECT GUTENBERG EBOOK A TALE OF TWO CITIES ***

Above the first marker is Gutenberg's preamble; below the second is the
license. That's where "ebooks", "newsletter" and "Mississippi" came from on
Friday. Dickens is innocent.
"""

from urllib.request import urlopen

# The plain-text version of A Tale of Two Cities on the Gutenberg server.
BOOK_URL = "https://www.gutenberg.org/cache/epub/98/pg98.txt"

# Every marker line starts with three stars and a space. On Friday I used the
# slice line[0:4] to grab the beginning of each line, and the 4 was a magic
# number. Its real meaning is "as many characters as the sentinel has", so
# below I write len(SENTINEL) instead, and the 4 disappears.
SENTINEL = "*** "

# A file on a remote server arrives as bytes, not characters (the b'...'
# strings we saw on Wednesday). Decoding with UTF-8, the Unicode encoding most
# files use today, turns the bytes back into a normal string.
ENCODING = "utf-8"


def count_words(book_url: str) -> dict:
    """Return a dictionary that maps each word in the book to the number of
    times it appears.

    Only the book itself is counted: lines before the first line that starts
    with SENTINEL are ignored, and so is everything from the next line that
    starts with SENTINEL onward. The sentinel lines are not counted either.

    A "word" is whatever split() gives us, made lowercase. That's all the
    cleaning we do for now: "cat." and "cat" still count as two different
    words. Your proposals for Monday are about fixing exactly that.

    Yes, this one function both reads the file and counts the words. Reading
    and counting are two different jobs, and they'd be cleaner as two
    functions. We'll get there; for now, everything is in one place so you
    can follow it top to bottom.
    """
    word_counts = dict()  # same as word_counts = {}

    # These are the two flags from Friday. Raise your hand when you see the
    # first sentinel; keep it raised while you read the book; lower it when
    # you see the second sentinel. One flag couldn't tell "before the book"
    # from "after the book", because both look like "not in the book". Two
    # flags can.
    first_sentinel_found = False
    second_sentinel_found = False

    with urlopen(book_url) as book:
        # The for loop goes through every line of the file, the license
        # included. The flags decide which lines we count; the loop itself
        # doesn't stop early.
        for raw_line in book:
            # Decode BEFORE comparing. On Friday the comparison kept failing
            # because I was comparing bytes to a string, and bytes never
            # equal a string, no matter how alike they look.
            line = raw_line.decode(ENCODING)
            beginning = line[0:len(SENTINEL)]
            is_sentinel = beginning == SENTINEL

            if is_sentinel and first_sentinel_found:
                # This is the second sentinel: the book is over. From here
                # on, every line is license text, and we ignore it.
                second_sentinel_found = True
            elif is_sentinel:
                # This is the first sentinel: the book starts on the next line.
                first_sentinel_found = True
            elif first_sentinel_found and not second_sentinel_found:
                # Hand raised, not yet lowered: this line belongs to the
                # book, so we count its words.
                words = line.split()
                for word in words:
                    # "Cat" at the start of a sentence and "cat" in the
                    # middle of one are the same word, so everything becomes
                    # lowercase.
                    clean_word = word.lower()
                    if clean_word in word_counts:
                        # Seen it before: one more time.
                        word_counts[clean_word] += 1
                    else:
                        # First time we see it, so its count starts at 1,
                        # not 0. (That was the attendance bug from Monday.)
                        word_counts[clean_word] = 1
            # Any other line is preamble or license, so we just skip it.

    return word_counts


if __name__ == "__main__":
    # Fetching the book over the network takes a few seconds. If the
    # Gutenberg server or the wifi is down, this line is where it fails. A
    # robust program would deal with that; this one trusts the internet.
    word_counts = count_words(BOOK_URL)
    print(f"Distinct words:           {len(word_counts)}")
    print(f"'the' appears             {word_counts['the']} times")
    print(f"'a' appears               {word_counts['a']} times")

    # The boilerplate words from Friday should be gone. "in" asks the
    # dictionary whether a key exists, without crashing if it doesn't (which
    # is what happened with word_counts['hobbit']).
    print(f"Is 'ebooks' still here?   {'ebooks' in word_counts}")
    print(f"Is 'newsletter' here?     {'newsletter' in word_counts}")

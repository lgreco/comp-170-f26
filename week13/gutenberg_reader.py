from urllib.request import urlopen

BOOK_URL = "https://www.gutenberg.org/cache/epub/98/pg98.txt"
ALT_URL = "https://raw.githubusercontent.com/lgreco/comp-170-f26/refs/heads/main/week11/taleoftwocities.txt"
SENTINEL = "*** "
ENCODING = "utf-8"


def count_words(book_url: str) -> dict:
    word_counts = dict()  # same as word_counts = {}

    first_sentinel_found = False
    second_sentinel_found = False

    with urlopen(book_url) as book:
        for raw_line in book:
            line = raw_line.decode(ENCODING)
            beginning = line[0 : len(SENTINEL)]
            is_sentinel = beginning == SENTINEL
            if is_sentinel and first_sentinel_found:
                second_sentinel_found = True
            elif is_sentinel:
                first_sentinel_found = True
            elif first_sentinel_found and not second_sentinel_found:
                words = line.split()
                for word in words:
                    clean_word = word.lower()
                    if clean_word in word_counts:
                        word_counts[clean_word] += 1
                    else:
                        word_counts[clean_word] = 1
    return word_counts


if __name__ == "__main__":
    word_counts = count_words(ALT_URL)
    print(f"Distinct words:           {len(word_counts)}")
    print(f"'the' appears             {word_counts['the']} times")
    print(f"'a' appears               {word_counts['a']} times")
    print(f"Is 'ebooks' still here?   {'ebooks' in word_counts}")
    print(f"Is 'newsletter' here?     {'newsletter' in word_counts}")

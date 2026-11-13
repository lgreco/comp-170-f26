from urllib.request import urlopen

book_url = "https://www.gutenberg.org/cache/epub/98/pg98.txt"
sentinel = "*** "
word_counts = dict()
first_sentinel_found = False
second_sentinel_found = False

with urlopen(book_url) as book:
    for line in book:
            words = line.decode("utf-8").split()
            for word in words:
                cleaned_word = word.lower()
                if cleaned_word in word_counts:
                    word_counts[cleaned_word] += 1
                else:
                    word_counts[cleaned_word] = 1

#rint(word_counts)

#print(word_counts['a'])
#print(word_counts['the'])
print(len(word_counts))
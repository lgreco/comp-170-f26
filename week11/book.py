book_to_read = 'taleoftwocities.txt'
READ_MODE = 'r'
line_counter = 0
word_counter = 0
with open(book_to_read, READ_MODE) as book:
    for line in book:
        line_counter += 1  # line_counter++
        word_counter += len(line.split())

print(f"There are {line_counter:,d} lines in the book.")
print(f"Ther are {word_counter:,d} words in the book.")


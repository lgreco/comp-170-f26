# Week 11 Assignment — Searching a Text File

Due Friday, November 13. Deliverable is a single file, `file_search.py`. Start from the starter file in this folder, [`file_search.py`](./file_search.py).

## Where we are

For two weeks we have been asking questions about a *list*: where is this value (`index_of`), is it there at all (`contains`), how many times (`count`). This week the data moved out of the program and into a **file**, as it did in the 11/4 and 11/6 classes. The questions are the same. Only the place where the data lives has changed.

In class on 11/6 we read *A Tale of Two Cities* line by line, counted its lines, and used `split()` to count its words. You will now build the three questions on top of those two moves:

| Function | Question it answers |
|---|---|
| `index_of(file_name, word)` | Where does `word` first appear? Answer: `[line, position]`, or `[-1, -1]` if it never does |
| `search(file_name, word)` | Is `word` in the file at all? Answer: `True` or `False` |
| `count(file_name, word)` | How many times does `word` appear in the whole file? |

## Your task

Complete the three functions in the starter file.

- A **word** is exactly what `split()` returns for a line. Matching is exact, so `"The"` is not `"the"`, and `"Hello,"` (with its comma) is not `"Hello"`.
- **`line`** is the number of the line the word is on, and **`position`** is the place of the word among the words of that line. Both are counted from **0**, like every index in this course. A blank line is still a line.
- **`index_of`** reports only the **first** appearance.
- **`search`** should not repeat the work of `index_of`. In Week 9, `contains` asked `index_of` and compared. The same relationship holds here.
- **`count`** has to read the entire file, and a word that appears twice on one line counts twice.

You may assume the file exists. You do not need to handle a missing file.

## Constraints

- Every function that returns a value has exactly one `return`. Start from a pessimistic default and overwrite it when you find what you are looking for.
- Open files with `with`, and use named constants (`READ_MODE`) instead of repeating `'r'`.
- Every function has a docstring. Keep the ones in the starter file.
- No `.index()`, `.count()`, or `in` on a list of words inside `index_of`; write the loop yourself, as we did on 10/19. (`in` on a *string*, and `split()`, are fine.)
- Do not change the given tests, and do not use `sample_text.txt` for your own work: the tests recreate it every run.

## Run it on a real book

Use [`taleoftwocities.txt`](./taleoftwocities.txt), the copy of the book already in this week's folder (the same file we used on 11/6; do not download or edit another). Keep it in the same folder as `file_search.py` so you can open it by name, and run your functions on it. In a comment block at the end of your file, answer:

1. How many times does `"the"` appear? `"The"`? Add them. Is that the number of times the word *the* appears in the book? What does your answer miss?
2. Where does `"Defarge"` first appear? Is that line near the beginning, the middle, or the end of the book? How did you decide?
3. Pick two other words that interest you. Report `search`, `count`, and `index_of` for each, and one thing about the answers that surprised you.
4. `search` and `count` both read the whole book when the word is absent. When the word is present, does `search` have to? Does `count`? Explain in two sentences.

## Reading

- [*Introducing Python*, 3rd ed., Ch. 17, Text Data](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch17.html) — strings and the text methods behind `split()` and `strip()`. *Optional.*
- [*Introducing Python*, 3rd ed., Ch. 20, Files](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch20.html) — opening, reading, writing, and closing files.
- [Python tutorial, input and output](https://docs.python.org/3/tutorial/inputoutput.html) — formatting output, then `open`, modes, `with`, and looping over a file's lines (start at the section on reading and writing files).
- [Python docs, string `split` method](https://docs.python.org/3/library/stdtypes.html#str.split) — exactly what a "word" means in this assignment, including what happens with runs of spaces.
- [Python docs, string `strip` method](https://docs.python.org/3/library/stdtypes.html#str.strip) — the newline cleanup from 11/4.
- [Project Gutenberg, *A Tale of Two Cities*](https://www.gutenberg.org/ebooks/98) — where our book came from, if you are curious about the original.
- For the commands explained in the test comments (you do not need to master them): the Week 9 reading on `assert`, `isinstance`, and f-strings.

Previously assigned readings are still fair game for questions in class or on assessments.

## Thanksgiving week: tell me what you prefer

We do not meet on Wednesday or Friday of Thanksgiving week. The Monday before, **November 23**, is up to you: we can meet in person, meet on Zoom, or skip the meeting and replace it with a reading or other learning activity you do on your own. Please answer the one-question survey so I can plan:

[Thanksgiving Monday survey: in person, Zoom, or asynchronous](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=408fApwrJEiDeLvPnsWsy7I196tvCVFAgylhP23oZuNUMVFFT1BHNlAwRTROOVBFUUU1TTFLUENGVy4u)

## Turning it in

Upload `file_search.py` to Sakai, containing your three functions, the given tests, and your answers to the book questions in a comment block at the end.

Before you upload, run the file. It prints one line per given test, and you want every one to say `ok`.

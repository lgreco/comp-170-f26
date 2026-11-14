# Week 12 — Dictionaries, and a Memo on Cleaning Text

Due **Monday, November 16**. No code this time: the deliverable is a memo of two to three pages (about 600–900 words).

## This week in class

**Monday 11/9: the problem dictionaries solve.** We kept attendance with two lists synchronized by index, one of names and one of absence counts. [`sync_lists.py`](./sync_lists.py) is that version: `index_of` finds a student's position, `add_absence` adds one at the same position in the other list, and `report` prints both side by side. It works as long as the two lists never fall out of step. Insert one student in one list but not the other, and every count after that point belongs to the wrong person. Keeping lists in step by hand is how record keeping was done for decades. It is also where relational databases came from: Ted Codd's paper, which IBM didn't want, and Oracle, which built on it. We also talked about why a first name makes a poor unique identifier.

**Wednesday 11/11: the dictionary.** A Python dictionary (elsewhere called a lookup table, hash table, or hash map) stores **key–value pairs**. Every key is unique. [`dict_demo.py`](./dict_demo.py) is the attendance tracker rewritten with a dictionary: if the student is already a key, add one to their count; otherwise add them with a count of **1**, not 0 (Monday's bug). We then counted every word in *A Tale of Two Cities*, reading it straight from the Project Gutenberg server with `urlopen` instead of from a local file, and decoding each line from bytes to text. We also moved from Vim into VS Code.

**Friday 11/13: what are we actually counting?** The counts said that Dickens wrote about ebooks, newsletters, and Mississippi. They came from Gutenberg's preamble and license, which wrap the book. The book itself sits between two lines that start with `*** `, and we used two flags to count only what lies between them.

- [`gutenberg.py`](./gutenberg.py) is the code as it stood in class.
- [`gutenberg_reader.py`](./gutenberg_reader.py) is the cleaned-up version, with comments. Its single function, `count_words`, reads the book from the server, skips everything outside the two `*** ` lines, and returns the word counts. Reading and counting are mixed in one function on purpose, so you can follow it from top to bottom.

## The assignment: a memo on cleaning text

`gutenberg_reader.py` now counts only Dickens. It still counts badly, because to `split()` a "word" is anything between two spaces. Here is what its dictionary holds for a few words:

| Key | Count | | Key | Count |
|---|---|---|---|---|
| `time` | 146 | | `be` | 689 |
| `time,` | 72 | | `is` | 709 |
| `times` | 26 | | `was` | 1677 |
| `time.` | 18 | | `were` | 633 |
| | | | `been` | 415 |

The word *time* turns up in about two dozen different keys: with a comma, with a period, with a quotation mark, with a dash and the next word glued on, and as a plural. Is `time` 146 times, or more like 300? And should *be*, *is*, *was*, *were*, and *been* count as five words or as one?

Write a memo proposing how we should clean the text before a word goes into the dictionary. I want your ideas, not an implementation, so **do not write code**. Your memo must cover:

1. **Punctuation.** This part is not optional. `"cat"` and `"cat."` end up as two different keys, and we don't want that. Propose how to get rid of punctuation. Then find a case where your rule removes something it shouldn't. Look at apostrophes (`don't`, `Defarge's`) and at dashes in particular.
2. **Nouns: singular and plural.** Pick a few nouns from the book (`time`/`times`, `man`/`men`, `child`/`children`). Should each pair count as one word or two? Why?
3. **Verbs: different forms.** Pick a verb or two (`be`/`is`/`was`/`were`, `walk`/`walked`/`walking`, `go`/`went`). Same question.
4. **Your approach.** Read the background notes below. Would you use stemming, lemmatization, both, or neither? Explain what each would get right and get wrong on *your* examples.
5. **What you would not merge, and why.** Sometimes two forms should stay apart. Give at least one case, and the reason.

Find your examples by running `gutenberg_reader.py` and looking in the dictionary it returns. You can print the whole thing, or ask about specific keys with `in` the way the bottom of the file does. Use real keys and real counts from the book. The four above are a starting point; don't stop there.

Write it as a memo: a heading with To, From, Date, and Subject lines, then paragraphs. No bullet-point dumps. Make a recommendation and defend it.

## Background: tokens, stems, and lemmas

Counting words is one of the oldest problems in **natural language processing** (NLP), the part of computing that deals with human language. Three ideas from that field apply directly to your memo.

**Tokenization** means breaking text into units, called **tokens**, that a program can count or look up. `line.split()` is a tokenizer, just a crude one: it breaks only at spaces, so punctuation stays stuck to the words. Better tokenizers also split off punctuation, and they have to make decisions as they go. Is `don't` one token or two? Is `wine-shop` one or two? What about `to-morrow`, which is how Dickens spelled it? Every cleaning rule in your memo is really a decision about tokenization.

**Stemming** cuts a word down to a **stem** by following spelling rules, most often by stripping endings: *if the word ends in "ing", remove "ing"*. The stemmer looks at one word at a time. It knows nothing about the sentence the word came from or what it means. That makes it simple and fast, and it does fine on regular words: *fishing*, *fished*, and *fisher* all become *fish*. The stem doesn't have to be a real word. The best-known English stemmer, Porter's (1980), turns *argue*, *argued*, *argues*, and *arguing* into *argu*, which is fine for counting, since all four still land in the same place. Rules about spelling fail on irregular words, though: no ending you can strip turns *ran* into *run*, or *was* into *be*. Stemming can also merge words that only look related.

**Lemmatization** maps each word to its **lemma**, the form you'd look up in a dictionary: *walked*, *walks*, and *walking* all go to *walk*, *better* goes to *good*, and *was* goes to *be*. To do that, it has to know what the word is doing in its sentence. *Meeting* is a noun in "our last meeting" and a verb in "we are meeting tomorrow", and the lemma is different in each case. That makes lemmatization more accurate than stemming. It is also much harder: it needs a dictionary of word forms, it needs grammar, and on difficult cases it is still a research problem.

In short, stemming is a fast set of rules that doesn't understand the text, and lemmatization tries to understand it, so it is slower and harder to build. Both are ways of deciding which keys should really be the same word. That is the question your memo answers.

## Reading

### New this week

- [Wikipedia, stemming: suffix-stripping rules and their limits](https://en.wikipedia.org/wiki/Stemming). Read the introduction, Examples, and the Algorithms section through suffix stripping.
- [Wikipedia, lemmatization: dictionary forms and why context matters](https://en.wikipedia.org/wiki/Lemmatization). Short; read all of it. The "better" → "good" and "meeting" examples are worth remembering.
- [Wikipedia, how tokenization splits text into tokens](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization). Just this section. It is written for programming languages, but the idea is the same for English. *Optional.*
- [Python tutorial, dictionaries: keys, lookups, and looping](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). Creating a dictionary, checking for a key with `in`, and listing the keys. The "Looping Techniques" section right after it shows the `for key, value in ... .items()` loop from 11/11.

Previously assigned readings are still fair game for questions in class or on assessments.

## Turning it in

Upload your memo to Sakai as a PDF or Word file, and bring a copy to class on **Monday, November 16**. We will start that meeting by comparing proposals, so be ready to read one of your rules out loud and defend it.

Before you turn it in, check that the memo:

- uses real keys and counts from the book, not made-up examples;
- deals with punctuation explicitly;
- names at least one case where your own rules get it wrong;
- runs between 600 and 900 words.

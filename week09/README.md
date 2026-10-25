# Assignment: Comparing Two Lists

Deliverable is a single file, `list_compare.py`. Start from the starter file in this folder, [`list_compare.py`](./list_compare.py), which gives you the list functions we built in class on 10/19 and 10/21, cleaned up, and a stub for the new one.

## Where we are

Over the last two weeks we gave Python's lists a small toolkit of our own:

| Function | Question it answers |
|---|---|
| `index_of(values, target)` | Where is `target`? (`-1` if it is not there) |
| `contains(values, target)` | Is `target` there at all? |
| `indices_of(values, target)` | Where is `target`, every time it appears? |
| `count(values, target)` | How many times does `target` appear? |
| `index_of_min(values)` | Where is the smallest element? (`-1` for an empty list) |
| `index_of_max(values)` | Where is the largest element? (`-1` for an empty list) |

On Wednesday 10/21 we noticed that `contains` and `index_of` were nearly the same function, so `contains` became one line that calls `index_of`, and `count` became one line that returns the length of what `indices_of` finds. On Friday 10/23 we wrote a greedy search: assume position 0 holds the answer, and move the pointer whenever another element challenges that assumption. `index_of_min` and `index_of_max` are that same search, written for any list whose elements Python can compare with `<` and `>`, numbers or strings. Python already provides `min()` and `max()`, so these are not new capabilities; we write them to see how such functions work. The starter file has all six functions above, complete. Read them; do not change them.

## Your task: `compare(first, second)`

Add one more function to the toolkit. It takes **two lists** and decides which of the two is the **greater**. It returns:

- a **negative** integer if `first` is less than `second`,
- **zero** if the two lists are equal,
- a **positive** integer if `first` is greater than `second`.

Both lists hold integers, or both hold strings. You will never be given one list of numbers and one list of strings, so you do not need to handle that case.

## The part that is yours

**This assignment does not tell you what "greater" means for a list.** You decide. There is more than one defensible answer, and part of the work is choosing one and being able to defend it.

You must:

1. Pick a rule and implement it in `compare`. Start from an everyday question: how do you decide which of two things is "greater"? Two bicycles, two pizzas, two cities, two baseball teams, two video games? Most of the time we invent our own rule, one that reflects what we value. Lists are no different: the rule is yours to choose.
2. State your rule in the docstring of `compare`, in plain language, including what it does when the two lists are empty, or when they tie.
3. In two or three sentences in the docstring, say why you chose it and one situation where it gives an answer you find surprising.
4. Run the given tests in the starter file. They do not know your rule; they check what any sensible rule must satisfy (for example, that a list equals itself and that swapping the two lists reverses the answer). If your `compare` passes all of them, it meets the specification. The test code uses a few commands we have not covered, such as `assert` and `isinstance`; comments in the file explain them, and you do not need to write them yourself. Also try a few pairs of your own.

Think about what would make a comparison feel *fair* to someone who uses your function, and try it on pairs of lists before you settle. You are free to use the other functions in the file if they help, but you are not required to.

## Constraints

- Every function that returns a value has exactly one `return`.
- Type hints are optional, but please try them.
- Every function you write needs a docstring.
- No `sorted()`, `.sort()`, `min()`, `max()` or `sum()` in `compare`. You may use `len()` and the functions in the starter file, including `index_of_min` and `index_of_max`. Write any other loops yourself.
- Do not change the six given functions.
- Nothing runs automatically when your file is imported, except what is already under `if __name__ == "__main__":` in the starter.

## Reading

### New this week (Week 9)

- [`list_compare.py`](./list_compare.py) — this week's starter code: the six list functions from class, the `compare` stub, and the given tests.
- [Wikipedia, checking items one by one](https://en.wikipedia.org/wiki/Linear_search) — linear search, the idea behind `index_of` and `contains` from 10/19 and 10/21.
- [Wikipedia, always taking the best-looking choice](https://en.wikipedia.org/wiki/Greedy_algorithm) — greedy algorithms, the idea behind `index_of_min` and `index_of_max` from 10/23.
- [Wikipedia, repeatedly halving a sorted list](https://en.wikipedia.org/wiki/Binary_search) — binary search, the 10/23 preview of why sorting matters.
- [Python tutorial, list methods `index` and `count`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) — Python's own versions of the functions we wrote.
- [Python docs, built-in `min`](https://docs.python.org/3/library/functions.html#min) and [built-in `max`](https://docs.python.org/3/library/functions.html#max) — the one-line versions of our greedy searches.
- For the commands explained in the test comments (you do not need to master them):
  [`assert` statements](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement),
  [`isinstance`](https://docs.python.org/3/library/functions.html#isinstance),
  [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings).

### Previously assigned (cumulative)

Everything in the Reading section of the [Week 8 assignment](../week08/README.md) is still fair game for questions in class or on assessments.

## Turning it in

Upload `list_compare.py` to Sakai, containing the six given functions and your `compare`. Leave the given tests in the file.

Before you upload, run the file. It prints a line for each given test, and you want every one to say `ok`. Then try `compare(first, second)` and `compare(second, first)` on a few pairs in the interactive shell, and see whether the two answers agree with each other the way you would expect.

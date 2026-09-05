# Python: An Introduction for New Programmers

Python's own documentation is upfront that its official tutorial is "for programmers that are new to the Python language, not beginners who are new to programming." This brief tutorial fills that gap: it's what gets you to the point where terms like "expression," "type," and "interpreter" mean something concrete instead of just vocabulary.

New to the terminal itself? `./intro-linux.md` covers navigating and managing files from the command line — read that first if `cd`, `ls`, and paths aren't yet familiar. This tutorial assumes you can already get a shell prompt open; it teaches Python itself, not the shell around it. Editing files comes up near the end — `./intro-vim.md` and `./intro-nano.md` cover that when you get there.

---

## First, a Word That Means Something Different Here: "Prompt"

If your only experience with the word "prompt" is typing a question into ChatGPT, Claude, or similar, set that meaning aside for this tutorial. There, a prompt is the message *you* compose, in ordinary English, to a model that interprets your intent and writes a reply in kind.

Here, a prompt is the opposite kind of thing: it's a short, fixed string — `$` or `>>>` — that a program prints to tell *you* "I'm done with the last thing, and idle, waiting for the next line." It isn't addressed to you in English, isn't asking a question, and isn't interpreting anything. It's a signal, the same way a blinking text cursor in an empty search box tells you it's ready for input — nothing more. The program behind it (a **shell**, or the **Python interpreter**) recognizes only a small, fixed, exact vocabulary — a command name spelled exactly right, or a line of Python written to exact syntax rules — and fails the instant you deviate, rather than guessing at what you probably meant.

A **shell** is one specific, decades-old kind of program (`bash`, `zsh`, and similar) whose entire job is reading the text you type and handing it to the operating system to run. It's not a chat interface and nothing behind it is a language model.

With that cleared up:

---

## The One Thing You Must Understand First: Two Different Prompts, Two Different Programs

Every prompt you'll see is a program waiting for you to type something, but *which* program is listening changes what your typing means.

| Prompt | Program listening | Understands |
|---|---|---|
| `$` | Operating system shell  | Linux commands like `ls`, `cd`, `python3`, `vim`, ... |
| `>>>` | The Python interpreter | Python code — `2 + 2`, `print(...)`, ... |

Here's the important distinction. When you type an operating system command (like `ls`) at the shell prompt, the operating system executes it and returns control to that same shell prompt.

But when you type `python3` at the shell prompt, something different happens: control passes to the Python shell — technically called the **interpreter** — and stays there. From that point on, you can only type Python code. To exit the interpreter and return to the operating system shell, type `exit()`.

This is the single most common early confusion: typing a shell command at `>>>`, or Python code at `$`, and getting a baffling error instead of the "wrong prompt" explanation that's actually going on. When something you're sure is correct produces nonsense, the first question is always: *which prompt am I looking at?*

---

## Your First Interactive Session, Step by Step

**1. Start the interpreter, from the shell:**
```
$ python3
Python 3.12.3 (main, ...) [GCC ...] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The prompt changed from `$` to `>>>`. You're now talking to Python, not the shell.

**2. Type an expression and press Enter:**
```
>>> 2 + 3
5
```
You typed something Python could evaluate, and it evaluated it and showed you the answer immediately. This immediate-feedback loop — type, see result, type again — is why it's called a **REPL** (Read–Evaluate–Print–Loop), and it's also why the interpreter is the right place to start: every idea below can be tested the moment you think of it.

**3. Leave the interpreter, back to the shell:**
```
>>> exit()
$
```
`Ctrl-D` does the same thing. You're back at `$`, and the shell has no memory that Python was ever running.

Everything in the next four sections happens at `>>>`. Don't reach for a file yet — there's nothing here that needs one.

---

## Python as a Calculator

```
>>> 7 + 5
12
>>> 7 - 5
2
>>> 7 * 5
35
>>> 7 / 5
1.4
>>> 7 // 5
1
>>> 7 % 5
2
>>> 7 ** 2
49
```

`/` always gives a precise (decimal) answer; `//` throws away the remainder and keeps only the whole number; `%` keeps *only* the remainder. `**` is exponentiation, not `^`. Parentheses control order of operations exactly like in arithmetic class:

```
>>> (2 + 3) * 4
20
>>> 2 + 3 * 4
14
```

## Every Value Has a Type

```
>>> type(5)
<class 'int'>
>>> type(5.0)
<class 'float'>
>>> type("5")
<class 'str'>
```

`5`, `5.0`, and `"5"` look related but are three different kinds of value: a whole number (`int`), a decimal number (`float`), and text (`str`) — and Python keeps them strictly separate rather than guessing what you meant.

## Text Is Not Numbers

Quote text with `'` or `"` (either works; be consistent) to make a `str`. `+` on strings concatenates instead of adding, and `*` repeats:

```
>>> "Py" + "thon"
'Python'
>>> "ab" * 3
'ababab'
```

Mixing a `str` and a number with `+` fails — Python won't silently guess whether you meant addition or concatenation:

```
>>> "score: " + 7
Traceback (most recent call last):
TypeError: can only concatenate str (not "int") to str
```

Read the error, don't just note that it happened — this one is telling you exactly what's wrong and what type it expected. Fix it by converting explicitly: `str(7)` turns `7` into `"7"`; `int("7")` and `float("7")` go the other direction.

## Variables: Naming a Value So You Can Reuse It

```
>>> age = 19
>>> age
19
```

`=` stores a value under a name; it doesn't ask a question, so it produces nothing to show and the shell stays silent. A bare name (or any expression) *is* a question — "what does this evaluate to?" — so the shell always answers it. That's the whole rule: silence means "stored," output means "you asked."

Names are letters, digits, and underscores, can't start with a digit, are case-sensitive, and can't be one of Python's reserved words (`if`, `for`, `class`, ...). Reassigning a name points it at a new value — it doesn't change the old value, it just stops looking at it:

```
>>> age = age + 1
>>> age
20
```

---

## Recovering from Common Problems

**"I typed `ls` (or `cd`, `pwd`, ...) and got `NameError: name 'ls' is not defined`."**
You're at `>>>`, not `$`. Exit with `exit()` first if you actually wanted the shell.

**"I typed `2 + 2` at my terminal and got `command not found` or similar."**
You're at `$`, not `>>>`. Run `python3` first.

**"`TypeError: can only concatenate str ... to str`."**
You mixed a string and a number with `+`. Convert one side with `str()`, `int()`, or `float()` so both sides match.

**"`SyntaxError` and I don't see anything wrong."**
Check for a missing closing quote or parenthesis — Python often reports the error on the line *after* the real mistake, since that's where it finally noticed something didn't add up.

**"Nothing is happening / it looks frozen."**
`Ctrl-C` cancels whatever's in progress, at either prompt, and gets you back to a fresh one.

---

## From the Interactive Shell to a Real Program

The interpreter forgets everything the instant you `exit()` — there's no file, nothing to hand in, nothing that survives to run again tomorrow. That's fine for testing a one-line idea; it stops being fine the moment a program needs more than a line or two, or needs to exist after you close the terminal.

A **file** solves that: it's the same Python, stored under a name, that you can edit, save, and run as many times as you want. The workflow changes shape, but nothing about the language does:

**1. Leave the interpreter if you're in it** (`exit()`), so you're back at `$`.

**2. Open a file in an editor** — `vim hello.py` or `nano hello.py` (mechanics in `./intro-vim.md` / `./intro-nano.md`).

**3. Write the same kind of code as before** — with one difference. At `>>>`, a bare expression echoes itself automatically. In a file, nothing echoes anything; `print()` is the only way a value ever reaches the screen:
```python
print(2 + 3)
```

**4. Save and quit the editor**, back to `$`.

**5. Run the file from the shell** — not from inside `python3`:
```
$ python3 hello.py
5
```

You didn't retype `python3` and land at `>>>` this time — `python3 hello.py` tells the interpreter "run this whole file," rather than "give me a prompt to type at."

---

## What It Looks Like in Practice

```
$ python3
>>> 19.99 + 19.99 * 0.08
21.5892
>>> exit()
$ nano total.py
```
*(inside the editor, type the three lines below, then save and exit)*
```python
price = 19.99
tax = 0.08
print(price + price * tax)
```
```
$ python3 total.py
21.5892
```
Same computation, two different homes: a throwaway check at `>>>`, then a saved, rerunnable version in a file.

---

## Cheat Sheet (One Page)

| Thing | Example | Meaning |
|---|---|---|
| `python3` | (at `$`) | Enter the interpreter |
| `exit()` / `Ctrl-D` | (at `>>>`) | Leave the interpreter, back to `$` |
| `+` `-` `*` | `7 + 5` | Addition, subtraction, multiplication |
| `/` | `7 / 5` → `1.4` | True (decimal) division |
| `//` | `7 // 5` → `1` | Floor (whole-number) division |
| `%` | `7 % 5` → `2` | Remainder |
| `**` | `7 ** 2` → `49` | Exponentiation |
| `type(x)` | `type(5)` | Shows a value's type |
| `str(x)` `int(x)` `float(x)` | `str(7)` → `'7'` | Convert between types |
| `=` | `age = 19` | Assign (store), not compare |
| `print(x)` | `print(5)` | The only way to show a value from a file |

---

## Going Further (Optional)

Everything above is deliberately small — enough to make the official Python tutorial's stated audience ("programmers new to the language") actually describe you. From here:

- [Python 3 Tutorial, Ch. 3.1, "Using Python as a Calculator"](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator) — the [Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers) and [Text](https://docs.python.org/3/tutorial/introduction.html#text) subsections cover the same ground as this tutorial, in the language's own words.
- [Think Python, 3rd edition, Ch. 1–2](https://greenteapress.com/wp/think-python-3rd-edition/) — "The Way of the Program" and "Variables, Expressions, and Statements" build the same foundation with more worked examples.
- [Introducing Python, 3rd edition, Ch. 1–3](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/) — free via O'Reilly with a LUC login; a third angle on the same material, written for people who've never programmed before.
- The full [Python 3 Tutorial](https://docs.python.org/3/tutorial/index.html) is worth returning to later in the course, once functions, lists, and control flow are in play — that's the point where its assumed audience and yours actually converge.

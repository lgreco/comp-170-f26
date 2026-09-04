# Reading: The Interactive Python Shell

## Two ways to run Python

 Python offers a
second way to work that skips the file entirely: the **interactive shell**.

Type `python3` at the terminal with no filename after it, and instead of
returning to your normal prompt, you get:

```
>>>
```

That `>>>` is Python waiting for you, one line at a time. Whatever you type
next is executed the instant you press Enter — there's no separate "save"
step and no separate "run" step. This is sometimes called a **REPL**
(Read–Evaluate–Print–Loop): Python reads what you typed, evaluates it,
prints the result, and loops back to wait for your next line.

Exit the shell with `exit()` or Ctrl-D when you're done.

## The one big difference from a script: everything talks back

In a file, `print()` is the only way to see a value — if you write `x + 1`
on its own line with no `print`, nothing appears when you run the script.
In the interactive shell, that rule changes. Type an expression by itself,
and Python echoes its value back to you automatically:

```
>>> 3 + 4
7
```

You didn't need `print()`. The shell shows you the result of anything it
can evaluate, because "evaluate and show me" is the entire point of typing
at a prompt instead of writing a file.

Assignment is the one exception, and it's worth noticing *why*. Recall from
class: `=` means "store this value under this name," not "show me this
value." An assignment statement produces no value of its own to echo —
it's an instruction to memory, not an expression — so the shell stays
silent:

```
>>> x = 5
>>>
```

No output. The store happened, silently, exactly as it would in a script.
If you then want to see what got stored, ask for it, on its own line:

```
>>> x
5
```

That's the whole rule. **Assignment is silent because it's an instruction,
not a question. A bare name (or expression) is not silent, because it's a
question, and the shell always answers questions.**

## Why this is useful: fast, disposable experiments

The interactive shell is not where you write real programs — it forgets
everything the moment you close it, and there's no file to hand in. What
it's good for is testing a small idea in seconds, without the overhead of
opening Vim, saving a file, and running it. If you're not sure what
`7 / 2` gives you versus `7 // 2`, or whether `"3" + "4"` behaves like
addition or concatenation, don't guess — ask the shell:

```
>>> 7 / 2
3.5
>>> 7 // 2
3
>>> "3" + "4"
'34'
```

Three questions, three immediate answers, no file involved. This is the
same `+` and `/` from class, the same `str` vs. numeric distinction from
class — the shell just removes the round-trip through a saved file so you
can check your understanding as fast as you can type.

## Checking types the same way

`type()` works identically at the prompt, and because the shell echoes
results automatically, you don't even need to wrap it in `print()`:

```
>>> type(5)
<class 'int'>
>>> type(5.0)
<class 'float'>
>>> type("5")
<class 'str'>
```

Same three types from class — `int`, `float`, `str` — same distinction
between the number `5`, the number `5.0`, and the text `"5"`. The shell
just gets you the answer one line at a time instead of one whole script at
a time.

## What doesn't change

Everything you already know about variables, types, and arithmetic is
exactly the same in the shell as in a file:

- `=` still means assignment, not equality.
- A variable still holds one type until you reassign it.
- `+` still means addition between numbers and concatenation between
  strings — mixing an `int` and a `str` with `+` still fails the same way
  it would in a script.

The shell changes *how fast you see feedback*. It changes nothing about
*what the language does*.

## Assigned reading (Week 2)

From
[Introducing Python, 3rd edition](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/),
by Bill Lubanovic (O'Reilly — free on the platform if you log in with
your LUC email):

- [Ch. 1, "Introduction"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch01.html) —
  in full.
- [Ch. 2, "Types and Variables"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch02.html) —
  up to and including the "Variables" section, not beyond.
- [Ch. 3, "Numbers"](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html) —
  only the sections on integers and floats, for now.

## Complementary reading

[Think Python, 3rd edition, Ch. 2 ("Variables, Expressions, and
Statements")](https://greenteapress.com/wp/think-python-3rd-edition/)
covers this same material — assignment, expressions vs. statements, and
the interactive interpreter — from a slightly different angle. Worth a
read alongside this note, not instead of it.

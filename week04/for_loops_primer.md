# For Loops: Repeating a Group of Statements

A loop is how you tell Python "do this group of statements more than
once" without writing that group out by hand every time. That's the
whole idea — everything else in this note is detail on how Python lets
you say that precisely.

## The simplest possible loop

Say you want to print the numbers 1 through 5. Without a loop, that's
five separate lines:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

With a `for` loop, it's two:

```python
for number in range(1, 6):
    print(number)
```

`range(1, 6)` produces the numbers 1, 2, 3, 4, 5 — five values in total,
starting at 1 and stopping *before* 6. Each time through the loop,
`number` takes on the next of those values, and the indented line
underneath runs once for that value. Five values, five runs, five lines
printed — same result as the five `print` statements above, but written
once.

## The colon opens scope, indentation says what's inside

Every `for` loop has the same two-part shape:

```python
for number in range(1, 6):     # the loop header, ending in a colon
    print(number)               # the loop's scope — what repeats
```

The colon at the end of the header is what opens the loop's scope.
Everything indented underneath it belongs to the loop and runs on every
pass; the first line that goes back to the original indentation level is
outside the loop and runs only once, after the loop finishes entirely.
Indentation isn't a style preference here — it's how Python knows where
the loop's body ends. Four spaces is the standard; whatever amount you
pick, use it consistently, or Python will raise an error.

You can see this directly by moving a line in or out:

```python
total = 0
for number in range(1, 6):
    total = total + number
    print(total)        # inside the loop: prints the running total each time
```

```
1
3
6
10
15
```

Move that same `print(total)` one level to the left, outside the loop:

```python
total = 0
for number in range(1, 6):
    total = total + number
print(total)             # outside the loop: prints only the final total
```

```
15
```

Same numbers being added, same final answer — the only thing that
changed is which lines are "inside" the repeating part and which run
once at the end. That's the entire difference indentation makes.

## Looping over something other than numbers

`range()` isn't the only thing you can put after `in`. A string works
the same way — Python hands you one character at a time, in order from left to right.

```python
for symbol in "1967":
    print(symbol)
```

```
1
9
6
7
```

Same shape as before: a header ending in a colon, an indented block that
runs once per value. What changes is only what you're looping *over* —
a range of numbers, or the characters of a string.

## A loop with a purpose: growing a bank balance

Here's where a loop actually earns its keep. Suppose you put $1,000 into
an account that pays 5% interest a year, and you want to know what it's
worth after 30 years. By hand, that's: multiply by 1.05, take that
result and multiply by 1.05 again, and again, thirty times over. A loop
does exactly that — one line of arithmetic, repeated:

```python
PRINCIPAL = 1_000
INTEREST_RATE = 0.05
YEARS_TO_INVEST = 30

balance = PRINCIPAL
for year in range(1, YEARS_TO_INVEST + 1):
    balance = balance * (1 + INTEREST_RATE)
    print(f"Year {year}: ${balance:,.2f}")
```

Each pass through the loop takes the balance from the *previous* pass
and rolls it forward one more year — this is the same "new principal for
the next year" idea from the compound-interest arithmetic, just written
as code instead of done by hand. Notice `1_000`: the underscore is
purely for a human reading the code and means nothing extra to Python —
`1_000` and `1000` are the same value. And `f"...{balance:,.2f}"` is
just a formatting instruction: comma-separate the thousands, show two
decimal places. Neither of those is required to make the loop work; both
just make the output easier to read.

## You don't always need the loop

It's worth being honest about something: the loop above isn't strictly
necessary. Compounding for a fixed number of years has a direct formula
— principal times $(1 + \text{rate})^{\text{years}}$ — and Python can
compute that in one line with `**`, no repetition required:

```python
final_balance = PRINCIPAL * (1 + INTEREST_RATE) ** YEARS_TO_INVEST
print(f"${final_balance:,.2f}")
```

This gives the same final number as the loop, faster and without ever
repeating anything. The loop is still worth knowing, though — the
closed-form shortcut only exists because compound interest happens to
have a clean formula behind it. Plenty of tasks that repeat (checking
every character of a string, printing every row of a table, processing
every item in a list) have no such shortcut; a loop is the only way to
say "do this once for each one" in those cases.

## Assigned reading

A chapter reference from Bill Lubanovic's *Introducing Python*, 3rd
edition, covering `for` loops is coming separately — check for that link
before doing the reading. In the meantime, practice writing and running
the `for` loop shapes above on your own machine: loop over a `range()`,
loop over a string, and try moving a `print` line in and out of a loop's
indentation to see the scope boundary for yourself.

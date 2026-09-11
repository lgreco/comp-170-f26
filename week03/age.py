# Bring in the tiny "check" command we invented ourselves in
# our_first_function.py, so we can reuse it here without retyping it.
from our_first_function import *

# Values that don't change while the program runs are written as
# constants, in ALL CAPS by convention -- that's how we signal to anyone
# reading the code "hey, this is a constant." It also makes the age
# computation below read like a sentence (current year minus year born)
# instead of a magic number that only makes sense for one person, one year.
CURRENT_YEAR = 2026
ENTRY_PROMPT = "Year you were born. "

# First take the keyboard entry
# We don't call this "year_born" yet, because at this point we don't know
# if what the user typed is actually a valid year -- it's just user input.
user_input = input(ENTRY_PROMPT)

# Evaluate it to verify it's legit (numbers only)
# Instead of converting straight to int() (which would crash the program
# on something like "19Y7"), we validate first and only convert once we
# know it's safe. This is the "avoid the error" approach, not "catch it
# after it happens."
#
# check, below, is not a Python command. It's the tiny program we invented 
# ourselves in our_first_function.py, and we imported it above so we can reuse 
# it here. It returns True if the string is all digits, and False if it 
# contains any non-digit symbols.
if check(user_input):
    # Now that check() confirmed every symbol is a digit, it's safe to
    # hand the string to int().
    year_born = int(user_input)
    age = CURRENT_YEAR - year_born
    print("Your are", age, "years old")
else:
    # Bad input doesn't crash the program -- we handle it gracefully
    # with a message instead of an unhandled error.
    print("Really, you think", user_input, "is an integer?")
    # OK, maybe this is not a very graceful message, but hey, it's Friday.

from our_first_function import *

CURRENT_YEAR = 2026
ENTRY_PROMPT = "Year you were born. "

# First take the keyboard entry
user_input = input(ENTRY_PROMPT)
# Evaluate it to verify its legit (numbers only)
if check(user_input):
    year_born = int(user_input)
    age = CURRENT_YEAR - year_born
    print("Your are", age, "years old")
else:
    print("Really, you think", user_input, "is an integer?")


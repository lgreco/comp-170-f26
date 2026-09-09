
CURRENT_YEAR = 2026
ENTRY_PROMPT = "Year you were born. "

year_born = int(input(ENTRY_PROMPT))

age = CURRENT_YEAR - year_born

print("Your are", age, "years old")

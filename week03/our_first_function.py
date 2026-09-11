# check(): our first function -- a tiny program we invent ourselves and
# name ourselves, because Python doesn't already have a command that does
# exactly this. It answers a yes/no question about the contents of a string.
#
# The goal: look at a string one symbol at a time and make sure every
# symbol is a numeric digit. This is how we validate keyboard input
# (like a birth year) before we ever try to convert it with int(), so a
# stray non-digit (e.g. "19Y7") doesn't crash the program.
#
# This program is a function, which is a named block of code that can be run
# over and over again. Functions are like little machines that take in
# some input, do something with it, and then spit out an answer. The input
# is called an argument, and the answer is called a return value. The function
# is defined with the def keyword, followed by the function name, a list of
# arguments in parentheses, and a colon. The body of the function is indented
# and contains the code that will be executed when the function is called.

def check(this_string):
    # A loop iterates over a collection one item at a time, the same way
    # taking attendance goes through a roster name by name. Here the
    # collection is the string, and each item is one symbol (a letter,
    # digit, space, or punctuation mark -- not just "letters").
    for symbol in this_string:
        # Every symbol has a numeric code (ASCII). ord() looks it up.
        ascii_code = ord(symbol)

        # The digits 0-9 occupy ASCII codes 48 through 57, inclusive.
        # If this symbol's code falls outside that range, it isn't a
        # digit -- one bad symbol is enough to disqualify the whole string, 
        # so we stop immediately and report False instead of checking the rest.
        if ascii_code < 48 or ascii_code > 57:\
            # We just found a bad symbol, so we can stop checking 
            # and and report that the string is not valid.
            return False
    # At this point we are done with every symbol
    # We made it through every symbol without finding a bad one, so the
    # string is legit -- report True.
    return True
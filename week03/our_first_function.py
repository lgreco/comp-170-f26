def check(this_string):
    """Looks at the contents of the given string and
    returns True if the string contains only numbers 
    and False otherwise.
    """
    for symbol in this_string:
        ascii_code = ord(symbol)
        if ascii_code < 48 or ascii_code > 57:
            return False
    # At this point we are done with every symbol
    return True


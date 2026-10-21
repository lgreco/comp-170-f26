friends = [
    "Hamza",
    "Allie",
    "Sia",
    "Anthony",
    "Isabella",
    "Tommy",
    "Yasmin",
    "Adem",
    "Aldin",
    "MaryGrace",
    "Drew",
    "Veloashan",
]


def contains(values: list[str], target: str) -> bool:
    """Searches through a list of strings to find a target string.
    Return True if target is in values, False otherwise."""
    i = 0  # start at the beginning of the list
    found = False  # Assume target not present
    while not found and i < len(values):
        # Update the found status
        found = values[i] == target
        i = i + 1  # Move to the next value
    # Loop ends when the target is found or when
    # all values have been checked, and we reach
    # the end of the list without finding target.
    return found

def index_of(values: list[str], target: str) -> int:
    # Assume that target not present in list
    idx = -1
    i = 0
    while i < len(values) and idx == -1:
        if values[i] == target:
            idx = i
        i = i+1    
    return idx


def count(values: list[str], target: str) -> int:
    """Counts and returns the number of times a target string appears
    in a list of strings. If no strings with the target value are found,
    the method returns 0."""
    # Initialize a counter to keep track of the number of occurrences
    counter = 0
    # Go through every string in the list and check if it\
    # matches the target string
    for i in range(len(values)):
        if values[i] == target:
            # Increment the counter if a match is found
            counter = counter + 1
    # Return the final count
    return counter

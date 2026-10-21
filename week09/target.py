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
    found = (values[i] == target)
    i = i + 1  # Move to the next value
  # Loop ends when the target is found or when
  # all values have been checked, and we reach
  # the end of the list without finding target.
  return found

def count(values: list[str], target: str) -> int:
    """Counts and returns the number of times a target string appears 
    in a list of strings. If no strings with the target value are found, 
    the method returns 0."""
    # Initialize a counter to keep track of the number of occurrences
    counter = 0
    # Iterate through the list of strings
    for i in range(len(values)):
        # Check if the current string matches the target string
        if values[i] == target:
            # Increment the counter if a match is found
            counter = counter + 1
    # Return the final count
    return counter

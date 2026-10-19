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
    counter = 0
    for i in range(len(values)):
        if values[i] == target:
            counter = counter + 1
    return counter

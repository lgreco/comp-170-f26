friends = [
    "Hamza",
    "Allie",
    "Sia",
    "Anthony",
    "Sia",
    "Isabella",
    "Tommy",
    "Sia",
    "Yasmin",
    "Adem",
    "Aldin",
    "MaryGrace",
    "Drew",
    "Sia",
    "Veloashan",
]





def contains(values: list[str], target: str) -> bool:
    #i = 0
    #found = False
    #while not found and i < len(values):
    #    if values[i] == target:
    #        found = True
    #    i = i + 1
    return index_of(values, target) != -1






def index_of(values: list[str], target: str) -> int:
    i = 0
    idx = -1
    while i < len(values) and idx == -1:
        if values[i] == target:
            idx = i
        i = i + 1
    return idx


def indices_of(values: list[str], target: str) -> list[int]:
    paper = []
    for i in range(len(values)):
        if values[i] == target:
            paper.append(i)
    return paper



def count(values: list[str], target: str) -> int:
    """Counts and returns the number of times a target string appears
    in a list of strings. If no strings with the target value are found,
    the method returns 0."""
    # Initialize a counter to keep track of the number of occurrences
    #counter = 0
    # Go through every string in the list and check if it\
    # matches the target string
    #for i in range(len(values)):
    #    if values[i] == target:
    #        # Increment the counter if a match is found
    #        counter = counter + 1
    # Return the final count
    return len(indices_of(values,target)) 

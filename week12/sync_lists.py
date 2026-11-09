students = [
        "Allie",
        "Anthony",
        "Hamza"
        ]

absences = [0,
            0,
            0
            ]


def index_of(student_name: str, roster: list[str]) -> int:
    idx = -1
    i = 0 
    while i < len(roster) and idx == -1:
        if roster[i] == student_name:
            idx = i
        i += 1
    return idx

def add_absence(student_name: str, roster: list[str], attendance: list[int]) -> None:
    # Make sure student is real
    idx = index_of(student_name, roster)
    if idx > -1:
        # Student is real and their position in the synchronized
        # lists is given by [idx]
        attendance[idx] += 1

def report(roster: list[str], attendance: list[int]) -> None:
    for i in range(len(roster)):
        student_name = roster[i]
        absences = attendance[i]
        print(f"{student_name:20s}: {absences}")


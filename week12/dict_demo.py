
class_roster = dict()  # same as = {}

def add_absence(student_name: str, roster: dict):
    if student_name in roster:
        roster[student_name] += 1
    else:
        roster[student_name] = 1

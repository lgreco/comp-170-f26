
class_roster = dict()  # same as = {}

def add_absence(student_name: str, roster: dict):
    if student_name in roster:
        roster[student_name] += 1
    else:
        roster[student_name] = 1

print(class_roster)
add_absence("Allie", class_roster)
print(class_roster)

add_absence("Allie", class_roster)
print(class_roster)
add_absence("Anthony", class_roster)
add_absence("Hamza", class_roster)  
add_absence("Yazmin", class_roster)
add_absence("Allie", class_roster)
print(class_roster)
print(class_roster['Allie'])

for key in class_roster:
    print(key, class_roster[key])

for key, value in class_roster.items():
    print(key, value)
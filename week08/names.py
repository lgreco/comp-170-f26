paper = [
        "Albus",
        "Hermione",
        "Charlie",
        "Tom",
        "Petunia",
        "Luna",
        "Ron",
        "Rubius",
        "Severus"]

names_per_line = 3

def show_in_columns(paper, names_per_line):
  for position in range(len(paper)):
      if position % names_per_line == 0:
          print()
      print(paper[position], end = ", ")

def longest(paper):
    first_person_name = paper[0]
    length_of_first_person_name = len(first_person)
    persons_on_paper = len(paper)
    longest_length = len(first_person_name)
    for position in range(1, person_on_paper):
        length_of_current_person = len(paper[position])
        if length_of_current_person > longest_length:
            longest_lenght = length_of_current_person
    return longest_length


show_in_columns(paper, names_per_line)

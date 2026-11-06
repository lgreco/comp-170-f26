counter = 0
total = 0
filename = 'data.txt'
READ_MODE = 'r'
with open(filename, READ_MODE) as my_file:
    for line in my_file:
        temperature = int(line.strip())
        total  += temperature
        counter += 1

average = total / counter

print(f"The average temperature is {average:.2f}")

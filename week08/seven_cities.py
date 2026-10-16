# 7 days of temperature measurements for 7 cities
# Each row is a city, each column is a day
temperatures = [
    [72, 75, 78, 74, 77, 79, 80],
    [68, 70, 73, 71, 72, 76, 78],
    [81, 83, 85, 84, 86, 88, 90],
    [65, 67, 69, 70, 71, 73, 74],
    [74, 76, 77, 79, 80, 82, 84],
    [69, 71, 72, 75, 78, 80, 82],
    [77, 79, 81, 82, 84, 85, 87],
]

total = 0
for row in range(len(temperatures)):
    for col in range(len(temperatures[row])):
        total = total + temperatures[row][col]

number_of_data_points = len(temperatures) * len(temperatures[0])

avg = total / number_of_data_points

# now do the same thing with value loops

total = 0
for city in temperatures:
    for day_temperature in city:
        total = total + day_temperature


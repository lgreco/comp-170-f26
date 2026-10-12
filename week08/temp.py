temperatures = [ 55, 61, 62, 63, 54, 65, 66, 57, 67, 65, 71, 71, 73, 74, 76 ] 

n = len(temperatures)  # number of data points in array

total = 0
for i in range(n):
    total = total + temperatures[i]
avg = total / n
print(f"Average temperature over past {n} days is {avg:.2f}")

n = 10
char = '.'

for i in range(n):
    for j in range(n):
        print(char, end="")
    print()

## better version 

print("\nHere's a better version:")


for i in range(n):
    print(char*n)


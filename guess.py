number_in_my_mind = 6

# The following code is TERRIBLE

while True:
    n = int(input("Guess the number I have in mind? "))
    if n == number_in_my_mind:
        break
    print("Ooops! Try again!\n")

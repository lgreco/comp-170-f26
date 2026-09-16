number_in_my_mind = 6
your_guess = number_in_my_mind + 1
max_attempts = 5
count = 0

while your_guess != number_in_my_mind and count < max_attempts:
    your_guess = int(input("What's your guess? "))
    count = count + 1

if your_guess == number_in_my_mind:
    print("Good job!")
else:
    print("Looser!")

import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess > num:
        guess = input("Lower: ")
        guess = int(guess)
    if guess < num:
        guess = input("Higher: ")
        guess = int(guess)

    if guess == num:
        print("congratulations! You won!")
        break
    else:
        print("Nope, sorry. Try again!")
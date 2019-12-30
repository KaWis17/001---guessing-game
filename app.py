import random

the_number = random.randint(0, 20)

print("Guess the number between 0-20")
counter = 1

try:
    while True:
        guess = int(input(f"Your {counter} guess: "))
        if guess < the_number:
            print("Sorry but your number is too small")
            counter += 1
        elif guess > the_number:
            print("Sorry, but your number is too big")
            counter += 1
        elif the_number == guess:
            break
    print(f"Congrats, you WON by {counter} guess")

except ValueError:
    print("Sorry, but your guess must be a number")
